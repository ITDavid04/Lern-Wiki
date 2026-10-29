# KI-E2 · Die Vielfalt der Werkzeuge

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Einsteiger-Track, Artikel E2 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Wenn du KI nur als Chatfenster kennst, nutzt du einen kleinen Teil dessen, was möglich ist. Es gibt Werkzeuge, die Quellen durchsuchen, eigene Unterlagen auswerten, Code schreiben und testen, Sprache in Text verwandeln, Bilder erzeugen oder mehrstufige Aufgaben selbstständig abarbeiten. Sie unterscheiden sich in Stärken, Risiken und Kosten, und für dieselbe Aufgabe passt nicht jedes gleich gut.

Dieser Artikel baut eine Landkarte der **Werkzeugtypen** auf, damit du zu einer Aufgabe das passende Werkzeug findest. Produktnamen und kommerzielle Angebote tauchen nur in einer datierten Beispielbox am Ende auf, weil sie sich schnell ändern. Die Typen bleiben deutlich länger stabil. Vorausgesetzt werden die Begriffe aus E1 (KI, maschinelles Lernen, Sprachmodell).

---

## 1. Modell, Anwendung und Werkzeug: der Unterschied, der alles ordnet

Derselbe Dieselmotor kann in einem Traktor, einem Radlader oder einer Pumpe stecken. Was du damit erledigen kannst, hängt am Fahrzeug und am Anbaugerät, nicht nur am Motor. Bei KI-Werkzeugen ist es genauso. Zwei Dinge werden dort oft in einen Topf geworfen:

- Das **Modell** ist der Motor. Es berechnet die Antworten (zum Beispiel ein Sprachmodell, ein Bildmodell oder ein Spracherkennungsmodell).
- Die **Anwendung** ist das Fahrzeug um den Motor: Bedienoberfläche, Zugriff auf Dateien, Suche, Gedächtnis, Anbindung an andere Programme.

Dasselbe Sprachmodell kann in einem einfachen Chat, in einer Dokumentensuche und in einem Programmierwerkzeug stecken. Je nach Anwendung kann es ganz unterschiedliche Dinge tun.

Daraus folgt eine nützliche Regel: **Wähle zuerst die Aufgabe und den Werkzeugtyp, erst danach das Produkt.**

---

## 2. Die Landkarte: Werkzeugtypen im Überblick

Die Liste mischt Fähigkeiten (was ein Werkzeug tut) mit Arten der Bereitstellung (wo es läuft oder wie es eingebettet ist). Ein Werkzeug kann deshalb zu mehreren Einträgen gehören.

- **Chat-Assistent:** Führt ein Gespräch, erklärt, entwirft, formuliert um. Typisch: Begriffe erklären, Texte überarbeiten, Ideen sammeln. Achte darauf: Er kann halluzinieren, und Eingaben können beim Anbieter landen. Wie du ihn gut nutzt, zeigen E3 und E4.
- **Suche mit Quellen:** Sucht im Web und fasst die Funde mit Fundstellen zusammen. Typisch: aktuelle Informationen, Recherche mit Belegen. Achte darauf: Öffne die Quellen selbst und prüfe sie, denn auch zitierte Zusammenfassungen können Fehler enthalten.
- **Dokumenten-Assistent:** Beantwortet Fragen auf Basis eigener Dateien. Typisch: Skript, Handbuch oder Vertrag befragen, Zusammenfassungen, Lernmaterial aufbereiten. Achte darauf: Er kann scheitern, die passenden Textstellen zu finden oder richtig wiederzugeben. Prüfe bei wichtigen Antworten die Fundstelle im Original und beachte vertrauliche Dokumente.
- **Code-Assistent:** Erklärt, ergänzt und prüft Programmcode. Typisch: Fehlermeldungen deuten, Tests vorschlagen, Code erklären. Achte darauf: Vorschläge verstehen und testen, nicht blind übernehmen.
- **Bildmodelle:** Verarbeiten Bilder in verschiedenen Fähigkeiten: Erzeugen, Beschreiben, Texterkennung. Typisch: Illustrationen, Skizzen, Bildbeschreibungen, Text aus Fotos. Achte darauf: Urheberrecht und Kennzeichnung beachten, Details sind oft fehlerhaft.
- **Audio- und Sprachmodelle:** Wandeln Sprache in Text um (Spracherkennung) und Text in Sprache (Sprachausgabe). Typisch: Meetings transkribieren, Vorlesefunktion, Sprachsteuerung. Achte darauf: Bei Fachbegriffen und Dialekten gibt es Erkennungsfehler. Bei Aufnahmen von Gesprächen klärst du Vertraulichkeit und die Erlaubnis der Beteiligten.
- **Agenten:** Führen mehrere Schritte selbstständig aus und nutzen dabei Werkzeuge. Typisch: Aufgaben mit mehreren Stationen, Programmierarbeit über viele Dateien. Achte darauf: Sie brauchen klare Grenzen und Kontrolle, weil Fehler sich fortpflanzen können.
- **Lokale Modelle:** Laufen auf dem eigenen Rechner statt beim Anbieter. Typisch: datensparsames Arbeiten, Experimentieren, Offline-Nutzung. Achte darauf: Sie brauchen passende Hardware und Strom, und die Modelle sind oft kleiner und weniger leistungsfähig.
- **KI in Alltagssoftware:** Steckt in Office-Programmen, Suchmaschinen, Handys, Browsern. Typisch: Zusammenfassen, Übersetzen, Vorschläge, Fotosuche. Achte darauf: Sie ist oft unauffällig zugeschaltet, prüfe Einstellungen und Datenschutz. Mehr dazu in E8.

Die Grenzen sind fließend. Viele moderne Assistenten bündeln mehrere Typen in einer Oberfläche: Sie chatten, durchsuchen das Web, lesen hochgeladene Dateien und erzeugen Bilder. Hilfreich bleibt die Frage, **welche Fähigkeit** du gerade brauchst.

Beim Dokumenten-Assistenten steckt meist eine einfache Idee dahinter: Aus den hochgeladenen Unterlagen werden zur Frage passende Textstellen herausgesucht und dem Sprachmodell als Grundlage mitgegeben. Das Modell antwortet dann auf dieser Basis, statt nur aus dem Training. Die Technik dahinter behandelt der Artikel P4.

---

## 3. Von der Aufgabe zum Werkzeugtyp

Die Tabelle zeigt, wie sich Alltagsaufgaben auf Typen verteilen. Sie ist eine Orientierung, keine Regel: Mehrere Typen können passen, die Spalte „Erste Wahl" nennt den naheliegendsten.

| Aufgabe | Erste Wahl | Warum |
| --- | --- | --- |
| Ein Fachbegriff soll auf einfachem Niveau erklärt werden | Chat-Assistent | Gespräch mit Nachfragen, Erklärung in verschiedenen Tiefen |
| Du brauchst aktuelle Fakten, etwa zu einem Gesetzesstand | Suche mit Quellen | Fundstellen lassen sich öffnen und gegenprüfen |
| Ein 80-seitiges Skript soll abgefragt werden | Dokumenten-Assistent | Antworten beziehen sich auf die eigenen Unterlagen |
| Du verstehst eine Fehlermeldung beim Programmieren nicht | Code-Assistent oder Chat-Assistent | Code und Meldung lassen sich gemeinsam analysieren |
| Eine Besprechung soll protokolliert werden, mit Erlaubnis der Beteiligten | Audio-/Sprachmodell, danach Chat-Assistent zum Zusammenfassen | Erst Sprache zu Text, dann Text verdichten |
| Du brauchst eine Skizze oder Grafik für eine Präsentation | Bildmodell | Erzeugt Entwürfe aus Beschreibungen |
| Ein wiederkehrender Ablauf soll automatisiert werden | Agent oder Skript mit KI-Baustein | Mehrere Schritte laufen ohne manuelles Zutun |
| Vertrauliche Notizen sollen ausgewertet werden | Lokales Modell | Bei vollständig lokalem Betrieb können die Daten auf dem eigenen Rechner bleiben; Zusatzfunktionen und Einstellungen prüfen |

Das Muster dahinter: **Je mehr es auf aktuelle Fakten und Belege ankommt, desto wichtiger sind Suche und Quellen. Je mehr es um eigene Unterlagen geht, desto wichtiger ist die Anbindung an diese Unterlagen. Je vertraulicher die Daten, desto eher gehört das Werkzeug auf den eigenen Rechner oder in eine geprüfte Umgebung.**

---

## 4. Vier Unterscheidungen, die Werkzeuge einordnen helfen

### 4.1 Assistent oder Agent

Ein **Assistent** antwortet auf eine Anfrage, danach bist wieder du am Zug. Ein **Agent** bekommt ein Ziel und arbeitet mehrere Schritte selbstständig ab: Er plant, nutzt Werkzeuge (etwa Suche, Dateien, Programmierumgebungen), prüft das Zwischenergebnis und macht weiter. Wie viel Eigenständigkeit ein Agent hat, hängt vom Werkzeug und den Einstellungen ab. „Agent" bedeutet nicht automatisch vollständige Autonomie.

Das spart Handarbeit, bedeutet aber auch, dass sich ein früher Fehler durch alle folgenden Schritte ziehen kann. Je größer der Handlungsspielraum, desto wichtiger sind klare Grenzen, Protokolle und eine Kontrolle durch Menschen.

Ein möglicher Weg, KI-Anwendungen mit externen Werkzeugen und Datenquellen zu verbinden, ist das **Model Context Protocol (MCP)**, ein offener Standard. Er ist nicht nur für Agenten gedacht und keine Voraussetzung für sie. Anthropic hat MCP im Dezember 2025 an die Agentic AI Foundation übergeben, die unter dem Dach der Linux Foundation arbeitet. Wie MCP funktioniert, behandelt der Artikel P5.

### 4.2 Allgemein oder spezialisiert

Allgemeine Assistenten können vieles halbwegs gut. Spezialisierte Werkzeuge, etwa für Programmcode, Transkription oder Literaturrecherche, sind auf eine Aufgabenklasse zugeschnitten und bieten dort häufig passende Funktionen und Arbeitsabläufe. Ob sie bessere Ergebnisse liefern als ein allgemeiner Assistent, prüfst du am besten an deiner eigenen Aufgabe. Ein Spezialwerkzeug kann in einem Punkt glänzen und in einem anderen schwächer sein.

### 4.3 Cloud oder lokal

| | Cloud | Lokal |
| --- | --- | --- |
| **Wo läuft das Modell?** | Bei einem Anbieter | Auf dem eigenen Rechner |
| **Stärken** | Leistungsfähige Modelle, kein eigener Aufwand, meist vom Anbieter aktuell gehalten | Daten können für die Modellverarbeitung auf dem eigenen Rechner bleiben, Offline-Nutzung möglich, keine Gebühren pro Anfrage |
| **Schwächen** | Eingaben gehen an den Anbieter, laufende Kosten, Abhängigkeit | Hardware und Strom kosten, Einrichtung nötig, oft kleinere Modelle |

„Lokal" ist keine pauschale Datenschutzgarantie: Es gilt nur, solange Verarbeitung und genutzte Zusatzfunktionen (etwa Plug-ins oder Internetzugriff) tatsächlich auf dem eigenen Rechner bleiben.

Für den Speicherbedarf lokaler Modelle zählt der verfügbare Arbeitsspeicher bzw. GPU-Speicher. Wie viel tatsächlich gebraucht wird, hängt von der Modellgröße, der Quantisierung (Verringern der Zahlengenauigkeit, siehe P1) und der Kontextlänge ab. Manche Programme können ein Modell außerdem auf Prozessor und Grafikkarte aufteilen.

Eine grobe Faustregel für die Modellgewichte bei 4-Bit-Quantisierung: Parameterzahl mal 0,5 Byte. Kontext und Laufzeit brauchen zusätzlichen Speicher. Zur Orientierung: Eine quantisierte 8-Milliarden-Variante eines verbreiteten offenen Modells ist rund 5 GB groß, die 70-Milliarden-Variante rund 43 GB. Die Dateien liegen damit etwas über der Faustregel, weil sie zusätzliche Daten enthalten. Kleine Modelle laufen also auch auf Rechnern mit wenig Speicher, große brauchen deutlich mehr. Prüfe den Bedarf für das konkrete Modell und Programm.

### 4.4 Offen oder geschlossen

Bei **offenen Modellen** sind die Gewichte, also die gelernten Zahlenwerte des Modells, öffentlich verfügbar. Je nach Lizenz und technischer Ausstattung lassen sie sich herunterladen, lokal betreiben und teils anpassen. **Geschlossene Modelle** werden dagegen in der Regel nur über eine Anwendung oder Schnittstelle des Anbieters genutzt.

„Offene Gewichte" ist dabei nicht dasselbe wie „Open Source". Nach der Definition der Open Source Initiative (Version 1.0, Oktober 2024) gehören zu einer Open-Source-KI neben den Parametern auch der Code und ausreichend genaue Informationen zu den Trainingsdaten. Wenn du ein Modell einsetzen willst, lies deshalb die Lizenzbedingungen.

---

## 5. Drei Fragen vor der Wahl

Die drei Fragen greifen das Muster aus Abschnitt 3 als Checkliste auf.

1. **Was ist die Aufgabe, und was ist ein gutes Ergebnis?** Ein Entwurf, ein belegter Fakt, eine fertige Datei, ein automatisierter Ablauf?
2. **Welche Daten gehen hinein?** Öffentliche Texte, eigene Notizen, personenbezogene oder vertrauliche Daten? Je sensibler, desto sorgfältiger die Wahl von Anbieter, Einstellungen oder lokaler Lösung. Mehr dazu in E7.
3. **Wie wichtig ist Richtigkeit?** Bei einem Ideenentwurf reicht ein grober Treffer, bei Zahlen, Gesetzen oder Code im Einsatz braucht es eine Prüfung der Ergebnisse. Mehr dazu in E6 und A8.

---

## 6. Häufige Fehlgriffe

- **Ein Werkzeug für alles.** Wenn du jede Aufgabe im Chatfenster löst, verschenkst du Möglichkeiten und riskierst falsche Fakten, wo eine Suche mit Quellen besser wäre.
- **Dateien hochladen, ohne nachzudenken.** Vertrauliche Unterlagen gehören nicht in jedes Werkzeug. Das ist eine Frage der Umgebung, nicht nur des Misstrauens.
- **Agenten ohne Aufsicht.** Je mehr Spielraum, desto genauer ist zu prüfen, was das System getan hat.
- **Produktname statt Aufgabe.** Marken wechseln, Modelle werden ersetzt. Wenn du in Aufgaben und Typen denkst, kommst du mit jedem Neuling schnell zurecht.
- **Bunte Oberfläche gleich Qualität.** Ob ein Werkzeug sauber arbeitet, zeigt sich an geprüften Ergebnissen, nicht am Auftritt.

---

## Beispielbox: Produkte und Projekte zu den Typen

> **Stand: 01.10.2026.** Die Auswahl stützt sich auf Quellen aus dem Frühjahr und Sommer 2026. Sie ist eine Orientierung ohne Anspruch auf Vollständigkeit und ohne Bewertung. Angebote, Namen und Funktionen ändern sich schnell; der Haupttext oben bleibt davon unberührt.

| Typ | Beispiele |
| --- | --- |
| Chat-Assistenten | ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Copilot (Microsoft), Angebote von Mistral, DeepSeek und xAI (Grok) |
| Suche mit Quellen | Perplexity; außerdem Suchfunktionen innerhalb der Chat-Assistenten |
| Dokumenten-Assistent | Gemini Notebook (Google, bis Juli 2026 unter dem Namen NotebookLM): beantwortet Fragen auf Basis hochgeladener Quellen |
| Code-Assistenten in der Entwicklungsumgebung | Cursor, GitHub Copilot |
| Code-Agenten im Terminal | Claude Code, OpenCode, Aider |
| Code-Agenten in der Cloud | Devin, Codex Cloud (OpenAI) |
| Bildmodelle | Midjourney, Stable Diffusion, Adobe Firefly |
| Sprachausgabe | ElevenLabs (Cloud), Piper (lokal) |
| Spracherkennung | Whisper (OpenAI), offenes Modell, lokal betreibbar |
| KI in Alltagssoftware | Copilot in Windows und Office (Microsoft), Gemini in Google-Diensten, Firefly in Adobe-Programmen |
| Lokale Modelle (Programme) | Ollama, llama.cpp, LM Studio |
| Offener Standard zur Werkzeuganbindung | Model Context Protocol (MCP) |


---

## Fazit

KI ist ein Werkzeugkasten, kein einzelnes Werkzeug. Die wichtigste Unterscheidung ist die zwischen Modell (Motor) und Anwendung (Fahrzeug): Was ein Werkzeug kann, hängt an beidem. Werkzeugtypen wie Chat-Assistent, Suche mit Quellen, Dokumenten-Assistent, Code-Assistent, Bildmodelle, Audio- und Sprachmodelle, Agenten, lokale Modelle und KI in Alltagssoftware decken sehr verschiedene Aufgaben ab. Wenn du erst die Aufgabe klärst, dann die Daten und die Anforderung an die Richtigkeit, findest du meist schnell den passenden Typ. Als Nächstes geht es in E3 darum, mit einem Chat-Assistenten ein Gespräch zu führen statt nur Einzelfragen zu stellen.

```yaml
dokument: ki-e2-die-vielfalt-der-werkzeuge
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
status: final
stand: 2026-10-01
quellen_fachlich:
  - "MCP-Blog, MCP joins the Agentic AI Foundation (09.12.2025)"
  - "Google, NotebookLM wird Gemini Notebook (16.07.2026)"
  - "Continue-Repository (nicht mehr gepflegt, daher nicht in der Box)"
  - "OpenAI Hilfezentrum, Using Codex Cloud"
  - "Open Source Initiative, Open Source AI Definition 1.0 (28.10.2024)"
  - "Ollama-Bibliothek Llama 3.1 (Dateigrößen 8B ca. 4,9 GB, 70B ca. 43 GB, jeweils q4_K_M)"
  - "IT-Daily, KI-Assistenten im Vergleich 2026 (01.05.2026); Firecrawl, Best AI Coding Agents (2026); daily.dev, Running LLMs Locally (2026); innfactory.ai, Whisper; itgrundlagen.com, KI-Liste 2026; kopfundstift.de, KI-Sprachgeneratoren (Stand Juli 2026) – nur für Produktbox, Sekundärquellen"
verifikation_offen:
  - "Produktzeilen ohne Primärbeleg (Perplexity, Cursor, GitHub Copilot, Claude Code, OpenCode, Aider, Devin, Bildmodelle, ElevenLabs, Piper, Alltagssoftware, Mistral/DeepSeek/xAI) über Herstellerseiten prüfen"
  - "Faustregel 0,5 Byte pro Parameter und CPU/GPU-Aufteilung gegen Ollama- bzw. llama.cpp-Dokumentation abgleichen (Artikel P1)"
  - "MCP-Angaben gegen Mitteilung der Linux Foundation prüfen"
review_historie:
  - runde: 0
    datum: 2026-10-01
    ergebnis: "Erster Draft nach Recherche."
  - runde: 1
    datum: 2026-10-01
    ergebnis: "Drei externe Reviews eingearbeitet und gegen Primärquellen geprüft: NotebookLM zu Gemini Notebook (16.07.2026), Continue entfernt, Open Weights von Open Source AI getrennt, VRAM-Tabelle durch qualitative Aussage und Faustregel ersetzt, Lokal-Datenschutz und Kosten präzisiert, MCP von Agenten gelöst, Agent nicht automatisch autonom, Spezialwerkzeuge neutral, Box um Bildmodelle, Sprachausgabe und Alltagssoftware ergänzt, Anbieter bei Grok ergänzt, Hoflader durch Radlader ersetzt. Nicht übernommen: weitere Zahlenstaffel zu VRAM, Produktvergleiche."
  - runde: 2
    datum: 2026-10-01
    ergebnis: "Letzter Selbstcheck: Typ-C-Regeln und alte Formulierungen geprüft, keine Befunde. Kleine Glättungen (Faustregel mit Dateigröße abgeglichen, zwei Absolutformulierungen entschärft). Final nach ausdrücklichem OK von David. Produktzeilen bleiben Sekundärquellen-Stand, siehe verifikation_offen."
  - runde: 3
    datum: 2026-10-07
    ergebnis: "Sprachliche Überarbeitung durch Claude zur Angleichung der Reihe E1 bis E8: Ansprache durchgehend du, Bild vor Regel, einzelne Tabellen in Fließtext oder Liste, Querverweise und kurze Hinweise ergänzt, lange Sätze geteilt. Inhaltlich unverändert (Zahlen, Fachbegriffe, Verweise maschinell geprüft). Freigabe durch David steht aus."
```