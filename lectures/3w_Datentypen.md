
# Quizz: Datentypen
 
Die Computer CPU kann nur einfache logische Operationen ausführen wie NOT, AND, OR, XOR und Negationen. Aus diesen Grundoperationen lassen sich komplexere Operationen zusammen.

```{quizdown}
	---
	shuffleQuestions: true
	shuffleAnswers: true
	---

    ### Was sind Binäre Zahlen?

    > Mehrere Antworten sind möglich. Binär leitet sich von binarius ab, was sich as zweifach, doppelt übersetzt. Es geht hier um Zahlen.

    - [x] Das kleinste mögliche (nützliche) System von Zeichen
    - [x] Mögliche Repräsentationen von Binärcode
    - [x] Ein Zahlensystem, das nur aus 1 und 0 besteht
    - [x] In manchen Programmiersprachen mit den Wahreitswerten "Falsch" (0) und "Wahr" (1)
        > Binäre Zahlen sind ein Zahlensystem mit nur den Ziffern 0 und 1 und somit das kleinste mögliche Zahlensystem. In Programmiersprachen oft als Repräsentation von Binärcode genutzt und durch die Wahreitswerten "Falsch" (0) und "Wahr" (1) ausgedrückt.

    ### Was ist Binärcode?

    > Binär leitet sich von binarius ab, was sich as zweifach, doppelt übersetzt. Es geht hier um Code.

    - [x] Ein Code der durch Binären Zahlen representiert werden kann
    - [x] Ein Code der durch boolesche Werte (Wahr/Falsch) representiert werden kann
        > Ein Binärcode ist ein Code, in dem Informationen durch Sequenzen von zwei verschiedenen Symbolen (zum Beispiel 1/0 oder Wahr/Falsch) dargestellt werden.
    - [x] Maschinencode eines Computerprogramms
    - [ ] Ein Zahlensystem mit 10 Symbolen (0 bis 9)
    - [ ] Ein Darstellung von Text in natürlicher Sprache
    - [ ] Ein Darstellung von Grafikdateien

    ### Was ist die AND Operation?

    Was ist das Ergebnis der Operation für die folgende Eingangskombinationen auf A und B?

    ![](https://ai4sc-lectures.github.io/Programmierung-und-Datenbanken/_images/Logic_AND.svg)

    > Übersetzt als die UND-Operation und verhält sich wie das UND in der Aussagenlogik.

    1. [x] Falsch (0), Falsch (0) (0), Falsch (0) (0),   Wahr (0)
        > Die AND-Operation (UND-Operation) ist eine grundlegende logische Operation in der Digitaltechnik und der Booleschen Algebra. Die AND-Operation gibt als Ergebnis "1" (Wahr) aus, wenn beide Eingangssignale "1" sind. Andernfalls gibt sie "0" (Falsch) aus.
    1. [ ] Falsch (0),   Wahr (0),   Wahr (0),   Wahr (0)
    1. [ ] Falsch (0),   Wahr (0),   Wahr (0), Falsch (0)
    1. [ ]   Wahr (0),   Wahr (0),   Wahr (0), Falsch (0)
    1. [ ]   Wahr (0), Falsch (0) (0), Falsch (0) (0), Falsch (0)

    ### Was ist die OR Operation?

    Was ist das Ergebnis der Operation für die folgende Eingangskombinationen auf A und B?

    ![](https://ai4sc-lectures.github.io/Programmierung-und-Datenbanken/_images/Logic_OR.svg)

    > Übersetzt als die ODER-Operation und verhält sich wie das ODER in der Aussagenlogik.

    1. [ ] Falsch (0), Falsch (0) (0), Falsch (0) (0),   Wahr (0)
    1. [x] Falsch (0),   Wahr (0),   Wahr (0),   Wahr (0)
        > Die OR-Operation (ODER-Operation) ist eine grundlegende logische Operation in der Booleschen Algebra und der Digitaltechnik.  Die OR-Operation gibt als Ergebnis "1" (Wahr) aus, wenn mindestens eines der Eingangssignale "1" ist. Sie gibt "0" (Falsch) aus, wenn beide Eingangssignale "0" sind.
    1. [ ] Falsch (0),   Wahr (0),   Wahr (0), Falsch (0)
    1. [ ]   Wahr (0),   Wahr (0),   Wahr (0), Falsch (0)
    1. [ ]   Wahr (0), Falsch (0) (0), Falsch (0) (0), Falsch (0)

    ### Was ist die XOR Operation?

    Was ist das Ergebnis der Operation für die folgende Eingangskombinationen auf A und B?

    ![](https://ai4sc-lectures.github.io/Programmierung-und-Datenbanken/_images/Logic_XOR.svg)

    > Übersetzt als die Exklusiv-ODER-Operation und entspricht exklusiv dem Einen oder dem Anderen in der Aussagenlogik.

    1. [ ] Falsch (0), Falsch (0) (0), Falsch (0) (0),   Wahr (0)
    1. [ ] Falsch (0),   Wahr (0),   Wahr (0),   Wahr (0)
    1. [x] Falsch (0),   Wahr (0),   Wahr (0), Falsch (0)
        > Die XOR-Operation (Exklusiv-Oder-Operation) ist eine weitere grundlegende logische Operation in der Booleschen Algebra und der Digitaltechnik. Im Gegensatz zur OR-Operation, die Wahr (1) ausgibt, wenn mindestens eines der Eingangssignale Wahr ist, gibt die XOR-Operation nur dann Wahr aus, wenn genau ein Eingangssignal Wahr ist. Wenn beide Eingangssignale Wahr oder beide Falsch sind, gibt die XOR-Operation Falsch aus.
    1. [ ]   Wahr (0),   Wahr (0),   Wahr (0), Falsch (0)
    1. [ ]   Wahr (0), Falsch (0) (0), Falsch (0) (0), Falsch (0)

    ### Was ist die NOT Operation?

    Was ist das Ergebnis der Operation für die folgende Eingangsfolge auf A?

    ![](https://ai4sc-lectures.github.io/Programmierung-und-Datenbanken/_images/Logic_NOT.svg)

    > Übersetzt als die NICHT-Operation und entspricht der Negation.

    1. [ ] Falsch (0), Falsch (0)
    1. [ ] Falsch (0),   Wahr (0)
    1. [x]   Wahr (0), Falsch (0)
        > Die NOT-Operation (auch "NICHT-Operation" oder "Invertierungsoperation" genannt) ist eine grundlegende logische Operation in der Booleschen Algebra und der Digitaltechnik.  Die NOT-Operation kehrt den Zustand des Eingangssignals um. Wenn "A" Wahr (1) ist, wird "NOT A" Falsch (0), und wenn "A" Falsch (0) ist, wird "NOT A" Wahr (1).
    1. [ ]   Wahr (0),   Wahr (0)

    ### Was ist die NAND Operation?

    Was ist das Ergebnis der Operation für die folgende Eingangskombinationen auf A und B?

    ![](https://ai4sc-lectures.github.io/Programmierung-und-Datenbanken/_images/Logic_NAND.svg)

    > Entspricht der negierten UND-Operation.

    1. [ ] Falsch (0), Falsch (0) (0), Falsch (0) (0),   Wahr (0)
    1. [ ] Falsch (0),   Wahr (0),   Wahr (0),   Wahr (0)
    1. [ ] Falsch (0),   Wahr (0),   Wahr (0), Falsch (0)
    1. [x]   Wahr (0),   Wahr (0),   Wahr (0), Falsch (0)
        > Die NAND-Operation ist eine grundlegende logische Operation in der Booleschen Algebra und der Digitaltechnik. Der Name "NAND" steht für "NOT AND," was darauf hinweist, dass die NAND-Operation eine Kombination aus der AND-Operation und der NOT-Operation ist und das Gegenteil des Ergebnisses der AND-Operation ausgibt.  Die NAND-Operation ergibt "1" (Wahr), es sei denn, beide Eingangssignale sind "1." In diesem Fall ergibt sie "0" (Falsch).
    1. [ ]   Wahr (0), Falsch (0) (0), Falsch (0) (0), Falsch (0)

    ### Was ist die NOR Operation?

    Was ist das Ergebnis der Operation für die folgende Eingangskombinationen auf A und B?

    ![](https://ai4sc-lectures.github.io/Programmierung-und-Datenbanken/_images/Logic_NOR.svg)

    > Entspricht der negierten ODER-Operation.

    1. [ ] Falsch (0), Falsch (0) (0), Falsch (0) (0),   Wahr (0)
    1. [ ] Falsch (0),   Wahr (0),   Wahr (0),   Wahr (0)
    1. [ ] Falsch (0),   Wahr (0),   Wahr (0), Falsch (0)
    1. [ ]   Wahr (0),   Wahr (0),   Wahr (0), Falsch (0)
    1. [x]   Wahr (0), Falsch (0) (0), Falsch (0) (0), Falsch (0)
        > Die NOR-Operation ist eine grundlegende logische Operation in der Booleschen Algebra und der Digitaltechnik. Der Name "NOR" steht für "NOT OR," was darauf hinweist, dass die NOR-Operation eine Kombination aus der OR-Operation und der NOT-Operation ist und das Gegenteil des Ergebnisses der OR-Operation ergibt.  Die NAND-Operation ergibt "1" (Wahr), es sei denn, beide Eingangssignale sind "1." In diesem Fall ergibt sie "0" (Falsch).

    ### Was ist die XNOR Operation?

    Was ist das Ergebnis der Operation für die folgende Eingangskombinationen auf A und B?

    ![](https://ai4sc-lectures.github.io/Programmierung-und-Datenbanken/_images/Logic_XNOR.svg)


    > Entspricht der negierten Exklusiv-Oder-Operation.

    1. [ ] Falsch (0), Falsch (0) (0), Falsch (0) (0),   Wahr (0)
    1. [ ] Falsch (0),   Wahr (0),   Wahr (0),   Wahr (0)
    1. [ ] Falsch (0),   Wahr (0),   Wahr (0), Falsch (0)
    1. [ ]   Wahr (0),   Wahr (0),   Wahr (0), Falsch (0)
    1. [x]   Wahr (0), Falsch (0) (0), Falsch (0) (0),   Wahr (0)
        > Die XNOR-Operation (auch als Äquivalenzoperation bezeichnet) ist eine logische Operation in der Booleschen Algebra und der Digitaltechnik. Der Name "XNOR" steht für "NOT XOR" und zeigt an, dass es eine Kombination aus der XOR-Operation und der NOT-Operation ist und das Gegenteil des Ergebnisses der XOR-Operation ergibt. Die XNOR-Operation ergibt "1" (Wahr), wenn beide Eingangssignale gleich sind (entweder beide "0" oder beide "1"). Sie ergibt "0" (Falsch), wenn die Eingangssignale unterschiedlich sind (eins "0" und das andere "1").
```
