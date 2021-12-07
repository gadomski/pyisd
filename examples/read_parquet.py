"""Reads an ISD parquet table and prints it to stdout."""

import sys

import isd.parquet

directory = sys.argv[1]
data_frame = isd.parquet.read(directory).compute()
print(data_frame)
