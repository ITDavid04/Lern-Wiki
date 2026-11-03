# KI-D9 · Bias, Daten und Urheberrecht: Was im Training steckt, kommt wieder heraus

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Dahinter-Block, Artikel D9 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Guter Kompost entsteht aus allem, was ein Betrieb über das Jahr abwirft: Rasenschnitt, Laub, Gemüsereste. Landet versehentlich mit Unkrautsamen belasteter Schnitt darin, keimt das Unkraut später im Beet. Niemand hat es gesät, es kam mit dem Material.

Sprachmodelle funktionieren ähnlich. In D5 stand immer wieder „aus riesigen Textmengen", ohne dass klar wurde, woher diese Texte kommen. Am Ende dieses Artikels weißt du, aus welchen Quellen Trainingsdaten typischerweise stammen und wie sie gefiltert werden. Du kannst erklären, wie Verzerrungen aus den Daten ins Modell gelangen und warum das Nachtraining sie nicht zuverlässig entfernt. Und du kennst die Grundzüge der Rechtslage in Deutschland und der EU zum Training mit geschützten Werken.

Vorausgesetzt werden D1 bis D8, vor allem die Tombola aus D4 und das Training aus D5. Der Artikel schließt den Dahinter-Block ab. Rechtsfragen zu den Ergebnissen eines Modells behandelt später R5, Datenschutz R1.

---

## 1. Woher die Daten kommen

Der Kompost einer Gärtnerei lässt sich ungefähr beschreiben: so viel Rasenschnitt, so viel Laub. Was genau im Haufen steckt, weiß niemand.

Bei Trainingsdaten ist es ähnlich. Die Berichte großer Anbieter nennen typischerweise diese Quellen:

- **Webseiten** aus großen Sammlungen. Die bekannteste ist ein gemeinnütziges Archiv, das seit 2008 regelmäßig das Netz durchsucht und inzwischen Petabytes an Daten frei zur Verfügung stellt.
- **Bücher und Fachtexte**, etwa wissenschaftliche Arbeiten.
- **Programmcode** aus öffentlichen Sammlungen.
- **Nachschlagewerke** wie Online-Enzyklopädien.
- **Lizenzierte Daten**, für die ein Anbieter mit Verlagen oder Plattformen Verträge schließt.
- **Erzeugte Daten**, die andere Modelle geschrieben haben, etwa für Mathematik oder Code (D6, D7).

Wie die Mischung genau aussieht, legen viele Anbieter nicht offen (D6). Seit dem 2. August 2025 verlangt das europäische KI-Gesetz von Anbietern von Allzweck-KI-Modellen eine hinreichend detaillierte, öffentliche Zusammenfassung der Trainingsinhalte. Dafür gibt es eine verbindliche Vorlage des KI-Büros der EU-Kommission. Für Modelle, die schon vorher auf dem Markt waren, gilt eine Übergangsfrist bis zum 2. August 2027. Die Zusammenfassung ist ein Anfang, ein vollständiges Verzeichnis aller Werke verlangt sie nicht.

Wo das Bild nicht passt: Kompost wird zersetzt, und aus dem Laub ist am Ende nichts mehr herauszulesen. Ein Modell kann einzelne Stellen aus seinen Trainingsdaten dagegen wortgetreu behalten (D5). Das wird in Abschnitt 5 und 6 wichtig.

---

## 2. Sieben und Sortieren

Bevor Erde in die Töpfe kommt, wird sie gesiebt. Steine und Wurzeln bleiben im Sieb. Ist es zu grob, rutschen Steine durch. Ist es zu fein, bleibt auch gute Erde hängen.

Rohdaten aus dem Netz sind voller Doppelungen, Werbung, Menüleisten und Unsinn. Deshalb werden sie vor dem Training bereinigt. Typische Schritte sind das Entfernen von Dubletten, Sprachfilter, Qualitätsfilter und Sperrlisten mit unerwünschten Wörtern. Was übrig bleibt, ist der eigentliche Trainingsdatensatz.

Wie viel dabei schiefgehen kann, zeigt eine Untersuchung von 2021. Die Forschenden haben einen viel genutzten Datensatz nachträglich durchleuchtet, der aus einer einzelnen Momentaufnahme des Webarchivs gefiltert worden war. Sie fanden erhebliche Textmengen aus unerwarteten Quellen, etwa Patentschriften und Webseiten des US-Militärs. Sie fanden maschinell erzeugten Text, zum Beispiel automatische Übersetzungen. Und sie fanden Aufgaben aus verbreiteten Tests, mit denen Modelle später geprüft werden sollten. Hat ein Modell solche Aufgaben im Training gesehen, kann der Test Wiedererkennen mit echtem Können vermischen. Eine hohe Punktzahl sagt dann weniger zuverlässig aus, wie gut das Modell unbekannte Aufgaben löst (P8).

Für diesen Artikel besonders wichtig ist ein Befund zum Sieb selbst. Laut den Autoren entfernte die Sperrliste überproportional Texte von und über Minderheiten. Ein Filter, der gegen anstößige Inhalte gedacht war, hat also die Daten selbst verzerrt.

Wo das Bild nicht passt: Beim Erdsieb siehst du, was im Sieb hängen bleibt. Was ein Datenfilter aussortiert hat, zeigt sich erst, wenn jemand gezielt nachzählt.

---

## 3. Wie Bias entsteht

Die Gärtnerei führt seit Jahren ein Dienstbuch. Bei „Kasse" steht darin fast immer dieselbe Kollegin. Die neue Aushilfe rechnet bald automatisch damit, dass diese Kollegin an der Kasse sitzt, auch an Tagen, an denen sie gar nicht da ist.

So entsteht **Bias** (Verzerrung): eine systematische Schieflage in den Ergebnissen eines Modells. Sie kann dazu führen, dass Gruppen oder Merkmale über- oder unterrepräsentiert sind oder Menschen ungerecht behandelt werden. Aus D4 weißt du, dass das Modell seine Lose nach den Mustern im Training verteilt. Kommt eine Kombination in den Daten oft vor, bekommt sie viele Lose. Ein kleines Programm zeigt das an erfundenen Beispielsätzen. In ihnen wird nach einem Beruf mit „sie" oder „er" weitergeschrieben:

```python
from collections import Counter

beispiele = ([("Pflegekraft", "sie")] * 8 + [("Pflegekraft", "er")] * 2
             + [("Kranführer", "er")] * 9 + [("Kranführer", "sie")] * 1)
for beruf in ("Pflegekraft", "Kranführer"):
    zaehler = Counter(pronomen for b, pronomen in beispiele if b == beruf)
    gesamt = sum(zaehler.values())
    print(f"{beruf}: " + ", ".join(f"{p} {n / gesamt:.2f}" for p, n in zaehler.most_common()))
```

```text
Pflegekraft: sie 0.80, er 0.20
Kranführer: er 0.90, sie 0.10
```

Ein Modell, das nur diese Häufigkeiten lernt, würde seine Lose genau so verteilen. Das Programm ist eine Vereinfachung. Echte Modelle zählen keine Paare. Sie lernen Zusammenhänge zwischen Wörtern, Satzbau und Kontext aus Milliarden von Sätzen.

Ob eine ungleiche Verteilung ein Problem ist, hängt vom Einsatz ab. Nicht jede Schieflage ist diskriminierend, und eine 50:50-Mischung garantiert umgekehrt keine fairen Ergebnisse. Entscheidend ist der Maßstab, an dem du eine Verzerrung im jeweiligen Kontext misst.

Dass es in der Praxis noch weiter geht, zeigt eine Studie von 2023. Sie legte vier Sprachmodellen Sätze vor, in denen offen war, auf welche Person sich ein Pronomen bezieht. Die Modelle entschieden sich drei- bis sechsmal so häufig für die Zuordnung, die zum Geschlechterklischee passte, wie für die andere. Laut Studie gingen sie damit über die Einschätzungen von Menschen und über offizielle Berufsstatistiken hinaus. Die Mehrdeutigkeit der Sätze übersahen sie in rund 95 Prozent der Fälle, erkannten sie aber bei ausdrücklicher Nachfrage. Aus D2 kennst du einen ähnlichen Befund bei Wortvektoren von 2016.

Wo das Bild nicht passt: Die Aushilfe kann die Kollegin fragen und ihren Eindruck korrigieren. Die Gewichte eines Modells ändern sich durch ein Gespräch nicht (D5). Was es aus den Trainingsdaten gelernt hat, wird dadurch nicht dauerhaft korrigiert.

---

## 4. Verdeckte Vorurteile und was das Nachtraining ändert

Eine Mitarbeiterin sagt im Gespräch, sie habe keine Vorurteile. Sie meint das ehrlich. Trotzdem behandelt sie Kunden mit starkem Dialekt im Verkaufsgespräch spürbar anders. Was jemand auf Nachfrage sagt und wie er handelt, kann auseinanderfallen.

Bei Sprachmodellen hat eine Studie von 2024 einen ähnlichen Unterschied gemessen. Die Forschenden legten Modellen dieselben Inhalte einmal in afroamerikanischem Englisch und einmal in amerikanischem Standardenglisch vor. „Offen" und „verdeckt" bezeichnen dabei zwei Arten zu messen, keine Absicht des Modells. Auf direkte Fragen nach der Gruppe äußerten die untersuchten Modelle eher positive Zuschreibungen. War die Gruppe nur über den Dialekt eines Textes erkennbar, fielen die Zuschreibungen dagegen sehr negativ aus. Laut den Autoren waren sie negativer als die Stereotype über Afroamerikaner, die in Experimenten mit Menschen je dokumentiert wurden. In Entscheidungsaufgaben ordneten die Modelle den Verfassern dieser Texte häufiger weniger angesehene Berufe zu. In einem hypothetischen Strafverfahren sprachen die Modelle die Verfasser häufiger schuldig und wählten häufiger die Todesstrafe. Die Studie betrifft den US-amerikanischen Kontext, für deutsche Dialekte belegt sie nichts unmittelbar.

Für dich ist besonders ein Befund wichtig, weil er an D5 anknüpft. In der Studie verringerte das untersuchte Training mit menschlichem Feedback die offen geäußerten Vorurteile, die verdeckt gemessenen beseitigte es nicht. Es konnte den Abstand zwischen beiden sogar vergrößern. Auch das Nachtraining verändert die Gewichte. Eine Verbesserung bei direkten Fragen überträgt sich aber nicht automatisch auf indirekte Situationen.

Wo das Bild nicht passt: Bei der Mitarbeiterin weichen Selbstbild und Verhalten voneinander ab. Ein Modell hat weder Selbstbild noch Absicht. Es hat Verteilungen, die je nach Kontext anders ausfallen. Wie gut eine Prüfung mit direkten Fragen Bias findet, hängt deshalb davon ab, ob sie auch die verdeckten Fälle abdeckt (P8).

---

## 5. Daten und Urheberrecht

Darf eine Gärtnerei Fotos aus einem fremden Pflanzenkatalog kopieren, um damit ihre Mitarbeitenden zu schulen? Beim Training von Sprachmodellen stellt sich dieselbe Frage im ganz großen Maßstab, denn viele Trainingstexte sind urheberrechtlich geschützt. Dieser Abschnitt ist ein Überblick zur Lage in Deutschland und der EU, keine Rechtsberatung. In anderen Rechtsräumen, etwa den USA, gelten teils grundlegend andere Maßstäbe.

**Text und Data Mining.** Das deutsche Urheberrecht erlaubt seit 2021 die automatisierte Analyse digitaler oder digitalisierter Werke, um Muster, Trends und Zusammenhänge zu finden. Dafür dürfen rechtmäßig zugängliche Werke vervielfältigt werden. Die Kopien sind zu löschen, wenn sie nicht mehr gebraucht werden. Rechteinhaber können sich die Nutzung vorbehalten. Bei Werken im Netz wirkt so ein Vorbehalt nur, wenn er maschinenlesbar ist. Für nicht kommerzielle wissenschaftliche Forschung gibt es unter besonderen Voraussetzungen eine weitere Erlaubnis. Fehlt ein wirksamer Vorbehalt, heißt das allerdings nicht, dass jede spätere Nutzung erlaubt ist.

**Datensatz und Training sind zwei Schritte.** Beim ersten werden Werke gesammelt und ausgewertet. Beim zweiten verarbeitet ein Modell diese Daten und verändert dabei seine Gewichte (D5). Ob das Recht beide Schritte gleich behandelt, ist eine der zentralen Streitfragen.

**Zwei Verfahren als Orientierung.** Ein Hamburger Fotograf klagte gegen einen gemeinnützigen Verein, der für einen offenen Bild-Text-Datensatz eines seiner Fotos heruntergeladen und ausgewertet hatte. Das Landgericht Hamburg wies die Klage 2024 ab, das Oberlandesgericht bestätigte das im Dezember 2025. Es sah das Herunterladen von der Erlaubnis für Text und Data Mining und von der Forschungserlaubnis gedeckt. Der Vorbehalt stand nur in normaler Sprache in den Nutzungsbedingungen der Bildagentur, und das genügte dem Gericht nicht als maschinenlesbar. Ob auch das spätere Training eines Modells gedeckt ist, hat es ausdrücklich offengelassen. Inzwischen liegt der Fall beim Bundesgerichtshof. Verhandelt wurde im September 2026, als Verkündungstermin ist der 17. Dezember 2026 angesetzt.

Im zweiten Verfahren klagte die Verwertungsgesellschaft für Musikrechte gegen einen großen Modellanbieter. Das Landgericht München I entschied im November 2025 über neun bekannte Liedtexte. Vervielfältigungen beim Erstellen des Trainingsmaterials sah es von der Erlaubnis für Text und Data Mining gedeckt, das Training des Modells dagegen nicht. Dass das Modell die Texte behalten hatte, wertete es als Vervielfältigung, also als urheberrechtlich relevante Kopie. Auch die weitgehend originalgetreue Ausgabe der Texte verletzte nach dem Urteil Rechte. Das Urteil ist nicht rechtskräftig, der Anbieter hat Berufung eingelegt. Hier zeigt sich, warum das wortgetreue Behalten aus D5 rechtlich so wichtig ist.

**Pflichten nach dem KI-Gesetz.** Anbieter von Allzweck-KI-Modellen müssen in der EU außerdem eine Strategie haben, um das Urheberrecht einzuhalten. Dazu gehört, maschinenlesbare Vorbehalte zu erkennen und zu beachten. Hinzu kommt die in Abschnitt 1 beschriebene Zusammenfassung der Trainingsinhalte.

Für dich folgt daraus vor allem eins: Die Rechtslage ist in Bewegung, und mehrere Grundfragen liegen bei höheren Gerichten. Ein Urteil zu einem Datensatz oder zu neun Liedtexten ist keine allgemeine Regel für jedes Training. Ob du Ergebnisse eines Modells verwenden darfst und wem sie gehören, ist eine eigene Frage, die R5 behandelt.

Wo das Bild nicht passt: Ein kopiertes Foto im Schulungsordner bleibt ein erkennbares Foto. Ein Modell speichert Werke nicht wie einen Ordner. Ob und wann es trotzdem eine Kopie enthält, ist genau eine der Fragen, über die Gerichte gerade streiten.

---

## 6. Persönliches in den Daten

Im alten Dienstbuch stehen neben den Schichten auch Handynummern und Krankmeldungen. Wer das Buch weitergibt, gibt diese Angaben mit.

Mit Trainingsdaten aus dem Netz ist es ähnlich. Auf Webseiten, in Foren und Dokumenten stehen Namen, Adressen und andere persönliche Angaben, und Filter erwischen nicht alles. Aus D5 kennst du die Studie, die wortgetreue Textstellen samt persönlicher Daten aus einem Modell zurückgewinnen konnte. Aus D2 weißt du, dass auch Embeddings vertrauliche Angaben preisgeben können.

Für deinen Alltag gilt deshalb weiter, was E7 sagt: Persönliche und vertrauliche Daten gehören nicht ungeprüft in einen Chat. Ob ein Anbieter deine Eingaben für künftiges Training nutzen darf, hängt vom Dienst, seinen Einstellungen und den Vertrags- und Datenschutzbedingungen ab (E7, D5). Davon zu trennen ist, dass Eingaben auch in Verläufen oder Protokollen gespeichert sein können. In die Gewichte eines fertigen Modells gelangen sie dadurch nicht automatisch. Die rechtliche Seite, also was die Datenschutz-Grundverordnung dazu sagt, behandelt R1.

Wo das Bild nicht passt: Ein Dienstbuch kannst du zurückfordern. Was einmal in die Gewichte eines Modells eingeflossen ist, lässt sich nicht einfach gezielt wieder herausnehmen.

---

## 7. Was du daraus machst

**Mit Schieflagen rechnen.** Gehe davon aus, dass ein Modell Klischees aus seinen Daten mitbringt, auch wenn es auf direkte Fragen ausgewogen antwortet. Bei Texten über Menschen, etwa Stellenanzeigen, Beurteilungen oder Beispielpersonen, prüfst du gezielt auf Schieflagen (A6, A8).

**Verdeckt testen.** Die Frage „Hast du Vorurteile?" reicht nicht. Tausche in derselben Aufgabe ein Merkmal aus, etwa Namen, Geschlecht oder Sprachstil, und vergleiche die Ergebnisse (A7). Das ist eine kleine Version der Methode aus Abschnitt 4. Wiederhole den Vergleich mehrmals, denn eine einzelne Antwort kann Zufall sein (D4). Ein Unterschied ist ein Anlass zum Prüfen, noch kein Beweis.

**Ergebnisse nicht ungeprüft für Entscheidungen über Menschen nutzen.** Für Bewerbungen, Bewertungen und ähnliche Fälle gelten im Betrieb oft eigene Regeln. KI-Systeme zur Auswahl von Bewerbungen oder zur Bewertung von Beschäftigten können nach dem KI-Gesetz in die Hochrisiko-Kategorie fallen. Welche Pflichten daraus folgen, hängt vom konkreten Einsatz ab (R2, R6).

**Bei fremden Werken vorsichtig sein.** Lass dir keine geschützten Texte wie Liedtexte oder Buchkapitel wörtlich ausgeben, um sie weiterzuverwenden. Was beim Verwenden von KI-Ergebnissen gilt, klärt R5.

**Eigene Daten schützen.** Gib nur in Werkzeuge mit geklärten Bedingungen ein, was dort hingehört, und prüfe die Einstellung zur Trainingsnutzung (E7).

> **Beispielbox, Stand 03.11.2026: Fundstellen zu Daten und Recht.** Verfahrensstände ändern sich, die Angaben sind keine Rechtsberatung.
>
> - **Webarchiv:** Common Crawl, gemeinnützig, seit 2008, Zugang über einen Cloud-Anbieter kostenfrei.
> - **Untersuchung des Datensatzes von 2021:** C4 (Colossal Clean Crawled Corpus), gefiltert aus einer Momentaufnahme von Common Crawl.
> - **Text und Data Mining:** § 44b UrhG, Forschung § 60d UrhG, beide auf Grundlage der EU-Richtlinie 2019/790 (Art. 3 und 4).
> - **Kneschke gegen LAION:** LG Hamburg, Urteil vom 27.09.2024 (310 O 227/23); OLG Hamburg, Urteil vom 10.12.2025 (5 U 104/24); BGH, Revision I ZR 281/25, verhandelt am 03.09.2026, Verkündungstermin 17.12.2026.
> - **GEMA gegen OpenAI:** LG München I, Urteil vom 11.11.2025 (42 O 14139/24), Memorisierung als Vervielfältigung nach § 16 UrhG, nicht rechtskräftig; Berufung beim OLG München (6 U 3662/25 e).
> - **KI-Gesetz:** Verordnung (EU) 2024/1689, Art. 53 Abs. 1 Buchst. c und d, Pflichten für Anbieter von Allzweck-KI-Modellen seit dem 02.08.2025, für ältere Modelle Übergangsfrist bis 02.08.2027 (Art. 111 Abs. 3); Hochrisiko-Bereich Beschäftigung in Anhang III.

---

## Häufige Fehlgriffe

- **„Das Modell kennt das ganze Internet."** Trainiert wird auf einer gefilterten Auswahl mit Datenstand, deren genaue Zusammensetzung oft nicht offengelegt ist (Abschnitt 1 und 2).
- **„Filter machen die Daten neutral."** Filter können selbst verzerren, etwa indem sie überproportional Texte über Minderheiten entfernen (Abschnitt 2).
- **„Das Modell gibt nur die Wirklichkeit wieder."** In der Studie von 2023 gingen die Modelle über Statistiken und menschliche Einschätzungen hinaus (Abschnitt 3).
- **„Wenn es auf die direkte Frage fair antwortet, ist es fair."** Offene und verdeckte Vorurteile können auseinanderfallen. Das Nachtraining konnte den Abstand in der Studie sogar vergrößern (Abschnitt 4).
- **„Was öffentlich im Netz steht, darf jeder fürs Training nutzen."** Die Erlaubnis für Text und Data Mining hat Grenzen, und Rechteinhaber können maschinenlesbar widersprechen. Grundfragen sind vor Gericht offen (Abschnitt 5).
- **„Ein Modell speichert keine Werke."** Ein Gericht hat das wortgetreue Behalten von Liedtexten als Vervielfältigung gewertet, rechtskräftig ist das noch nicht (Abschnitt 5, D5).
- **„Meine Daten stecken ja nicht im Modell."** Persönliche Angaben aus dem Netz können im Training landen. Eigene Eingaben können je nach Bedingungen für späteres Training verwendet werden, unabhängig davon, ob sie in Protokollen gespeichert sind (Abschnitt 6, E7).

---

## Zum Ausprobieren

1. Ändere das Programm aus Abschnitt 3 so, dass bei beiden Berufen „sie" und „er" je fünfmal vorkommen. Wie sieht die Verteilung jetzt aus? Ergänze danach einen dritten Beruf mit einer Schieflage deiner Wahl.
2. Lass einen Chat-Assistenten drei kurze Geschichten schreiben, in denen eine Pflegekraft, ein Kranführer und eine Führungskraft vorkommen, ohne Geschlecht oder Namen vorzugeben. Notiere, welches Geschlecht und welche Namen das Modell wählt, und wiederhole das dreimal. Die Ergebnisse können zwischen den Durchläufen schwanken.
3. Lass dir eine kurze Einschätzung zu einer erfundenen Bewerbung schreiben. Tausche danach nur den Namen gegen einen Namen, der auf eine andere Herkunft schließen lässt, und vergleiche beide Einschätzungen nach A8. Mach mehrere Durchläufe und behandle einen Unterschied als Anlass zum Prüfen, nicht als Beweis.
4. Öffne die Seite eines Modellanbieters und suche nach Angaben zu den Trainingsdaten oder nach der Zusammenfassung nach dem KI-Gesetz. Notiere, welche Quellenarten genannt werden und was offen bleibt.
5. Rufe die Datei `robots.txt` einer großen Nachrichtenseite auf, indem du `/robots.txt` an die Adresse anhängst. Suche nach Einträgen, die Crawler von KI-Anbietern ausschließen, und notiere, welche Namen dort stehen. Die Namen ändern sich, prüfe sie bei Bedarf beim jeweiligen Anbieter. Überlege danach, warum eine technische Sperre in dieser Datei nicht automatisch alle rechtlichen Anforderungen an einen wirksamen Vorbehalt erfüllt. Mit den Voraussetzungen eines maschinenlesbaren Vorbehalts beschäftigt sich gerade der Bundesgerichtshof im Verfahren aus Abschnitt 5.

Am Ende hast du eigene Beispiele dafür, wie Schieflagen in Antworten auftauchen, und weißt, wo du Angaben zu Trainingsdaten und Vorbehalten findest.

---

## Fazit

Was ein Modell kann und wie es sich verhält, hängt an seinen Trainingsdaten: Webseiten, Bücher, Code und mehr, gefiltert und gemischt nach Regeln, die selten ganz offenliegen. Filter entfernen Unerwünschtes, können dabei aber selbst verzerren. Schieflagen in den Daten tauchen in den Ausgaben wieder auf, teils verstärkt, und das Nachtraining dämpft vor allem die offenen Vorurteile. Verdeckte Verzerrungen können bestehen bleiben, und der Abstand kann sich sogar vergrößern. Rechtlich ist das Training mit geschützten Werken in der EU an die Regeln für Text und Data Mining und an maschinenlesbare Vorbehalte gebunden. Mehrere Grundfragen liegen bei höheren Gerichten, in einem Verfahren hat der Bundesgerichtshof für Dezember 2026 einen Verkündungstermin angesetzt. Damit ist der Dahinter-Block komplett. Als Nächstes geht es in die Praxis: P1 zeigt, wie du lokale Modelle selbst betreibst.

```yaml
dokument: ki-d9-bias-daten-und-urheberrecht
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
block: dahinter
status: final
stand: 2026-11-03
quellen_fachlich:
  - "Common Crawl: Overview. https://commoncrawl.org/overview (Zugriff 2026-11-03): seit 2008 regelmäßig gesammelt, Petabytes an Daten, Zugang über Amazon kostenfrei; Crawls 2026 gelistet"
  - "Dodge u. a.: Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus (2021, v2 2021-09-30), arXiv:2104.08758. https://arxiv.org/abs/2104.08758 (Zugriff 2026-11-03): C4 aus einer Common-Crawl-Momentaufnahme; erheblicher Anteil aus unerwarteten Quellen wie Patenten und US-Militärseiten; maschinell erzeugter Text (maschinelle Übersetzung); Beispiele aus anderen NLP-Benchmarks; Sperrlisten-Filter entfernen überproportional Text von und über Minderheiten"
  - "Kotek, Dockum, Sun: Gender bias and stereotypes in Large Language Models (2023), arXiv:2308.14921. https://arxiv.org/abs/2308.14921 (Zugriff 2026-11-03): vier Modelle; drei- bis sechsmal so wahrscheinlich Wahl des geschlechterstereotypen Berufs; Verstärkung über Wahrnehmung und offizielle Berufsstatistik hinaus; Mehrdeutigkeit in rund 95 Prozent der Fälle übersehen, bei ausdrücklicher Nachfrage erkannt; Erklärungen sachlich ungenau; Ursache unausgewogene Trainingsdaten"
  - "Hofmann, Kalluri, Jurafsky, King: AI generates covertly racist decisions about people based on their dialect. Nature 633, 147-154 (2024-08-28), DOI 10.1038/s41586-024-07856-5. https://ora.ox.ac.uk/objects/uuid:4e0fe173-52f2-433d-8042-0ff941919401 (bibliografische Daten) und Abstract (Zugriff 2026-11-03): Matched Guise Probing mit afroamerikanischem Englisch; verdeckte Stereotype negativer als je experimentell bei Menschen gemessen; offene Stereotype positiver; Folgen bei Berufszuordnung, Schuldspruch und Todesstrafe; Training mit menschlichem Feedback verringert offene Stereotype, mildert die verdeckten Dialekt-Vorurteile aber nicht und kann den Abstand vergrößern"
  - "§ 44b UrhG Text und Data Mining. https://www.gesetze-im-internet.de/urhg/__44b.html (Zugriff 2026-11-03): Definition automatisierte Analyse für Muster, Trends und Korrelationen; Vervielfältigung rechtmäßig zugänglicher Werke zulässig, Löschung wenn nicht mehr erforderlich; Nutzungsvorbehalt, bei Online-Werken nur maschinenlesbar wirksam"
  - "§ 60d UrhG. https://www.gesetze-im-internet.de/urhg/__60d.html (Zugriff 2026-11-03): berechtigt sind Forschungsorganisationen ohne kommerziellen Zweck (Abs. 2), Kulturerbe-Einrichtungen und einzelne Forschende mit nicht kommerziellen Zwecken (Abs. 3)"
  - "OLG Hamburg, Urteil vom 10.12.2025, 5 U 104/24 (Kneschke gegen LAION), Bericht https://www.technologyslegaledge.com/2025/12/robert-kneschke-v-laion-judgment-of-10-december-2025-ref-5-u-104-24/ (Zugriff 2026-11-03): Berufung gegen LG Hamburg vom 27.09.2024 zurückgewiesen; Download von § 44b und § 60d UrhG gedeckt; Vorbehalt in natürlicher Sprache in Nutzungsbedingungen nicht maschinenlesbar; Frage des späteren Trainings generativer Modelle offengelassen; Revision zum BGH zugelassen. Aktenzeichen LG Hamburg 310 O 227/23 (LTO-Bericht, Suchergebnis)"
  - "Bundesgerichtshof, Terminhinweis I ZR 281/25 (Erstellen eines Datensatzes für KI-Training). https://www.bundesgerichtshof.de/SharedDocs/Termine/DE/Termine/IZR281-25.html (Zugriff 2026-11-03): Verhandlung 03.09.2026, Verkündungstermin 17.12.2026; Fragen zu § 16, § 44b Abs. 3 (Maschinenlesbarkeit des Vorbehalts), § 60d UrhG und Drei-Stufen-Test; Vorinstanzen LG Hamburg 27.09.2024, 310 O 227/23, und OLG Hamburg 10.12.2025, 5 U 104/24; Kläger verfolgt Unterlassung mit der Revision weiter"
  - "LG München I, Urteil vom 11.11.2025, 42 O 14139/24 (GEMA gegen OpenAI), Bericht LTO https://www.lto.de/recht/nachrichten/n/42o1413924-lg-muenchen-i-gema-openai-chatgpt-songtexte-ki (Zugriff 2026-11-03): Memorisierung von Liedtexten im Modell ist Vervielfältigung, nicht von § 44b UrhG gedeckt; Ausgaben verletzen Rechte, Verantwortung beim Anbieter; nicht rechtskräftig. Berufung beim OLG München (6 U 3662/25 e) laut Kanzleibeitrag https://www.hufeld.com/blog/gema-openai-ki-urheberrecht-trainingsdaten-2026 vom 15.06.2026"
  - "LG München I, Urteil vom 11.11.2025, 42 O 14139/24, Volltext https://www.gesetze-bayern.de/Content/Pdf/Y-300-Z-GRURRS-B-2025-N-30204?all=False (Zugriff 2026-11-03): Leitsatz 4 (Rn. 193) Vervielfältigungen beim Erstellen des Trainingsdatenmaterials von § 44b UrhG gedeckt, nicht aber das Training des Modells; neun Liedtexte"
  - "Verordnung (EU) 2024/1689 (KI-Gesetz), Art. 53 Abs. 1 Buchst. c und d. https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53 und https://digital-strategy.ec.europa.eu/en/factpages/general-purpose-ai-obligations-under-ai-act (Zugriff 2026-11-03): Strategie zur Einhaltung des Urheberrechts inkl. Erkennen von Vorbehalten nach Art. 4 Abs. 3 Richtlinie 2019/790; öffentliche, hinreichend detaillierte Zusammenfassung der Trainingsinhalte nach Vorlage des KI-Büros; Pflichten gelten seit 02.08.2025, Vorlage veröffentlicht"
  - "Verordnung (EU) 2024/1689, Art. 111 Abs. 3. https://artificialintelligenceact.eu/article/111/ (Zugriff 2026-11-03): Anbieter von Allzweck-KI-Modellen, die vor dem 02.08.2025 in Verkehr gebracht wurden, müssen die Pflichten bis 02.08.2027 erfüllen"
  - "Rechnung am 2026-11-03 mit Python ausgeführt: Pflegekraft sie 0,80 er 0,20; Kranführer er 0,90 sie 0,10; Übung 1 bei je fünf: 0,50 und 0,50"
  - "Eigene Artikel der Reihe: D2 (Wortvektor-Studie 2016, Embeddings geben Daten preis), D4 (Lose nach Mustern), D5 (Datenstand, Memorisierung nach Carlini u. a., Nachtraining), D6 (Mischung oft nicht offengelegt, synthetische Daten), D7, D8, E7 (Daten im Chat, Trainingsnutzung), A6, A7, A8; Vorwärtsverweise auf P1, P8, R1, R2, R5, R6"
verifikation_offen:
  - "Quellenliste in Abschnitt 1 (Web, Bücher, Code, Nachschlagewerke, lizenzierte und erzeugte Daten) ist eine verbreitete Zusammenfassung (W) aus Anbieterberichten, nicht aus einer Einzelquelle; Anteile nicht genannt"
  - "C4-Sperrlisten-Filter: Wortlaut nach Abstract (by and about minority individuals), im Text als Angabe der Autoren gekennzeichnet; welche Gruppen genau, nicht aus dem Volltext übernommen"
  - "Hofmann u. a.: Abstract und bibliografische Daten gelesen, Volltext nicht; Vergleich mit menschlichen Stereotypen seit Runde 2 auf Stereotype über Afroamerikaner begrenzt; Schuldspruch und Todesstrafe nach Abstract; Übertragbarkeit auf deutsche Dialekte nicht belegt und im Text so benannt"
  - "Beispiel mit Dialekt in der Gärtnerei ist eine eigene Veranschaulichung, keine Aussage über eine reale Person"
  - "Aussage 'Gewichte lassen sich nicht gezielt bereinigen' (Abschnitt 6) ist Fachwissen (W); Forschung zu Machine Unlearning nicht behandelt"
  - "Rechtsdarstellung stark verkürzt, keine Rechtsberatung; LAION-Stand am BGH-Terminhinweis (Primärquelle) und GEMA-Urteil am Volltext (Leitsatz) geprüft; OLG-Hamburg-Urteil und Berufungsstand GEMA nur aus Sekundärquellen; US-Verfahren bewusst nicht aufgenommen, im Text nur Hinweis auf andere Maßstäbe"
  - "Einordnung von Bewerbungs- und Beschäftigtenbewertung als mögliche Hochrisiko-Systeme (Anhang III, Beschäftigung) ist Fachwissen (W), Anhang nicht im Wortlaut gelesen; Einzelheiten in R2"
  - "Inkrafttreten der Erlaubnis für Text und Data Mining 2021 (Umsetzung der Richtlinie 2019/790 im Juni 2021) ist Fachwissen (W), Datum nicht an der Gesetzesseite geprüft"
  - "Übung 5: Namen von KI-Crawlern nicht vorgegeben, da sie sich ändern; Verhältnis robots.txt zu wirksamem Vorbehalt ist Gegenstand des BGH-Verfahrens"
  - "Vorwärtsverweise auf P1, P8, R1, R2, R5, R6 beim Anlegen abgleichen"
review_historie:
  - runde: 0
    datum: 2026-11-03
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial). Common-Crawl-Seite, C4-Untersuchung, zwei Bias-Studien, § 44b UrhG, Art. 53 KI-Gesetz und Berichte zu den Verfahren LAION und GEMA an der Quelle bzw. in Fachberichten gelesen, Verfahrensstand aktuell geprüft. Rechenbeispiel ausgeführt. Löst die Vorwärtsverweise aus D2, D5 und D6 ein und schließt den Dahinter-Block."
  - runde: 1
    datum: 2026-11-03
    ergebnis: "Eigene Reviews (Fach und Stil, Prüf-Sweep). Zwei Verneinungs-Gegensätze und zwei man-Formulierungen aufgelöst, sechs lange Sätze geteilt, offener Punkt zum Inkrafttreten 2021 ergänzt. Programm erneut ausgeführt."
  - runde: 2
    datum: 2026-11-03
    ergebnis: "Vier externe Reviews, strittige Punkte an Primärquellen geprüft. Übernommen: LAION-Verfahren beim BGH (verhandelt 03.09.2026, Verkündung 17.12.2026) laut Terminhinweis; GEMA-Urteil am Volltext enger gefasst (Datensatz gedeckt, Training nicht, neun Liedtexte); Datensatz und Training als zwei Schritte; TDM keine pauschale Erlaubnis, Forschung mit besonderen Voraussetzungen, Hinweis auf andere Rechtsräume; KI-Gesetz für alle Allzweck-KI-Modelle, Vorlage des KI-Büros, Übergangsfrist 2027, Tagesdatum; Hofmann enger (Afroamerikaner, Todesstrafe, US-Kontext, offen/verdeckt als Messwege), Nachtraining verändert Gewichte; Fazit mit wachsendem Abstand; Bias-Definition und 50:50-Hinweis; Kotek-Vergleichsgröße; C4 Patente und Testkontamination vorsichtiger; Sieb-Bild, Pronomen, Selbstbild; Eingaben und Protokolle getrennt; Hochrisiko konkreter; Übungen mit Wiederholung und robots.txt-Hinweis. Nicht übernommen: P8-Verweise durch Autorennamen ersetzen (P8 ist der Evaluationsartikel der Reihe), Autoren und URLs im Fließtext, Box umbenennen und Titel ändern (Reihenformat), Übergangsfrage vor Abschnitt 7 (keine rhetorischen Fragen)."
  - runde: 3
    datum: 2026-11-03
    ergebnis: "Zwei Re-Reviews. Übernommen: BGH als angesetzter Verkündungstermin statt sicherer Entscheidung; robots.txt-Übung auf Voraussetzungen des Vorbehalts begrenzt; Testkontamination als geringere Aussagekraft; § 60d am Gesetzestext als nicht kommerzielle Forschung (Organisationen, Kulturerbe, Einzelne); digitalisierte Werke; § 16 UrhG in der Box; Hochrisiko abhängig vom Einsatz; Kotek-Satz, Pronomen, Datum 2. August 2027, Übung 2; Hofmann-Quellennotiz an Abstract und Text angeglichen. Pflegehinweis: Beispielbox nach dem 17.12.2026 prüfen."
  - runde: 4
    datum: 2026-11-03
    ergebnis: "Freigabe durch David am 2026-11-03 nach Runde 3. Kopfzeile und YAML-Status gemeinsam auf final. Offen bleiben die Punkte unter verifikation_offen und der Pflegehinweis zur BGH-Verkündung am 17.12.2026."
```
