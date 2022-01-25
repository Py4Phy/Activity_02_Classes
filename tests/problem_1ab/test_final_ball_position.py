import pytest

from ..tst import get_attribute

FILENAME = "ball.py"

def test_final_ball_position(ref=(0, 0, 0)):
    ball = get_attribute('ball', FILENAME)
    try:
        assert ball.pos == pytest.approx(ref)
    except AttributeError:
        raise AssertionError("ball.ball does not have the pos attribute")

def test_ball_volume_method(ref=33.510321638291124):
    ball = get_attribute('ball', FILENAME)
    try:
        assert ball.volume() == pytest.approx(ref)
    except AttributeError:
        raise AssertionError("ball.ball does not have the volume() method")

