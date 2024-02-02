from __future__ import annotations
import gzip
import json
from io import BytesIO
from pathlib import Path
from dataclasses import dataclass
from typing import List, Union, Optional, Dict, Any, Iterator, TYPE_CHECKING
import datetime

from isd.record import Record

import pandas

if TYPE_CHECKING:
    import polars


@dataclass
class Batch:
    records: List[Record]

    def __len__(self) -> int:
        return len(self.records)

    def __getitem__(self, index: int) -> Record:
        return self.records[index]

    def __iter__(self) -> Iterator[Record]:
        return iter(self.records)

    @classmethod
    def parse(cls, lines: Union[str, BytesIO]) -> Batch:
        """Reads records from a text io stream."""
        if isinstance(lines, BytesIO):
            lines = lines.read().decode("utf-8")
        return cls([Record.parse(line) for line in lines.splitlines()])

    @classmethod
    def from_path(cls, path: Union[str, Path]) -> Batch:
        """Opens a local ISD file and returns an iterator over its records.

        If the path has a .gz extension, this function will assume it has gzip
        compression and will attempt to open it using `gzip.open`.
        """
        path = Path(path)
        if path.suffix == ".gz":
            with gzip.open(path) as gzip_file:
                return cls(
                    [Record.parse(gzip_line.decode("utf-8")) for gzip_line in gzip_file]
                )
        else:
            with open(path) as uncompressed_file:
                return cls(
                    [
                        Record.parse(uncompressed_line)
                        for uncompressed_line in uncompressed_file
                    ]
                )

    def filter_by_datetime(
        self,
        start_date: Optional[datetime.datetime] = None,
        end_date: Optional[datetime.datetime] = None,
    ) -> Batch:
        """Returns a new Batch with records filtered by start and end datetimes (both optional)."""
        return Batch(
            [
                record
                for record in self.records
                if (not start_date or record.datetime() >= start_date)
                and (not end_date or record.datetime() < end_date)
            ]
        )

    def to_dict(self) -> List[Dict[str, Any]]:
        """Returns a list of dictionaries, one for each record."""
        return [record.to_dict() for record in self.records]

    def to_json(self, indent: int = 4) -> str:
        """Returns a JSON line of all records."""
        data = []
        for d in self.to_dict():
            d["datetime"] = d["datetime"].isoformat()
            data.append(d)
        return json.dumps(data, indent=indent)

    def to_data_frame(self) -> pandas.DataFrame:
        """Reads a local ISD file into a DataFrame."""
        return pandas.DataFrame([record.to_dict() for record in self.records])

    def to_polars(self) -> polars.DataFrame:
        """Reads a local ISD file into a Polars DataFrame."""
        try:
            import polars
        except ImportError as e:
            message = (
                "The `polars` optional dependency is required to use `to_polars`. "
                "Install this dependency with `pip install 'isd[polars]'`"
            )
            raise ImportError(message) from e

        return polars.DataFrame([record.to_dict() for record in self.records])
