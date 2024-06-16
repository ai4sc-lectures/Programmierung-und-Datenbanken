from sympy.geometry import Segment, Ray
from random import random


def line_ray_intersection(line, ray):
  l = Segment(line.start.as_tuple(), line.end.as_tuple())
  r = Ray(ray[0], angle=ray[1])
  if r.intersection(l):
    return 1
  else:
    return 0


def construct_ray(point):
  random_ray = (point.as_tuple(), random() * 360)
  return random_ray


def point_in_polygon(poly, point):
  ray = construct_ray(point)
  intersections = 0
  for line in poly.lines:
    intersections += line_ray_intersection(line, ray)
  if (intersections % 2) == 0:
    return False
  else:
    return True
