#! /usr/bin/env python3

# Imports
import sys
import json

# Single source versioning
# Learnt from https://stackoverflow.com/a/7071358/13095028
from .__version import __version__

def nbcheck(nbdirs, return_ooo_cells=False):
    """
    Given a list of directories pointing to Jupyter notebooks, checks that code cells
    are run in order.

    Note: Usage of f-strings in this code requires Python 3.6, introduced in
    [PEP 498](https://www.python.org/dev/peps/pep-0498/)

    Usage
    -----
    >>> nbdirs = ["notebook1.ipynb", "notebook2.ipynb"]
    >>> nbcheck(nbdirs)

    Input
    -----
    nbdirs: list
        List of directories / PathLikes.
        Note `open()` wasn't able to handle PathLikes until the ability was introduced in
        Python 3.6 via [PEP 519](https://www.python.org/dev/peps/pep-0519/)

    return_ooo_cells: bool
        Returns out-of-order cells instead of 0 / 1 if True. Primarily for testing purposes only.


    Output
    ------
    results: boolean / dict
        If return_ooo_cells is True, returns dict w/ format {nbdir: cells_out_of_order} for testing purposes.
        Else, returns 0 for perfect notebooks, and returns 1 for notebooks w/ cells out of order.
    """
    results = {}

    for nbdir in nbdirs:
        # Load notebook
        try:
            with open(nbdir, "r") as f:
                file = json.load(f)
        except json.decoder.JSONDecodeError:
            print(f"{nbdir}: Not a notebook, skipped!")
            continue

        # Retrieve cells only as a list
        cells = file["cells"]

        # Preserve only code cells
        cells = [i for i in cells if i["cell_type"] == "code"]
        num_cells = len(cells)

        # Remove code cells that are not run and raise warnings
        cells = [i for i in cells if isinstance(i["execution_count"], int)]

        if num_cells - len(cells) != 0:
            print(f"{nbdir}: Warning: {num_cells - len(cells)} code cells are not run!")
            num_cells = len(cells)

        # Check that all cells are sorted
        cells_out_of_order = []

        for i in range(1, num_cells):
            # Use less than since all `execution_count` numbers are unique
            if cells[i]["execution_count"] < cells[i - 1]["execution_count"]:
                cells_out_of_order.append(i)

        # Track results
        results[nbdir] = cells_out_of_order

        # Print closing message
        if len(cells_out_of_order) == 0:
            print(f"{nbdir}: All cells executed in order!")

        else:
            print(f"{nbdir}: {len(cells_out_of_order)} cells executed out of order!")
            print(f"{nbdir}: Cells: {cells_out_of_order}")

    if return_ooo_cells is False:
        if len(results) == 0:
            return 0
        else:
            return 1
    else:
        return results


def cli_nbcheck():
    # Retrieve list of notebook(s)
    nbdirs = sys.argv[1:]

    # Run check
    results = nbcheck(nbdirs)
    return results
