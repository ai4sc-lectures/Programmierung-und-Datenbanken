# Programmablauf

Die wichtigste Fähigkeit beim Programmieren ist es, ein Problem der echten Welt in einzelne Schritte zu übersetzen und zu kommunizieren. Ein Werkzeug zum Darstellen dieser Schritte sind "Programmablaufpläne" die allgemein auch als "Flussdiagramme" bezeichnet werden.

<center><img src="https://mermaid.ink/svg/pako:eNplkbFuwyAURX8FMSVSouxWlSqJHQ_tVA8ZsAcKzwEZniMDQ2X534thaWUmuPccngQzFaMEWtDnxF-KfH61SOJyO9Z4PvluT47HM7nk9MIeMQPCQ__2PZ0foBVyoTxgl7CanWowkqjRAJ66LNWpus1XcB7c6tXghAIc3pdM3CJB4mWYyJKxSuMQZwCutLapM1zGMd0foxnFANmpts6HAS0DPt1WvAahknbfamv3zygTCTtWoYRun8Mqh_lwzwd6oBYmy7WMrzmvVUu9AgstLeJWQs-D8S1tcYkoD35sflDQwk8BDjS8JPdQah7_wdKi58bB8gsH3IB5"></center>

Sie bestehen aus einzelnen Elementen, die durch gerichtete Linien in der Ablauffolge verbunden werden. Die Form der Elemente definiert dabei ihre Bedeutung.

Es gibt Start- und End-Elemente mit runden Ecken. Sie sind die einzigen mit genau einem Ausgang- bzw. genau einem Eingang. Sie werden z.T. wegelassen, wenn Start und Ende z.B. durch die Leserichtung klar erkennbar sind.

<center><img src="https://mermaid.ink/svg/pako:eNoVjTEOgzAQBL9y2gok-ICLVEmXKpQcxQkfAQkbZM4FQvw9zlRbzGoujJtXOHyT7DO9PxypcFR9Z5JsqKltH0Ra9a_odajRIGgKsvjyuf4yw2YNynBlep0kr8bgeBdVsm3dGUc4S1kb5N2L6XORUgtwk6yH3j9tCCps" width="200"></center>

Anweisungen (Statements) werden mit eckigen Elementen dargestellt. Sie können mehrere Eingänge, aber nur einen Ausgang haben. Der Text in dem Element beschreibt die auszuführende Anweisung. Die Ein- und Ausgangsvariablen können an die Pfeile geschrieben werden.

<center><img src="https://mermaid.ink/svg/pako:eNptjzEOgzAQBL9yuiqR4AMuUqVMlRQUmOKEj2DFGGSfhRDi73EgRYpstcWMtLtiOxpGhc9AUw-3u_aQE081NGcoywvAXFcUhIFSBxXb3lPbC_vmIOcD4l34yrI4hgiddU750XMRJYwv3vsvwv8RLHDgMJA1edf6ETRKzwNrVLka7ig50aj9llFKMj4W36KSkLjANBkSvlrKjwZUHbnI2xv_DEvD" width="350"></center>

Eingaben und Ausgaben werden durch Rhomben dargestellt. Hier die Eingabe `Geld holen`.

<center><img src="https://mermaid.ink/svg/pako:eNptj7sKwkAURH_lciuFhPRbWAlprLR0UyzZiQnuI-yjCCH_7hotLJxqYM7AzMq912DBj6DmkS5X6agoHu7UHamuT9TemxZG0-gNXNN98naPCDv2raTFgCINkzHCeYcqpuCf2P0vgv8IV2wRrJp0WbO-C5LTCAvJoliNQWWTJEu3FVTl5G-L61mkkFFxnrVKOE-q_LAsBmUithdoTkdm" width="300"></center>

`if`-Anweisungen werden durch Drachenviereck dargestellt. Sie haben mindestens zwei Ausgänge. Die Bedingung wird in das Viereck geschrieben, die alternativen Werte der Bedingung (meist Ja/Nein) wird an die ausgehenden Pfeile geschrieben.

<center><img src="https://mermaid.ink/svg/pako:eNqF0M-KwjAQBvBXGea0Qn2BIApa9eJJDx7MHrLp121pmkj-HKT03c1WWBQE5zR8328uM7B2FVjwr1fXhg5HaSlP-LrQ94zm8yXRZlgjRITFj1_uEXQD263Gh9tkQme0dqJlPnrKT053eDTb12addDPlu_88xJsBBapbY4R1FkWI3nWY9mdSfibbz2T3nnDBPXyv2iq_ZPg7kBwb9JAs8lqhVslEydKOmaoU3elmNYvoEwpO10pFlK3Kz-xZ1MoEjHdF83Dg" width="350"></center>

Unterprogramme, wie z.B. Funktionsaufrufe, werden durch eckige Elemente mit doppelter Linie dargestellt.

<center><img src="https://mermaid.ink/svg/pako:eNptjzsOwjAQRK-y2gqkcAELpQpUVFBQxCkWvCFW7E3k2EUU5e6YT0HBVFO8J80seB8Mo8JHoLGD01kL5EybGpot7HYlQFXXBys9pZZlfwul9XBlK44MS9N8-OqNHrP09ePsGCZorXNKBuFiimHo-d1_keN_BAv0HDxZk6ctL0Fj7NizRpWr4ZaSixq1rBmlFIfLLHdUMSQuMI2GIleW8imPqiU38foEAr9M6g" width="300"></center>
