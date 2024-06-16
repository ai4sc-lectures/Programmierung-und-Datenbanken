from sympy.geometry import Segment, Ray
from random import random

def line_ray_intersection(line, ray):
  l = Segment(line[0], line[1])
  r = Ray(ray[0], angle = ray[1])
  if r.intersection(l):
    return 1
  else:
    return 0

#Ab hier eigener Code


test_line = [((0,0),(3,3)), ((3,3),(3,-3)), ((3,-3),(0,0))]