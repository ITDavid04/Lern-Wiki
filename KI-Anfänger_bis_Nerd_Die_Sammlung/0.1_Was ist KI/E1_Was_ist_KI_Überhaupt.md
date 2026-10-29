# KI-E1 · Was ist KI überhaupt?

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Einsteiger-Track, Artikel E1 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Du hast bestimmt schon einmal mit einem Chat-Assistenten geschrieben. Für viele bleibt es dabei: eine bessere Suchmaschine, ein Textautomat. „KI" ist aber ein weites Feld mit sehr verschiedenen Techniken, Werkzeugen und Einsatzgebieten.

Dieser Artikel räumt zuerst die Begriffe auf. Wenn du weißt, was mit KI gemeint ist, was nicht und wie die Teilbegriffe zusammenhängen, kannst du Werkzeuge später gezielt auswählen und Ergebnisse richtig einschätzen.

Der Artikel ist freiwilliges Zusatzmaterial, egal ob du Anwendungsentwicklung oder Systemintegration lernst. Vorkenntnisse brauchst du nicht. Er ist der Anfang der Reihe, danach geht es in E2 weiter.

---

## 1. Was KI ist, und was nicht

### 1.1 Feste Abläufe, Wissensregeln und gelernte Muster

Stell dir drei Arten vor, wie in einer Gärtnerei gegossen werden kann.

Der Gießplan sagt: montags und donnerstags, 6 Uhr, zehn Minuten. Jeder Fall ist vorab festgelegt. Der Bewässerungscomputer folgt der Regel „unter 30 Prozent Bodenfeuchte wird gegossen". Auch das ist eine feste Anweisung, nur mit Sensor. Ein erfahrener Gärtner dagegen sieht Blattfarbe, Wetter und Sorte und entscheidet nach Mustern, die er an tausenden Pflanzen gelernt hat.

Der Gärtner ist natürlich kein KI-System. Das Bild zeigt nur, warum moderne KI oft nicht für jeden Einzelfall eine eigene Regel braucht.

Normale Software arbeitet im Kern wie Gießplan und Sensor: Menschen haben ausdrücklich festgelegt, was in jedem Einzelfall passiert. Ein KI-System leitet dagegen aus seinen Eingaben ab, wie eine Ausgabe erzeugt wird. Für den Einzelfall steht keine feste Anweisung bereit. Dafür gibt es zwei große Wege:

- **Maschinelles Lernen:** Das System hat Muster aus Daten gelernt. Das ist der Weg, der heute die meisten bekannten Anwendungen antreibt, vom Spamfilter bis zum Chat-Assistenten.
- **Wissens- und regelbasierte Ansätze:** Das System arbeitet mit einem ausdrücklich hinterlegten Wissens- und Regelbestand und zieht daraus Schlüsse, etwa ein Expertensystem. Solche Ansätze gelten seit den Anfängen der KI-Forschung als KI.

Beide Wege sind **Ableiten**, aber nur der erste ist **Lernen**. Das ist wichtig, weil man „KI" und „maschinelles Lernen" sonst leicht gleichsetzt. Wo die Grenze zu normaler Software genau verläuft, zeigt Abschnitt 1.3.

### 1.2 Die Definition der EU

Die EU-KI-Verordnung (Art. 3 Nr. 1) beschreibt ein **KI-System** sinngemäß mit diesen Merkmalen:

| Merkmal | Bedeutung |
| --- | --- |
| Maschinengestützt | Läuft auf Hardware und Software |
| Autonomie | Arbeitet in unterschiedlichem Grad, ohne dass jeder Schritt von Hand vorgegeben wird |
| Ableiten aus Eingaben | Das System leitet aus Eingaben ab, wie eine Ausgabe erzeugt wird. Ableiten ist dabei nicht dasselbe wie Lernen |
| Art der Ausgabe | Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen |
| Wirkung | Die Ausgabe kann physische oder virtuelle Umgebungen beeinflussen |
| Anpassungsfähigkeit | Das System kann sich nach der Inbetriebnahme verändern, muss es aber nicht |

Die OECD hat ihre Definition im November 2023 fast gleichlautend überarbeitet und „Inhalte" als mögliche Ausgabe ergänzt, damit auch generative KI darunter fällt. Das erläuternde Dokument dazu erschien im März 2024.

### 1.3 Was nach der KI-Verordnung nicht als KI-System gilt

Dieser Abschnitt beschreibt die Abgrenzung **der Verordnung**, nicht jede umgangssprachliche oder historische Einordnung. Die Leitlinien der EU-Kommission sind rechtlich nicht bindend. Sie nennen Beispiele für Systeme, die nur vordefinierte Operationen ausführen und im Sinne der Verordnung nicht aus Eingaben inferieren. „Ableiten" meint hier also nicht jede Berechnung, sondern ein Schlussfolgern, das nicht schon durch feste Operationen vorgegeben ist. Solche Systeme liegen außerhalb des KI-Begriffs:

- Datenbankverwaltung und Standard-Tabellenkalkulation
- klassische Schachprogramme, die ausschließlich mit fest programmierten Such- und Bewertungsregeln arbeiten
- beschreibende Statistik, Berichte und Diagramme
- einfache Prognosen wie ein Durchschnittswert

Die Grenze ist fließend und entscheidet sich an der tatsächlichen Funktionsweise. Ein „intelligent" beworbenes Produkt kann nur feste Wenn-dann-Logik enthalten, ein unscheinbares kann ein gelerntes Modell nutzen. Ein Schachprogramm liegt nur dann außerhalb des Begriffs, wenn es allein fest vorgegebene Regeln abarbeitet.

---

## 2. Die Begriffsfamilie

Die gängigen Begriffe sind ineinander verschachtelt und nicht gleichbedeutend:

```text
Künstliche Intelligenz (KI)
├── regelbasierte / symbolische KI
│     (Wissen und Regeln werden ausdrücklich hinterlegt)
└── Maschinelles Lernen (ML)
      (Muster werden aus Daten gelernt)
      └── Deep Learning
            (tiefe neuronale Netze)
            └── viele heutige generative KI-Systeme
                  └── z. B. große Sprachmodelle (LLMs)
```

Das Bild ist vereinfacht. Generative Verfahren gibt es auch außerhalb von Deep Learning, die heute verbreiteten Sprach-, Bild- und Audiomodelle beruhen aber fast alle darauf. In der Praxis gibt es außerdem Mischformen, etwa regelbasierte Vorprüfungen, die mit gelernten Modellen kombiniert werden.

| Begriff | Kurzdefinition | Alltagsbeispiel |
| --- | --- | --- |
| **KI** | Oberbegriff für Systeme, die Aufgaben lösen, für die man üblicherweise menschliche Intelligenz braucht | Spamfilter, Navigation, Chat-Assistent |
| **Regelbasierte (symbolische) KI** | Wissen und Regeln werden von Menschen hinterlegt, das System zieht daraus Schlüsse | Expertensystem mit Entscheidungsbaum |
| **Maschinelles Lernen** | Das System lernt Muster aus Daten, statt dass jede Regel programmiert wird | Betrugserkennung bei Zahlungen |
| **Deep Learning** | Maschinelles Lernen mit vielschichtigen neuronalen Netzen | Bild- und Spracherkennung |
| **Generative KI** | Erzeugt neue Inhalte wie Text, Bild, Audio oder Code | Text- oder Bildgenerator |
| **LLM** (Large Language Model) | Großes Sprachmodell, das auf umfangreichen Textdaten trainiert wurde und Sprache verarbeiten und erzeugen kann | Chat-Assistent |
| **Schwache (enge) KI** | Löst einen begrenzten Aufgabenbereich; alle heute produktiv genutzten Systeme. „Schwach" heißt nicht schlecht, sondern begrenzt | Übersetzer, Empfehlungssystem |
| **Starke KI / AGI** | Hypothetisch: allgemein menschenähnlich; kein Stand der Technik, Definitionen uneinheitlich | keines, bisher nur Theorie |

Wichtig für die Praxis: „KI" ist nicht gleich „Chatbot". Der Spamfilter im Postfach, die Texterkennung auf einem Foto, die Empfehlung im Streamingdienst und der Assistent, mit dem du schreibst, sind alle KI, aber sehr unterschiedliche Werkzeuge für sehr unterschiedliche Aufgaben. Wie sich diese Werkzeuge unterscheiden, zeigt E2.

---

## 3. Wie ein System aus Daten lernt

### 3.1 Beispiele statt Regeln

Stell dir einen Azubi vor, der Pflanzenkrankheiten lernt. Er kann das auf drei Wegen: Er bekommt 500 Fotos mit der richtigen Diagnose (überwacht). Er sortiert Pflanzen nach Ähnlichkeit, ohne ihre Namen zu kennen (unüberwacht). Oder er wird durch Ausprobieren und Rückmeldung besser (bestärkend).

Beim maschinellen Lernen entsprechen dem drei Grundarten. Dem System wird meist anhand von Beispielen gezeigt, worauf es ankommt, statt Regeln einzeln aufzuschreiben. Ergebnis ist ein **Modell**, das auf neue Eingaben angewendet wird.

| Lernart | Prinzip | Beispiel |
| --- | --- | --- |
| Überwachtes Lernen | Die Trainingsdaten tragen die richtige Antwort | E-Mails, die als „Spam" oder „kein Spam" markiert sind |
| Unüberwachtes Lernen | Das System findet Strukturen ohne vorgegebene Antworten | Kunden in Gruppen mit ähnlichem Verhalten einteilen |
| Bestärkendes Lernen | Das System erhält Rückmeldungen (Belohnung oder Strafe) zu seinen Aktionen und verbessert sich damit | Spielstrategien, Robotersteuerung |

### 3.2 Training und Nutzung sind zwei Phasen

Beim **Training** wird das Modell aus Daten erzeugt. Bei großen Grundmodellen ist das sehr rechenintensiv und passiert selten, kleine Modelle lassen sich oft in Minuten trainieren. Bei der **Inferenz** beantwortet das fertige Modell eine Anfrage. Das ist je Anfrage deutlich weniger Aufwand, passiert aber dauernd.

Daraus folgt ein verbreitetes Missverständnis: Ein Chat-Assistent lernt nicht bei jedem Gespräch dauerhaft dazu. Das im Modell gespeicherte Wissen stammt aus dem Training. Was ein Assistent in einem Gespräch zusätzlich berücksichtigt, kommt aus dem aktuellen Gesprächskontext, also dem Text, den er gerade vor sich hat, oder je nach System aus weiteren zugänglichen Quellen. Manche Systeme bieten außerdem eine Erinnerungsfunktion (Memory), die Angaben für spätere Gespräche speichert. Das ist ein zusätzlicher Mechanismus und kein Weitertrainieren des Modells. Mehr zum Gesprächskontext steht in E3.

---

## 4. Sprachmodelle, kurz erklärt

Mit Sprachmodellen schreiben viele Menschen heute direkt, deshalb sind sie der auffälligste Teil der KI. Drei Gedanken reichen für ein tragfähiges Grundverständnis:

1. Das Modell wurde auf riesigen Textmengen trainiert und hat dabei statistische Muster der Sprache gelernt.
2. Bei einer Anfrage erzeugt es Stück für Stück eine plausible Fortsetzung. Die Stücke heißen **Tokens**, kleine Textbausteine. Ein Wort kann aus mehreren bestehen.
3. Das Modell schlägt dabei nichts nach und garantiert nicht, dass eine Aussage wahr ist. Es rechnet, was wahrscheinlich als Nächstes kommt.

Aus Punkt 3 folgen die **Halluzinationen**: flüssig formulierte, aber erfundene Aussagen, Zahlen oder Quellen. Das Modell ist dabei nicht „kaputt". Es tut genau das, wofür es gebaut wurde: Plausibles erzeugen. Plausibel ist nicht dasselbe wie wahr.

Ein fertiger Chat-Assistent besteht oft aus mehr als dem Sprachmodell. Je nach System kann er zusätzlich Suchfunktionen, Dateien oder andere Werkzeuge nutzen und dort Informationen nachschlagen. Das verringert Fehler, schließt sie aber nicht aus, denn auch Suchergebnisse können falsch gelesen oder falsch zusammengefasst werden.

Das Bundesamt für Sicherheit in der Informationstechnik (BSI) weist darauf hin, dass gerade die oft fehlerfreie Formulierung eine falsche Sicherheit erzeugt. Es empfiehlt, Ausgaben kritisch zu lesen und von Menschen kontrollieren zu lassen. Für dich heißt das: Ergebnisse sind Entwürfe. Prüfe sie, besonders wenn Zahlen, Namen, Gesetze oder Quellen darin vorkommen. Wie man das systematisch macht, behandeln die Artikel E6 und A8.

---

## 5. Wo KI heute zum Einsatz kommt

Die Einsatzfelder sind breiter, als der Chat-Alltag vermuten lässt:

- **Entwicklung:** Code erklären, Fehler suchen, Tests vorschlagen, Dokumentation entwerfen
- **Büro und Projektarbeit:** Texte entwerfen, Protokolle zusammenfassen, Ideen sammeln, Unterlagen sichten
- **Kundenkontakt:** Anfragen vorsortieren, Antworten vorbereiten, Sprachassistenten
- **IT-Betrieb und Sicherheit:** Auffälligkeiten erkennen, Phishing-Mails erkennen, Logs auswerten
- **Lernen:** Erklärungen auf verschiedenen Niveaus, Quizfragen, Feedback zu eigenen Antworten
- **Bild, Ton, Sprache:** Transkription, Übersetzung, Bildbeschreibung, Bild- und Audiogenerierung
- **Industrie und Alltag:** Qualitätskontrolle, Prognosen, Empfehlungssysteme, Navigation

Eine Bitkom-Befragung von 604 Unternehmen in Deutschland mit mindestens 20 Beschäftigten (Herbst 2025) zeigt, wie ungleich Nutzung und Regeln verteilt sind. 8 Prozent der Unternehmen gaben an, dass Beschäftigte verbreitet private KI-Werkzeuge für die Arbeit nutzen, ohne dass der Betrieb sie freigegeben hat („Schatten-KI"). Weitere 17 Prozent nannten einzelne Fälle. 23 Prozent der Unternehmen hatten Regeln für die Nutzung aufgestellt. Die Zahlen beruhen auf den Auskünften der Unternehmen, nicht auf einer Messung der Beschäftigten. Wer Grundbegriffe und Grenzen kennt, kann sich in solchen Umgebungen sicherer bewegen. Was das für Ausbildung, Schule und Betrieb bedeutet, steht in E7.

---

## 6. Chancen und Grenzen

| Chancen | Grenzen |
| --- | --- |
| Zeitgewinn bei Routineaufgaben | Halluzinationen machen Prüfung nötig |
| Schneller Einstieg in neue Themen | Kein verlässlich überprüftes Verständnis von Fakten oder Anwendungskontext |
| Alternativen und neue Blickwinkel | Eingegebene Daten können beim Anbieter landen |
| Unterstützung bei Dokumentation und Code | Verzerrungen (Bias) aus den Trainingsdaten |
| Jederzeit verfügbar | Wer ein Ergebnis nutzt oder weitergibt, bleibt dafür verantwortlich |

Die letzte Zeile ist die wichtigste: KI nimmt dir Arbeit ab, aber nicht die Verantwortung für die Verwendung des Ergebnisses. Daneben können auch Anbieter und Organisationen eigene Pflichten haben, etwa beim Datenschutz.

---

## 7. Der rechtliche Rahmen in einem Absatz

Die EU-KI-Verordnung gilt stufenweise. Artikel 4 zur KI-Kompetenz gilt seit dem 2. Februar 2025; seine Anforderungen wurden durch die Verordnung (EU) 2026/1744 geändert. Anbieter und Betreiber von KI-Systemen müssen Maßnahmen ergreifen, die die Entwicklung der KI-Kompetenz ihres Personals und weiterer in ihrem Auftrag tätiger Personen unterstützen. Ein bestimmtes Kompetenzniveau jedes Einzelnen müssen sie nicht garantieren. Die Bundesnetzagentur nennt weder verpflichtende Zertifikate noch standardisierte Schulungen. Sie empfiehlt, Maßnahmen passend zum Einsatzkontext auszuwählen, regelmäßig aufzufrischen und zu dokumentieren. Dieselbe Änderungsverordnung hat auch mehrere Fristen für Hochrisiko-Systeme verschoben. Weitere Einzelheiten behandelt der Artikel R2. Dieser Absatz ist eine Orientierung und keine Rechtsberatung.

---

## Fazit

Du hast jetzt das Grundgerüst: KI ist ein Oberbegriff, kein einzelnes Produkt. Dazu gehören regelbasierte Systeme, maschinelles Lernen, Deep Learning und generative Verfahren. Viele heute verbreitete generative Sprach-, Bild- und Audiomodelle basieren auf Deep Learning. Der wichtigste Unterschied zu normaler Software: Ein KI-System leitet seine Ausgabe aus den Eingaben ab. Bei maschinell lernenden Systemen geschieht das aus gelernten Mustern statt aus festen Regeln. Sprachmodelle berechnen plausible Fortsetzungen und garantieren keine Wahrheit. Ihre Ergebnisse musst du deshalb prüfen, besonders bei Fakten und Quellen. Als Nächstes geht es in E2 um die Vielfalt der Werkzeuge und die Frage, welches Werkzeug zu welcher Aufgabe passt.

```yaml
dokument: ki-e1-was-ist-ki
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
status: final
stand: 2026-10-01
quellen_fachlich:
  - "EU-Kommission, Leitlinien zur Definition eines KI-Systems (veröffentlicht 06.02.2025, rechtlich nicht bindend; Service-Desk-Fassung trägt C(2025) 5053 vom 29.07.2025, Nummer/Datum separat prüfen)"
  - "Bundesnetzagentur, KI-Definitionen sowie Seite und Hinweispapier zur KI-Kompetenz nach Art. 4 KI-VO"
  - "OECD.AI, überarbeitete Definition eines KI-Systems (beschlossen Nov. 2023, Erläuterung 05.03.2024)"
  - "BSI, Generative KI-Modelle: Chancen und Risiken (02.05.2024) sowie Position zu LLMs (Mai 2023)"
  - "Bitkom Research, Schatten-KI (21.10.2025; 604 Unternehmen ab 20 Beschäftigten)"
  - "Verordnung (EU) 2026/1744 (Digital Omnibus on AI), Art. 4 gemäß Bundesnetzagentur-Darstellung; Wortlaut auf EUR-Lex noch nicht direkt gelesen"
verifikation_offen:
  - "Wortlaut Art. 3, Art. 4 KI-VO (konsolidierte Fassung) und Verordnung (EU) 2026/1744 direkt auf EUR-Lex gegenlesen; Inkrafttreten 27.07.2026 bisher nur über Sekundärquelle"
  - "Dokumentnummer und Annahmedatum der Kommissionsleitlinien klären (Veröffentlichung 06.02.2025 vs. Service-Desk-Fassung 29.07.2025)"
review_historie:
  - runde: 0
    datum: 2026-10-01
    ergebnis: "Erster Draft als Typ C ausführlich nach Recherche."
  - runde: 1
    datum: 2026-10-01
    ergebnis: "Drei externe Reviews eingearbeitet: KI/ML sauber getrennt (1.1, 1.2, Fazit), 1.3 auf KI-VO bezogen, Art. 4 auf geänderte Fassung (VO 2026/1744, per BNetzA belegt), OECD-Datum berichtigt, Aussagen zu Sprachmodell, Training, Verständnis und Verantwortung relativiert, Bitkom-Basis ergänzt. Nicht übernommen: Quellenlinks im Text (Typ C), Art. 113 und weitere Rechtsdetails (Scope)."
  - runde: 2
    datum: 2026-10-01
    ergebnis: "Zwei weitere Reviews eingearbeitet: 1.1 ohne Determinismus-Argument (Regeln je Einzelfall vs. Ableiten), 1.3 mit technischem Ableitungsbegriff, Fazit zur Verschachtelung korrigiert, Mischformen und „auffälligster Teil“ ergänzt. EUR-Lex von hier aus weiterhin nicht abrufbar, Verifikation Art. 3/4 bleibt offen (inhaltlich durch Bundesnetzagentur und zwei Reviews gestützt)."
  - runde: 3
    datum: 2026-10-01
    ergebnis: "Letzter Selbstcheck (Typ-C-Regeln, Konsistenz, alte Formulierungen): keine Befunde. Final nach ausdrücklichem OK von David. Offen bleiben die beiden Punkte unter verifikation_offen."
  - runde: 4
    datum: 2026-10-07
    ergebnis: "Sprachliche Überarbeitung durch Claude zur Angleichung der Reihe E1 bis E8: Ansprache durchgehend du, Bild vor Regel, einzelne Tabellen in Fließtext oder Liste, Querverweise und kurze Hinweise ergänzt, lange Sätze geteilt. Inhaltlich unverändert (Zahlen, Fachbegriffe, Verweise maschinell geprüft). Freigabe durch David steht aus."
```