# KI-A5 · Code mit KI: Mitarbeiten lassen, ohne das Können abzugeben

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Aufbau-Track, Artikel A5 · Typ C (ausführlich) · Draft · Stand 2026*

---

## Worum es geht

Du kopierst eine Fehlermeldung in den Chat, setzt die Antwort ein, und das Programm läuft. Zwei Tage später taucht derselbe Fehler in anderer Gestalt wieder auf, und du weißt nicht mehr, was du geändert hast. Das kennt fast jeder, der mit einem Code-Assistenten arbeitet. Dieser Artikel zeigt, wie du KI beim Programmieren so einsetzt, dass der Code läuft und du ihn danach auch verstehst.

Am Ende kannst du eine Programmieranfrage so aufbauen, dass die Antwort weiterhilft. Du prüfst vorgeschlagenen Code in fünf Schritten, erkennst Tests, die nur den Code abschreiben, und sicherst größere Änderungen so ab, dass du sie zurückdrehen kannst. Außerdem weißt du, bei welchen Arbeitsweisen das eigene Können leidet und bei welchen nicht.

Vorausgesetzt wird der Einsteiger-Track E1 bis E8, besonders E4 (Prompts), E6 (Halluzinationen) und E7 (Datenschutz). Aus dem Aufbau-Track hilft vor allem A2 (Kontext). Ein paar Zeilen Python oder Shell reichen als Vorkenntnis, die Beispiele sind klein.

---

## 1. Wofür KI beim Programmieren taugt

Du öffnest eine Datei, die ein Kollege vor drei Jahren geschrieben hat, und verstehst keine Zeile. Genau für solche Momente ist ein Code-Assistent da. Er hat sehr viel Code gesehen, kennt aber dein Projekt nur so weit, wie du es ihm zeigst (A2).

Gut geeignet:

- **Erklären:** Code, Fehlermeldungen, Shell-Befehle, reguläre Ausdrücke und SQL-Abfragen. Einen Befehl lässt du dir erklären, bevor du ihn ausführst.
- **Fehler eingrenzen:** Das Werkzeug nennt mögliche Ursachen und sagt dir, was du dazu ausprobieren kannst.
- **Kleine, klar beschriebene Bausteine:** eine Funktion, ein kurzes Skript, ein Ausschnitt einer Konfiguration.
- **Tests entwerfen:** Dazu gibt es in Abschnitt 5 eine wichtige Einschränkung.
- **Umbauen in kleinen Schritten:** Umbenennen, Aufteilen, Vereinfachen (Abschnitt 6).
- **Zweite Meinung zu eigenem Code:** Wo fehlen Sonderfälle, wo sind Namen unklar, was könnte schiefgehen?

Mit Vorsicht:

- **Neue oder seltene Bibliotheken und Versionen.** Das Wissen eines Sprachmodells kann veraltet sein. Nenne die Version und lies die offizielle Dokumentation gegen (E6, A3).
- **Sicherheitsrelevanter Code** wie Anmeldung, Passwörter oder Eingabeprüfung (Abschnitt 7).
- **Entscheidungen über den Aufbau deines Projekts.** Randbedingungen, Team und Betrieb kennt das Werkzeug nur, wenn du sie nennst.

---

## 2. Zusehen ist noch kein Schneiden

Obstbäume veredeln lernst du nicht vom Zusehen. Der Meister zeigt den Schnitt zehnmal, du nickst jedes Mal, und beim ersten eigenen Versuch geht er trotzdem daneben. Das Können entsteht erst, wenn du selbst schneidest. Beim Programmieren ist es ähnlich: Wenn die KI den Schnitt immer macht, sitzt er bei dir nie.

Das Bild hinkt an einer Stelle, die dir zugutekommt. Ein verpfuschter Schnitt am Baum bleibt verpfuscht. Code kannst du dagegen beliebig oft neu versuchen und zurücknehmen. Du darfst also großzügiger üben als ein Gärtner.

Für den Programmieralltag gibt es dazu eine Untersuchung eines KI-Herstellers. In dem Experiment sollten 52 überwiegend junge Entwickler eine ihnen unbekannte Python-Bibliothek einsetzen. Die eine Hälfte durfte einen Chat-Assistenten fragen, die andere schrieb den Code von Hand. In einem anschließenden Quiz erreichte die KI-Gruppe im Schnitt 50 Prozent, die Gruppe ohne KI 67 Prozent. Die größte Lücke zeigte sich bei Fragen zum Fehlersuchen. Schneller war die KI-Gruppe nur um etwa zwei Minuten, und dieser Unterschied war statistisch nicht belastbar.

Dazu gehören ein paar Einschränkungen. Die Gruppe war klein, das Quiz kam direkt nach der Aufgabe, und es ging um einen Chat-Assistenten und nicht um Werkzeuge, die selbstständig arbeiten. Die Autoren selbst nennen die Ergebnisse vorläufig. Interessant ist der Blick auf die einzelnen Arbeitsweisen. Unter 40 Prozent lagen im Schnitt drei Gruppen: wer das Schreiben ganz abgab, wer erst fragte und dann alles abgab, und wer die KI vor allem zum Beheben und Prüfen des eigenen Codes nutzte. Ab 65 Prozent lagen ebenfalls drei Gruppen: wer gezielt Konzeptfragen stellte und Fehler selbst löste, wer Code zusammen mit einer Erklärung anforderte, und wer Code erzeugen ließ und danach Rückfragen stellte, um ihn zu verstehen. Diese Untergruppen waren mit zwei bis sieben Personen sehr klein. Die Autoren betonen, dass die Muster Zusammenhänge zeigen und keine Ursachen belegen.

Daraus folgt eine einfache Unterscheidung für jede Aufgabe:

- **Lernmodus:** Du willst etwas können. Probiere zuerst selbst, zum Beispiel eine Viertelstunde lang, das ist eine persönliche Faustregel. Frag dann nach einem Hinweis oder einer Erklärung statt nach der fertigen Lösung (E5, A4).
- **Liefermodus:** Du brauchst ein Ergebnis, etwa ein Wegwerfskript für heute Abend. Hier darfst du mehr delegieren. Prüfen musst du trotzdem (Abschnitt 4).

Die Entscheidung triffst du vor der Frage, nicht danach.

---

## 3. Eine Anfrage, die weiterhilft

„Das geht nicht, bitte fixen" plus eine Fehlermeldung ergibt meist eine Raterunde. Dieselbe Frage mit fünf Angaben ergibt oft eine Antwort, die passt. Die Bausteine kennst du aus E4 und A2, hier in der Programmierfassung:

- **Erwartung:** Was soll der Code tun?
- **Ist-Zustand:** Was passiert stattdessen? Die Fehlermeldung kopierst du wörtlich und vollständig.
- **Ausschnitt:** So klein wie möglich, aber so vollständig, dass du ihn nachvollziehen kannst. Meist genügt die betroffene Funktion samt Aufruf.
- **Umgebung:** Sprache, Version, Betriebssystem, eingesetzte Bibliotheken.
- **Bisherige Versuche:** Was hast du schon geprüft? Dann schlägt dir die Antwort nicht vor, was du längst ausgeschlossen hast.

Ein Beispiel:

```text
Erwartung: Das Skript soll alle .log-Dateien in einem Ordner lesen
und die Zeilen mit "ERROR" zählen.
Ist-Zustand: Es bricht nach der ersten Datei ab (Meldung unten).
Umgebung: Python 3.12, Ubuntu.
Bisher geprüft: Pfad stimmt, die Dateien sind lesbar.
Fehlermeldung: [wörtlich einfügen]
Code: [nur die betroffene Funktion]

Erkläre mir zuerst, woran es liegt. Schlage danach eine Korrektur vor.
```

Der letzte Satz ist kein Zufall. Wenn die Erklärung vor der Korrektur kommt, liest du zuerst die Ursache, und das ist der Teil, der beim nächsten Mal hilft.

Wenn du das Problem auf ein kleines Beispiel eindampfst, findest du den Fehler oft selbst. Das hilft bei der Fehlersuche auch ganz ohne KI.

Bevor du etwas einfügst, entferne Passwörter, Tokens, Schlüssel, interne Hostnamen und personenbezogene Daten (E7). Das gilt besonders für Konfigurationsdateien wie `.env`. Ein Schlüssel, der einmal in einem Chat stand, gilt als offengelegt, und du tauschst ihn aus.

---

## 4. Vorgeschlagenen Code prüfen: fünf Schritte

Die Antwort kommt nach Sekunden, sieht aufgeräumt aus und hat sogar Kommentare. Genau das macht sie gefährlich, denn Ordnung ist kein Beweis für Richtigkeit. Auch das eigene Gefühl hilft nicht viel. In einer Studie einer unabhängigen Forschungsorganisation arbeiteten 16 erfahrene Entwickler an echten Aufgaben aus ihren eigenen Projekten. Mit KI brauchten sie im Schnitt 19 Prozent länger, glaubten aber danach, 20 Prozent schneller gewesen zu sein. Die Zahlen stammen von Anfang 2025, und die Forscher selbst sagen inzwischen, dass sie aktuelle Werkzeuge nicht mehr gut abbilden. Geblieben ist die Lehre, dass Gefühl und Messung auseinanderliegen können.

Die Prüfung läuft in fünf Schritten:

1. **Lesen und zurückerklären.** Lass dir den Code Zeile für Zeile erklären und gib die Erklärung in eigenen Worten zurück. Kannst du es nicht, gehört der Code dir noch nicht.
2. **Prüfen, ob es das alles gibt.** Funktionen, Optionen und vor allem Pakete können erfunden sein (E6). Bei Paketen ist das mehr als ein Schönheitsfehler. Eine Untersuchung prüfte 576.000 erzeugte Codebeispiele aus 16 Sprachmodellen. Im Schnitt waren mindestens 5,2 Prozent der genannten Pakete bei kommerziellen und 21,7 Prozent bei offenen Modellen erfunden. Wer einen erfundenen Namen installiert, holt sich im ungünstigen Fall das, was ein Angreifer unter diesem Namen hinterlegt hat. Neuere Modelle schneiden womöglich besser ab, aber der Aufwand für die Gegenprobe ist klein. Schau dir vor dem Installieren Herausgeber, Alter und Quellcode-Verzeichnis an:

   ```bash
   npm view paketname name version time.created repository.url
   ```

   Bei Python-Paketen liefert die Projektseite auf PyPI ähnliche Angaben. Kennst du den Namen nicht und findest kaum Spuren, lässt du die Finger davon.
3. **Geschützt ausführen.** Nutze ein Testprojekt, einen eigenen Branch, einen Container oder eine virtuelle Maschine, und nie zuerst deine echten Daten. Bei Shell-Befehlen mit `rm`, `sudo` oder einem direkt in die Shell geleiteten Download (`curl ... | sh`) lässt du dir zuerst erklären, was jeder Teil bewirkt.
4. **Testen.** Abschnitt 5 zeigt, warum der Test nicht einfach aus dem Code abgeleitet sein sollte.
5. **Änderungen ansehen.** Bei jedem Eingriff in vorhandenen Code liest du die Unterschiede, bevor du sie übernimmst (Abschnitt 6).

---

## 5. Tests: Wer prüft den Prüfer?

Du bittest die KI: „Schreibe Tests für diese Funktion." Alle Tests laufen grün. Das fühlt sich gut an, ist aber so, als würde der Schüler seine Klassenarbeit selbst korrigieren. Ein Beispiel zeigt, was gemeint ist.

Die Anforderung lautet: „Ab 100 Euro gibt es 10 Prozent Rabatt." Die KI liefert diese Funktion:

```python
# rabatt.py
def preis_mit_rabatt(preis):
    if preis > 100:
        return preis * 0.9
    return preis
```

Findest du den Fehler? „Ab 100" heißt 100 oder mehr, die Funktion rechnet aber erst bei Beträgen über 100. Lässt du Tests aus diesem Code ableiten, bekommst du zum Beispiel:

```python
# test_aus_code.py
import pytest
from rabatt import preis_mit_rabatt


def test_unter_grenze():
    assert preis_mit_rabatt(50) == 50


def test_ueber_grenze():
    assert preis_mit_rabatt(150) == pytest.approx(135)


def test_genau_grenze():
    assert preis_mit_rabatt(100) == 100
```

Alle drei laufen durch. Der dritte Test bestätigt sogar den Fehler, weil er festhält, was der Code tut. Was er tun soll, steht in keinem der drei Tests. Schreibst du dagegen einen Test aus der Anforderung:

```python
# test_aus_anforderung.py
import pytest
from rabatt import preis_mit_rabatt


def test_ab_100_euro_gibt_es_rabatt():
    assert preis_mit_rabatt(100) == pytest.approx(90)
```

dann schlägt er fehl:

```text
FAILED test_aus_anforderung.py::test_ab_100_euro_gibt_es_rabatt
1 failed, 3 passed
```

Daraus ergeben sich drei Regeln:

- **Zuerst die Anforderung in Beispielen formulieren.** Eingabe und erwartetes Ergebnis schreibst du selbst, besonders an den Grenzen (genau 100, null, negativ, leer). Beim Ausformulieren zu Testcode darf dir die KI helfen.
- **Tests nicht aus dem fertigen Code ableiten lassen.** Sonst prüft der Test den Code gegen sich selbst.
- **Gegenprobe machen.** Baue absichtlich einen Fehler ein, etwa `>` statt `>=`. Wird kein Test rot, prüft die Testsammlung weniger, als sie verspricht.

Grüne Tests beweisen übrigens nie, dass der Code richtig ist. Sie zeigen nur, dass die geprüften Fälle klappen. Wie du Ergebnisse noch breiter absicherst, zeigt A8.

---

## 6. Größere Änderungen: kleine Schritte und ein Sicherheitsnetz

Du schreibst „Räum die Datei mal auf", und zurück kommen 400 geänderte Zeilen. Irgendetwas läuft jetzt nicht mehr, und du weißt nicht, was. Mit Versionskontrolle ist das ein lösbares Problem, ohne sie ein Nachmittag Detektivarbeit.

Ein Ablauf, den du übernehmen kannst:

```bash
git status                    # Ist der Stand sauber? Sonst zuerst committen.
git switch -c ki-aufraeumen   # Eigener Zweig für den Versuch
# ... Änderung durch das Werkzeug ...
git diff --stat               # Welche Dateien, wie viele Zeilen?
git diff                      # Jede Änderung lesen
git restore .                 # Alles verwerfen, falls es nichts wird
```

Vorsicht bei der letzten Zeile: `git restore .` verwirft alle noch nicht eingecheckten Änderungen im Verzeichnis. Das ist hier gewollt, weil der Versuch auf einem eigenen Zweig lief.

Dazu drei Gewohnheiten:

- **Kleine Aufträge:** „Benenne die Variablen in dieser Funktion verständlicher" statt „Verbessere das Projekt". Kleine Änderungen lassen sich lesen.
- **Nur übernehmen, was du erklären kannst.** Was du nicht verstehst, bleibt draußen oder wandert in eine Rückfrage.
- **Erst Tests, dann Umbau.** Gibt es Tests für das Verhalten, das erhalten bleiben soll, siehst du sofort, ob der Umbau etwas kaputt gemacht hat.

Werkzeuge, die selbstständig Dateien ändern und Befehle ausführen, arbeiten in der Schleife, die E4 als Loopen beschreibt. Für sie gilt dasselbe Sicherheitsnetz, nur strenger: eigener Zweig, möglichst enge Berechtigungen, Ergebnis als Unterschied lesen. Wie solche Agenten aufgebaut sind, zeigt P5. Dateien, Webseiten oder Dokumente, die ein Agent liest, können selbst Anweisungen enthalten. Das Thema heißt Prompt Injection und steht in R3.

---

## 7. Sicherheit, Geheimnisse und Regeln

Schlecht ist KI-Code nicht von Haus aus. Seine Schwächen fallen dir aber schwerer auf. Eine Studie aus dem Jahr 2022 ließ 47 Teilnehmende sicherheitsrelevante Programmieraufgaben lösen, mit und ohne Code-Assistent. Mit Assistent entstand weniger sicherer Code, und die Teilnehmenden hielten ihren Code häufiger für sicher. Die Studie ist klein und stammt aus einer früheren Modellgeneration. Die Warnung passt trotzdem: Wer Hilfe hat, schaut weniger genau hin.

Daraus ergeben sich Gewohnheiten:

- **Sicherheit ausdrücklich ansprechen.** Frage nach Schwachstellen („Wo könnte jemand diese Eingabe missbrauchen?") und prüfe die Antwort wie jede andere. Bei Datenbankzugriffen achte darauf, dass Eingaben nicht direkt in den Abfragetext gebaut werden.
- **Keine Geheimnisse in Prompts und im Code.** Passwörter und Schlüssel gehören in eine geschützte Konfiguration und nicht in einen Chat oder ein Repository (E7, R4).
- **Fremde Inhalte als Daten behandeln.** Was ein Agent aus Dateien oder dem Netz liest, ist nicht automatisch vertrauenswürdig (R3).
- **Herkunft von Code ernst nehmen.** Wem KI-erzeugter Code gehört und was bei Lizenzen gilt, behandelt R5.
- **Regeln der Stelle erfragen.** Für Prüfungen, Projektarbeiten und den Betrieb, in dem du arbeitest, gelten eigene Vorgaben zur KI-Nutzung. Frag vorher nach (R6).

---

## 8. Häufige Fehlgriffe

- **Fehlermeldung kopieren, Lösung einfügen, weitermachen.** Der Fehler ist weg, das Verständnis fehlt, und die nächste Meldung kommt bestimmt.
- **Zu viel auf einmal verlangen.** Ein ganzes Programm in einem Auftrag ergibt Code, den niemand mehr überblickt. Kleine Bausteine lassen sich prüfen.
- **Grün mit richtig verwechseln.** Tests aus dem fertigen Code bestätigen oft nur, was der Code ohnehin tut (Abschnitt 5).
- **Pakete und Befehle blind übernehmen.** Erfundene Paketnamen und riskante Befehle sind in KI-Antworten nicht selten (Abschnitt 4).
- **Vibe-Coding für Dinge, die bleiben.** Gemeint ist das Vorgehen, ein Ergebnis anzufordern, auszuprobieren und nachbessern zu lassen, ohne den Code je anzusehen. Für ein Wegwerfskript mag das reichen. Für alles, was weiterlebt, brauchst du Verständnis und Prüfung.
- **Ohne Versionsangabe fragen.** Das Werkzeug rät dann eine Version, und der Code passt nicht zu deiner Umgebung.
- **Im Kreis diskutieren.** Nach zwei oder drei erfolglosen Anläufen hilft meist ein Neustart: Problem auf ein kleines Beispiel eindampfen und ein neues Gespräch beginnen (E3, A1).

---

## Zum Ausprobieren

1. Nimm ein kleines Skript von dir oder zehn Zeilen aus einem Übungsprojekt. Lass dir jede Zeile erklären und erkläre sie dann in eigenen Worten zurück. Notiere, wo du hängen bleibst.
2. Baue absichtlich einen Fehler in ein Skript ein. Formuliere die Anfrage mit den fünf Angaben aus Abschnitt 3 und bitte um Ursache zuerst, Korrektur danach.
3. Nimm eine kleine Funktion mit einer klaren Anforderung. Schreibe drei Beispiele mit Eingabe und erwartetem Ergebnis selbst auf, auch eines an der Grenze. Lass daraus Tests formulieren und danach die Funktion schreiben. Baue zur Gegenprobe einen Fehler ein und prüfe, ob ein Test rot wird.
4. Lege einen Branch an, lass das Werkzeug eine Datei aufräumen und lies die Unterschiede. Übernimm nur, was du erklären kannst, und verwirf den Rest.
5. Schreibe zwei Sätze dazu auf: Was hast du bei dieser Übung gelernt, das du ohne KI nicht gelernt hättest, und wo hast du abgekürzt?

Am Ende hast du eine kleine eigene Arbeitsweise für Code mit KI, die zu deinem Alltag passt.

---

## Fazit

KI beim Programmieren hilft am meisten, wenn du vorher entscheidest, ob du gerade lernst oder liefern musst. Eine gute Anfrage nennt Erwartung, Ist-Zustand, Ausschnitt, Umgebung und bisherige Versuche. Vorgeschlagenen Code liest du, erklärst du dir selbst, prüfst du auf Existenz, führst du geschützt aus und testest du mit Tests, die aus der Anforderung stammen. Größere Änderungen laufen auf einem eigenen Zweig und in kleinen Schritten. Geheimnisse bleiben aus Prompts und Repositories draußen. Als Nächstes geht es in A6 um Texte, Dokumentation und Bewerbungen und darum, wie du dabei deine eigene Stimme behältst.

```yaml
dokument: ki-a5-code-mit-ki
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
status: draft
stand: 2026-10-08
quellen_fachlich:
  - "Anthropic: How AI assistance impacts the formation of coding skills. https://www.anthropic.com/research/AI-assistance-coding-skills (Zugriff 2026-10-08): 52 überwiegend junge Entwickler, Bibliothek Trio, Quiz 50 % (KI) gegen 67 % (ohne KI), größte Lücke bei Debugging-Fragen, Zeitunterschied etwa zwei Minuten nicht signifikant, Interaktionsmuster als Zusammenhänge; Autoren nennen Ergebnisse vorläufig, Chat-Assistent statt agentischer Werkzeuge"
  - "Shen, Tamkin: How AI Impacts Skill Formation. arXiv:2601.20245 (eingereicht 2026-01-28). https://arxiv.org/abs/2601.20245 (Zugriff 2026-10-08, nur Abstract gelesen)"
  - "METR: Early-2025 AI experienced open-source developer study. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ und arXiv:2507.09089 (Zugriff 2026-10-08): 16 Entwickler, 246 Aufgaben, 19 % länger mit KI, erwartet 24 % schneller, danach geglaubt 20 % schneller"
  - "METR: We are Changing our Developer Productivity Experiment Design. https://metr.org/blog/2026-02-24-uplift-update/ (Zugriff 2026-10-08): frühere Zahl bildet aktuelle Werkzeuge nicht mehr ab, neue Daten gelten als schwache Evidenz"
  - "Spracklen et al.: We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs. arXiv:2406.10279 (v3), USENIX Security 2025. https://arxiv.org/abs/2406.10279v3 (Zugriff 2026-10-08): 576.000 Codebeispiele, 16 Modelle, mindestens 5,2 % (kommerziell) und 21,7 % (offen) erfundene Pakete im Schnitt, 205.474 verschiedene erfundene Namen, Risiko Package Confusion"
  - "Perry, Srivastava, Kumar, Boneh: Do Users Write More Insecure Code with AI Assistants? arXiv:2211.03622. https://arxiv.org/abs/2211.03622 (Zugriff 2026-10-08): 47 Teilnehmende nach Ausschluss, weniger sicherer Code mit Assistent, höhere Sicherheitseinschätzung"
  - "Fowler: Vibe Coding. https://martinfowler.com/bliki/VibeCoding.html (Zugriff 2026-10-08): Begriff von Andrej Karpathy, Februar 2025, im Text ohne Namensnennung definiert"
  - "Eigene Artikel der Reihe: E3, E4 (Loopen), E5, E6, E7, A1, A2, A3, A4 (Querverweise); Vorwärtsverweise auf A6, A8, P5, R3, R4, R5, R6"
  - "Beispiel Rabatt-Funktion in Abschnitt 5 und Git-Ablauf in Abschnitt 6 am 2026-10-08 mit Python 3.11, pytest und Git 2.43 ausgeführt; npm view mit Feldern name, version, time.created, repository.url am selben Tag getestet"
verifikation_offen:
  - "Stack-Overflow-Umfrage 2025 bewusst nicht verwendet: Prozentwerte aus zwei Abrufen nicht eindeutig zuzuordnen"
  - "Anthropic-Studie nur über die Webseite des Herstellers gelesen, Volltext der arXiv-Fassung nicht geöffnet; Teilnehmerzahl und Quizwerte stammen von der Herstellerseite"
  - "Spracklen: Zahlen stammen von Modellen aus dem Entstehungszeitraum der Studie; ein Nachfolgepreprint zu Modellen von 2026 wurde nur als Titel in Suchergebnissen gesehen und nicht geöffnet"
  - "Perry et al.: Fachzeitschrift/Konferenz (vermutlich ACM CCS 2023) und eingesetztes Modell nicht erneut geprüft; im Text nur als Studie aus 2022 geführt"
  - "Faustregeln (Viertelstunde, zwei bis drei Anläufe, Gegenprobe bei Tests, Schlüssel nach Offenlegung tauschen) sind didaktische Empfehlungen ohne Einzelquelle"
  - "Vorwärtsverweise R3 (Prompt Injection), R4 (Datenabfluss), R5 (Urheberrecht), R6 (Regeln im Betrieb), P5 (Agenten), A6 und A8 beim Anlegen dieser Artikel abgleichen"
review_historie:
  - runde: 0
    datum: 2026-10-08
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial) nach Websuche zu Anthropic-Studie, METR, Paket-Halluzinationen, Perry et al. und Begriff Vibe-Coding. Code- und Git-Beispiele ausgeführt."
  - runde: 1
    datum: 2026-10-08
    ergebnis: "Eigene Fachreview und Stil-Sweep. Anbieter- und Organisationsnamen aus dem Fließtext entfernt (Reihenregel), Anthropic-Muster genauer wiedergegeben (Schwellen unter 40 und ab 65 Prozent, kleine Untergruppen), unbelegte Wertung zur Fehlersuche entfernt, man und Wir-Form aufgelöst, Verneinungs-Gegensatz und ein langer Satz umgeschrieben. Externe Reviews stehen aus."
```