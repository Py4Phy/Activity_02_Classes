# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 02 (Classes)
# PROBLEM NUMBER: 1c

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'ball_oon.py'
POINTS = 4

def test_python3():
    assert_python3()

def test_instances_independence():
    return _test_output(FILENAME,
                        r"""ball at (-1, -1, 0) != balloon at (0, 0, 10)""",
                        input_values=None,
                        regex=False)


