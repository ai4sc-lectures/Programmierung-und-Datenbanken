import math

def distance(p1, p2):
  a = p1[0] - p2[0]
  b = p1[1] - p2[1]
  result = math.sqrt((a**2)+(b**2))
  return result

#Eigener Code ab hier

def calculate_cost(road):
