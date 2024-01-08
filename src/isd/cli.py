# type: ignore

import click
from click import ClickException

from isd.batch import Batch


@click.group()
def main() -> None:
    """Work with NOAA's Integrated Surface Database (ISD) from the command line."""


@main.command()
@click.argument("INFILE")
@click.option("-i", "--index", default=0)
def record(infile: str, index: int) -> None:
    """Prints a single record to standard output in JSON format."""
    batch = Batch.from_path(infile)
    try:
        record_ = batch[index]
        print(record_.to_json())
    except IndexError as e:
        raise ClickException(f"No record with index {index}") from e
