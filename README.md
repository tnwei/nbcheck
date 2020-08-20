# nbcheck

Simple CLI tool to check Jupyter notebook reproducibility, highlighting cells executed out of order. 

## Usage as pre-commit hook

This repo is written as a plugin to the `pre-commit` framework. Commits will only pass if all notebook cells are executed in order. To ignore the warning, users will need to pass the `--no-verify` flag to `git commit`.

If you're following the [`pre-commit` quickstart](https://pre-commit.com/#quick-start), this is part of Step 2. Specify this repo as part of `.pre-commit-config.yaml` as follows: 

``` yaml
repos:
-  repo: https://github.com/tnwei/nbcheck
   rev: v0.0.2
   hooks:
     - id: nbcheck
```

Note: replace `rev` with the latest tag on this repo.

## Output example

``` bash
(base) tnwei@rama:~/projects/test$ git add cells-not-in-order.ipynb
(base) tnwei@rama:~/projects/test$ pre-commit run
Check Jupyter notebook cells executed out of order.......................Failed
- hook id: nbcheck
- exit code: 1

cells-not-in-order.ipynb: 2 cells executed out of order!
cells-not-in-order.ipynb: Cells: [3, 7]
```
