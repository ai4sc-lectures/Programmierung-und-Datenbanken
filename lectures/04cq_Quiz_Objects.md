## Objekte

```{quizdown}
	---
	shuffleQuestions: true
	shuffleAnswers: true
	---

    ### Was beschreibt ein Objekt in der objektorientierten Programmierung?
    - [x] Eine Einheit mit Zustand (Attribute) und Verhalten (Methoden)
    - [ ] Eine reine Datenstruktur ohne Funktionen
    - [ ] Nur eine Methode in einem Programm
    - [ ] Eine Zeile in einer Datenbank

    ### Wozu dienen Methoden in einem Objekt?
    - [x] Zur Änderung des Objektzustands
    - [ ] Zur Definition von Klassen
    - [ ] Zum Kompilieren des Codes
    - [ ] Zur Initialisierung von Attributen

    ### Warum verwendet man Objekte bei wiederholenden Datenstrukturen?
    - [x] Um missverständliche Strukturen zu vermeiden
    - [x] Um redundante Strukturen zu vermeiden
    - [ ] Um Daten alphabetisch zu sortieren
    - [ ] Um den Programmfluss zu verlangsamen

    ### Welcher Nachteil ergibt sich aus unterschiedlichen Datentypen wie Liste und Tupel zur Darstellung eines Punkts?
    - [x] Sie haben unterschiedliche Syntax und Verhalten
    - [x] Sie führen zu uneinheitlichem Zugriff
    - [ ] Sie sind nicht speicherbar in Python
    - [ ] Sie brauchen zwingend gleiche Länge

    ### Warum helfen Objekte bei semantischen Problemen?
    - [x] Sie machen Bedeutung der Werte durch Attributnamen klar
    - [ ] Sie ersetzen alle Werte automatisch durch Strings
    - [ ] Sie benötigen keine Werte zur Laufzeit
    - [ ] Sie wandeln alles in Listen um

    ### Warum kann die Funktion `distance(a, b)` problematisch sein?
    ```python
    def distance(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    ```
    - [x] Sie ist nicht auf einen bestimmten Typ beschränkt
    - [ ] Sie verwendet `math` und das ist nicht erlaubt
    - [ ] Sie benötigt Strings statt Zahlen
    - [ ] Sie berechnet die Distanz nicht korrekt

    ### Sortiere die folgenden Zeilen, um eine einfache Klasse `Punkt` korrekt zu definieren:
    ```python
    # Instanziiere ein Objekt
    ```
    1. `class Punkt:`
    2. `  def __init__(self, x, y):`
    3. `    self.x = x`
    4. `    self.y = y`
    5. `p = Punkt(1, 2)`

    ### Welcher Fehler steckt in diesem Beispiel?
    ```python
    class Hund:
        def bellen():
            print("Wuff")

    h = Hund()
    h.bellen()
    ```
    - [x] Der Methode fehlt der Parameter `self`
    - [ ] Die Methode heißt falsch
    - [ ] Die Klasse `Hund` darf nicht so definiert werden
    - [ ] Methoden dürfen nicht `print` verwenden

    ### Welcher Fehler kann in folgendem Beispiel auftreten?
    ```python
    import math

    def distance(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    print(distance("Berlin", "Paris"))
    ```
    - [x] Strings sind keine gültigen Punktkoordinaten
    - [ ] Der Funktionsname ist reserviert
    - [ ] `math.sqrt` funktioniert nicht
    - [ ] Die Funktion hat keine Rückgabe


    ### Was ist der Zweck des Konstruktors `__init__()`?
    - [x] Initialisierung von Attributen beim Erzeugen eines Objekts
    - [x] Durchführung von Startaufgaben wie Berechnungen oder Prüfungen
    - [ ] Erstellen von Klassennamen
    - [ ] Kompilieren von Methoden

    ### Was passiert, wenn kein Konstruktor definiert wird?
    - [x] Python erzeugt automatisch einen leeren Konstruktor
    - [ ] Das Programm wird nicht ausgeführt
    - [ ] Es wird ein Fehler geworfen
    - [ ] Alle Attribute werden automatisch gesetzt

    ### Was beschreibt ein Instanzattribut?
    - [x] Eine Eigenschaft, die in jeder Objektinstanz unterschiedlich sein kann
    - [ ] Eine Eigenschaft, die alle Klassen gemeinsam haben
    - [ ] Ein Modul-Import
    - [ ] Eine Klasse im Konstruktor

    ### Warum verwendet man `self` im Konstruktor?
    - [x] Um Attribute der Instanz zu definieren
    - [ ] Um Klassenmethoden zu importieren
    - [ ] Um globale Variablen zu ersetzen
    - [ ] Um den Konstruktor aufzurufen

    ### Warum verwendet man Klassen in Python?
    - [x] Um Objekte zu strukturieren und Daten + Verhalten zu bündeln
    - [x] Um einen Bauplan für gleichartige Objekte zu schaffen
    - [ ] Um schneller zu kompilieren
    - [ ] Um Variablennamen zu ersetzen

    ### Was gehört typischerweise zur Definition einer Klasse?
    - [x] Welche Attribute ein Objekt hat
    - [x] Welche Methoden ein Objekt bereitstellt
    - [ ] Welche Module importiert werden
    - [ ] Welche Variablen global verfügbar sind

    ### Sortiere die folgenden Zeilen, um eine vollständige Klasse `Hund` mit Konstruktor zu definieren:
    ```python
    # Erzeuge ein Objekt mit Eigenschaften
    ```
    1. `class Hund:`
    2. `  def __init__(self, name):`
    3. `    self.name = name`
    4. `mein_hund = Hund("Fiffi")`


    ### Was passiert, wenn bei folgender Klasse keine Argumente übergeben werden?
    ```python
    class Point:
        def __init__(self, x = 0.0, y = 0.0):
            self.x = x
            self.y = y

    p = Point()
    ```
    - [x] Die Werte `0.0` werden für `x` und `y` verwendet
    - [ ] Es wird ein Fehler ausgegeben
    - [ ] Die Attribute bleiben undefiniert
    - [ ] Die Konstruktion ist in Python nicht erlaubt

    ### Was ist ein Klassenattribut?
    - [x] Ein Attribut, das allen Instanzen einer Klasse gemeinsam ist
    - [ ] Ein Attribut, das innerhalb der Methode `__init__()` definiert wird
    - [ ] Eine Methode mit Funktionsinhalt
    - [ ] Ein lokal verwendetes Attribut

    ### Welche Gefahr besteht bei veränderlichen Klassenattributen?
    - [x] Änderungen durch eine Instanz wirken sich auf alle anderen aus
    - [ ] Sie sind nicht zugänglich von Methoden
    - [ ] Sie werden nicht gespeichert
    - [ ] Sie führen zu Syntaxfehlern

    ### Was ist eine Methode in einer Klasse?
    - [x] Eine Funktion, die auf eine Instanz der Klasse angewendet wird
    - [ ] Eine globale Funktion
    - [ ] Eine Variable mit Funktionsinhalt
    - [ ] Eine Schleife mit Klassenname

    ### Warum hat eine Methode in einer Klasse immer `self` als ersten Parameter?
    - [x] Damit sie auf Attribute der Instanz zugreifen kann
    - [ ] Damit der Konstruktor korrekt aufgerufen wird
    - [ ] Damit man sie nur einmal aufrufen kann
    - [ ] Damit sie von außen nicht sichtbar ist

    ### Was ist eine Klasseninstanz?
    - [x] Ein konkretes Objekt, das nach dem Bauplan der Klasse erstellt wurde
    - [ ] Eine Methode einer Klasse
    - [ ] Eine spezielle Variable im Konstruktor
    - [ ] Eine Liste von Methoden

    ### Wie wird eine Instanz einer Klasse erzeugt?
    - [x] Durch Aufruf des Klassennamens mit passenden Argumenten
    - [ ] Durch Aufruf von `__init__()` direkt
    - [ ] Durch eine Zuweisung im Konstruktor
    - [ ] Durch Deklaration mit `new`

    ### Was ist der Vorteil benannter Parameter bei der Objekterzeugung?
    - [x] Die Reihenfolge der Argumente spielt keine Rolle mehr
    - [ ] Die Parameter werden automatisch validiert
    - [ ] Es wird automatisch `self` übergeben
    - [ ] Nur benannte Parameter sind erlaubt in Python

    ### Wie greift man auf das Attribut `x` eines Objekts `p` zu?
    - [x] Mit `p.x`
    - [ ] Mit `x.p`
    - [ ] Mit `p->x`
    - [ ] Mit `get(x, p)`

    ### Was gibt folgender Ausdruck zurück?
    ```python
    point_1.unit
    ```
    - [x] Das Klassenattribut `unit` von `point_1`
    - [ ] Den Standardwert von `x`
    - [ ] Die Methode `unit()` als Funktion
    - [ ] Eine Fehlermeldung

    ### Was passiert bei folgender Anweisung?
    ```python
    point_1.x = 54.08
    ```
    - [x] Der Wert des Attributs `x` von `point_1` wird auf `54.08` gesetzt
    - [ ] Es wird ein neues Attribut `x` erstellt
    - [ ] Das Klassenattribut wird überschrieben
    - [ ] Eine neue Instanz wird erzeugt

    ### Was ist Polymorphismus?
    - [x] Die Fähigkeit, dass verschiedene Klassen die gleiche Methode unterschiedlich implementieren
    - [ ] Eine spezielle Art von Schleife
    - [ ] Eine Methode, die nur in einer Klasse existiert
    - [ ] Eine Variable, die mehrere Typen annehmen kann

    ### Was ist Kapselung?
    - [x] Das Verbergen von Implementierungsdetails und Zugriff auf Attribute über Methoden
    - [ ] Eine spezielle Art von Datenstruktur
    - [ ] Eine Methode, die nur in einer Klasse existiert
    - [ ] Eine Variable, die nur innerhalb der Klasse sichtbar ist

    ### Was ist Vererbung?
    - [x] Die Möglichkeit, eine Klasse von einer anderen abzuleiten und deren Eigenschaften zu übernehmen
    - [ ] Eine spezielle Art von Schleife
    - [ ] Eine Methode, die nur in einer Klasse existiert
    - [ ] Eine Variable, die mehrere Typen annehmen kann
    - [ ] Eine Klasse, die keine Attribute hat

    ### Was sind objektorientierte Programmierparadigmen?
    - [x] Polymorphismus
    - [x] Kapselung
    - [ ] Multiplizität
    - [ ] Redundanz
    - [x] Vererbung
    - [x] Generalisierung
    - [ ] Spezialisierung

    ### Was ist UML?
    - [x] Eine grafische Notation für Software-Design
    - [ ] Die Programmiersprache
    - [ ] Die Datenbank-Sprache
    - [ ] Eine Art von Algorithmus 
```