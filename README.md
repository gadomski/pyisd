# pyisd

Reads NOAA [Integrated Surface Database (ISD)](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) data.

[![CI](https://github.com/gadomski/pyisd/actions/workflows/ci.yaml/badge.svg)](https://github.com/gadomski/pyisd/actions/workflows/ci.yaml)
![PyPI](https://img.shields.io/pypi/v/isd)
[![Documentation Status](https://readthedocs.org/projects/isd/badge/?version=latest)](https://isd.readthedocs.io/en/latest/?badge=latest)

## Installation

```shell
$ pip install isd
```

## Usage

There is a simple command line interface.
The `isd record` command prints a single record in JSON format:

```shell
$ isd record 720538-00164-2021
```

The Python API allows reading compressed and uncompressed ISD files:

```python
import isd
with isd.open("isd-file") as records_iterator:
    records = list(records_iterator)
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
