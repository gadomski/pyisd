from typing import List

import dask.dataframe
import dask.delayed

import isd.io

DEFAULT_REPARTITION_FREQUENCY = "2w"


def write(
    paths: List[str],
    directory: str,
    append: bool = False,
    repartition_frequency: str = DEFAULT_REPARTITION_FREQUENCY,
) -> None:
    """Writes the ISD data located in `paths` to a partitioned parquet table at `directory`.

    Uses dask under the hood to read the data and write the output file.
    """
    if append:
        data_frame = read(directory)
        last_division = data_frame.divisions[-1]
        data_frames = [
            dask.delayed(isd.io.read_to_data_frame)(path, since=last_division)
            for path in paths
        ]
    else:
        data_frames = [dask.delayed(isd.io.read_to_data_frame)(path) for path in paths]
    data_frame = dask.dataframe.from_delayed(data_frames)
    data_frame = data_frame.persist()
    data_frame = data_frame.set_index("timestamp").repartition(
        freq=repartition_frequency
    )
    data_frame.to_parquet(directory, append=append)


def read(directory: str) -> dask.dataframe.DataFrame:
    """Reads a parquet table as a dask data frame."""
    return dask.dataframe.read_parquet(directory)
