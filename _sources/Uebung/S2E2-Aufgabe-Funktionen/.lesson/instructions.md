# Aufgabe 2.2

**Simple Funktionen**

In dieser Aufgabe sollen fünf einfache Funktionen geschrieben werden. Jede von ihnen benötigt einen oder mehrere Parameter sowie eine Ausgabe. Recherchiere Formeln und Faktoren die du nicht kennst. Bitte haltet dich an die folgende Namensgebung der Funktionen:


``def greet(name):``

  Diese Funktion soll unter Berücksichtigung eines gegebenen Namens den Begrüßungstext "Guten Tag _Name_" zurückgeben. Zum Kombinieren von Strings kann der **+** Operator genutzt werden. **Achtung:** Es soll keine Ausgabe mittels ``print`` ausgeführt werden.
   
``def convert_celsius_to_fahrenheit(celsius):``

  Diese Funktion soll einen gegebenen Celsius-Wert in einen Fahrenheit-Wert umrechnen und diesen zurückgeben.

``def volume(x, y, z):``

  Diese Funktion soll das Volumen eines Quaders mit den gegebenen Seitenlängen x, y, z berechnen und zurückgeben.

``def mean3(a, b, c):``
  
  Diese Funktion soll den Mittelwert aus den gegebenen Werten a, b, c berechnen und zurückgeben.

``def calculate_volume_mean(k1, k2, k3):``
  
  Diese Funktion soll den Mittelwert aus den Volumina der Körper k1, k2 und k3 berechnen und zurückgeben. Dazu sollen bereits geschriebene Funktionen genutzt werden. k1, k2 und k3 sind dabei Listen mit jeweils drei Werten, welche die Höhe, Länge und Breite von Quadern repräsentieren.


## Hinweis:
Diesmal ist die Art es Testens eine andere - die Tests rufen die Funktionen direkt auf. Es sind keine Ausgaben mit ``print()``-Funktion notwendig. Etwaige Aufrufe der ```input()```-Funktion sind auch nicht notwendig und sollten vor dem Ausführen der Tests entfernt werden.

Gibt es Fehlermeldungen, versuche diese erst zu lesen und zu verstehen bevor du anderweitig nach Hilfe schaust. Lasse dich dabei nicht von schwer verständlichen Ausgaben wie "Stack Trace" und "Traceback..." einschüchtern, suche stattdessen nach den folgenden Zeilen welche Informationen über das eigentliche Problem geben. Eine Fehlermeldung die von einer nicht existierenden Funktion redet könnte z.B. bedeuten dass der Name der Funktion falsch geschrieben ist.