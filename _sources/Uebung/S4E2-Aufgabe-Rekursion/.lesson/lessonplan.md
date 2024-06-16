# Musterlösung

```python
def binary_search (list, start, end, x):
    if end >= start:
        mid = start + (end - start) // 2
        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return binary_search(list, start, mid-1, x)
        else:
            return binary_search(list, mid + 1, end, x)
    else:
        return -1

# Aufruf-Code zum Testen
example = [ 2, 3, 4, 10, 40 ]
x = 10
# Function call
result = binary_search(example, 0, len(example)-1, x)
 
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")
```
  