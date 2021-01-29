# -*- coding: utf-8 -*-

import pytest

from nba_predictions.skeleton import fib

__author__ = "Brett Harder"
__copyright__ = "Brett Harder"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
