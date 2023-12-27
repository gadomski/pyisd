# pyisd

[![Tests](https://img.shields.io/github/actions/workflow/status/gadomski/pyisd/tests.yml?style=for-the-badge&label=Tests)](https://github.com/gadomski/pyisd/actions/workflows/tests.yaml)
[![Lint](https://img.shields.io/github/actions/workflow/status/gadomski/pyisd/lint.yml?style=for-the-badge&label=Lint)](https://github.com/gadomski/pyisd/actions/workflows/lint.yaml)
[![PyPI - Version](https://img.shields.io/pypi/v/isd?style=for-the-badge)](https://pypi.org/project/isd/)
[![Read the Docs (version)](https://img.shields.io/readthedocs/isd/stable?style=for-the-badge)](https://isd.readthedocs.io)

Reads NOAA [Integrated Surface Database (ISD)](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) data.

## Installation

```shell
pip install isd
```

## Usage

There is a simple command line interface.
The `isd record` command prints a single record in JSON format:

```shell
isd record 720538-00164-2021
```

The Python API allows reading compressed and uncompressed ISD files:

```python
import isd.io

with isd.io.open("isd-file") as records_iterator:
    records = list(records_iterator)
```

There is currently no parsing of the `additional_data` section, but all mandatory fields are parsed out into appropriately-typed fields on a `Record`.

## Development

Install the development requirements and the package in editable mode:

```shell
pip install -e '.[dev]'
```

To run the unit tests:

```shell
pytest
```

## Release

To cut a new release of **pyisd** (assuming you have the appropriate permissions):

1. Create a new branch, e.g. `release/v0.1.4`.
2. Update pre-commit hooks: `pre-commit autoupdate`
3. Update the [CHANGELOG](CHANGELOG.md) and [pyproject.toml](./pyproject.toml).
4. Open a pull request with the changes.
5. Merge the pull request once all required checks pass.
6. Create an annotated tag, e.g. `git tag -a v0.1.4`.
7. Push the annotated tag to github.
   This will trigger a new pypi release.
