# KI-E6 · Grenzen und Halluzinationen

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Einsteiger-Track, Artikel E6 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Chat-Assistenten antworten flüssig, selbstsicher und in korrektem Deutsch, auch dann, wenn die Antwort falsch ist. Wenn du das nicht weißt, übernimmst du Fehler ungeprüft. Wenn du es weißt, kannst du KI trotzdem vielseitig nutzen und weißt, wo Prüfen Pflicht ist. Dieser Artikel erklärt, was **Halluzinationen** sind, warum sie entstehen, in welchen Situationen das Risiko besonders hoch ist und wie du Antworten überprüfst, ohne dafür jedes Mal eine halbe Stunde zu brauchen.

Vorausgesetzt werden E1 (wie Sprachmodelle arbeiten), E2 (Werkzeugtypen), E3 (Gespräch und Kontext) und E4 (Prompts). Datenschutz und Sicherheit behandelt E7.

---

## 1. Was eine Halluzination ist

Als **Halluzination** bezeichnet man eine Aussage eines Sprachmodells, die **plausibel klingt, aber falsch oder nicht durch die angegebene Quelle gedeckt ist**. Typische Formen:

- **Erfundene Quellen.** Eine Studie, ein Buch, ein Gerichtsurteil, ein Paragraf, eine Webseite, die es nicht gibt, oft mit passendem Autorennamen, Zeitschrift und Jahreszahl.
- **Falsche Einzelheiten.** Zahlen, Namen, Daten oder Orte, die nicht stimmen.
- **Erfundene Details in einem sonst richtigen Zusammenhang.** Die Grundidee stimmt, ein Detail darin nicht.
- **Falsche Zuschreibungen.** Ein Zitat wird der falschen Person zugeordnet.
- **Erfundene Funktionen oder Befehle in Code** (siehe Abschnitt 3).

Das Besondere: Die Antwort **sieht genauso aus wie eine richtige**. Es gibt in der Regel kein Warnsignal im Tonfall.

---

## 2. Warum das passiert

In E1 wurde erklärt, dass ein Sprachmodell Text auf Basis von Mustern erzeugt, die es im Training gelernt hat. Daraus folgt: Es erzeugt **wahrscheinlich klingende Fortsetzungen**, und das ist etwas anderes als „nachschlagen und wiedergeben". Eine Arbeit von 2025 (arXiv-Preprint, also noch nicht begutachtet), die auch ein großer Anbieter in einem Blogbeitrag zusammenfasst, beschreibt unter anderem zwei wichtige Mechanismen:

- **Muster reichen für manche Fakten nicht.** Rechtschreibung und Grammatik folgen klaren Mustern und werden zuverlässig gelernt. Einzelne, selten vorkommende Fakten (die Autorin einer Nischenstudie, das Geburtsdatum einer wenig bekannten Person) lassen sich aus Mustern allein nicht herleiten. Das Modell erzeugt dann trotzdem etwas Passendes.
- **In vielen Tests lohnt sich Raten.** Viele gängige Tests vergeben Punkte für richtige Antworten, aber weder für falsche noch für „Das weiß ich nicht". Das ist wie bei einer Multiple-Choice-Prüfung: Raten kann sich lohnen, Leerlassen nie. Wer Modelle auf solche Tests hin optimiert, belohnt dadurch ungewollt das Raten. Das ist keine Absicht der Entwickler. Es ist ein Nebeneffekt der Bewertung.

Eine Halluzination ist also **keine bewusste Lüge** (das Modell hat keine menschliche Absicht, jemanden zu täuschen) und **kein auf einzelne Ausrutscher beschränktes Problem**, sondern eine bekannte Fehlerklasse von Sprachmodellen. Ihre Häufigkeit lässt sich verringern, bei allgemeinen, offenen Sprachmodellen aber nicht zuverlässig auf null bringen. Selbst Werkzeuge, die zusätzlich in Quellen suchen, machen Fehler, wie das Beispiel in Abschnitt 5 zeigt.

---

## 3. Wann besondere Vorsicht nötig ist

Das Risiko ist nicht überall gleich. Eine grobe Orientierung (keine Messwerte, sondern Erfahrungswerte):

- **Einzelne Fakten:** Zahlen, Namen, Daten. Selten vorkommende Einzelheiten lassen sich schlecht aus Mustern ableiten. Prüfe gegen eine verlässliche Quelle.
- **Quellen, Zitate, Paragrafen, Aktenzeichen.** Sie sehen echt aus und lassen sich leicht erfinden. Suche und öffne sie immer im Original.
- **Aktuelles.** Ohne aktuelle, verlässliche Informationen im Gespräch oder durch ein Werkzeug kann das Modell Neues nicht zuverlässig wissen. Auch Suchergebnisse können fehlerhaft sein. Prüfe die aktuelle Quelle im Original.
- **Recht, Medizin, Finanzen.** Fehler können hier Schaden oder Haftung nach sich ziehen. Ziehe immer eine Fachquelle oder Fachperson hinzu.
- **Nischenthemen.** Es gibt wenig Trainingsmaterial. Sei skeptischer und prüfe mehr.
- **Rechnen und Logik.** Rechenwege können plausibel wirken und trotzdem falsch sein. Rechne nach.
- **Code mit unbekannten Bibliotheken.** Funktionen, Befehle oder Optionen können erfunden sein. Prüfe die offizielle Dokumentation und führe den Code aus.
- **Aussagen über sich selbst** („Ich habe das geprüft", „Ich bin sicher"). Die Selbstauskunft ist selbst eine erzeugte Antwort. Zähle sie nicht als Prüfung.

Weniger riskant, aber nicht risikofrei, sind Aufgaben, bei denen das Modell **mit deinem Material arbeitet**: umformulieren, gliedern, zusammenfassen, Fragen zu einem mitgegebenen Text beantworten (E4). Auch dabei können Details falsch wiedergegeben werden, deshalb gehört ein Stichprobenvergleich mit dem Original dazu.

---

## 4. Warum „Bist du sicher?" keine Prüfung ist

In E3 stand: Wer nur nachfragt „Bist du sicher?", bekommt häufig eine geänderte Antwort, nicht unbedingt eine richtigere. Das gilt verschärft für Quellen. Fragst du ein Modell, ob die Quelle echt ist, antwortet es mit dem gleichen Mechanismus, der die Quelle erzeugt hat, und kann sie „bestätigen". Im bekannten US-Fall **Mata v. Avianca** (2023) reichte ein Anwalt sechs erfundene Gerichtsentscheidungen ein, die er mit einem Chat-Assistenten recherchiert hatte. Auf seine Nachfrage hatte der Assistent die Fälle als echt bezeichnet und behauptet, sie stünden in Rechtsdatenbanken. Der Anwalt prüfte das nicht selbst nach. Das Gericht verhängte eine Sanktion.

Merksatz: **Eine KI kann sich nicht selbst als Quelle bestätigen.** Die endgültige Prüfung darf nicht allein auf der Behauptung desselben Modells beruhen, sie findet außerhalb des Gesprächs statt.

---

## 5. So prüfst du Antworten

Du musst nicht alles prüfen, aber das Wichtige. Eine Reihenfolge, die sich bewährt:

1. **Entscheide, was wichtig ist.** Zahlen, Namen, Quellen, Rechtliches, Medizinisches, Dinge, die du weitergibst oder auf die du etwas aufbaust. Eine freundliche Umformulierung brauchst du weniger streng zu prüfen.
2. **Suche außerhalb des Gesprächs.** Öffne die Quelle selbst: Gibt es den Titel, den Autor, die Zeitschrift? Steht die Aussage dort tatsächlich drin? Eine Quelle zu finden, die so ähnlich heißt, reicht nicht.
3. **Lies „lateral".** Wenn du eine Seite nicht kennst, bleib nicht auf ihr, um sie zu beurteilen. Öffne neue Tabs und suche, was andere über Autor, Herausgeber oder Behauptung sagen. In einer Untersuchung von Wineburg und McGrew (2019) arbeiteten professionelle Faktenprüfer so und kamen schneller zu begründeteren Urteilen als Historiker und Studierende, die Seiten vor allem von innen beurteilten.
4. **Rechne nach, führe aus.** Rechne Zahlen nach, führe Code aus und teste ihn, schlage Befehle in der offiziellen Dokumentation nach.
5. **Hol dir eine zweite, unabhängige Quelle.** Ein zweites KI-Werkzeug kann helfen, Ungereimtheiten zu finden, ist aber keine unabhängige Prüfung: Beide Werkzeuge können denselben Fehler haben.

Ein durchgespieltes Beispiel für ein Dokument steht in E8.

### Was Prompts beitragen können

Ein guter Prompt (E4) kann das Risiko senken, aber nicht beseitigen:

- **Material mitgeben,** wenn die Antwort darauf beruhen soll.
- **Unsicherheit erlauben.** „Wenn du etwas nicht sicher weißt, sag das, statt zu raten."
- **Fundstellen verlangen und dann prüfen.** „Nenne zu jeder Aussage die Stelle im Text." Das macht Prüfen leichter, ist aber selbst nur eine Behauptung des Modells.
- **Werkzeuge mit Suche nutzen** (E2). Sie können Halluzinationen verringern. In einer Auswertung spezialisierter Recherchewerkzeuge für den Rechtsbereich (2024) lag die Fehlerquote der geprüften Produkte dennoch zwischen etwa 17 und 33 Prozent, obwohl sie besser abschnitten als allgemeine Chatbots. Das bedeutet nicht, dass eine beliebige KI-Antwort mit dieser Wahrscheinlichkeit falsch ist. Die Zahl stammt aus einem bestimmten Test mit bestimmten Rechts-Recherchewerkzeugen und Aufgaben (Stand 2024). Sie zeigt aber, dass auch mit Quellenanbindung geprüft werden muss.

---

## 6. Was in der Praxis passiert ist

Drei dokumentierte Fälle zeigen, dass das keine Theorie ist:

- **Erfundene Gerichtsentscheidungen (2023).** Siehe Abschnitt 4. Folge: Das Gericht verhängte eine Sanktion von 5.000 US-Dollar und verpflichtete die Beteiligten unter anderem, den Kläger und die betroffenen Richter schriftlich zu informieren. Die Kanzlei hatte eine verpflichtende Schulung zu KI und technologischer Kompetenz bereits selbst organisiert.
- **Bericht für eine Behörde (2025).** Deloitte Australia lieferte dem australischen Arbeitsministerium einen Bericht, der erfundene Literaturverweise und ein erfundenes Gerichtszitat enthielt. Die korrigierte Fassung nannte den Einsatz eines Sprachmodells, das Unternehmen erstattete einen Teil des Honorars.
- **Falsche Auskunft eines Firmen-Chatbots (Moffatt v. Air Canada, 2024).** Ein Chatbot auf der Website der Fluggesellschaft Air Canada nannte einem Kunden falsche Regeln zu einem Tarif. Ein Tribunal in der kanadischen Provinz British Columbia entschied, dass das Unternehmen für Angaben auf der eigenen Website einschließlich des Chatbots verantwortlich bleibt, und sprach dem Kunden Schadenersatz zu. Aus der Entscheidung geht nicht hervor, ob es sich technisch um ein generatives Sprachmodell handelte. Der Fall zeigt aber, dass auch ein automatisierter Chatbot falsche Informationen mit realen Folgen liefern kann.

Gemeinsam ist: **Die eigene Verantwortung lässt sich nicht einfach auf eine KI abwälzen.** Wer Ergebnisse verwendet, veröffentlicht oder einen Chatbot anbietet, muss je nach Rolle für deren Folgen einstehen und prüfen, ob sie zuverlässig genug sind. Wer im Einzelfall rechtlich verantwortlich ist, hängt von der Situation und der Rechtsordnung ab; der Air-Canada-Fall ist eine konkrete Tribunalentscheidung, keine allgemeine Regel.

---

## 7. Beispiel: Eine erfundene Quelle aufspüren

Angenommen, ein Assistent nennt dir zu einem Nischenthema diese Quelle: *„Müller, K. & Schmidt, A. (2021): Effekte von Containerisierung auf die Wartbarkeit. Journal of Applied Software Engineering, 34(2), 112–130."* So gehst du vor:

1. Gib den Titel in Anführungszeichen in eine Suchmaschine ein. Gibt es einen Treffer, der genau diesen Titel trägt?
2. Suche die Zeitschrift und öffne gegebenenfalls DOI oder Verlagsseite. Existiert sie? Gibt es Band 34, Heft 2?
3. Suche die Autoren. Gibt es sie, und haben sie zu diesem Thema veröffentlicht?
4. Falls es die Quelle gibt: Suche die Aussage im Original. Steht dort tatsächlich, was die KI behauptet?
5. Falls nichts auftaucht: Behandle die Quelle als „nicht belegt". Verwende sie nicht und suche nach einer anderen Quelle.

Wichtig sind Schritt 4 und 5: Auch eine **echte** Quelle kann falsch wiedergegeben sein, und eine **nicht auffindbare** Quelle ist als nicht belegt zu behandeln, auch wenn sie plausibel klingt. (Die Quelle im Beispiel ist frei erfunden.)

---

## 8. Häufige Fehlgriffe

- **Dem Tonfall vertrauen.** Sicher klingen heißt nicht richtig sein.
- **Das Modell selbst prüfen lassen.** „Stimmt das?" an dieselbe KI ist keine unabhängige Prüfung (Abschnitt 4).
- **Quellen nur auf Plausibilität prüfen.** Titel, Autor und Jahr passen, die Quelle existiert trotzdem nicht.
- **Alles gleich streng prüfen.** Wenn du jedes Wort prüfst, nutzt du KI nicht mehr. Wenn du nichts prüfst, übernimmst du Fehler. Gewichte nach Risiko.
- **Einmal geprüft, immer vertraut.** Ein richtiges Ergebnis heute sagt wenig über das nächste.
- **Verantwortung abgeben.** „Die KI hat es gesagt" gilt gegenüber Dritten nicht als Entschuldigung.

---

## Zum Ausprobieren

1. Bitte einen Chat-Assistenten, dir zu einem Nischenthema, das du kennst oder gut prüfen kannst, drei Quellen mit Autor, Jahr und Fundstelle zu nennen.
2. Prüfe jede nach den Schritten aus Abschnitt 7.
3. Notiere, wie viele Quellen du findest, wie viele davon die behauptete Aussage tatsächlich enthalten und woran du die Probleme erkannt hast.
4. Wiederhole den Versuch mit einem Werkzeug, das im Web sucht, und vergleiche.

„Nicht gefunden" heißt dabei nur „nicht belegt", nicht automatisch „existiert nicht". Gewöhnlich lohnt sich dann eine zweite Suche mit anderen Suchbegriffen oder in einem Fachverzeichnis.

---

## Fazit

Sprachmodelle erzeugen plausible Antworten, nicht garantiert wahre. Halluzinationen sind deshalb eine bekannte Fehlerklasse dieser Technik und kein reiner Ausrutscher. Besonders riskant sind Einzelfakten, Quellen und Zitate, Aktuelles, Nischenthemen, Rechnen und Code mit unbekannten Funktionen. Du prüfst außerhalb des Gesprächs: Öffne Quellen im Original, rechne nach, führe aus und sieh dir eine zweite unabhängige Quelle an, gewichtet nach Wichtigkeit. Gute Prompts und Werkzeuge mit Quellenanbindung senken das Risiko, ersetzen die Prüfung aber nicht. Wenn du ein Ergebnis weitergibst, kannst du die Verantwortung dafür nicht an die KI abgeben. Als Nächstes zeigt E7, welche Daten gar nicht in ein Chatfenster gehören.

```yaml
dokument: ki-e6-grenzen-und-halluzinationen
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
status: final
stand: 2026-10-01
quellen_fachlich:
  - "Kalai et al. (2025): Why Language Models Hallucinate. arXiv:2509.04664. https://arxiv.org/abs/2509.04664; OpenAI-Beitrag (05.09.2025): https://openai.com/index/why-language-models-hallucinate/ (Zugriff 2026-10-01)"
  - "Magesh, Surani, Dahl, Suzgun, Manning, Ho (2024): Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. arXiv:2405.20362. https://arxiv.org/abs/2405.20362 (Zugriff 2026-10-01)"
  - "Wineburg & McGrew (2019): Lateral Reading and the Nature of Expertise: Reading Less and Learning More When Evaluating Digital Information. Teachers College Record. https://eric.ed.gov/?id=EJ1262001 (Zugriff 2026-10-01)"
  - "Mata v. Avianca, Inc., No. 1:22-cv-01461 (S.D.N.Y. 2023), Opinion and Order on Sanctions, Dok. 54. https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1%3A2022cv01461/575368/54/ (Zugriff 2026-10-01; Primärdokument, Sanktion 5.000 USD, Benachrichtigungsschreiben, keine zusätzliche Schulungsauflage)"
  - "CourtDocket: Mata v. Avianca: Fake ChatGPT Cases, Sanctions, and Fallout. https://courtdocket.org/mata-v-avianca-fake-chatgpt-cases-sanctions-and-fallout/ (Zugriff 2026-10-01; Sekundärquelle)"
  - "The Register (06.10.2025): Deloitte refunds Australian government over AI in report. https://www.theregister.com/2025/10/06/deloitte_ai_report_australia/ (Zugriff 2026-10-01; Sekundärquelle)"
  - "Moffatt v Air Canada, 2024 BCCRT 149 (BC Civil Resolution Tribunal, 14.02.2024); Beschreibung der Entscheidung: https://www.dww.com/articles/bc-tribunal-finds-air-canada-liable-for-inaccurate-advice-given-by-website-chatbot (Zugriff 2026-10-01; Rechtsgrundlage negligent misrepresentation; Entscheidung beschreibt Chatbot nicht als generative KI)"
  - "American Bar Association (Feb. 2024): BC Tribunal Confirms Companies Remain Liable for Information Provided by AI Chatbot (Moffatt v. Air Canada, 14.02.2024). https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/ (Zugriff 2026-10-01)"
verifikation_offen:
  - "Moffatt v. Air Canada: Primärentscheidung (CanLII, 2024 BCCRT 149) nicht selbst geöffnet, Beschreibung über Kanzleiartikel/ABA"
  - "Deloitte-Fall: Sekundärquelle (The Register); offizielle Ministeriumsunterlagen nicht selbst geöffnet; Rückerstattungsbetrag im Text bewusst offen"
  - "Risikotabelle (Abschnitt 3) und Aussage zu erfundenen Funktionen in Code beruhen auf Erfahrungswerten ohne Einzelquelle; im Text als Orientierung gekennzeichnet"
  - "Magesh et al.: Ergebnis gilt für Rechts-Recherchewerkzeuge, Stand 2024; im Text entsprechend eingeschränkt"
review_historie:
  - runde: 0
    datum: 2026-10-01
    ergebnis: "Erster Draft nach Recherche (Kontextmaterial Abschnitt 12)."
  - runde: 1
    datum: 2026-10-01
    ergebnis: "Zwei externe Reviews geprüft; Mata-Beschluss im Volltext gegengeprüft (Sanktion 5.000 USD, Benachrichtigungsschreiben, zusätzliche Schulung ausdrücklich nicht angeordnet, Kanzlei hatte selbst CLE organisiert, ChatGPT 'bestätigte' Fälle); Moffatt: Entscheidung beschreibt Chatbot nicht als generative KI. Übernommen: Mata-Folgen korrigiert, Air-Canada-Darstellung mit Fallnamen und Einschränkung, Verantwortungsaussage differenziert, 'bewusste Lüge', Fehlerklasse statt 'nicht auf null', Aktualität differenziert, Kalai als Preprint, E2 in Voraussetzungen, Magesh-Warnhinweis, Zeile Recht/Medizin/Finanzen, Übung mit 'nicht gefunden ≠ existiert nicht', Definition mit 'nicht durch Quelle gedeckt', Zitierhinweis Wineburg & McGrew. Nicht übernommen: Kurzbox 'Auf einen Blick' (Typ C), Umstellung Prävention vor Prüfreihenfolge, Zeitangabe in Übung."
  - runde: 2
    datum: 2026-10-01
    ergebnis: "Zwei weitere Re-Reviews bezogen sich auf eine ältere Fassung (Muss-Korrekturen waren bereits enthalten). Abschließender Selbstcheck: Typ-C-Regeln eingehalten, keine Produktnamen im Fließtext, Querverweise (E1–E4, E7, Abschnitte 3/4/5/7) stimmig, Header und YAML-Status konsistent. Fazit-Formulierung 'kein seltener Fehler' zu 'bekannte Fehlerklasse' präzisiert. Final auf Davids Freigabe."
  - runde: 3
    datum: 2026-10-07
    ergebnis: "Sprachliche Überarbeitung durch Claude zur Angleichung der Reihe E1 bis E8: Ansprache durchgehend du, Bild vor Regel, einzelne Tabellen in Fließtext oder Liste, Querverweise und kurze Hinweise ergänzt, lange Sätze geteilt. Inhaltlich unverändert (Zahlen, Fachbegriffe, Verweise maschinell geprüft). Freigabe durch David steht aus."
```