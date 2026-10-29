# KI-A2 · Kontext ist alles: Dem Werkzeug geben, was es wissen muss

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Aufbau-Track, Artikel A2 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Stell dir vor, du kommst am ersten Tag in eine fremde Gärtnerei und der Chef sagt nur: „Mach mal den Vorgarten." Ohne Plan, ohne Fotos, ohne Budget, ohne zu wissen, ob die Kundin Rosen hasst. Du würdest raten. Oder zurückfragen. Ein KI-Werkzeug fragt oft nicht zurück. Es **rät einfach los**, und meist rät es erstaunlich überzeugend.

Ein wichtiger Hebel im Alltag ist deshalb das, was du dem Werkzeug **mitgibst**, mehr als jeder clevere Prompt-Trick. In E3 hast du gesehen, dass ein Gespräch aus Kontext besteht, und in E4, dass Ziel und Kontext die wichtigsten Prompt-Bausteine sind. Dieser Artikel macht daraus eine Arbeitsweise: Was gehört in den Kontext, in welcher Form, wie viel davon, und was lässt du besser draußen? Danach stellst du Anfragen so zusammen, dass das Werkzeug nicht raten muss.

Vorausgesetzt werden E3 (Gespräch und Kontext), E4 (Prompts), E6 (Grenzen), E7 (Daten-Ampel), E8 (Dokumente) und A1 (Werkzeugwahl).

---

## 1. Was alles „Kontext" ist

Kontext sind alle Informationen, Anweisungen und Materialien, die dem Werkzeug für eine Aufgabe zur Verfügung stehen und seine Antwort beeinflussen können. Das ist mehr als dein letzter Satz. Als Faustbild: Der Auftrag sagt, was das Werkzeug tun soll; Hintergrund, Material, Beispiele und Vorgaben sagen ihm, worum es geht und woran es sich halten soll.

- **Auftrag**: das Ziel, zum Beispiel „Erkläre mir Subnetting für meine Netzwerktechnik-Klausur".
- **Hintergrund**: das Niveau, zum Beispiel „Ich bin Umschüler, kenne Binärzahlen, aber keine Netzwerke".
- **Material**: die Grundlage, etwa Skriptseiten, eine Fehlermeldung, ein Entwurf oder eine Tabelle.
- **Beispiele**: die Vorlage, etwa ein gelungener Absatz oder eine Musterlösung.
- **Vorgaben**: der Rahmen, zum Beispiel „Maximal eine Seite, Du-Form, keine Aufzählung".
- **Dauerhafte Anweisungen**: der Standard, in Projekten oder Einstellungen hinterlegt (Abschnitt 5).

Nicht jede Aufgabe braucht alle sechs. Wenn eine Antwort enttäuscht, lohnt sich zuerst der Blick auf diese Zeilen, und die Fehlersuche wird einfacher: Welche Zeile hätte ich ausfüllen können?

---

## 2. Das Kontext-Paket: Was in eine gute Anfrage gehört

Statt einer Checkliste hilft ein Bild: Du packst dem Werkzeug eine kleine **Arbeitsmappe** zusammen. Darin liegen typischerweise fünf Bausteine, je nach Aufgabe unterschiedlich gewichtet (bei einer Fehlersuche zählt das Material oft mehr als alles andere):

**Erstens: Wofür?** Ein Satz zum Zweck. „Das ist für den Praktikumsbericht" verändert die Antwort mehr als drei Sätze zum Thema.

**Zweitens: Für wen und auf welchem Stand?** Dein Vorwissen, die Zielgruppe, der Anlass. Das spart dir das Gefühl „viel zu einfach" und das Gegenteil.

**Drittens: Das Material selbst.** Wenn es um deinen Text, deinen Code oder dein Skript geht, gib ihn mit, statt ihn aus dem Gedächtnis zu beschreiben. Eine Beschreibung ist immer schon eine Auswahl, und im Zweifel fehlt genau die Zeile, in der der Fehler steckt.

**Viertens: Vorgaben und Grenzen.** Was soll die Antwort beachten, was soll sie lassen? Etwa Länge, Du-Form oder „nur vorhandene Informationen verwenden", am besten mit Grund („Der Text wird vorgelesen, daher keine Tabellen", E4).

**Fünftens: Ein Beispiel, wenn Form oder Ton wichtig sind.** Ein gelungener Absatz zeigt oft schneller als zehn Adjektive, was du meinst (E4, Few-Shot).

Das klingt nach viel, ist aber in zwei, drei Sätzen erledigt. Ein Beispiel:

> *Schwach:* „Schreib mir was zum Thema VLAN."
>
> *Mit Kontext:* „Ich bereite mich auf eine mündliche Prüfung in Netzwerktechnik vor und kenne Switche, aber VLANs noch nicht. Erkläre mir in etwa einer Bildschirmseite, wozu man sie braucht und was ein Trunk-Port ist. Hier ist die Folie aus dem Unterricht: [Text]. Gib mir am Ende drei Fragen, mit denen ich mich selbst testen kann."

Die zweite Anfrage ist vor allem **besser ausgestattet**, an der Formulierung liegt der Unterschied weniger.

---

## 3. Material richtig mitgeben

Dateien, Screenshots und Textauszüge können besonders wertvoll sein, wenn sich die Aufgabe auf genau dieses Material bezieht. Ein paar Handgriffe machen den Unterschied:

**Auszug statt Aktenordner.** Gib das Relevante mit, nicht alles, was du hast. Bei einer Fehlermeldung startest du mit der Meldung und dem betroffenen Codeabschnitt und ergänzt bei Bedarf Umgebung oder Schritte zum Nachstellen. Bei einem Skript startest du mit dem Kapitel, um das es geht. Mehr Material ist nicht automatisch besser: Das Kontextfenster ist endlich, und bei sehr umfangreichen Eingaben kann es schwerer werden, die wirklich relevante Stelle zuverlässig zu berücksichtigen, besonders wenn sie zwischen viel Nebensächlichem liegt (E3). Relevanter Kontext hilft, unnötiger nicht.

**Sag, was das Material ist.** „Das ist mein erster Entwurf, bitte nur Struktur und Logik prüfen" ist etwas anderes als „Das ist die Aufgabenstellung des Dozenten". Ohne diese Angabe weiß das Werkzeug nicht, ob es den Text verbessern oder befolgen soll. Dasselbe gilt für Muster: „Das ist die Musterlösung, nutze sie als Vergleich, nicht als zusätzliche Aufgabe."

**Trenne Material und Auftrag.** Eine saubere Grenze hilft, etwa so: erst der Auftrag in ein, zwei Sätzen, dann das Material, klar abgesetzt. Dann bleibt unterscheidbar, was Anweisung ist und was nur Text zum Bearbeiten (das ist auch ein Sicherheitsthema).

**Prüfe, ob es wirklich gelesen wurde.** Dass eine Datei hochgeladen ist, bedeutet noch nicht, dass jede Aussage der Antwort tatsächlich auf ihr beruht (E8). Frag nach einer konkreten Stelle oder Seite, und prüfe die Antwort selbst.

**Schütze, was nicht raus soll.** Zu jedem Material gehört der Blick auf die Daten-Ampel (E7): Namen, Zugangsdaten und Betriebsinterna ersetzt du oder lässt sie weg, bevor du etwas einfügst. Mehr Kontext heißt nicht, mehr Vertrauliches zu übergeben.

---

## 4. Ein Gespräch, das den Faden hält

Auch während eines Gesprächs lässt sich Kontext pflegen, damit es nicht abdriftet.

**Zwischenstand festhalten.** Nach einer längeren Arbeitsphase hilft ein kurzer Satz wie: „Fass in fünf Zeilen zusammen, was wir bisher entschieden haben." Das ist doppelt nützlich: Du siehst, ob das Werkzeug den Faden hat, und du bekommst einen Text, den du in ein neues Gespräch mitnehmen kannst. Lies die Zusammenfassung vorher durch, denn Fehler darin wandern sonst mit (E3).

**Korrigieren statt hoffen.** Wenn eine Annahme falsch ist, sag es ausdrücklich: „Nein, die Anwendung läuft nicht in der Cloud, sondern auf einem lokalen Server." Ein Hinweis im Gespräch kann die nächsten Antworten beeinflussen, ist aber nicht in Stein gemeißelt.

**Neu starten, wenn es sich lohnt.** Wechselt das Thema oder das Material, ist ein frisches Gespräch mit sauberem Startkontext oft besser als die zwanzigste Korrektur. Das gilt besonders, wenn das Gespräch nach mehreren Korrekturen immer wieder auf alten Annahmen aufbaut (A1, E3).

---

## 5. Dauerhafte Anweisungen und Projekte: Kontext, der mitreist

Wenn du dieselben Hinweise immer wieder eintippst („Antworte auf Deutsch, in Du-Form, ich bin Umschüler"), lohnt sich eine feste Hinterlegung. Viele Werkzeuge bieten dafür etwas an, die Namen, Umfang und Zusammenspiel unterscheiden sich von Anbieter zu Anbieter, von Tarif zu Tarif und mit der Zeit:

- **Persönliche Einstellungen oder Anweisungen**, die je nach Werkzeug für viele Gespräche gelten können: gut für Sprache, Ton, Grundniveau.
- **Projekte oder Arbeitsbereiche**, in denen Chats, Dateien und Anweisungen für ein Vorhaben zusammengefasst werden können: gut für ein Thema, das über Wochen läuft, etwa die Prüfungsvorbereitung oder die Projektarbeit. Projektanweisungen können dabei anders gelten als die persönlichen.
- **Erinnerungsfunktionen (Memory)**, die relevante Angaben aus früheren Gesprächen aufgreifen können (E3, E7): bequem, aber du solltest wissen, was gespeichert ist, und es prüfen und korrigieren können.

Dabei sind Anweisungen und Memory nicht dasselbe: Anweisungen sind Vorgaben, die du bewusst setzt, Memory greift Informationen auf, die sich im Lauf der Gespräche ergeben haben.

Drei Faustregeln gelten für alle drei:

1. **Halte es kurz und wahr.** Wenige klare Zeilen wirken besser als ein Roman, und veraltete Angaben („Ich lerne gerade für Klausur X") verfälschen Antworten, wenn niemand sie aufräumt.
2. **Hinterlege nichts, was du nicht auch in einen einzelnen Chat schreiben würdest.** Was du hinterlegst, kann auch in späteren Gesprächen wieder als Kontext dienen. Prüfe deshalb vorher die Einstellungen zu Speicherung, Nutzung und Löschung (E7).
3. **Dauerhafte Anweisungen ersetzen keine Prüfung.** Auch mit perfektem Hintergrund kann eine Antwort falsch sein (E6).

Wie du daraus wiederverwendbare Anweisungen und Vorlagen baust, ist Thema von A7. Hier genügt: Es gibt diese Möglichkeit, und sie spart Tipparbeit, wenn du sie bewusst einsetzt.

---

## 6. Häufige Fehlgriffe

- **Zu wenig sagen und dann über „generische" Antworten ärgern.** Das Werkzeug kann nur verwenden, was im Kontext steht.
- **Alles hineinkippen.** Zehn Seiten Material für eine Frage, die eine Seite beantwortet, verwässern die Antwort (E3, Kontextfenster).
- **Material beschreiben statt zeigen.** Wer seinen Code „sinngemäß" schildert, bekommt Antworten zu einem Code, den es so nicht gibt.
- **Vertrauliches mitgeben, weil es „zum Kontext gehört".** Erst die Daten-Ampel (E7), dann das Einfügen.
- **Alte Hinterlegungen nie aufräumen.** Ein überholter Hinweis in den Einstellungen färbt jede künftige Antwort.
- **Dem Kontext blind vertrauen.** Der beste Kontext erhöht die Chance auf eine gute Antwort, nicht die Garantie.

---

## Zum Ausprobieren

1. Nimm eine Frage, die du in letzter Zeit gestellt und eher mittelmäßig beantwortet bekommen hast.
2. Stell sie in einem neuen Gespräch noch einmal, diesmal mit dem Kontext-Paket aus Abschnitt 2: Zweck, Stand, Material, Vorgaben und, wenn Ton oder Form wichtig sind, ein Beispiel.
3. Vergleiche die beiden Antworten und überlege, welcher Baustein den größten Unterschied gemacht hat.
4. Wenn du Lust hast, schreib dir daraus drei Sätze, die du künftig als Standardstart verwendest.

---

## Fazit

Gute Antworten beginnen mit guter Ausstattung. Zweck, Vorwissen, Material, Vorgaben und ein Beispiel sind eine kleine Arbeitsmappe, die das Werkzeug vom Raten zum Arbeiten bringt. Gib Auszüge statt Aktenordner mit, sag, was dein Material ist, prüfe, ob es gelesen wurde, und behalte die Daten-Ampel im Blick. Dauerhafte Anweisungen und Projekte lassen Kontext mitreisen, wollen aber kurz, aktuell und datensparsam gepflegt sein. Als Nächstes geht es in A3 darum, wie du bei Recherchen mit KI Quellen wirklich prüfst.

```yaml
dokument: ki-a2-kontext-ist-alles
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
status: final
stand: 2026-10-01
quellen_fachlich:
  - "Eigene Artikel der Reihe: KI-E3 (Kontext, Kontextfenster, Memory), E4 (Ziel und Kontext, Few-Shot, Begründung statt Verbot), E6, E7 (Daten-Ampel, Memory/Verlauf/Training), E8 (Datei gelesen?), A1 (Werkzeugwahl)"
  - "OpenAI Hilfezentrum: Memory in ChatGPT. https://help.openai.com/en/articles/8590148-memory-in-chatgpt (Zugriff 2026-10-01) – nur als Beispiel: Custom Instructions (direkte Vorgaben) und Memory (aus Gesprächen entwickelte Informationen) sind getrennte Funktionen; Funktionen und Steuerung variieren nach Tarif, Region, Plattform und Workspace; Memory lässt sich einsehen, bearbeiten, löschen und abschalten"
  - "OpenAI Hilfezentrum: Using projects in ChatGPT. https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt (Zugriff 2026-10-01) – nur als Beispiel: Projekte bündeln Chats, Dateien und Anweisungen; Projektanweisungen gelten nur im Projekt und überschreiben globale Custom Instructions; Verfügbarkeit je nach Tarif und Workspace"
verifikation_offen:
  - "Kontext-Paket (Reihenfolge der Bausteine), Material-Handgriffe und Faustregeln zu dauerhaften Anweisungen sind Praxisregeln ohne Einzelquelle, keine empirischen Aussagen"
  - "Funktionsumfang von Projekten, persönlichen Anweisungen und Memory ist anbieter-, tarif- und zeitabhängig; bewusst ohne Produktnamen formuliert"
  - "Der Satz 'auch ein Sicherheitsthema' in Abschnitt 3 meint Prompt Injection, bewusst ohne Begriff und ohne Verweis auf einen noch nicht geplanten Artikel; bei Reihenplanung (P/R-Track) abgleichen"
  - "Die ChatGPT-Hilfeseiten dienen nur als Beleg, dass die beschriebenen Funktionstypen existieren und sich unterscheiden; der Artikel bleibt produktneutral"
review_historie:
  - runde: 0
    datum: 2026-10-01
    ergebnis: "Erster Draft im lockeren Ton (Gärtnerei-Einstieg, Arbeitsmappe-Bild, wenig Tabellen). Bewusst ohne neue externe Zahlen und ohne Produktnamen. Abgrenzung: A7 vertieft wiederverwendbare Anweisungen, A2 nur Einführung."
  - runde: 1
    datum: 2026-10-01
    ergebnis: "Drei externe Reviews geprüft; Aussagen zu Memory/Custom Instructions/Projekten gegen die OpenAI-Hilfeseiten verifiziert (Memory und Custom Instructions getrennt, Variation nach Tarif/Region/Workspace; Projekte bündeln Chats, Dateien, Anweisungen, Projektanweisungen überschreiben globale). Übernommen: präzisere Kontext-Definition samt Faustbild Auftrag vs. Hintergrund/Material/Vorgaben (als Fließtext, kein Merksatz-Kasten), Abschwächung 'größter Hebel' und 'fehlt meistens', 'typische' statt 'Reihenfolge der Wichtigkeit', 'Vorgaben und Grenzen', 'können besonders wertvoll sein' statt 'stärkster Kontext', Fehlermeldung 'starte mit … ergänze bei Bedarf', Kontextfenster als Begriff und 'relevanter Kontext hilft, unnötiger nicht', Musterlösung als Materialbeispiel, präzisierte Datei-Aussage, 'Hinweis kann beeinflussen', Neustart-Begründung, Abschnitt 5 produktneutral mit Chats/Dateien/Anweisungen und Abgrenzung Anweisungen vs. Memory, 'dauerhaft verarbeitet' ersetzt (zwei Reviews dagegen, eines dafür), Voraussetzungen E6/E8, 'Klausur am Freitag' ersetzt, 'später in der Reihe' neutralisiert. Nicht übernommen: ASCII-Baum/Merksatz-Kasten (Typ C), Prompt-Injection-Begriff im Text (noch nicht in der Reihe eingeführt), weitere Kürzung von Abschnitt 6 (Wiederholung als Zusammenfassung vertretbar)."
  - runde: 2
    datum: 2026-10-01
    ergebnis: "Zwei Re-Reviews hatten die alte Fassung geprüft; Abgleich mit der Datei: alle genannten Punkte bereits umgesetzt. Abschluss-Selbstcheck: Querverweise (E3, E4, E6, E7, E8, A1, A7, A3) konsistent, sechs Kontextarten und fünf Bausteine stimmen mit Text und Fazit überein, keine verbotenen Typ-C-Elemente. Kopfzeile und YAML-Status gemeinsam auf final. Freigabe durch David."
  - runde: 3
    datum: 2026-10-08
    ergebnis: "Sprachliche Überarbeitung durch Claude zur Angleichung an die Einsteiger-Reihe E1 bis E8: Verneinungs-Gegensatz-Muster aufgelöst, lange Sätze geteilt, Kontextarten-Tabelle in Liste, Übungen als nummerierte Liste, kurze Querverweise ergänzt. Inhaltlich unverändert (Zahlen, Fachbegriffe, Studienangaben, Verweise maschinell geprüft). Freigabe durch David steht aus."
```