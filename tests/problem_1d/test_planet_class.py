import pytest
import math

from ..tst import get_attribute

FILENAME = "astronomy.py"

def vecadd(x, y):
    return tuple(xi + yi for xi, yi in zip(x, y))

def volume(radius):
    return 4/3 * math.pi * radius**3

@pytest.fixture(scope="function",
                params=[["Vorgsphere", (0, 0, 0), 9.99999e26, 1.8e8],
                        ["Betelgeuze VI", (0, 0, -10e8), 7.878e25, 6.3e7],
                        ["Zquornshellish Zeta", (-1.23e7, 1.23e+7, -8.15e-1), 3.1415e26, 5.55e6]
                        ])
def planet_data(request):
    name, pos, mass, r = request.param
    sphere_class = get_attribute("Planet", FILENAME)
    return {'name': name, 'pos': pos, 'mass': mass, 'radius': r}, sphere_class(name, pos, mass, r)

def test_planet_class(planet_data):
    ref, planet = planet_data
    assert planet.name == ref['name']
    assert planet.pos == pytest.approx(ref['pos'])
    assert planet.mass == pytest.approx(ref['mass'])
    assert planet.radius == pytest.approx(ref['radius'])

@pytest.mark.parametrize("t", [(0., 0., 0.),
                               (10e4, -10e4, 0),
                               (10.1e4, -10e8, 1e-6),
                               (-1.234e19, 6.5e+14, 6.e-14)])
def test_translate(planet_data, t):
    ref, planet = planet_data
    reference = vecadd(ref['pos'], t)
    planet.translate(t)
    assert planet.pos == pytest.approx(reference)

def test_volume(planet_data):
    ref, planet = planet_data
    reference = volume(ref['radius'])
    assert planet.volume() == pytest.approx(reference)

def test_density(planet_data):
    ref, planet = planet_data
    reference = ref['mass'] / volume(ref['radius'])
    assert planet.density() == pytest.approx(reference)

