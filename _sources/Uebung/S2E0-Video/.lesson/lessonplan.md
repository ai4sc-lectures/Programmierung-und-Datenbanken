# Musterlösung

```python3
import math
#Berechnung zeigen
#In Funktion umwandeln
#zeigen dass Funktion aufgerufen werden muss damit sich ausführt
#Zeigen dass sie dabei vorher definiert sein muss
#Zwei Varianten mit anderen Datentypen zeigen

#Für die Übung: Aufgabenstellung genau lesen
#Etwas komplexer als letztes mal, es ist so gedacht dass man in den Vorlesungsfolien/dem Übungsvideo nach Lösungsansätzen schauen muss, bzw. gewisse Dinge auch auf Google suchen muss

#Variante 1, mit Integern
a1, a2 = 2, 3
b1, b2 = 6, 6

def distance(a1, a2, b1, b2):
  return math.sqrt((a1-b1)**2 + (a2-b2)**2)

print(distance(a1, a2, b1, b2)) #Funktion muss aufgerufen werden damit sie ausführt, und Parameter != Variablen

#Variante 2, mit Input/Strings und Konvertierung in Zahlen
def distance2():
  x_1 = float(input("Enter x1:"))
  x_2 = float(input("Enter x2:"))
  y_1 = float(input("Enter y1:"))
  y_2 = float(input("Enter y2:"))
  return math.sqrt((x_1-y_1)**2 + (x_2-y_2)**2)

print(distance2())

#Variante 3, mit Listen
pt1 = [2, 3]
pt2 = [6, 6]

def distance(p1, p2):
  return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

print(distance(pt1, pt2))
```