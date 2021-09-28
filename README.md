# pyisd

Reads NOAA [Integrated Surface Database (ISD)](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) data.

[![CI](https://github.com/gadomski/pyisd/actions/workflows/ci.yaml/badge.svg)](https://github.com/gadomski/pyisd/actions/workflows/ci.yaml)

## Installation

```shell
$ pip install isd
```

## Usage

There is no command line interface yet.
The Python API is pretty simple:

```python
from isd import Record
records = []
with open("isd-file") as file:
    records.append(Record.parse(file))
```

There is currently no parsing of the `additional_data` section, but all mandatory fields are parsed out into appropriately-typed fields on a `Record`.


## Development

Install the development requirements and the package in editable mode:

```shell
$ pip install -e .
$ pip install -r requirements-dev.txt
```

To run the unit tests:

```shell
$ pytest
```
