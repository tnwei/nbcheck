from nbcheck import nbcheck
from pathlib import Path

fdir = Path(__file__).parent

def test_notebook_in_order():
    """
    Tests that a notebook w/ all code cells executed in
    order is determined so correctly.
    """
    nbdirs = [fdir / "cells-in-order.ipynb"]
    results = nbcheck(nbdirs)
    print(results)


def test_notebook_not_in_order():
    """
    Tests that a notebook with cells not in order are
    detected correctly.
    """
    nbdirs = [fdir / "cells-not-in-order.ipynb"]
    results = nbcheck(nbdirs)
    print(results)


def test_no_code_cells():
    """
    Tests the edge case where a notebook has no code cells.
    """
    nbdirs = [fdir / "no-code-cells.ipynb"]
    results = nbcheck(nbdirs)
    print(results)


def test_not_a_notebook():
    """
    Raises errors when files that are not Jupyter notebooks
    are passed.
    """
    nbdirs = [fdir / "not-a-notebook.txt"]
    results = nbcheck(nbdirs)
    print(results)
