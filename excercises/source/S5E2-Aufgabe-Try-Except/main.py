try:
  pass
except ZeroDivisionError:
  print("Division failed!")
else:
  print("No exception occurred.")

try:
  pass
except NameError:
  print("Undefined name found!")
else:
  print("No exception occurred.")

try:
  pass
except IndexError:
  print("List index out of range!")
else:
  print("No exception occurred.")

try:
  pass
except RecursionError:
  print("Infinite recursion detected!")
else:
  print("No exception occurred.")
