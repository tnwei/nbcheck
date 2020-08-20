from nbcheck import nbcheck
from pathlib import Path

fdir = Path(__file__).parent

def test_notebook_in_order():
    """
    Tests that a notebook w/ all code cells executed in
    order is determined so correctly.

    Expected stdout:
    tests/cells-in-order.ipynb: All cells executed in order!

    Expected return:
    {'tests/cells-in-order.ipynb': []}
    """
    nbdirs = [fdir / "cells-in-order.ipynb"]
    results = nbcheck(nbdirs, return_ooo_cells=True)
    expected_results = dict(zip(nbdirs, [[]]))
    assert results == expected_results


def test_notebook_not_in_order():
    """
    Tests that a notebook with cells not in order are
    detected correctly.

    Expected stdout:
    tests/cells-not-in-order.ipynb: 2 cells executed out of order!
    tests/cells-not-in-order.ipynb: Cells: [3, 7]

    Expected return:
    {'tests/cells-not-in-order.ipynb': [3, 7]}
    """
    nbdirs = [fdir / "cells-not-in-order.ipynb"]
    results = nbcheck(nbdirs, return_ooo_cells=True)
    expected_results = dict(zip(nbdirs, [[3, 7]]))
    assert results == expected_results


def test_no_code_cells():
    """
    Tests the edge case where a notebook has no code cells.

    Expected stdout:
    tests/no-code-cells.ipynb: All cells executed in order!

    Expected return:
    {'tests/no-code-cells.ipynb': []}
    """
    nbdirs = [fdir / "no-code-cells.ipynb"]
    results = nbcheck(nbdirs, return_ooo_cells=True)
    expected_results = dict(zip(nbdirs, [[]]))
    assert results == expected_results


def test_not_a_notebook():
    """
    Raises errors when files that are not Jupyter notebooks
    are passed.

    Expected stdout:
    tests/not-a-notebook.txt: Not a notebook, skipped!

    Expected return:
    {}
    """
    nbdirs = [fdir / "not-a-notebook.txt"]
    results = nbcheck(nbdirs, return_ooo_cells=True)
    expected_results = {}
    assert results == expected_results
