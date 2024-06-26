"""Given a directory of ISD files, checks that all timesteps monotonically increase."""

import os
import sys

import tqdm

from isd import Batch

directory = sys.argv[1]
paths = [os.path.join(directory, file_name) for file_name in os.listdir(directory)]
all_monotonic = True
bad_paths = []
for path in tqdm.tqdm(paths):
    data_frame = Batch.from_path(path).to_data_frame()
    min = data_frame.datetime.min()
    max = data_frame.datetime.max()
    is_monotonic_increasing = data_frame.datetime.is_monotonic_increasing
    if not is_monotonic_increasing:
        all_monotonic = False
        bad_paths.append(path)
    tqdm.tqdm.write(
        f"{path}: min={min}, max={max}, is_monotonic_increasing={is_monotonic_increasing}"
    )

if all_monotonic:
    print("All files have monotonically increasing timestamps!")
else:
    print("Not all files have monotonically increasing timestamps, here they are:")
    for path in bad_paths:
        print(f"    - {path}")
    sys.exit(1)
