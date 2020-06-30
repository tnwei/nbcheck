#! /usr/bin/env python3

# Imports
import sys
import json

# Load notebook(s)
nbdir = sys.argv[1]

with open(nbdir, "r") as f:
    file = json.load(f)

# Retrieve cells only as a list
cells = file["cells"]

# Preserve only code cells
cells = [i for i in cells if i["cell_type"] == "code"]
num_cells = len(cells)

# Remove null code cells, raise warnings on them though!
cells = [i for i in cells if isinstance(i["execution_count"], int)]

if num_cells - len(cells) != 0:
    print(f"Warning: {num_cells - len(cells)} code cells are not run!")
    num_cells = len(cells)

# Check that all cells are sorted
cells_out_of_order = []

for i in range(1, num_cells):
    # Use less than since all `execution_count` numbers are unique
    if cells[i]["execution_count"] < cells[i-1]["execution_count"]:
        cells_out_of_order.append(i)
        print(f"Cell {i} is out of order!")

# Print closing message
if len(cells_out_of_order) == 0:
    print(f"{nbdir} has all cells executed in order!")
else:
    print(f"{nbdir} has {len(cells_out_of_order)} cells ran out of order!")
