# Aufgabe 4.2  

**Rekursion**

Implementiere die Methode der **binären Suche** mit Hilfe von Rekursion, d.h. die Funktion muss sich selbst wieder aufrufen. Nutze dafür folgende Funktionsdefinition: ```binary_search(list, start, end, x)```, wobei ```list``` die (sortierte) Eingabeliste ist, ```start``` und ```end``` die Indizes der Listenelemente zwischen denen grade gesucht wird und ```x``` das gesuchte Element. ``start`` und ``end`` sind notwendig um die Liste pro Rekursionsschritt weiter einzugrenzen. 

Als Ergebnis wird entweder der Listenindex der gesuchten Zahl oder der Abbruchwert -1 erwartet.

Diese Aufgabe ist anspruchsvoller als vorhergegangene Aufgaben. Bist du dir unsicher wie das Problem zu lösen ist, dann folge zur Hilfe erst dem beiliegenden Flussdiagramm. Hilft dies nicht weiter, recherchiere online nach Lösungen.

Die roten Linien geben hier die Fälle an in denen ein rekursiver Aufruf stattfindet.

  ![alt text](assets/Aufgabe_4_2.png)
  
### Wichtige Hinweise

```start``` und ```end``` müssen beim ersten Aufrufen der Funktion einfach mit 0 und dem Index des letzten Listenelementes (``len(list)-1``) belegt, jedoch im späteren Verlauf durch rekursives Aufrufen weiter eingegrenzt werden. Würde die Funktion sich nicht selbst aufrufen wären diese beiden Eingaben also nicht notwendig.

Die Berechnung des mittleren Listenelementes muss einen Integer ergeben, da Listenindizes nur ganze Zahlen sein können! Es muss also entweder gerundet oder eine Integer-Division durchgeführt werden. Der Operator für so eine Division ist ```//```.