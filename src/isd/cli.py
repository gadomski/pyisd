# type: ignore

import dataclasses
import itertools
import json
from typing import List

import click
from click import ClickException

import isd.io
import isd.parquet


@click.group()
def main() -> None:
    """Work with NOAA's Integrated Surface Database (ISD) from the command line."""


@main.command()
@click.argument("INFILE")
@click.option("-i", "--index", default=0)
def record(infile: str, index: int) -> None:
    """Prints a single record to standard output in JSON format."""
    with isd.io.open(infile) as records:
        record = next(itertools.islice(records, index, None), None)
        if record:
            print(json.dumps(dataclasses.asdict(record), indent=4))
        else:
            raise ClickException(f"No record with index {index}")


@main.command()
@click.argument("INFILES", nargs=-1)
@click.argument("DIRECTORY")
def to_parquet(infiles: List[str], directory: str) -> None:
    """Writes one or more ISD files to a parquet table."""
    isd.parquet.write(infiles, directory)
