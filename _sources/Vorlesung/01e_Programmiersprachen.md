## Programmiersprachen

Programmiersprache
: Eine Programmiersprache ist eine formale Sprache für die Erstellung von Programmen zur Datenverarbeitung an einem Computer. Sie ist durch ihren Zeichensatz, Syntax und ihre Semantik definiert. Die Programmiersprache erlaub es dem Menschen (Programmierer), dem Computer in einer „verständlichen” Form das Programm zu erstellen.

### Generationen der Programmiersprachen

1. Generation - Maschinenorientierte Sprachen sind Programmiersprachen, die ein Prozessor direkt ausführen kann und meist nur für den Prozessortyp verständlich sind. Der Programmcode wird Maschinencode genannt und ist binär (0/1) codiert. 
    ```
      1101 0000 0000 0111 1011
      1011 1111 1110 1000 1010
      1101 0010 0000 0111 1111
    ```

2. Generation – Assemblersprachen nutzen Abkürzungen (ADD, MOV, …) für Maschienenbefehle eines bestimmten Prozessortyps. Der Quelltext eines Assemblerprogramms wird mit Hilfe einer Übersetzungssoftware (Assembler) in Maschinencode übersetzt.
    ```nasm
      CLO
      MOV AL, 2     ;kopiert 2 in Register AL
      ADD AL, 3     ;Addiert 3 zu Register AL
      END
    ```

3. Generation - Höhere Programmiersprachen: orientieren sich am Menschen, dem Programmierer. Ein sogenannter Compiler übersetzt den gegebenen abstrakteren Befehlssatz in den Maschinencode der gegebenen Zielarchitektur oder in eine Zwischensprache.
    ```python
      while i < 20:
          x = x + i * i
          if x > 100:
              i = i + 3
    ```

### Die beliebtesten Programmiersprachen

<!-- ![Most popular programming languages on stack overflow](images/stackoverflow.png) -->

Durch die Änderungen der Anforderungen an Software entwickeln sich nicht nur die Softwarearchitekturen sondern auch neue Programmiersprachen die an Popularität gewinnen. So wurden zuerst traditionelle Anwendungssprachen (C++) ersetzt durch Serversprachen wie Java und dann durch Websprachen (PHP, Perl, JavaScript). Über die letzten 20 Jahren hat sich in diesem Bereich vor allem JavaScript durchgesetzt da es Client- und Serverseitig eingesetzt werden kann. Seit 2017 gewinnt vor allem Python massiv an popularität, da es insbesondere im KI-Bereich eingesetzt wird.

<video width="584" height="315" controls>
  <source src="_images/top_prog_languages.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>


### Python

<!-- ![Development of popularity of python](images/python_popularity.png) -->

Python hat in den letzten Jahren zunehmend an Popularität gewonnen, ist allerdings älter als Java, C# und JavaScript. Die Popularität ist zum einen darauf zurück zu führen, dass die Sprache sehr auf Lesbarkeit und Einfachheit ausgelegt ist und dadurch sehr leicht zu erlernen ist. Ferner gibt es durch ihr Alter heutzutage sehr viele Bibliotheken und für fast jedes Problem eine existierende Lösung. Dadurch ist Python auch sehr vielseitig einsetzbar ist.