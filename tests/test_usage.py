from nbcheck import nbcheck
from pathlib import Path

def test_notebook_in_order():
    """
    Tests that a notebook w/ all code cells executed in
    order is determined so correctly.
    """
    fdir = [Path(".") / "cells-in-order.ipynb"]
    results = nbcheck(fdir)
    print(results)


def test_notebook_not_in_order():
    """
    Tests that a notebook with cells not in order are
    detected correctly.
    """
    fdir = [Path(".") / "cells-not-in-order.ipynb"]
    results = nbcheck(fdir)
    print(results)


def test_no_code_cells():
    """
    Tests the edge case where a notebook has no code cells.
    """
    fdir = [Path(".") / "no-code-cells.ipynb"]
    results = nbcheck(fdir)
    print(results)


def test_not_a_notebook():
    """
    Raises errors when files that are not Jupyter notebooks
    are passed.
    """
    fdir = [Path(".") / "not-a-notebook.txt"]
    results = nbcheck(fdir)
    print(results)
