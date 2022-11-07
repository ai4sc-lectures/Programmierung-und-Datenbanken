# Übung 5.2
  
**Try and Except** 

In dieser Übung geht es darum selbst gezielt Fehler zu erzeugen.

Die ```try```-```except``` Statements mit den passenden Fehlermeldungen und Exceptions sind bereit vorgegeben. Die ```pass``` Statements müssen mit fehlerhaftem Code ersetzt werden, um jeweils den zugeordneten Fehler innerhalb des ```try```-Blocks auftreten zu lassen.

Ist dir eine der Exceptions nicht bekannt, dann versuche im Internet nach Beispielen zu suchen.

## Tipps und Hinweise

```pass``` ist äquivalent zu einer leeren Zeile, kann also ohne weiteres gelöscht werden. Es ist nur notwendig um keine Syntaxfehler in leeren ```if```- oder ```try```-Blöcken entstehen zu lassen.

```RecursionError``` - Die rekursive Funktion die den Fehler erzeugt muss bereits vor dem Try-Block definiert werden.

## Vorgegebener Code

``` Python
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

```