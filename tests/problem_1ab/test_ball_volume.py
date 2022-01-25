# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 02 (Classes)
# PROBLEM NUMBER: 1ab

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'ball.py'
POINTS = 2

def test_ball_volume():
    return _test_variable("volume", 33.510321638291124,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )
