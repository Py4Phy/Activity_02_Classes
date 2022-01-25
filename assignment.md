<!-- -*- coding: utf-8 -*- -->
# Activity 02: Classes
[![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=main)](../../actions/workflows/classroom.yml) ![Points badge](../../blob/badges/.github/badges/points.svg)


Solve the following problems.

See https://py4phy.github.io/PHY432/modules/python/objects/ for help.


## Classes create new Python objects

### `Sphere` class definition
Create a file `bodies.py` that contains the class `Sphere`.

* A `Sphere` instance is initialized with its *position* (Cartesian
  coordinates a list or tuple with three floating point numbers) and
  optionally its *radius*; the default for *radius* is 1.0.
* Store the position in an attribute `pos` and the radius in attribute `radius`.
* The class has a method `volume()` that returns the volume of the sphere.
* The class has a method `translate(t)`, that changes the position of
  the sphere by adding the translation vector `t` (tuple with three
  floats) to the current position.


### Instantiation: A ball is a sphere

Create a file `balls.py` in which you

1. create an object representing a ball by instantiating a `Sphere` at
   position `(0, 0, 10)` with radius 2 and assigning it to variable
   `ball`
2. change the position of the ball to `(-5, 0, 0)`,
3. assign the volume of the ball to a variable `volume` and print it to 3 decimals,
4. translate the ball by `(5, 0, 0)`

After each step, print the position of the ball.


### Independence: A balloon is not a ball

Create a file `ball_oons.py` in which you

1. create a ball (as a `Sphere`) at position `(0, 0, 10)` with radius
   2 (variable `ball`),
2. create a balloon (as a `Sphere`) at position `(0, 0, 10)` with radius
   6 (variable `balloon`),
3. change the ball's position to `(-1, -1, 0)`
4. compare the balloon's and the ball's position by printing
   ```python
   print(f"ball at {ball.pos} != balloon at {balloon.pos}")
   ```
   
### Inheritance: Earth is a Sphere

In file `astronomy.py`, define a class `Planet` that is derived from
`Sphere` and is instantiated as `Planet(name, pos, mass, radius)`.

`Planet` must have a method `Planet.density()` that returns the
density of the planet, mass/volume.

Use your class to represent Earth (quantities from <http://www.wolframalpha.com>)
```python
# lengths in m and mass in kg
earth = Planet("Earth", (1.4959802296e11 , 0, 0), 5.9721986e24, 6371e3)
print(earth.density())
```
and print the density.
