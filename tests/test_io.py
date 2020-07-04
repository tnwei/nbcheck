from nbcheck import nbcheck
from pathlib import Path

fdir = Path(__file__).parent

def test_multiple_files():
    """
    Tests that multiple files can be processed

    Expected stdout:
    tests/cells-not-in-order.ipynb: 2 cells executed out of order!
    tests/cells-not-in-order.ipynb: Cells: [3, 7]
    tests/cells-in-order.ipynb: All cells executed in order!
    tests/no-code-cells.ipynb: All cells executed in order!
    tests/not-a-notebook.txt: Not a notebook, skipped!

    Expected return:
    {PosixPath('tests/cells-not-in-order.ipynb'): [3, 7],
    PosixPath('tests/cells-in-order.ipynb'): [],
    PosixPath('tests/no-code-cells.ipynb'): []}

    """
    nbdirs = [
        fdir / "cells-not-in-order.ipynb",
        fdir / "cells-in-order.ipynb",
        fdir / "no-code-cells.ipynb",
        fdir / "not-a-notebook.txt"
    ]
    results = nbcheck(nbdirs)
    expected_results = dict(zip(nbdirs, [[3, 7], [], []]))
    assert results == expected_results