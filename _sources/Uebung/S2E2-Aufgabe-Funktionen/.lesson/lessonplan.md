# Musterlösung
  
```python
#Eine Begrüssungs-Funktion
def greet(name):
  begruessungsText = "Guten Tag "+ name
  return (begruessungsText)

#Konvertierung von Celsius in Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
  fahrenheit = celsius * 1.8 + 32
  return fahrenheit

#Volumenberechnung eines Würfels
def volume(x, y, z):
  v = x * y * z
  return v

#Eine Funktion die den Mittelwert aus drei Werten bildet
def mean3(a, b, c):
  m = (a + b + c)/3
  return m

#Eine Funktion die den Mittelwert aus den Volumina von drei Würfeln bildet
def calculate_volume_mean(k1, k2, k3):
  volume1 = volume(k1[0], k1[1], k1[2])
  volume2 = volume(k2[0], k2[1], k2[2])
  volume3 = volume(k3[0], k3[1], k3[2])
  volume_mean = mean3(volume1, volume2, volume3)
  return volume_mean

```


  
  