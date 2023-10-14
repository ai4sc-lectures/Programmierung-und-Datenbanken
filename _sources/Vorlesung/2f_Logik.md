---
primaryColor: steelblue
secondaryColor: '#e8e8e8'
textColor: black
shuffleQuestions: false
shuffleAnswers: true
locale: de
---

## Boolesche Logik
 
Die Computer CPU kann nur einfache logische Operationen ausführen wie NOT, AND, OR, XOR und Negationen. Aus diesen Grundoperationen lassen sich komplexere Operationen zusammen.

#### Was sind Binäre Zahlen?

> Binäre Zahlen sind ein Zahlensystem mit nur den Ziffern 0 und 1 und somit das kleinste mögliche Zahlensystem. In Programmiersprachen oft als Repräsentation von Binärcode genutzt und durch die Wahreitswerten "falsch" (0) und "wahr" (1) ausgedrückt.

- [x] Das kleinste mögliche (nützliche) System von Zeichen
- [x] Mögliche Repräsentationen von Binärcode
- [x] Ein Zahlensystem, das nur aus 1 und 0 besteht
- [x] In manchen Programmiersprachen mit den Wahreitswerten "falsch" (0) und "wahr" (1)

#### Was ist Binärcode?

> Ein Binärcode ist ein Code, in dem Informationen durch Sequenzen von zwei verschiedenen Symbolen (zum Beispiel 1/0 oder wahr/falsch) dargestellt werden.

- [x] Ein Code der durch Binärcode representiert werden kann
- [x] Ein Code der durch boolesche Werte (wahr/falsch) representiert werden kann
- [x] Maschinencode eines Computerprogramms
- [ ] Ein Zahlensystem mit 10 Symbolen (0 bis 9)
- [ ] Ein Darstellung von Text in natürlicher Sprache
- [ ] Ein Darstellung von Grafikdateien

#### Was ist die AND Operation?

|      A     |      B     | A AND B  |
|:----------:|:----------:|----------|
| Falsch (0) | Falsch (0) |          |
| Falsch (0) |   Wahr (1) |          |
|   Wahr (1) | Falsch (0) |          |
|   Wahr (1) |   Wahr (1) |          |

> Die AND-Operation (UND-Operation) ist eine grundlegende logische Operation in der Digitaltechnik und der Booleschen Algebra. Die AND-Operation gibt als Ergebnis "1" (wahr) aus, wenn beide Eingangssignale "1" sind. Andernfalls gibt sie "0" (falsch) aus.

- [x] Falsch, Falsch, Falsch,   Wahr
- [ ] Falsch,   Wahr,   Wahr,   Wahr
- [ ] Falsch,   Wahr,   Wahr, Falsch
- [ ]   Wahr,   Wahr,   Wahr, Falsch
- [ ]   Wahr, Falsch, Falsch, Falsch

#### Was ist die OR Operation?

|      A     |      B     | A OR B   |
|:----------:|:----------:|----------|
| Falsch (0) | Falsch (0) |          |
| Falsch (0) |   Wahr (1) |          |
|   Wahr (1) | Falsch (0) |          |
|   Wahr (1) |   Wahr (1) |          |

> Die OR-Operation (ODER-Operation) ist eine grundlegende logische Operation in der Booleschen Algebra und der Digitaltechnik.  Die OR-Operation gibt als Ergebnis "1" (wahr) aus, wenn mindestens eines der Eingangssignale "1" ist. Sie gibt "0" (falsch) aus, wenn beide Eingangssignale "0" sind.

- [ ] Falsch, Falsch, Falsch,   Wahr
- [x] Falsch,   Wahr,   Wahr,   Wahr
- [ ] Falsch,   Wahr,   Wahr, Falsch
- [ ]   Wahr,   Wahr,   Wahr, Falsch
- [ ]   Wahr, Falsch, Falsch, Falsch

#### Was ist die XOR Operation?

|      A     |      B     |  A OR B  |
|:----------:|:----------:|----------|
| Falsch (0) | Falsch (0) |          |
| Falsch (0) |   Wahr (1) |          |
|   Wahr (1) | Falsch (0) |          |
|   Wahr (1) |   Wahr (1) |          |

> Die XOR-Operation (Exklusiv-Oder-Operation) ist eine weitere grundlegende logische Operation in der Booleschen Algebra und der Digitaltechnik. Im Gegensatz zur OR-Operation, die wahr (1) ausgibt, wenn mindestens eines der Eingangssignale wahr ist, gibt die XOR-Operation nur dann wahr aus, wenn genau ein Eingangssignal wahr ist. Wenn beide Eingangssignale wahr oder beide falsch sind, gibt die XOR-Operation falsch aus.

- [ ] Falsch, Falsch, Falsch,   Wahr
- [ ] Falsch,   Wahr,   Wahr,   Wahr
- [x] Falsch,   Wahr,   Wahr, Falsch
- [ ]   Wahr,   Wahr,   Wahr, Falsch
- [ ]   Wahr, Falsch, Falsch, Falsch

#### Was ist die NOT Operation?

|      A     | NOT A    |
|:----------:|----------|
| Falsch (0) |          |
|   Wahr (1) |          |

> Die NOT-Operation (auch "NICHT-Operation" oder "Invertierungsoperation" genannt) ist eine grundlegende logische Operation in der Booleschen Algebra und der Digitaltechnik.  Die NOT-Operation kehrt den Zustand des Eingangssignals um. Wenn "A" wahr (1) ist, wird "NOT A" falsch (0), und wenn "A" falsch (0) ist, wird "NOT A" wahr (1).

- [ ] Falsch, Falsch
- [ ] Falsch,   Wahr
- [x]   Wahr, Falsch
- [ ]   Wahr,   Wahr

#### Was ist die NAND Operation?

|      A     |      B     | A NAND B |
|:----------:|:----------:|----------|
| Falsch (0) | Falsch (0) |          |
| Falsch (0) |   Wahr (1) |          |
|   Wahr (1) | Falsch (0) |          |
|   Wahr (1) |   Wahr (1) |          |

> Die NAND-Operation ist eine grundlegende logische Operation in der Booleschen Algebra und der Digitaltechnik. Der Name "NAND" steht für "NOT AND," was darauf hinweist, dass die NAND-Operation eine Kombination aus der AND-Operation und der NOT-Operation ist und das Gegenteil des Ergebnisses der AND-Operation ausgibt.  Die NAND-Operation ergibt "1" (wahr), es sei denn, beide Eingangssignale sind "1." In diesem Fall ergibt sie "0" (falsch).

- [ ] Falsch, Falsch, Falsch,   Wahr
- [ ] Falsch,   Wahr,   Wahr,   Wahr
- [ ] Falsch,   Wahr,   Wahr, Falsch
- [x]   Wahr,   Wahr,   Wahr, Falsch
- [ ]   Wahr, Falsch, Falsch, Falsch

#### Was ist die NOR Operation?

|      A     |      B     | A NOR B  |
|:----------:|:----------:|----------|
| Falsch (0) | Falsch (0) |          |
| Falsch (0) |   Wahr (1) |          |
|   Wahr (1) | Falsch (0) |          |
|   Wahr (1) |   Wahr (1) |          |

> Die NOR-Operation ist eine grundlegende logische Operation in der Booleschen Algebra und der Digitaltechnik. Der Name "NOR" steht für "NOT OR," was darauf hinweist, dass die NOR-Operation eine Kombination aus der OR-Operation und der NOT-Operation ist und das Gegenteil des Ergebnisses der OR-Operation ergibt.  Die NAND-Operation ergibt "1" (wahr), es sei denn, beide Eingangssignale sind "1." In diesem Fall ergibt sie "0" (falsch).

- [ ] Falsch, Falsch, Falsch,   Wahr
- [ ] Falsch,   Wahr,   Wahr,   Wahr
- [ ] Falsch,   Wahr,   Wahr, Falsch
- [ ]   Wahr,   Wahr,   Wahr, Falsch
- [x]   Wahr, Falsch, Falsch, Falsch

#### Was ist die NXOR Operation?

|      A     |      B     | A NXOR B |
|:----------:|:----------:|----------|
| Falsch (0) | Falsch (0) |          |
| Falsch (0) |   Wahr (1) |          |
|   Wahr (1) | Falsch (0) |          |
|   Wahr (1) |   Wahr (1) |          |

> Die NXOR-Operation (auch als XNOR oder Äquivalenzoperation bezeichnet) ist eine logische Operation in der Booleschen Algebra und der Digitaltechnik. Der Name "NXOR" steht für "NOT XOR" und zeigt an, dass es eine Kombination aus der XOR-Operation und der NOT-Operation ist und das Gegenteil des Ergebnisses der XOR-Operation ergibt. Die NXOR-Operation ergibt "1" (wahr), wenn beide Eingangssignale gleich sind (entweder beide "0" oder beide "1"). Sie ergibt "0" (falsch), wenn die Eingangssignale unterschiedlich sind (eins "0" und das andere "1").

- [ ] Falsch, Falsch, Falsch,   Wahr
- [ ] Falsch,   Wahr,   Wahr,   Wahr
- [ ] Falsch,   Wahr,   Wahr, Falsch
- [ ]   Wahr,   Wahr,   Wahr, Falsch
- [x]   Wahr, Falsch, Falsch,   Wahr