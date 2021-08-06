import os

import click
import pandas
from pyarrow import Table, parquet as pq

from isd import io, IsdError


@click.group()
def cli() -> None:
    pass


@click.command()
@click.argument("directory")
@click.argument("root_path")
def parquet(directory: str, root_path: str) -> None:
    """Reads a directory of ISD data and builds a parquet table."""
    data_frames = []
    paths = [os.path.join(directory, file_name) for file_name in os.listdir(directory)]
    with click.progressbar(paths) as bar:
        for path in bar:
            try:
                data_frame = io.read_to_dataframe_lite(path)
            except IsdError:
                print(f"Invalid ISD file, skipping: {path}")
                continue
            except Exception as e:
                print(f"Exception while processing {path}: {e}")
                continue
            data_frames.append(data_frame)
    data_frame = pandas.concat(data_frames)
    table = Table.from_pandas(data_frame)
    pq.write_to_dataset(table, root_path=root_path, partition_cols=["month"])


cli.add_command(parquet)
