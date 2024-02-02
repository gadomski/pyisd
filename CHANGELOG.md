# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add support for polars ([#44](https://github.com/gadomski/pyisd/pull/44))
- Make pandas optional ([#43](https://github.com/gadomski/pyisd/pull/43))

## [0.3.0] - 2024-02-02

### Added

- Restructure library into record and batch ([#36](https://github.com/gadomski/pyisd/pull/36))

## [0.2.1] - 2023-12-27

### Fixed

- Ship `py.typed` ([#39](https://github.com/gadomski/pyisd/pull/39))

## [0.2.0] - 2021-12-21

### Removed

- geopandas support
- parquet support

## [0.1.5] - 2021-12-09

### Added

- `isd.io.from_text_io`
- Utility function for filtering records by datetime

## [0.1.4] - 2021-12-09

### Added

- Pip caching to CI

### Changed

- Downgrade dask requirement to ~=2021.08

### Fixed

- Add `dask[distributed]` to dependencies, as `distributed` is required by the cli
- API documentation

## [0.1.3] - 2021-12-08

### Added

- [shed](https://pypi.org/project/shed/) via pre-commit
- Timestamp field to the pandas data frame
- `isd.pandas.read_to_data_frame`
- Coordinate reference system to geopandas data frame points
- Example that demonstrates checking that timestamps increase monotonically for a directory of ISD files
- `since` argument for data frame creation
- parquet support

### Removed

- `isd.open` is now only available as `isd.io.open`

### Changed

- Set default python version for pre-commit

### Fixed

- Documentation
- Redundant casts

## [0.1.2] - 2020-09-30

### Added

- `isd.pandas.geo_data_frame`

## [0.1.1] - 2020-09-30

### Added

- Documentation: <https://isd.readthedocs.io/en/latest/>
- `isd.pandas.data_frame` to create a DataFrame with intelligent data types and categoricals
- Command line interface
- `isd.open`
- Badges and content to the README

### Changed

- CI tweaks
- Better checking for missing data in records

### Removed

- Helper methods in `Record`

## [0.1.0] - 2020-09-28

Initial release.

[Unreleased]: <https://github.com/gadomski/pyisd/compare/v0.3.0..main>
[0.3.0]: <https://github.com/gadomski/pyisd/compare/v0.2.1..v0.3.0>
[0.2.1]: <https://github.com/gadomski/pyisd/compare/v0.2.0..v0.2.1>
[0.2.0]: <https://github.com/gadomski/pyisd/compare/v0.1.5..v0.2.0>
[0.1.5]: <https://github.com/gadomski/pyisd/compare/v0.1.4..v0.1.5>
[0.1.4]: <https://github.com/gadomski/pyisd/compare/v0.1.3..v0.1.4>
[0.1.3]: <https://github.com/gadomski/pyisd/compare/v0.1.2..v0.1.3>
[0.1.2]: <https://github.com/gadomski/pyisd/compare/v0.1.1..v0.1.2>
[0.1.1]: <https://github.com/gadomski/pyisd/compare/v0.1.0..v0.1.1>
[0.1.0]: <https://github.com/gadomski/pyisd/tree/v0.1.0>
