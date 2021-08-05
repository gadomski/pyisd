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
@click.argument("outfile")
def parquet(directory: str, outfile: str) -> None:
    """Reads a directory of ISD data and builds a parquet table."""
    data_frames = []
    paths = [os.path.join(directory, file_name) for file_name in os.listdir(directory)]
    with click.progressbar(paths) as bar:
        for path in bar:
            try:
                data_frame = io.read_to_dataframe_lite(path)
            except IsdError:
                print(f"Invalid ISD file, skipping: {path}")
            data_frames.append(data_frame)
    data_frame = pandas.concat(data_frames)
    table = Table.from_pandas(data_frame)
    pq.write_table(table, outfile)


cli.add_command(parquet)
