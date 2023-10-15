# Lesson plan
  

Von: (Quelle: https://trinket.io/python/2da63b4823)
```Python
import Random
a = random.randint(1,12)
b = random.randint(1,12)
for i in range(l0):
  question = "What is "+a+" x "+b+"? "
  answer = input(question)
  if answer = a*b
    print (Well done!)
  else:
    print("No.")
```

Zu:
```Python
import random
a = 12
b = 12
for i in range(10):
  question = "What is "+str(a)+" x "+str(b)+"? "
  try:
    answer = int(input(question))
  except ValueError:
    print("Input error! Try again.")
    continue
  if answer == a*b:
    print("Well done!")
    break
  else:
    print("No.")
```