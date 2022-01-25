import pytest
import math

from ..tst import get_attribute

FILENAME = "bodies.py"

def vecadd(x, y):
    return tuple(xi + yi for xi, yi in zip(x, y))

def volume(radius):
    return 4/3 * math.pi * radius**3


@pytest.fixture(scope="function",
                params=[[(0, 0, 0), 2],
                        [(0, 0, -10.), 10.1],
                        [(-1.23, 1.23e+16, -8.15e-14), 3.1415e-2]
                        ])
def ball_data(request):
    pos, r = request.param
    sphere_class = get_attribute("Sphere", FILENAME)
    return {'pos': pos, 'radius': r}, sphere_class(pos, radius=r)

def test_sphere_class(ball_data):
    ref, ball = ball_data
    assert ball.pos == pytest.approx(ref['pos'])
    assert ball.radius == pytest.approx(ref['radius'])

@pytest.mark.parametrize("t", [(0., 0., 0.),
                               (10, -10, 0),
                               (10.1, -10, 0),
                               (-1.234, 6.5e+14, 6.e-14)])
def test_translate(ball_data, t):
    ref, ball = ball_data
    reference = vecadd(ref['pos'], t)
    ball.translate(t)
    assert ball.pos == pytest.approx(reference)

def test_volume(ball_data):
    ref, ball = ball_data
    reference = volume(ref['radius'])
    assert ball.volume() == pytest.approx(reference)
