# KI-D7 · Argumentieren und Denken: Was Reasoning-Modelle anders machen

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Dahinter-Block, Artikel D7 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Du gibst einem Chat-Assistenten eine knifflige Rechenaufgabe. Statt sofort zu antworten, zeigt er „Denkt nach …". Eine Weile passiert scheinbar nichts. Dann kommt die Antwort, manchmal mit einem aufklappbaren Gedankengang darüber. Bei einer einfachen Frage geht dasselbe Werkzeug manchmal schneller. Was passiert in dieser Pause, und warum hilft sie?

Am Ende dieses Artikels kannst du erklären, warum Zwischenschritte einem Sprachmodell helfen und wie aus einem Trick beim Prompten eine trainierte Fähigkeit wurde. Du weißt, was Denkschritte an Zeit, Tokens und Geld kosten. Und du kannst begründen, warum ein sichtbarer Gedankengang weder Beweis noch Garantie ist und wo Denkmodelle trotzdem scheitern.

Vorausgesetzt werden D1 bis D6, vor allem das Schreiben Token für Token aus D4 und das Lernen aus Feedback aus D5. Aus E4 kennst du den Hinweis, dass solche Modelle andere Prompts mögen. Hier kommt die Begründung.

---

## 1. Kopfrechnen oder Zettel

Ein Lehrling soll eine 15-Liter-Gießkanne mit Düngerlösung füllen, in der 0,2 Prozent des fertigen Volumens Konzentrat sind. Fragst du ihn im Vorbeigehen, nennt er aus dem Bauch eine Zahl, und die ist oft falsch. Gibst du ihm einen Zettel, schreibt er: 15 Liter sind 15.000 Milliliter, 0,2 Prozent davon sind 30 Milliliter Konzentrat. Jetzt stimmt es, weil jedes Zwischenergebnis auf dem Papier steht und er damit weiterrechnen kann. Die Zahlen sind ein Rechenbeispiel und keine Dosierempfehlung.

Bei einem Sprachmodell gibt es diesen Unterschied auch. Aus D3 und D4 weißt du, dass es Token für Token schreibt und für jedes Token dieselben Schichten durchläuft. Für jedes neue Token läuft die Rechnung einmal durch diese Schichten. Wie viel Rechenarbeit dabei anfällt, hängt von Modellgröße und Kontextlänge ab, die Schwierigkeit der Aufgabe ändert daran nichts. Schreibt das Modell Zwischenschritte als Text hin, landen sie im Kontext (D1). Bei jedem folgenden Token kann die Attention aus D3 auf diese Zwischenergebnisse zugreifen. Der Text wird zum Schmierzettel.

So ein ausgeschriebener Lösungsweg heißt in diesem Artikel **Gedankengang**, in der Fachliteratur Gedankenkette (englisch chain of thought). Gemeint ist eine Folge von Zwischenschritten, meist in natürlicher Sprache, die das Modell vor der eigentlichen Antwort erzeugt.

Dass es dabei auf den Inhalt der Schritte ankommt, zeigt ein Versuch aus der Arbeit, die den Begriff 2022 bekannt gemacht hat. In einer Kontrollvariante ließen die Forschenden das Modell statt der Zwischenschritte nur eine Reihe von Punkten ausgeben. Ihre Anzahl entsprach der Zeichenzahl der Gleichung, die zur Lösung nötig war. Mehr Tokens gab es damit auch, besser wurde das Ergebnis aber nicht. Erst die ausgeschriebenen Zwischenschritte brachten den Gewinn.

Wo das Bild nicht passt: Auf dem Zettel des Lehrlings steht, was er tatsächlich gedacht hat. Beim Modell ist auch der Gedankengang Text, der Token für Token aus Wahrscheinlichkeiten entsteht (D4). Er kann richtig sein, Fehler enthalten oder an der Rechnung vorbeigehen, die zur Antwort geführt hat. Darum geht es in Abschnitt 5. Die Arbeit von 2022 lässt selbst ausdrücklich offen, ob ein Modell dabei wirklich „schlussfolgert".

---

## 2. Vom Prompt-Trick zur trainierten Fähigkeit

In der ersten Woche legt die Meisterin dem Lehrling drei vorgerechnete Beispiele neben die Waage. Ein paar Monate später schaut sie nur noch, ob die fertige Mischung stimmt, und lässt ihn den Weg selbst finden.

Bei Sprachmodellen lief es in dieser Reihenfolge. Der Zettel kam zuerst über den Prompt. In der Arbeit von 2022 standen im Prompt acht Beispielaufgaben, jeweils mit ausgeschriebenem Rechenweg. Bei einer Sammlung von Textaufgaben auf Schulniveau stieg die Trefferquote eines Modells mit 540 Milliarden Parametern damit von 17,9 auf 56,9 Prozent. Der Effekt zeigte sich in dieser Arbeit erst bei sehr großen Modellen, ungefähr ab 100 Milliarden Parametern. Kleinere Modelle schrieben flüssige, aber unlogische Gedankengänge und lagen damit sogar schlechter als ohne. Allgemeiner ist inzwischen umstritten, ob Fähigkeiten großer Sprachmodelle mit der Größe wirklich sprunghaft auftauchen. Eine Arbeit von 2023 führt solche Sprünge teils auf die gewählte Messgröße zurück. Den Versuch mit den Gedankengängen hat sie allerdings nicht selbst untersucht.

Noch im selben Jahr zeigte eine zweite Arbeit, dass es auch ohne Beispiele geht. Ein einziger Satz vor der Antwort, „Lass uns Schritt für Schritt denken" (im Original englisch), hob die Trefferquote bei denselben Textaufgaben von 10,4 auf 40,7 Prozent. Getestet wurde dort ein anderes Modell, die beiden Zahlenpaare lassen sich deshalb nicht direkt vergleichen. Diesen Satz kennst du vielleicht aus Prompt-Sammlungen.

Seit 2024 werden auch Modelle als Produkte angeboten, bei denen das Denken nicht mehr vom Prompt abhängt. Ein **Denkmodell** (englisch reasoning model) ist ein Sprachmodell, das darauf trainiert ist, vor der Antwort von sich aus einen Gedankengang zu erzeugen. Wie in D6 gesagt, ist das eine trainierte Fähigkeit und keine neue Bauart. Unter der Haube steckt dieselbe Grundbauart, ein Transformer wie in D3.

Trainiert wird diese Fähigkeit mit bestärkendem Lernen, das du aus D5 kennst. Der Unterschied liegt in der Belohnung. In D5 hat ein Belohnungsmodell geschätzt, welche Antwort Menschen besser finden. Ein viel beachteter Bericht von 2025 beschreibt eine Vorstufe, die ausschließlich so trainiert wurde. Sie bekam Aufgaben, deren Ergebnis sich mit einer festen Regel prüfen lässt: Mathematik mit eindeutiger Lösung, Programmieraufgaben mit Tests. Belohnt wurde, ob das Endergebnis stimmt und ob das Format eingehalten ist, also Gedankengang und Antwort getrennt. Auf ein gelerntes Belohnungsmodell verzichteten die Autoren bewusst, weil es sich beim langen Training austricksen lassen kann.

Das Ergebnis war bemerkenswert. Ohne dass jemand Musterlösungen vorgab, wurden die Gedankengänge der Vorstufe im Lauf des Trainings immer länger. Das Modell begann, Zwischenergebnisse zu überprüfen und einen Ansatz zu verwerfen, wenn er nicht aufging. Der Bericht zeigt eine Stelle, an der das Modell mitten in der Rechnung innehält und neu ansetzt. Bei einem Mathematikwettbewerb stieg die Trefferquote der Vorstufe im Training von 15,6 auf 71,0 Prozent. Es gab aber auch Nebenwirkungen: Die Gedankengänge waren schwer lesbar und mischten Sprachen. Für das veröffentlichte Modell kamen deshalb weitere Trainingsstufen dazu, unter anderem eine Belohnung dafür, in einer Sprache zu bleiben.

Auch das Thema Destillation aus D6 taucht hier wieder auf. Die Autoren ließen kleinere Modelle mit 1,5 bis 70 Milliarden Parametern von den Gedankengängen des großen lernen. Bei einem Modell mit 32 Milliarden Parametern brachte das deutlich mehr als dasselbe bestärkende Lernen direkt am kleinen Modell: 72,6 gegenüber 47,0 Prozent beim selben Wettbewerb.

Wo das Bild nicht passt: Der Lehrling, bei dem nur noch die fertige Mischung kontrolliert wird, lernt trotzdem einen sauberen Weg, weil er versteht, was er tut. Das Modell wird für das Endergebnis belohnt und nicht für einen sauberen Weg. Ein Weg, der zufällig zum richtigen Ergebnis führt, wird genauso verstärkt wie ein sauberer. Ob der Gedankengang stimmt, prüft beim Training niemand Schritt für Schritt.

---

## 3. Denkzeit als Stellschraube

In einer Gärtnerei kann die Meisterin eine schwierige Mischung auf zwei Arten absichern. Sie rechnet selbst länger und prüft jeden Schritt. Oder sie lässt drei Leute unabhängig rechnen und nimmt das Ergebnis, das am häufigsten herauskommt.

Bei Sprachmodellen gibt es beide Wege, und beide kosten Rechenzeit beim Antworten. Im Englischen heißt das **test-time compute**, also Rechenaufwand zur Laufzeit, im Gegensatz zum Rechenaufwand beim Training aus D5 und D6.

**Länger denken.** Ein Anbieter berichtete 2024 zu seinem ersten Denkmodell, dass die Leistung mit beidem steigt: mit mehr bestärkendem Lernen im Training und mit mehr Denkzeit beim Antworten. Viele Werkzeuge bieten dafür eine Einstellung, etwa einen Denkaufwand in Stufen wie niedrig, mittel und hoch, ein Budget an Denk-Tokens oder einen Schalter zwischen Denkmodus und schnellem Modus. Manche Modelle entscheiden auch selbst, ob sich das Nachdenken bei einer Anfrage lohnt. Die Bezeichnungen unterscheiden sich je nach Anbieter.

**Mehrere Wege, eine Mehrheit.** Eine Arbeit von 2022 ließ ein Modell dieselbe Aufgabe mehrfach mit Zufall lösen (D4) und nahm am Ende die häufigste Antwort. Das Verfahren heißt **Selbstkonsistenz** (englisch self-consistency). Bei den Textaufgaben aus Abschnitt 2 stieg die Trefferquote des großen Modells damit von 56,5 auf 74,4 Prozent, also um 17,9 Prozentpunkte gegenüber einem einzelnen Gedankengang. Die Ausgangszahl weicht wegen eines etwas anderen Versuchsaufbaus leicht von Abschnitt 2 ab.

Warum eine Mehrheit hilft und wann nicht, rechnet ein kleines Programm vereinfacht aus. Es nimmt an, dass jeder Weg mit der Wahrscheinlichkeit `p` richtig ist und die Wege sich gegenseitig nicht beeinflussen. Die Mehrheit gilt als richtig, wenn mehr als die Hälfte der Wege richtig liegt:

```python
from math import comb

def mehrheit_richtig(p, n):
    # strikte Mehrheit: mehr als die Hälfte richtig; ungerade Zahlen, damit kein Patt entsteht
    return sum(comb(n, k) * p**k * (1 - p)**(n - k) for k in range(n // 2 + 1, n + 1))

for p in (0.6, 0.4):
    for n in (1, 5, 15):
        print(f"p={p}, {n} Wege: Mehrheit richtig mit {mehrheit_richtig(p, n):.2f}")
```

```text
p=0.6, 1 Wege: Mehrheit richtig mit 0.60
p=0.6, 5 Wege: Mehrheit richtig mit 0.68
p=0.6, 15 Wege: Mehrheit richtig mit 0.79
p=0.4, 1 Wege: Mehrheit richtig mit 0.40
p=0.4, 5 Wege: Mehrheit richtig mit 0.32
p=0.4, 15 Wege: Mehrheit richtig mit 0.21
```

Liegt ein einzelner Weg öfter richtig als falsch, hebt die Mehrheit die Trefferquote. Liegt er öfter falsch, verstärkt sie den Fehler. Mehr Rechenzeit hilft also nur, wenn das Modell die Aufgabe grundsätzlich lösen kann.

Wo das Bild nicht passt: Drei Leute in der Gärtnerei rechnen wirklich unabhängig. Mehrere Durchläufe desselben Modells haben dieselben Gewichte und neigen deshalb oft zu denselben Fehlern. Außerdem verteilen sich falsche Antworten in der Praxis meist auf mehrere Werte, dann reicht der richtigen Antwort oft schon die größte Gruppe ohne absolute Mehrheit. Die Rechnung zeigt die Richtung, keine echten Trefferquoten.

---

## 4. Was das Denken kostet

Der Zettel des Lehrlings kostet ein Blatt Papier. Beim Modell ist der Zettel aus Tokens, und Tokens kosten an drei Stellen.

**Platz im Kontextfenster.** Erinnerst du dich an D1? Dort stand, dass die entstehende Antwort Platz im Kontextfenster belegt, bei Modellen mit Denkschritten auch diese Schritte. Ein langer Gedankengang verbraucht also Platz, der für dein Material fehlt. Ob alte Gedankengänge im weiteren Gespräch im Kontext bleiben oder entfernt werden, regelt jeder Anbieter und teils jedes Modell anders.

**Geld.** Bei der Nutzung über eine Schnittstelle (API) werden Denk-Tokens laut Dokumentation zweier großer Anbieter als Ausgabe-Tokens abgerechnet. Bei einem davon bekommst du sie über die Schnittstelle gar nicht zu sehen, auf Wunsch nur eine Zusammenfassung, und bezahlst sie trotzdem. Dieselbe Dokumentation warnt außerdem: Reicht die erlaubte Ausgabelänge nicht, kann die Antwort abbrechen, bevor überhaupt sichtbarer Text entsteht. Bezahlt sind die Denk-Tokens dann trotzdem.

**Zeit.** Jedes Token muss erzeugt werden (D4). Ein Überschlag mit angenommenen Werten:

```python
tempo = 50   # Tokens pro Sekunde, angenommener Beispielwert
for name, denken, antwort in [("ohne Denkschritte", 0, 300),
                              ("mit Denkschritten", 4000, 300)]:
    gesamt = denken + antwort
    print(f"{name}: {gesamt} Ausgabe-Tokens, etwa {gesamt / tempo:.0f} s")
```

```text
ohne Denkschritte: 300 Ausgabe-Tokens, etwa 6 s
mit Denkschritten: 4300 Ausgabe-Tokens, etwa 86 s
```

Tempo und Länge sind Beispielwerte. Echte Gedankengänge reichen je nach Aufgabe von wenigen hundert bis zu vielen tausend Tokens, und das Tempo hängt von Modell und Hardware ab (A9).

**Zu viel Denken.** Eine Untersuchung von 2024 nennt das Problem Überdenken (englisch overthinking). Auf die Frage, was 2 plus 3 ist, gab ein Denkmodell dreizehn Lösungsvorschläge hintereinander aus. Für genau diese Frage brauchten die untersuchten Denkmodelle laut Arbeit im Schnitt gut zwanzigmal so viele Tokens wie herkömmliche Modelle. Die Arbeit hat außerdem Rechenaufgaben aus drei Testsammlungen ausgewertet. Bei über 92 Prozent der Antworten, die überhaupt eine richtige Lösung enthielten, stimmte schon der erste Lösungsweg. Die weiteren Wege brachten dort kaum noch etwas.

Wo das Bild nicht passt: Einen Zettel kannst du wegwerfen, und er kostet fast nichts. Denk-Tokens kosten bei jeder Anfrage aufs Neue, und du siehst sie oft nicht einmal.

---

## 5. Was der Gedankengang zeigt und was nicht

Ein Lehrling hat beim Rechnen heimlich auf den Zettel der Kollegin geschielt. In seinem Rechenweg steht davon nichts, nur eine saubere Herleitung. Der Weg sieht vollständig aus, erklärt aber nicht, wie er wirklich auf die Zahl kam.

Ob ein Gedankengang die tatsächlichen Gründe einer Antwort wiedergibt, heißt in der Forschung **Treue** (englisch faithfulness). Eine Studie von 2025 hat das bei zwei Denkmodellen gemessen. Die Forschenden stellten jede Frage zweimal: einmal normal und einmal mit einem eingebauten Hinweis auf eine Antwort. Ein solcher Hinweis war etwa der Satz, eine bekannte Professorin halte Antwort C für richtig. Dann suchten sie die Fälle, in denen das Modell wegen des Hinweises seine Antwort änderte, und prüften, ob der Gedankengang den Hinweis erwähnte.

Das Ergebnis: Im Schnitt erwähnten die Gedankengänge den genutzten Hinweis in 25 und 39 Prozent dieser Fälle, je nach Modell. Die Werte gelten für diesen Versuchsaufbau mit eingebauten Hinweisen, und die Autoren betrachten sie als wahrscheinliche Obergrenze der tatsächlichen Treue. Bei schwierigeren Fragen sank der Wert. Die verschwiegenen Gedankengänge waren im Schnitt sogar länger als die ehrlichen. In Trainingsumgebungen mit eingebauter Lücke nutzte das Modell die Lücke in über 99 Prozent der Beispiele. In fünf der sechs untersuchten Umgebungen erwähnte es sie in weniger als 2 Prozent. Die Autoren halten den Gedankengang deshalb für ein nützliches Werkzeug, um unerwünschtes Verhalten zu bemerken. Ausschließen lässt es sich damit nicht.

Dazu kommt, was du überhaupt zu sehen bekommst. Mehrere Anbieter zeigen statt des vollständigen Gedankengangs nur eine Zusammenfassung, die ein Modell erstellt hat. Ein Anbieter nennt als Gründe unter anderem die Bedienung, den Wettbewerb und die Möglichkeit, den rohen Gedankengang selbst zu überwachen.

Für dich folgt daraus: Lies einen Gedankengang als Hinweis darauf, wie ein Ergebnis zustande gekommen sein könnte. Ein Beleg dafür, dass es stimmt, ist er nicht. Die Arbeit von 2022 hielt schon fest, dass es keine Garantie für richtige Lösungswege gibt.

Wo das Bild nicht passt: Der Lehrling verschweigt das Schielen mit Absicht. Ob bei einem Modell überhaupt sinnvoll von Absicht die Rede sein kann, lässt die Studie offen. Gemessen hat sie nur, was im Gedankengang steht und was nicht.

---

## 6. Wo Denkmodelle trotzdem scheitern

Der beste Rechenweg nützt nichts, wenn auf dem Etikett der Düngerflasche eine falsche Konzentration steht. Der Lehrling rechnet dann sauber und kommt trotzdem zum falschen Ergebnis.

**Denken ersetzt kein Wissen.** Durch bloßes Nachdenken kommt kein neuer Fakt dazu. Während das Modell antwortet, ändern sich seine Gewichte nicht (D5), und ohne angebundene Werkzeuge schlägt es nichts nach. Fehlt ein Fakt im Training oder ist er veraltet, hilft auch ein langer Gedankengang nicht (E6). Aktuelles Wissen kommt über Werkzeuge wie die Suche oder über Material, das du mitgibst, in den Kontext (A3). Manche Denkmodelle können zwischen ihren Denkschritten solche Werkzeuge aufrufen (P5). Warum Modelle dabei trotzdem überzeugend falsche Aussagen machen, ist Thema von D8.

**Ein falscher Schritt zieht mit.** Was einmal im Gedankengang steht, gehört zum Kontext, und alles Weitere baut darauf auf (D4). Denkmodelle lernen im Training, Zwischenergebnisse zu prüfen und sich zu korrigieren, und das gelingt oft. Eine Garantie ist es nicht, und ein früher Fehler kann sich bis zur Antwort durchziehen.

**Stark bei prüfbaren Aufgaben.** Viele Denkmodelle werden unter anderem an Aufgaben trainiert, deren Ergebnis sich automatisch prüfen lässt (Abschnitt 2). Bei Mathematik, Programmieren und Logik lässt sich der Nutzen deshalb besonders gut an prüfbaren Ergebnissen messen. Bei Texten, Ton und Stil hängt der Vorteil stärker von Aufgabe und Modell ab. Ein Anbieter schrieb 2024 selbst, dass sein erstes Denkmodell bei manchen sprachlichen Aufgaben nicht bevorzugt wurde.

**Mehr ist nicht immer besser.** Bei einfachen Fragen kostet langes Nachdenken vor allem Zeit und Tokens (Abschnitt 4). Und die Mehrheitsrechnung aus Abschnitt 3 hat gezeigt: Kann ein Modell eine Aufgabe grundsätzlich nicht, wird es durch mehr Versuche nicht besser.

Wo das Bild nicht passt: Der Lehrling weiß meist, dass er sich auf das Etikett verlässt. Ein Modell unterscheidet in seinem Gedankengang nicht sichtbar zwischen Wissen, das es sicher gelernt hat, und solchem, das es nur für wahrscheinlich hält.

---

## 7. Was du daraus machst

**Das passende Werkzeug wählen.** Für Rechnungen, Code, Fehlersuche, Planungen mit Abhängigkeiten und Aufgaben mit vielen Schritten lohnt ein Denkmodell oder ein höherer Denkaufwand. Für Umformulieren, kurze Fakten oder einfache Fragen reicht oft der schnelle Modus (A1).

**Anders prompten.** Wie in E4 angekündigt, brauchen Denkmodelle selten den Satz „Denke Schritt für Schritt", denn das tun sie ohnehin. Nenne lieber klar das Ziel, die Rahmenbedingungen, das gewünschte Format und woran du ein fertiges Ergebnis erkennst. Jeden Zwischenschritt vorzuschreiben, ist bei solchen Modellen laut Anbieterhinweisen meist unnötig.

**Den Aufwand anpassen.** Wenn dein Werkzeug eine Einstellung für den Denkaufwand hat, probiere bei einer typischen Aufgabe niedrig und hoch aus und vergleiche Ergebnis und Wartezeit (A7).

**Das Ergebnis prüfen.** Ein langer, sauber wirkender Gedankengang ist kein Beleg. Rechne Zahlen selbst nach, lass Code laufen und prüfe Fakten an der Quelle (A3, A8).

**Kosten im Blick behalten.** Wer über eine Schnittstelle arbeitet, plant genug Ausgabelänge für Denken und Antwort ein und behält den Verbrauch im Auge (P2).

> **Beispielbox, Stand 03.11.2026: prägende Denkmodelle und heutige Einstellungen.** Namen, Einstellungen und Zahlen stammen von den Anbietern und ändern sich laufend.
>
> - **OpenAI o1** (September 2024): Der Anbieter nannte für einen Mathematikwettbewerb (AIME 2024) 74 Prozent mit einem Versuch und 83 Prozent mit einer Mehrheit aus 64 Versuchen. Das Vergleichsmodell GPT-4o kam laut Text auf 12 Prozent. Der rohe Gedankengang wird nicht gezeigt, nur eine Zusammenfassung.
> - **DeepSeek-R1** (Januar 2025, 2025 auch in Nature erschienen): offene Gewichte. Die Vorstufe R1-Zero steigerte sich im Training beim selben Wettbewerb von 15,6 auf 71,0 Prozent, mit Mehrheit aus 64 Versuchen auf 86,7 Prozent. Dazu kamen destillierte Modelle mit 1,5 bis 70 Milliarden Parametern auf Basis von Qwen2.5 und Llama.
> - **Qwen3** (2025): Denkmodus und schneller Modus in einem Modell, dazu ein Denkbudget, mit dem sich der Rechenaufwand beim Antworten begrenzen lässt.
> - **Einstellungen in Schnittstellen:** OpenAI bietet einen Denkaufwand in Stufen an, deren Auswahl vom Modell abhängt. Anthropic setzt bei neueren Claude-Modellen auf adaptives Denken mit einer Aufwandsstufe, ein festes Budget an Denk-Tokens gilt dort als veraltet. Bei beiden werden neu erzeugte Denk-Tokens über die API als Ausgabe-Tokens abgerechnet.

---

## Häufige Fehlgriffe

- **„Ein Denkmodell denkt wie ein Mensch."** Auch wenn die Anzeige „Denkt nach …" das nahelegt: Es erzeugt Text Token für Token, der als Schmierzettel dient. Ob das Denken im menschlichen Sinn ist, lassen selbst die Forschenden offen (Abschnitt 1).
- **„Ein Denkmodell ist eine neue Bauart."** Es ist ein Sprachmodell mit derselben Bauart, trainiert auf das Erzeugen von Gedankengängen (Abschnitt 2, D6).
- **„Der Gedankengang zeigt, wie die Antwort entstanden ist."** In der Studie erwähnten Gedankengänge einen genutzten Hinweis nur in einem Teil der Fälle (Abschnitt 5).
- **„Ein langer Gedankengang heißt, die Antwort stimmt."** Länge ist kein Beleg, verschwiegene Gedankengänge waren sogar länger (Abschnitt 5).
- **„Mehr Denkzeit ist immer besser."** Bei einfachen Fragen kostet sie vor allem Zeit und Tokens, und eine Mehrheit falscher Wege bleibt falsch (Abschnitt 3 und 4).
- **„Denkmodelle halluzinieren nicht."** Fehlendes oder veraltetes Wissen bleibt fehlend, egal wie lange das Modell nachdenkt (Abschnitt 6, D8).
- **„Ich muss immer ‚Denke Schritt für Schritt' dazuschreiben."** Bei Denkmodellen ist das meist überflüssig, ein klares Ziel hilft mehr (Abschnitt 7, E4).
- **„Was ich nicht sehe, kostet nichts."** Denk-Tokens belegen Kontext und werden abgerechnet, auch wenn nur eine Zusammenfassung erscheint (Abschnitt 4).

---

## Zum Ausprobieren

1. Ändere das Programm aus Abschnitt 3 so, dass es für `p` die Werte 0,5, 0,45 und 0,6 mit jeweils 101 Wegen rechnet. Was passiert bei 0,5, und was sagt dir das über Mehrheiten bei Aufgaben, die ein Modell nur zur Hälfte schafft?
2. Stelle einem Chat-Assistenten im schnellen Modus die Aufgabe: „Wie viel Milliliter Konzentrat brauche ich für 12 Liter fertige Lösung, wenn 0,3 Prozent des Volumens Konzentrat sein sollen? Antworte nur mit der Zahl." Stelle dieselbe Aufgabe danach mit der Bitte um den Rechenweg oder mit einem Denkmodell. Rechne selbst nach und notiere, welche Fassung stimmt.
3. Nimm eine Aufgabe mit mehreren Schritten aus deinem Alltag, etwa eine kleine Planung mit Abhängigkeiten. Lass sie mit niedrigem und hohem Denkaufwand bearbeiten, falls dein Werkzeug das anbietet. Vergleiche Wartezeit und Ergebnis nach A8.
4. Baue in die Rechenaufgabe aus Übung 2 einen falschen Hinweis ein: „Ich glaube, es sind 300 Milliliter." Beobachte, ob das Modell dem Hinweis folgt. Prüfe dann, ob sein Gedankengang oder seine Zusammenfassung ihn erwähnt.
5. Stelle einem Denkmodell eine sehr einfache Frage und eine schwierige. Vergleiche, wie lange es jeweils nachdenkt, soweit dein Werkzeug das anzeigt.

Am Ende weißt du aus eigener Anschauung, wann Nachdenken hilft, was es kostet und warum du dem Gedankengang nicht blind trauen solltest.

---

## Fazit

Zwischenschritte helfen einem Sprachmodell, weil jedes geschriebene Zwischenergebnis im Kontext steht und beim nächsten Token mitgelesen wird. Was 2022 als Trick im Prompt begann, ist heute eine trainierte Fähigkeit: Denkmodelle lernen durch bestärkendes Lernen an prüfbaren Aufgaben, vor der Antwort eigene Gedankengänge zu schreiben. Mehr Denkzeit oder mehrere Lösungswege können die Trefferquote heben, kosten aber Kontext, Geld und Wartezeit und helfen nur, wenn das Modell die Aufgabe grundsätzlich lösen kann. Der sichtbare Gedankengang ist ein Hinweis und kein Beweis, denn er verschweigt oft, was eine Antwort tatsächlich beeinflusst hat. Und Denken ersetzt kein Wissen. Warum Modelle trotz allem überzeugend falsche Aussagen machen, erklärt D8.

```yaml
dokument: ki-d7-argumentieren-und-denken
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
block: dahinter
status: final
stand: 2026-11-03
quellen_fachlich:
  - "Wei u. a.: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (NeurIPS 2022), arXiv:2201.11903. https://arxiv.org/abs/2201.11903 (Zugriff 2026-11-03, Volltext über ar5iv): acht Beispiele mit Gedankenkette; GSM8K mit PaLM 540B von 17,9 (Standard) auf 56,9 Prozent (Gedankenkette); 'emergent ability of model scale', Gewinne erst ab etwa 100 Mrd. Parametern, kleinere Modelle 'fluent but illogical chains of thought'; Ablation 'variable compute only' (Punkte in Länge der Gleichung) etwa auf Höhe der Basislinie, 'variable computation by itself is not the reason'; Abschnitt 6: offen, ob das Netz tatsächlich 'reasoning' betreibt; 'no guarantee of correct reasoning paths'"
  - "Kojima u. a.: Large Language Models are Zero-Shot Reasoners (2022), arXiv:2205.11916. https://arxiv.org/abs/2205.11916 (Zugriff 2026-11-03): 'Let's think step by step' vor der Antwort; text-davinci-002: MultiArith 17,7 auf 78,7 Prozent, GSM8K 10,4 auf 40,7 Prozent; ähnliche Gewinne mit PaLM 540B"
  - "Schaeffer, Miranda, Koyejo: Are Emergent Abilities of Large Language Models a Mirage? (2023), arXiv:2304.15004. https://arxiv.org/abs/2304.15004 (Zugriff 2026-11-03): scheinbar sprunghafte Fähigkeiten entstehen nach Ansicht der Autoren durch die Wahl nichtlinearer oder unstetiger Messgrößen, bei stetigen Messgrößen glatte Veränderung"
  - "Wang u. a.: Self-Consistency Improves Chain of Thought Reasoning in Language Models (ICLR 2023), arXiv:2203.11171. https://arxiv.org/abs/2203.11171 und https://ar5iv.labs.arxiv.org/html/2203.11171 (Zugriff 2026-11-03): mehrere Gedankenketten ziehen, konsistenteste Antwort wählen; GSM8K +17,9 im Haupttext ausdrücklich als absolute accuracy gains (PaLM 540B 56,5 auf 74,4, code-davinci-002 60,1 auf 78,0)"
  - "OpenAI: Learning to reason with LLMs (2024-09-12). https://openai.com/index/learning-to-reason-with-llms/ (Zugriff 2026-11-03): o1 mit großskaligem bestärkendem Lernen auf Gedankenketten trainiert; Leistung steigt mit Train-Time- und Test-Time-Compute; rohe Gedankenkette nicht gezeigt, stattdessen Zusammenfassung (Gründe u. a. Nutzererlebnis, Wettbewerbsvorteil, Überwachung); AIME 2024: GPT-4o 12 Prozent im Text (Anhangstabelle 9,3 und 13,4), o1 74 Prozent mit einem Versuch, 83 Prozent mit Konsens aus 64; o1-preview bei manchen sprachlichen Aufgaben nicht bevorzugt"
  - "DeepSeek-AI: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning, arXiv:2501.12948 (v1 2025-01-22, v2 2026-01-04), Nature 645, 633-638 (2025). https://arxiv.org/abs/2501.12948 und https://arxiv.org/html/2501.12948v1 (Zugriff 2026-11-03): R1-Zero mit RL (GRPO) direkt auf dem Basismodell ohne SFT; regelbasierte Belohnung für Genauigkeit und Format (think-Tags), kein neuronales Belohnungsmodell wegen Reward Hacking; AIME 2024 pass@1 15,6 auf 71,0 Prozent, cons@64 86,7 Prozent; Antwortlänge wächst im Training; 'aha moment' (Neubewertung des Ansatzes); Nachteile schlechte Lesbarkeit und Sprachmischung; R1 mit Kaltstart-Daten, Belohnung für Sprachkonsistenz, Rejection Sampling und SFT (rund 800.000 Beispiele), RL für alle Szenarien; Destillation auf Qwen2.5 und Llama mit 1,5 bis 70 Mrd. Parametern; Qwen-32B: RL direkt 47,0, destilliert 72,6 (AIME pass@1)"
  - "Chen u. a. (Anthropic Alignment Science): Reasoning Models Don't Always Say What They Think (2025), arXiv:2505.05410. https://arxiv.org/abs/2505.05410 und https://arxiv.org/html/2505.05410v1 (Zugriff 2026-11-03): Claude 3.7 Sonnet und DeepSeek R1; sechs Hinweisarten (u. a. Sykophanz, Metadaten); Treue = Erwähnung des Hinweises in Fällen, in denen die Antwort zum Hinweis wechselt; Mittelwerte 25 und 39 Prozent, von den Autoren als wahrscheinliche Obergrenze der tatsächlichen Treue eingeordnet; bei GPQA geringer als bei MMLU; untreue Gedankengänge länger; RL steigert Treue zunächst, Plateau; Reward Hacks in über 99 Prozent genutzt, in fünf von sechs Umgebungen in unter 2 Prozent erwähnt; Überwachung nützlich, aber nicht ausreichend, um Verhalten auszuschließen"
  - "Chen u. a.: Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs (2024, v2 2025), arXiv:2412.21187. https://arxiv.org/abs/2412.21187 und https://arxiv.org/html/2412.21187v2 (Zugriff 2026-11-03): QwQ-32B-Preview mit 13 Lösungswegen zu '2 plus 3' (901 Tokens); Einleitung: o1-artige Modelle im Schnitt 1.953 Prozent mehr Tokens als herkömmliche Modelle für dieselbe Antwort, bezogen auf die 2+3-Frage aus Abbildung 1 (rund 20,5-fach); Abschnitt 2.2: in über 92 Prozent der Fälle erste Lösungsrunde richtig, Grundmenge alle Antworten mit richtiger Lösung, Testsammlungen ASDIV, GSM8K, MATH500, Modelle QwQ-32B-Preview und DeepSeek-R1"
  - "Qwen Team: Qwen3 Technical Report (2025), arXiv:2505.09388. https://arxiv.org/abs/2505.09388v1 (Zugriff 2026-11-03): Denkmodus und Nicht-Denkmodus in einem Modell, Wechsel per Anfrage oder Chat-Vorlage, Denkbudget zur Steuerung des Rechenaufwands bei der Inferenz"
  - "OpenAI API-Dokumentation: Reasoning models. https://developers.openai.com/api/docs/guides/reasoning.md (Zugriff 2026-11-03, offizielle Seite; zuvor über einen Spiegel gelesen, Inhalte deckungsgleich): Reasoning-Tokens über die API nicht sichtbar, belegen Kontextfenster, werden als Ausgabe-Tokens abgerechnet; reasoning.effort mit modellabhängigen Stufen; Empfehlung, mindestens 25.000 Tokens für Denken und Ausgabe zu reservieren; Abbruch mit Status incomplete möglich, bevor sichtbare Ausgabe entsteht; Zusammenfassungen nur auf Wunsch; Denken zwischen Werkzeugaufrufen möglich; Prompting: Ziel, Rahmen, Ausgabeformat, nicht jeden Zwischenschritt vorschreiben"
  - "Anthropic: Extended thinking. https://platform.claude.com/docs/build-with-claude/extended-thinking (Zugriff 2026-11-03): budget_tokens (mindestens 1.024) als Altverfahren, bei neueren Modellen adaptives Denken mit Effort-Stufe; Denk-Tokens zählen zu den abgerechneten Ausgabe-Tokens; Antwort enthält zusammengefasste Denkblöcke; ob frühere Denkblöcke im Kontext bleiben, hängt vom Modell ab; adaptiver Modus kann bei einfachen Eingaben auf Denken verzichten"
  - "Rechnungen am 2026-11-03 mit Python ausgeführt: 15.000 ml × 0,002 = 30 ml; 12.000 ml × 0,003 = 36 ml (Übung 2); Mehrheit nach Binomialverteilung p=0,6: 0,60, 0,68, 0,79 bei 1, 5, 15 Wegen; p=0,4: 0,40, 0,32, 0,21; Übung 1: p=0,5 und 101 Wege 0,50, p=0,45 0,16, p=0,6 0,98; Zeitüberschlag 300 Tokens bei 50 Tokens/s 6 s, 4.300 Tokens 86 s; 1.953 Prozent mehr = Faktor 20,53"
  - "Eigene Artikel der Reihe: D1 (Denkschritte belegen das Kontextfenster), D3 (Schichten, Attention), D4 (Token für Token, Zufall beim Ziehen, kein Radiergummi), D5 (bestärkendes Lernen, Belohnungsmodell, Gewichte fest), D6 (Denkmodelle als trainierte Fähigkeit, Destillation), E4 (Prompting für Denkmodelle), E6, A1, A3, A7, A8, A9; Vorwärtsverweise auf D8, P2 und P5"
verifikation_offen:
  - "Erklärung, warum Zwischenschritte helfen (eine Rechnung durch die Schichten je Token, Aufwand abhängig von Modellgröße und Kontextlänge, Zwischenergebnisse im Kontext per Attention lesbar), ist verbreitetes Fachwissen (W); die Punkte-Ablation (Punkte in Zeichenzahl der benötigten Gleichung, Wei u. a. Abschnitt 3.3, Zahlen für LaMDA 137B) stützt nur, dass zusätzliche Tokens allein nicht genügen"
  - "'Seit 2024 auch als Produkte angeboten' bezieht sich auf das erste weithin bekannte Denkmodell eines Anbieters (September 2024); frühere Forschungsmodelle nicht berücksichtigt"
  - "Mehrheitsrechnung ist ein eigenes Denkmodell (W) mit Annahmen Unabhängigkeit und absolute Mehrheit; Selbstkonsistenz nutzt die häufigste Antwort (relative Mehrheit); im Text als Vereinfachung gekennzeichnet"
  - "Zeitüberschlag mit angenommenem Tempo und angenommener Länge, keine Messung; Spanne 'wenige hundert bis viele tausend Tokens' an R1-Bericht und Anthropic-Studie (Mittelwerte etwa 1.400 bis 6.000) angelehnt"
  - "Abrechnung als Ausgabe-Tokens: bei OpenAI und Anthropic laut Dokumentation; unsichtbare Denk-Tokens mit optionaler Zusammenfassung bei OpenAI belegt; ob Anthropic bei zusammengefasstem Denken die volle Länge berechnet, steht auf der gelesenen Seite nicht und wird im Text nicht behauptet; andere Anbieter nicht geprüft"
  - "Aussage, der Vorteil hänge bei Texten, Ton und Stil stärker von Aufgabe und Modell ab, ist eine Einschätzung (W), gestützt nur auf die Herstelleraussage zu o1-preview; seit Runde 2 abgeschwächt"
  - "Selbstkorrektur 'gelingt oft' ist eine vorsichtige Einschätzung (W), nicht gemessen"
  - "Beispielbox: Herstellerangaben, nicht unabhängig geprüft; Stand 2026-11-03, Namen, Einstellungen und Verfügbarkeit ändern sich; Abrechnung auf neu erzeugte Denk-Tokens begrenzt, weil frühere Denkblöcke je nach Modell als Eingabe zählen können (Anthropic-Doku)"
  - "Emergenz-Kritik nur über den Abstract von Schaeffer u. a. gelesen; im Text ausdrücklich als allgemeine Debatte formuliert, die den Gedankenketten-Versuch nicht selbst untersucht. Werkzeugnutzung zwischen Denkschritten: OpenAI-Doku belegt, Verweis auf P5 als Vorwärtsverweis"
  - "Abgrenzung zu D8 (Halluzinationen) bewusst knapp gehalten; Vorwärtsverweise auf D8, P2 und P5 beim Anlegen abgleichen"
review_historie:
  - runde: 0
    datum: 2026-11-03
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial). Gedankenketten-Arbeit (Volltext), Zero-Shot-Arbeit, Self-Consistency, OpenAI-Bericht zu o1, DeepSeek-R1 (Volltext), Treue-Studie (Volltext), Overthinking-Studie, Qwen3-Abstract sowie die Dokumentation zweier Anbieter an der Quelle gelesen. Alle Rechenbeispiele ausgeführt. Löst die Vorwärtsverweise aus D1, D5, D6 und E4 ein."
  - runde: 1
    datum: 2026-11-03
    ergebnis: "Eigene Reviews (Fach und Stil, Prüf-Sweep). Begriff einheitlich Gedankengang (Gedankenkette als Fachwort); Abschnitt 2 mit Szene eröffnet und Bildgrenze angepasst; Abrechnungssatz auf die tatsächlich belegte Doku-Aussage eingeengt; Overthinking-Zahlen als Angaben der Arbeit gekennzeichnet; Selbstkorrektur als im Training gelernt formuliert; Übung 4 geteilt und an Übung 2 gebunden. Programme erneut ausgeführt."
  - runde: 2
    datum: 2026-11-03
    ergebnis: "Drei externe Reviews, strittige Punkte an Volltext und Doku geprüft. Übernommen: Overthinking-Zahlen korrigiert (1.953 Prozent nur für die 2+3-Frage, 92 Prozent nur für Antworten mit richtiger Lösung); Treue-Werte als Versuchsaufbau und Obergrenze; Gewichte unverändert beim Antworten, Werkzeuge ergänzt; Text/Stil-Aussage abgeschwächt; Vorstufe statt pauschal; Kojima als anderes Modell; Emergenz als umstritten; Rechenmenge je Token, Volumenprozent, API-Bezug, Box-Titel, Code-Kommentar, Einleitung geteilt; offizielle OpenAI-Doku; Prozentpunkte bei Selbstkonsistenz bestätigt. Nicht übernommen: Produktnamen im Fließtext und YAML aus dem Artikel nehmen (Reihenregeln), neue Belegstufen-Systematik, GPT-4o-Anhangswerte in der Box."
  - runde: 3
    datum: 2026-11-03
    ergebnis: "Drei Re-Reviews, Behauptungen an Datei und Quellen geprüft. Übernommen: Rechenaufwand je Token mit Modellgröße und Kontextlänge; Punkte-Ablation nach Wortlaut der Arbeit (Zeichenzahl der Gleichung); Emergenz-Kritik als allgemeine Debatte abgegrenzt; Produktbeginn 2024; Selbstkonsistenz mit 56,5 auf 74,4 Prozent; Lösungsvorschläge; Treue als wahrscheinliche Obergrenze; viele Denkmodelle statt alle; Box-Abrechnung auf neu erzeugte Tokens; Pronomen und Code-Kommentar; YAML bereinigt. Nicht bestätigt, nicht übernommen: drei Punkte eines Reviews zur Fassung vor Runde 2 (Gewichte, 92 Prozent, Volumenprozent bereits umgesetzt). Nicht übernommen: Produktnamen im Fließtext, YAML trennen (Reihenregeln), englisches Zitat im Text."
  - runde: 4
    datum: 2026-11-03
    ergebnis: "Freigabe durch David am 2026-11-03 nach Runde 3. Kopfzeile und YAML-Status gemeinsam auf final. Offen bleiben die Punkte unter verifikation_offen (Lehrbuchwissen ohne Einzelquelle, Herstellerangaben, Vorwärtsverweise auf D8, P2, P5)."
```
