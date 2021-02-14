# -*- coding: utf-8 -*-
"""
    Setup file for nba_predictions.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.3.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import sys
from pkg_resources import VersionConflict, require
from setuptools import setup

try:
    require("setuptools>=38.3")
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)

entry_points = """
[console_scripts]
nba_predictions = nba_predictions.runner:main

[setup_parsers]
nba_predictions = nba_predictions.runner:get_parser
"""

if __name__ == "__main__":
    setup(use_pyscaffold=True)
