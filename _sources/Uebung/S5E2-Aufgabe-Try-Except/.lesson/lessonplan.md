# Musterlösung

````python
try:
  1/0
except ZeroDivisionError:
  print("Division failed.")
else:
  print("No exception occurred.")

try:
  x
except NameError:
  print("Undefined name found!")
else:
  print("No exception occurred.")

try:
  x = []
  x[1]
except IndexError:
  print("List index out of range!")
else:
  print("No exception occurred.")

def func():
  func()

try:
  func()
except RecursionError:
  print("Infinite recursion detected!")
else:
  print("No exception occurred.")

````
  