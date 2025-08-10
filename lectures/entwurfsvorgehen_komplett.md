# Entwurfsvorgehen in der Softwareentwicklung

## Grundlagen des Softwareentwurfs

Software wird heute fast ausschließlich im Team über längere Zeiträume entwickelt. Diese Teamarbeit erfordert einen durchdachten Projektplan, der sowohl den strukturellen Aufbau der Software als auch das zeitliche Vorgehen bei der Entwicklung festlegt. Der Softwareentwurf umfasst daher zwei wesentliche Komponenten: den Bauplan in Form des Klassenentwurfs und die Bauablaufplanung als Programmiervorgehen.

Das Vorgehen beim Softwareentwurf zeigt bemerkenswerte Ähnlichkeiten mit etablierten Praktiken im Bau- und Umweltingenieurwesen. Genau wie beim Bau einer Brücke oder einer Kläranlage müssen auch bei der Softwareentwicklung die Anforderungen klar definiert, ein strukturierter Entwurf erstellt und die Umsetzung systematisch geplant werden. Diese Parallelen helfen dabei, die Prinzipien des Softwareentwurfs besser zu verstehen.

Ein strukturiertes Vorgehen ist essentiell, weil es Teamarbeit ermöglicht, Qualität sicherstellt und Kosten kontrollierbar macht. Ohne systematische Planung entstehen oft chaotische Entwicklungsprozesse, die zu fehlerhafter Software, Terminüberschreitungen und Budgetproblemen führen.

## Die Phasen der Softwareentwicklung

### Anforderungsdefinition

Die erste Phase dient der präzisen Definition dessen, was die Software leisten soll. Hier werden sowohl die funktionalen Aspekte als auch die Randbedingungen festgelegt. Im Bauingenieurwesen entspricht dies der Ausschreibung, in der dokumentiert wird, welche Funktionen und Randbedingungen das Bauwerk erfüllen muss.

Bei einer Brücke werden beispielsweise die zulässigen Verkehrslasten, die zu überbrückende Spannweite und die geforderte Lebensdauer definiert. Für eine Kläranlage werden die Anzahl der anzuschließenden Einwohner, der geforderte Reinigungsgrad und die einzuhaltenden Grenzwerte spezifiziert. Genauso müssen bei der Softwareentwicklung alle funktionalen Anforderungen, Leistungsparameter und technischen Beschränkungen klar formuliert werden.

### Entwurfsphase

Der Entwurf definiert, wie die Software strukturell aufgebaut werden soll. Diese Phase gliedert sich in die Grobplanung, bei der die Software in logische Module aufgeteilt wird, und die Feinplanung, die festlegt, wann welche Komponenten von wem entwickelt werden.

Im Bauwesen entspricht dies der Architektur- und Entwurfsplanung. Bei einem Hochbau wird zunächst die Grundstruktur mit Fundament, Rohbau und Ausbau geplant, bevor die Details wie Bewehrungspläne und Installationen ausgearbeitet werden. Ähnlich wird bei der Softwareentwicklung erst die Gesamtarchitektur entworfen, bevor die einzelnen Klassen und ihre Schnittstellen definiert werden.

### Ausführungsphase

Die Ausführung umfasst sowohl die Implementation der einzelnen Softwarekomponenten als auch deren Integration zu einem funktionsfähigen Gesamtsystem. Während der Implementation werden die einzelnen Klassen und Module nach den Vorgaben des Entwurfs programmiert. Die anschließende Integration führt diese Einzelteile zur fertigen Lösung zusammen.

Im Bauwesen arbeiten verschiedene Gewerke parallel an ihren spezifischen Aufgaben, bevor ihre Arbeiten koordiniert zusammengeführt werden. Bei einem Wasserbauprojekt werden beispielsweise Pumpstationen, Rohrleitungen und Steuerungssysteme zunächst separat erstellt und dann zu einem funktionsfähigen Wasserversorgungssystem verbunden.

### Abnahme und Test

Die Abnahmephase stellt sicher, dass die fertige Software alle Anforderungen erfüllt. Dies geschieht in mehreren Stufen: Zunächst werden einzelne Module isoliert getestet, dann wird das Zusammenspiel zwischen den Modulen geprüft, und schließlich wird das Gesamtsystem unter realen Bedingungen getestet.

Diese Vorgehensweise entspricht der Bauabnahme, bei der ebenfalls stufenweise vorgegangen wird. Bei einer Kläranlage werden zunächst einzelne Pumpen auf ihre Funktion geprüft, dann das Zusammenspiel von Steuerung, Pumpen und Sensoren getestet, und schließlich wird die gesamte Anlage unter Realbedingungen abgenommen.

## Wasserfallmethode - Das traditionelle Entwicklungsmodell

Die Wasserfallmethode repräsentiert den traditionellen Ansatz der Softwareentwicklung und wird noch heute häufig in Ausschreibungen großer Systeme gefordert. Ihr charakteristisches Merkmal ist die streng sequenzielle Abarbeitung der Entwicklungsphasen, wobei jede Phase vollständig abgeschlossen werden muss, bevor die nächste beginnt.

Diese Methode zeichnet sich durch eine begrenzte Benutzerbeteiligung aus, die hauptsächlich auf die Anforderungsdefinition beschränkt ist. Jede Aktivität wird umfassend dokumentiert, was die Methode besonders für Ausschreibungen und ISO-9000-konforme Entwicklungen geeignet macht.

Die Wasserfallmethode entspricht dem traditionellen Bauvorgehen. Bei einer Autobahnbrücke werden zunächst alle Anforderungen in der Ausschreibung definiert, dann erfolgt die komplette Planung von der Statik bis zur Ausführungsplanung, bevor mit dem eigentlichen Bau begonnen wird. Erst nach Fertigstellung des gesamten Bauwerks erfolgen die Belastungstests und die Abnahme.

Der große Vorteil dieser Methode liegt in ihrer Planbarkeit und dem strukturierten Vorgehen. Kosten und Termine lassen sich präzise schätzen, und die umfassende Dokumentation erfüllt alle formalen Anforderungen. Allerdings führt die sequenzielle Natur dazu, dass Fehler aus frühen Phasen erst sehr spät entdeckt werden, was teure Nachbesserungen zur Folge haben kann.

## V-Methode - Entwicklung mit systematischer Testplanung

Die V-Methode wurde speziell für die Entwicklung sicherheitskritischer Software konzipiert und findet hauptsächlich in der Automobil- und Luftfahrtindustrie Anwendung. Sie erweitert das Wasserfallmodell um eine systematische Testplanung, die bereits während der Entwicklungsphase beginnt.

Das charakteristische V-förmige Modell trennt Entwicklungs- und Testaktivitäten klar voneinander. Während auf der linken Seite die eigentliche Entwicklung stattfindet, werden auf der rechten Seite die entsprechenden Tests definiert und durchgeführt. Jede Entwicklungsphase hat ihre korrespondierende Testphase, wodurch eine hohe Testabdeckung erreicht wird.

Im Tunnelbau, einem sicherheitskritischen Bereich des Bauingenieurwesens, wird ähnlich vorgegangen. Bereits während der Planung der Sicherheitssysteme werden die entsprechenden Testverfahren definiert. Für jeden Brandmelder wird festgelegt, wie er getestet wird, für das Zusammenspiel von Brandmeldung und Lüftungssteuerung werden Integrationstests geplant, und für das Gesamtsystem wird eine komplette Evakuierungsübung mit der Feuerwehr konzipiert.

Die V-Methode bietet den Vorteil einer systematischen Qualitätssicherung mit hoher Rückverfolgbarkeit. Allerdings ist sie aufwendiger als andere Methoden und eignet sich daher primär für Bereiche, in denen Sicherheit und Zuverlässigkeit oberste Priorität haben.

## Agile Methode - Flexibilität durch iterative Entwicklung

Die agile Methode stellt eine moderne Antwort auf die Herausforderungen sich schnell ändernder Anforderungen dar. Anstatt ein komplettes System von Anfang bis Ende zu planen, wird schrittweise entwickelt und kontinuierlich verbessert.

Der agile Ansatz beginnt mit einem Minimal Viable Product, einer einfachsten funktionsfähigen Version der Software. Diese wird dann in regelmäßigen Zyklen erweitert und verbessert, wobei jede Iteration neue Funktionen hinzufügt oder bestehende optimiert. Die Entwicklungszyklen sind typischerweise kurz und dauern meist nur wenige Monate.

Ein Beispiel aus dem Bauwesen wäre der modulare Brückenbau. Anstatt eine komplette Brücke zu planen und zu bauen, könnte zunächst eine provisorische Behelfsbrücke errichtet werden, die den sofortigen Verkehr ermöglicht. In späteren Phasen wird diese dann verstärkt, verbreitert und mit zusätzlichen Features wie Beleuchtung und Lärmschutz ausgestattet.

Bei einer Kläranlage könnte agil vorgegangen werden, indem zunächst nur die mechanische und eine einfache biologische Reinigungsstufe gebaut werden. In weiteren Phasen kommen dann erweiterte Reinigungsverfahren, Energierückgewinnung und automatisierte Steuerungssysteme hinzu.

Der große Vorteil der agilen Methode liegt in ihrer Flexibilität und der Möglichkeit, frühzeitig Feedback zu erhalten. Benutzer können bereits funktionsfähige Versionen testen und Verbesserungsvorschläge einbringen. Dies reduziert das Risiko, an den tatsächlichen Bedürfnissen vorbei zu entwickeln.

Allerdings birgt die agile Methode auch Risiken. Entwurfsfehler in frühen Iterationen können dazu führen, dass die gesamte Architektur überarbeitet werden muss. Zudem ist die Kosten- und Zeitplanung schwieriger, da das Endprodukt zu Projektbeginn nicht vollständig spezifiziert ist.

## Methodenwahl in der Praxis

Die Wahl der geeigneten Entwicklungsmethode hängt stark vom Projektkontext ab. Für standardisierte Systeme mit klaren Anforderungen eignet sich die Wasserfallmethode, während sicherheitskritische Anwendungen die systematische Testplanung der V-Methode erfordern. Agile Methoden sind ideal für innovative Projekte mit evolvierende Anforderungen.

In der Ingenieurspraxis zeigt sich, dass oft auch Mischformen sinnvoll sind. Ein Tunnelprojekt könnte beispielsweise die grundlegende Konstruktion nach dem Wasserfallmodell planen, die Sicherheitssysteme nach der V-Methode entwickeln und die Betriebsführungssoftware agil umsetzen.