# Lesson plan
  
  ** Zu ergänzender Code: **
```
def construct_ray(point):
  random_ray = (point, random() * 360)
  return random_ray

def point_in_polygon(poly, point):
  ray = construct_ray(point)
  intersections = 0
  for line in poly:
    intersections += line_ray_intersection(line, ray)
  if (intersections % 2) == 0:
    return False
  else:
    return True

test_line = [((0,0),(3,3)), ((3,3),(3,-3)), ((3,-3),(0,0))]
print(point_in_polygon(test_line, (1,0))) 
```