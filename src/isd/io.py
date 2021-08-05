from typing import List

import geopandas
from geopandas import GeoDataFrame
from pandas import DataFrame

from isd.record import Record, RecordLite


def read(path: str) -> List[Record]:
    """Reads records from a filesystem path."""
    with open(path) as f:
        records = [Record.parse(line) for line in f]
    return records


def read_lite(path: str) -> List[RecordLite]:
    """Reads lite records from a filesystem path."""
    with open(path) as f:
        records = [RecordLite.parse(line) for line in f]
    return records


def read_to_geodataframe_lite(path: str) -> GeoDataFrame:
    """Reads an ISD file into a GeoDataFrame, using lite ISD records."""
    records = read_lite(path)
    data_frame = DataFrame(records)
    return GeoDataFrame(
        data_frame,
        geometry=geopandas.points_from_xy(data_frame.latitude, data_frame.longitude),
    )
