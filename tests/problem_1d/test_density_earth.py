# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 02 (Classes)
# PROBLEM NUMBER: 1d

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'astronomy.py'
POINTS = 4

def test_python3():
    assert_python3()

def test_density_earth():
    return _test_output(FILENAME,
                        r"""\s*5513\.4[345][0-9]+""",
                        input_values=None,
                        regex=True)


