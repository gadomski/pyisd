"""Given a directory of ISD files, checks that all timesteps monotonically increase."""

import os
import sys

import tqdm

import isd.io

directory = sys.argv[1]
paths = [os.path.join(directory, file_name) for file_name in os.listdir(directory)]
all_monotonic = True
bad_paths = []
for path in tqdm.tqdm(paths):
    data_frame = isd.io.read_to_data_frame(path)
    min = data_frame.timestamp.min()
    max = data_frame.timestamp.max()
    is_monotonic = data_frame.timestamp.is_monotonic
    if not is_monotonic:
        all_monotonic = False
        bad_paths.append(path)
    tqdm.tqdm.write(f"{path}: min={min}, max={max}, is_monotonic={is_monotonic}")

if all_monotonic:
    print("All files have monotonically increasing timestamps!")
else:
    print("Not all files have monotonically increasing timestamps, here they are:")
    for path in bad_paths:
        print(f"    - {path}")
    sys.exit(1)
