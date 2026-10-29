# LF5.1 – Requirements & Analysis

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 70–90 Minuten für das erste Durcharbeiten, +50–70 Minuten mit Selbsttest und Wiederholung
> **Status:** Final
> **Stand:** 2026-09-11
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was unterscheidet Lastenheft und Pflichtenheft, und wer schreibt was? | [→ 1. Lastenheft & Pflichtenheft](#1-lastenheft-und-pflichtenheft) |
| 2 | Wie extrahiert man aus chaotischen Stakeholder-Aussagen konkrete Anforderungen? | [→ 2. Anforderungserhebung](#2-anforderungserhebung-und-interviewtechniken) |
| 3 | Wie werden Anforderungen kategorisiert, und was regelt ISO/IEC 25010? | [→ 3. Anforderungskategorien](#3-anforderungskategorien-und-isoiec-25010) |
| 4 | Wie formuliert man eine Anforderung strukturiert und testbar? | [→ 4. Anforderungen formulieren](#4-anforderungen-strukturiert-formulieren-orientiert-an-isoiecieee-29148) |
| 5 | Wie priorisiert das Kano-Modell Anforderungen nach Kundenzufriedenheit? | [→ 5. Kano-Modell](#5-priorisierung-mit-dem-kano-modell) |

---

## 1. Lastenheft und Pflichtenheft

> **Grundprinzip:** Ein Bauherr beschreibt einem Architekten, dass er "ein helles, modernes Haus mit drei Schlafzimmern und Platz für zwei Autos" will – das ist sein Wunsch, seine Last. Der Architekt macht daraus einen detaillierten Bauplan mit exakten Maßen, Materialien und Statik-Berechnungen – das ist seine Pflicht, diesen Wunsch technisch umzusetzen. Genau diese Arbeitsteilung beschreiben Lastenheft und Pflichtenheft in der IT.

### 1.1 Die Dokument-Dualität

Lastenheft und Pflichtenheft sind klassische Begriffe des deutschen Projektmanagements. Aktuelle Fachquellen beziehen sich für ihre Definitionen überwiegend auf **DIN 69901-5:2009-01** ("Projektmanagement – Projektmanagementsysteme – Teil 5: Begriffe"); die historische Ursprungsnorm **DIN 69905:1997** wird in älteren Unterlagen noch häufig genannt. Für die Prüfung sind Autor:in, Zweck und Perspektive der beiden Dokumente wichtiger als die exakte Normnummer.

| Merkmal | Lastenheft | Pflichtenheft |
| --- | --- | --- |
| **Autor:in** | Auftraggeber:in / Kundschaft | Auftragnehmer:in / IT-Team |
| **Kernfrage** | **WAS** soll gelöst werden, und **WARUM**? | **WIE** wird das System die Lösung technisch umsetzen? |
| **Inhalt** | Probleme, Ziele, Anwendungsfälle, Rahmenbedingungen | Architektur, Technologie-Stack, Datenmodelle, Schnittstellen |
| **Typischer Zeitpunkt** | Zu Beginn bzw. vor der Auswahl/Beauftragung eines Auftragnehmers | Auf Grundlage des Lastenhefts, häufig nach Beauftragung und vor der Umsetzung |

> **Merkhilfe:** *Lastenheft* = die **Last**, das Problem zu beschreiben, liegt beim Auftraggeber. *Pflichtenheft* = die **Pflicht**, die Lösung zu beschreiben, liegt beim Auftragnehmer.

### 1.2 Qualitätskriterien für Anforderungsdokumente

Ein gutes Anforderungsdokument (Requirements Engineering, IREB-Standard) sollte laut Fachliteratur diese Eigenschaften erfüllen:

- **Vollständig** – keine wichtigen Aspekte fehlen
- **Eindeutig** – keine unterschiedlichen Lesarten möglich
- **Widerspruchsfrei** – keine sich gegenseitig ausschließenden Anforderungen
- **Nachvollziehbar** – Herkunft und Begründung sind erkennbar
- **Überprüfbar** – es lässt sich eindeutig testen, ob die Anforderung erfüllt ist

### 1.3 Rechtliche Bedeutung

Ein Pflichtenheft kann als Leistungsbeschreibung in einen Vertrag einbezogen werden und dadurch mitbestimmen, welche Beschaffenheit bzw. welcher Erfolg geschuldet ist – bei einem entsprechend gestalteten Vertrag oft im Rahmen eines **Werkvertrags** (§ 631 BGB, siehe WiSo 4, Abschnitt 2.1). Ob im Einzelfall tatsächlich ein Werkvertrag vorliegt und welche rechtliche Wirkung das Dokument konkret hat, hängt jedoch von der jeweiligen Vertragsgestaltung ab – nicht jedes Softwareprojekt ist automatisch ein Werkvertrag, und ein Pflichtenheft wird nicht allein durch eine Unterschrift zwangsläufig zum vollständigen Vertragsinhalt.

> **IHK-Typfrage:** *"Ein Auftragnehmer beginnt mit der Programmierung, nachdem er nur das Lastenheft erhalten hat, ohne ein eigenes Pflichtenheft zu erstellen. Welche Risiken entstehen dadurch?"*
> **Musterantwort:** Das Lastenheft beschreibt nur das Problem und die Ziele aus Kundensicht, nicht aber die konkrete technische Umsetzung. Ohne ein Pflichtenheft fehlt die verbindliche, detaillierte Spezifikation (Architektur, Schnittstellen, Datenmodelle, Abnahmekriterien), auf die sich beide Seiten einigen. Das birgt erhebliche Risiken: Der Auftragnehmer trifft technische Entscheidungen ohne dokumentierte Abstimmung, spätere Änderungswünsche des Kunden sind schwer von "eigentlich schon vereinbart" zu unterscheiden, und im Streitfall (z. B. über Nacherfüllung oder Abnahme) fehlt eine klare vertragliche Referenz, was die eigentliche Leistung war.

---

## 2. Anforderungserhebung und Interviewtechniken

> **Grundprinzip:** Ein Kunde im Restaurant sagt nicht "Ich möchte ein Gericht mit 350 Kalorien, 20 g Protein und einer Garzeit von maximal 12 Minuten" – er sagt "Ich habe Hunger, aber es soll nicht zu schwer im Magen liegen." Die Aufgabe der Servicekraft (und in der IT: der Requirements Engineerin) ist es, aus solchen Alltagsformulierungen die eigentliche Anforderung herauszuhören.

### 2.1 Vom chaotischen Statement zur Anforderung

Stakeholder liefern selten fertige IT-Anforderungen – sie sprechen über Ängste, Wünsche und Probleme. Die Aufgabe besteht darin, zwischen den Zeilen zu lesen: Sagt eine Nutzerin "Ich hasse es, auf das Drehrädchen zu warten", ist die extrahierte technische Anforderung: *Das System hat ein Performance-/Latenzproblem.*

### 2.2 Interviewtechniken

| Fragetyp | Beispiel | Ergebnis | IHK-Relevanz |
| --- | --- | --- | --- |
| **Offene Frage** | "Wie gehen Sie aktuell mit X um?" | Erzählungen, Prozesse, Kontext | 🔴 |
| **Geschlossene Frage** | "Nutzen Sie Mac oder Windows?" | Harte Fakten, aber ohne Kontext | 🟡 |

> **Wichtige Prüfungsfalle:** Suggestivfragen wie "Wäre eine Datenbank hier nicht besser?" zwingen Stakeholder zu technischen Entscheidungen, die sie oft gar nicht beurteilen können. Immer nach dem **Problem** fragen, nicht nach der **Lösung** – die Lösung ist Aufgabe der IT, nicht des Stakeholders.

> **IHK-Typfrage:** *"Extrahieren Sie die technischen Anforderungen aus folgender Aussage: 'Mein Team beschwert sich ständig. Sie müssen von zuhause aus arbeiten können, aber das VPN bricht immer ab. Außerdem ist die App hässlich, und die Exportfunktion stürzt ab, wenn die Datei über 50 MB groß ist.'"*
> **Musterantwort:** Aus der Aussage lassen sich mindestens drei eigenständige technische Anforderungen extrahieren: (1) Eine stabile Remote-Zugriffslösung (VPN-Verbindung mit ausreichender Stabilität/Zuverlässigkeit), (2) eine überarbeitete Benutzeroberfläche (Usability-Anforderung, auch wenn "hässlich" subjektiv ist, deutet es auf ein UX-Problem hin, das konkretisiert werden muss), (3) eine funktionierende Exportfunktion für Dateien über 50 MB (funktionale Anforderung mit einer klaren Fehlergrenze). Wichtig: Die persönliche Formulierung ("hässlich", "ständig") ist keine technische Spezifikation – sie muss in den nächsten Schritten präzisiert werden (siehe Abschnitt 4).

---

## 3. Anforderungskategorien und ISO/IEC 25010

> **Grundprinzip:** Ein Auto muss fahren (das ist seine Funktion) – aber es soll auch sicher, sparsam und bequem sein (das sind Qualitätsmerkmale, keine reinen Funktionen). Software-Anforderungen lassen sich auf dieselbe Weise in "was das System tun muss" und "wie gut es das tun muss" trennen.

### 3.1 Die drei Anforderungstypen

| Kategorie | Bedeutung | Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **Funktionale Anforderungen (FR)** | Welches Verhalten/Ergebnis muss das System liefern? | "Das System berechnet die Steuer" | 🔴 |
| **Nicht-funktionale Anforderungen / Qualitätsanforderungen (NFR)** | Wie gut muss das System eine Funktion erfüllen, welche messbare Qualität muss es besitzen? | "Das System reagiert innerhalb von 2 Sekunden" | 🔴 |
| **Constraints (Rahmenbedingungen)** | Welche Vorgabe begrenzt den Lösungs- bzw. Entwicklungsraum? | "Budget: 5.000 €", "Muss auf dem vorhandenen Linux-Server laufen" | 🔴 |

> **Wichtige Prüfungsfalle:** Constraints und NFRs werden häufig verwechselt. Der Unterschied liegt **nicht** darin, ob eine Anforderung "von außen kommt" oder "selbst gesetzt" ist – beide können von Kundschaft, Gesetzgeber oder dem eigenen Unternehmen stammen. Entscheidend ist die **Funktion** der Anforderung: Ein **Constraint** begrenzt den Lösungsraum (z. B. vorgegebene Technologie, Budget, Infrastruktur), eine **Qualitätsanforderung (NFR)** beschreibt, wie gut eine Funktion erfüllt werden muss (z. B. Antwortzeit, Sicherheit). Beide können miteinander in Konflikt geraten – z. B. ein knappes Budget (Constraint) gegen eine hohe Performance-Anforderung (NFR). Constraints sind zudem nicht zwangsläufig für die gesamte Projektlaufzeit fix – sie können im Projekt neu verhandelt werden, begrenzen aber, solange sie gelten, den Lösungsraum.

### 3.2 Nicht-funktionale Anforderungen strukturieren: ISO/IEC 25010

Die Norm **ISO/IEC 25010** liefert ein Qualitätsmodell zur systematischen Einordnung von NFRs. Die aktuelle Fassung **ISO/IEC 25010:2023** definiert **neun** Produktqualitätsmerkmale (die ältere Fassung von 2011 mit acht Merkmalen ist inzwischen zurückgezogen, wird in vielen Ausbildungsunterlagen aber noch verwendet):

| Qualitätsmerkmal | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Functional Suitability** | Erfüllt das System die benötigten Funktionen vollständig und korrekt? | 🔴 |
| **Performance Efficiency** | Geschwindigkeit, Ressourcenverbrauch | 🔴 |
| **Compatibility** | Zusammenspiel mit anderen Systemen | 🟡 |
| **Interaction Capability** | Bedienbarkeit/Interaktion (in der 2011er-Fassung noch "Usability" genannt) | 🔴 |
| **Reliability** | Verfügbarkeit, Fehlertoleranz des Systems | 🔴 |
| **Security** | Vertraulichkeit, Integrität | 🔴 |
| **Maintainability** | Modularität, Testbarkeit, Änderbarkeit | 🟡 |
| **Flexibility** | Anpassbarkeit an veränderte Anforderungen (u. a. Nachfolger von "Portability") | 🟢 |
| **Safety** | Vermeidung/Begrenzung von Risiken für Menschen, Umwelt, Vermögen | 🟢 |

> **Hinweis zum Normstand:** Falls euer Unterricht noch mit dem verbreiteten 2011er-Modell arbeitet, sind dort insbesondere **Usability** (statt Interaction Capability) und **Portability** als eigenständige Hauptmerkmale zu nennen, dafür fehlen Flexibility und Safety. Für die Prüfung zählt vor allem das Prinzip (systematische Gliederung von NFRs), nicht das exakte Auswendiglernen aller neun Begriffe.

> **IHK-Typfrage:** *"Eine Kundin formuliert die vage Anforderung 'Die Software muss sicher sein.' Wie würden Sie das konkretisieren?"*
> **Musterantwort:** "Sicher" ist keine testbare Anforderung, sondern eine allgemeine Erwartung. Im ISO/IEC-25010-Modell fällt das primär unter die Kategorie **Security**, die sich weiter in Unterkategorien wie Vertraulichkeit, Integrität und Authentizität aufteilt. Eine konkrete, testbare Formulierung wäre z. B.: "Passwörter werden ausschließlich mit einer geeigneten Passwort-Hashfunktion inkl. individuellem Salt gespeichert, niemals im Klartext oder reversibel verschlüsselt" oder "Der Zugriff auf Kundendaten erfordert eine Zwei-Faktor-Authentifizierung." Erst durch diese Konkretisierung wird die vage Kundenaussage zu einer überprüfbaren Anforderung.

> **Wichtig für die Prüfung – Hashing ≠ Verschlüsselung:** Verschlüsselung ist grundsätzlich umkehrbar, wenn der passende Schlüssel vorliegt. Ein kryptografischer Hash (z. B. über bcrypt, scrypt oder Argon2id) ist bewusst **nicht** umkehrbar konzipiert – genau das macht ihn für die Passwortspeicherung geeignet. Beide Begriffe im Zusammenhang mit Passwörtern zu vermischen, ist ein klassischer Prüfungsfehler.

---

## 4. Anforderungen strukturiert formulieren (orientiert an ISO/IEC/IEEE 29148)

> **Grundprinzip:** Ein Kochrezept, das sagt "eine ordentliche Portion Salz, ungefähr fertig backen" führt bei jeder Köchin zu einem anderen Ergebnis. Ein Rezept mit "5 g Salz, 180 °C, 25 Minuten" lässt keinen Interpretationsspielraum. Genauso streng muss eine gute IT-Anforderung formuliert sein.

### 4.1 Eine didaktische Formulierungsschablone

**ISO/IEC/IEEE 29148** beschreibt vor allem, welche **Eigenschaften** eine gute Anforderung haben muss (siehe 4.2) – die Norm schreibt aber nicht eine einzige feste deutsche Satzschablone vor. In der Praxis (u. a. bei IREB) werden dafür **Anforderungsschablonen** verwendet, die je nach Kontext unterschiedlich aussehen können. Eine verbreitete, gut merkbare Lernschablone ist:

> **"Unter \[Bedingung\] muss das System \[Funktion\] mit \[messbarem Kriterium\] leisten."**

Das ist eine **didaktische Hilfe**, keine wörtlich vorgeschriebene Normgrammatik – für die Prüfung zählt vor allem, dass am Ende eine eindeutige, testbare Aussage steht, unabhängig von der exakten Satzform.

### 4.2 Die Regeln guter Anforderungen

| Regel | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Atomar** | Möglichst eine prüfbare Verpflichtung pro Anforderung. "Und"/"oder" sind Warnsignale für zusammengesetzte Anforderungen, aber nicht automatisch verboten (z. B. ist "zeigt Vor- und Nachnamen an" weiterhin eine einzelne fachliche Verpflichtung) | 🔴 |
| **Eindeutig** | Kein Interpretationsspielraum – Wörter wie "schnell" oder "benutzerfreundlich" vermeiden | 🔴 |
| **Testbar** | Ein klarer Ja/Nein-Test muss formulierbar sein | 🔴 |
| **Verbindlichkeit korrekt kennzeichnen** | **muss** (verbindlich, shall) / **sollte** (Empfehlung, geringere Verbindlichkeit, should) / **kann** (Erlaubnis/Option, may) – diese drei sauber auseinanderhalten | 🔴 |

> **Wichtige Prüfungsfalle:** "Soll" wird im Deutschen häufig fälschlich mit "Kann-Anforderung" gleichgesetzt. Fachlich korrekt ist die Dreiteilung **muss** (verbindlich) / **sollte** (Empfehlung) / **kann** (Option) – nicht "soll vs. sollte". Wird in einem Projekt "soll" als verbindliches Schlüsselwort verwendet, sollte das explizit definiert werden, um Missverständnisse zu vermeiden.

> **Wichtige Prüfungsfalle:** Zusammengesetzte Sätze wie "Das System soll den Nutzer einloggen UND sein Profil laden" sind ein Warnsignal für mangelnde Atomarität. Funktioniert der Login, aber das Profil lädt nicht – ist die Anforderung dann erfüllt oder nicht? Im Zweifel in einzelne Anforderungen aufteilen!

> **IHK-Typfrage:** *"Formen Sie die vage Anforderung 'Die App soll Bilder wirklich schnell laden' in eine testbare Anforderung um."*
> **Musterantwort:** Die ursprüngliche Formulierung enthält mit "wirklich schnell" ein nicht messbares Wort. Eine testbare Version wäre: "Das System muss ein nicht zwischengespeichertes Bild mit einer Dateigröße von bis zu 5 MB bei einer Internetverbindung von mindestens 10 Mbit/s innerhalb von 2 Sekunden laden." Diese Formulierung ist eindeutig (konkrete Zahlen statt "schnell") und testbar (die 2-Sekunden-Grenze lässt sich messen). Für eine vollständig reproduzierbare Testumgebung müssten in der Praxis noch weitere Randbedingungen geklärt werden (z. B. Referenzgerät, Serverlast, Bildformat) – für die Prüfung reicht in der Regel die grundsätzliche Umformulierung von vage zu messbar.

---

## 5. Priorisierung mit dem Kano-Modell

> **Grundprinzip:** Bremsen an einem Auto lösen keine Begeisterung aus – sie werden schlicht erwartet. Kostenloses Gebäck im Hotelzimmer erwartet dagegen niemand, löst aber pure Freude aus. Genau diesen Unterschied macht sich das Kano-Modell zunutze, um Anforderungen nach ihrer Wirkung auf die Kundenzufriedenheit zu ordnen.

### 5.1 Die drei Kano-Kategorien

Entwickelt von Noriaki Kano, kategorisiert das Modell Features nach der emotionalen Reaktion der Kundschaft:

| Kategorie | Bedeutung | Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **Basis-Anforderungen (Must-be)** | Werden als selbstverständlich vorausgesetzt. Fehlen sie → große Unzufriedenheit. Sind sie da → keine Extra-Freude | Bremsen im Auto | 🔴 |
| **Leistungs-Anforderungen (Performance)** | Je mehr, desto besser – direkt proportional zur Zufriedenheit | Akkulaufzeit | 🔴 |
| **Begeisterungs-Anforderungen (Excitement)** | Unerwartete Extras. Fehlen sie → niemand stört sich daran. Sind sie da → große Freude | Kostenlose Pralinen im Hotelzimmer | 🔴 |

> **Wichtig für die Prüfung:** Begeisterungsmerkmale wandern mit der Zeit oft zu Basis-Anforderungen. Kostenloses WLAN im Hotel war vor Jahren eine Begeisterung – heute ist es eine reine Selbstverständlichkeit, deren Fehlen für massive Unzufriedenheit sorgt.

> **Hinweis:** Für die Prüfung stehen meist die drei Hauptkategorien (Basis, Leistung, Begeisterung) im Mittelpunkt. Das vollständige Kano-Modell kennt zusätzlich weitere Ergebniskategorien (u. a. Indifferent-, Reverse- und Questionable-Merkmale) für Fälle, in denen eine Kundenbefragung kein eindeutiges Bild liefert.

> **IHK-Typfrage:** *"Ordnen Sie das Feature 'sichere Passwort-Anmeldung' bei einer Banking-App ins Kano-Modell ein, und begründen Sie."*
> **Musterantwort:** Eine sichere Anmeldung ist für eine Banking-App eine **Basis-Anforderung (Must-be)**. Kund:innen erwarten Sicherheit als absolute Selbstverständlichkeit – niemand wird "begeistert" sein, weil das Login sicher ist. Fehlt die Sicherheit jedoch oder wird sie kompromittiert, entsteht massive Unzufriedenheit (und ggf. Vertrauensverlust in die gesamte Bank). Das unterscheidet sich deutlich von einem echten Begeisterungsmerkmal wie z. B. einer automatischen Kategorisierung der Ausgaben mit persönlichen Sparvorschlägen.

---

## 6. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Lastenheft und Pflichtenheft werden von derselben Partei geschrieben | Das Lastenheft schreibt der Auftraggeber, das Pflichtenheft der Auftragnehmer – unterschiedliche Perspektiven (Problem vs. Lösung) |
| 2 | Man kann direkt mit dem Pflichtenheft beginnen, ohne ein Lastenheft zu haben | Das Pflichtenheft baut auf dem Lastenheft auf – ohne dokumentiertes Problem/Ziel fehlt die Grundlage für die technische Lösung |
| 3 | Constraints und nicht-funktionale Anforderungen sind dasselbe | Ein Constraint begrenzt den Lösungsraum (z. B. vorgegebene Technologie, Budget), ein NFR beschreibt, wie gut eine Funktion erfüllt werden muss (z. B. Antwortzeit) – der Unterschied liegt in der Funktion, nicht in der Herkunft (extern/intern) |
| 4 | Wörter wie "schnell" oder "benutzerfreundlich" sind für IHK-Zwecke ausreichend präzise Anforderungen | Solche Wörter sind nicht testbar – eine gute Anforderung braucht konkrete, messbare Werte |
| 5 | Alles, was der Kunde will, ist eine Begeisterungsanforderung im Kano-Modell | Viele scheinbar wichtige Features sind tatsächlich nur Basis-Anforderungen (selbstverständlich vorausgesetzt) – echte Begeisterungsmerkmale sind seltener, als man denkt |

---

## 7. Deep-Dive-Ausblick (freiwillig)

- **Objektorientierte Analyse (OOA) im Detail:** Wie Anforderungen über Use Cases und User Stories in UML-Diagrammen modelliert werden (Vertiefung siehe LF5.2, System Design Modeling).
- **Konfliktmanagement bei Anforderungen:** Systematische Strategien (z. B. Win-Win-Verhandlung) zur Auflösung widersprüchlicher Stakeholder-Anforderungen.
- **Agile Anforderungsdokumentation:** Wie Product Backlogs, User Stories und Akzeptanzkriterien in agilen Projekten Anforderungen dokumentieren und klassische Lasten-/Pflichtenhefte je nach Projekt ergänzen oder teilweise ersetzen (Vertiefung siehe LF5.6, Agile Methodologies).

---

## 8. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Wer schreibt das Lastenheft, wer das Pflichtenheft? | Lastenheft: Auftraggeber; Pflichtenheft: Auftragnehmer |
| 2 | Was ist der wichtigste Unterschied zwischen Lastenheft und Pflichtenheft? | Lastenheft: Anforderungen/Ziele aus Sicht des Auftraggebers (WAS/WARUM); Pflichtenheft: geplante technische Umsetzung aus Sicht des Auftragnehmers (WIE/WOMIT) |
| 3 | Was ist der Unterschied zwischen einer offenen und einer geschlossenen Interviewfrage? | Offene Fragen liefern Kontext/Prozesse, geschlossene Fragen liefern harte Fakten ohne Kontext |
| 4 | Was unterscheidet einen Constraint von einer nicht-funktionalen Anforderung? | Constraint = begrenzt den Lösungsraum (z. B. Budget, vorgegebene Technologie); NFR = beschreibt, wie gut eine Funktion erfüllt werden muss (z. B. Antwortzeit) |
| 5 | Nenne drei Qualitätsmerkmale nach ISO/IEC 25010:2023. | Z. B. Performance Efficiency, Interaction Capability, Security, Reliability, Maintainability, Compatibility |
| 6 | Schreibt ISO/IEC/IEEE 29148 eine feste deutsche Satzschablone für Anforderungen vor? | Nein – die Norm beschreibt vor allem Qualitätskriterien guter Anforderungen (u. a. eindeutig, testbar, atomar); Formulierungsschablonen wie "Unter [Bedingung] muss das System [Funktion] mit [Kriterium] leisten" sind didaktische Hilfen, keine wörtliche Normvorgabe |
| 7 | Was bedeutet "atomar" bei einer Anforderung? | Möglichst eine prüfbare Verpflichtung pro Anforderung; "und"/"oder" sind Warnsignale für zusammengesetzte Anforderungen, aber nicht automatisch verboten |
| 8 | Nenne die drei Kategorien des Kano-Modells. | Basis-Anforderungen (Must-be), Leistungs-Anforderungen (Performance), Begeisterungs-Anforderungen (Excitement) |
| 9 | Was passiert typischerweise mit Begeisterungsmerkmalen über die Zeit? | Sie wandern oft zu Basis-Anforderungen (werden zur Selbstverständlichkeit) |

---

## 9. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Lastenheft** | Vom Auftraggeber: WAS und WARUM (DIN 69901-5, historisch DIN 69905) |
| **Pflichtenheft** | Vom Auftragnehmer: WIE und WOMIT (DIN 69901-5, historisch DIN 69905) |
| **Stakeholder** | Personen/Gruppen/Organisationen, die vom System betroffen sind oder Einfluss darauf haben (z. B. Auftraggeber, Nutzende, Admins) |
| **Traceability (Rückverfolgbarkeit)** | Eine Anforderung lässt sich von ihrer Quelle über Umsetzung bis zum Test zurückverfolgen |
| **Offene/geschlossene Frage** | Kontext/Prozesse vs. harte Fakten |
| **Funktionale Anforderung (FR)** | Konkrete Handlung, die das System ausführen muss |
| **Nicht-funktionale Anforderung (NFR)** | Qualitätsmerkmal des Systems |
| **Constraint** | Begrenzt den Lösungs-/Entwicklungsraum (z. B. Budget, vorgegebene Technologie) |
| **ISO/IEC 25010:2023** | Qualitätsmodell für NFRs, 9 Merkmale (u. a. Performance Efficiency, Interaction Capability, Security, Reliability, Maintainability) |
| **ISO/IEC/IEEE 29148** | Beschreibt Qualitätskriterien guter Anforderungen (eindeutig, testbar, atomar) – keine feste Satzschablone |
| **muss / sollte / kann** | verbindlich (shall) / Empfehlung (should) / Option (may) |
| **Atomar** | Faustregel: eine Anforderung = eine prüfbare Verpflichtung; "und"/"oder" sind Warnsignale |
| **Kano-Modell** | Basis- / Leistungs- / Begeisterungs-Anforderungen nach Kundenwirkung |

---

## 10. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die Prüfung hören will |
| --- | --- | --- |
| Lastenheft/Pflichtenheft unterscheiden | "Wer erstellt Dokument X, und was steht drin?" | Autor:in UND Inhalt (Problem vs. Lösung) explizit nennen |
| Anforderung extrahieren | "Welche Anforderungen stecken in dieser Aussage?" | Jede eigenständige technische Anforderung einzeln benennen, subjektive Formulierungen von Fakten trennen |
| Anforderung kategorisieren | "Ist X funktional, nicht-funktional oder ein Constraint?" | Konkrete Begründung liefern, nicht nur die Kategorie nennen |
| Anforderung strukturiert formulieren | "Formen Sie Aussage X in eine testbare Anforderung um" | Konkrete Zahlen/Bedingungen statt vager Adjektive, muss/sollte/kann korrekt verwenden |
| Kano-Einordnung | "Wie ordnen Sie Feature X ein?" | Kategorie UND Begründung anhand der Kundenwirkung liefern |

---

## 11. Merksätze für das Fachgespräch

> Lastenheft = die Last, das Problem zu beschreiben; Pflichtenheft = die Pflicht, die Lösung zu liefern.

> Frag nach dem Problem, nicht nach der Lösung – die Lösung ist Aufgabe der IT, nicht des Stakeholders.

> Ein Constraint begrenzt den Lösungsraum, eine nicht-funktionale Anforderung beschreibt, wie gut eine Funktion erfüllt werden muss – der Unterschied liegt in der Funktion, nicht in der Herkunft.

> Gute Anforderungen ersetzen vage Adjektive durch beobachtbare oder messbare Kriterien – eine Zahl hilft oft dabei, ist aber nicht immer zwingend nötig.

> Was heute begeistert, ist morgen selbstverständlich – Kano-Kategorien verschieben sich mit der Zeit.

---

```yaml
dokument: LF5.1-wiki-artikel
themenfeld: "LF5.1 - Requirements & Analysis"
titel: "Requirements & Analysis"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-11
quellen_intern:
  - "LF5.1.1: The Specification Duel.md (User-Story/Bloom-Format)"
  - "LF5.1.2: Extracting Chaos & Interviewing Stakeholders.md"
  - "LF5.1.3: Categorizing & Resolving Conflicts.md"
  - "LF5.1.4: The IEEE Formulator.md"
  - "LF5.1.5: Analog Mindmap & IREB Kano Model.md"
  - "Zusätzliche Rechercheunterlagen vom Auftraggeber (zwei Dokumente, deutschsprachig, mit Quellenverweisen auf Fachliteratur) zu Requirements & Analysis, Writing the Logic, Ensuring Quality, Agile Methodologies"
quellen_fachlich:
  - titel: "DIN 69901-5:2009-01 (aktuelle Referenz) / DIN 69905:1997 (historischer Ursprung) - Lastenheft/Pflichtenheft"
    herausgeber: "diverse Fachquellen (REFA, Lexware, Wikipedia, Provimedia, e-teaching.org u.a.)"
    status: "web-verifiziert (zwei Recherche-Runden); aktuellere Quellen (2022-2026) zitieren überwiegend DIN 69901-5, ältere/allgemeinere Quellen nennen DIN 69905 als Ursprungsnorm"
  - titel: "ISO/IEC 25010:2023 Produktqualitätsmodell (9 Merkmale, Nachfolger der 2011er-Fassung mit 8 Merkmalen)"
    herausgeber: "ISO (committee.iso.org)"
    status: "web-verifiziert in Runde 2; 2011er-Fassung zurückgezogen, aber in Ausbildungsunterlagen teils noch in Gebrauch - Artikel stellt beide Versionen gegenüber"
  - titel: "ISO/IEC/IEEE 29148:2018 Requirements Engineering, Kano-Modell (Noriaki Kano)"
    herausgeber: "Rohmaterial + Fachliteratur"
    status: "stabile, langjährig etablierte Standards/Modelle; IEEE 29148 beschreibt Qualitätskriterien, keine feste Satzschablone (in Runde 2 korrigiert)"
review_historie:
  - runde: 1
    datum: 2026-09-11
    ergebnis: "Erstdraft erstellt. Kombiniert englisches Rohmaterial (User-Story/Bloom-Format, LF5.1.1-5) mit vom Auftraggeber bereitgestellter deutschsprachiger Zusatzrecherche zu LF5-Themen. DIN-69905-Referenz für Lastenheft/Pflichtenheft eigenständig web-verifiziert (mehrere übereinstimmende Fachquellen). IREB-Qualitätskriterien für Anforderungsdokumente (vollständig/eindeutig/widerspruchsfrei/nachvollziehbar/überprüfbar) aus der Zusatzrecherche übernommen. Bewusster Querverweis zu WiSo 4 (Werkvertrag) bei der rechtlichen Einordnung des Pflichtenhefts, um Wissen aus der WiSo-Serie zu verknüpfen statt zu wiederholen. Auf Deutsch verfasst (trotz englischsprachigem Rohmaterial), wie vom Auftraggeber ausdrücklich gewünscht, um Missverständnisse zu vermeiden. Eigene Review nach Style-Guide-Checkliste direkt eingearbeitet: Typische Prüfungsfallen und Deep-Dive-Ausblick von Anfang an vorhanden, Analogien aus mehreren Domänen (Bauherr/Architekt, Restaurant, Auto/Bremsen, Kochrezept)."
  - runde: 2
    datum: 2026-09-11
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet, gewichtet nach Quellenqualität. Von allen drei Reviews unabhängig bestätigt, mit ISO-Quelle belegt: ISO/IEC 25010 war veraltet dargestellt (nur 6 von 8 Merkmalen der 2011er-Fassung) – auf die aktuelle 2023er-Fassung (9 Merkmale) aktualisiert, alte 2011er-Fassung als Kontrast für den Fall genannt, dass der Unterricht noch damit arbeitet. Ebenfalls von allen drei Reviews bestätigt: Die 'goldene IEEE-29148-Syntax' war zu stark als wörtliche Normvorgabe dargestellt – die Norm beschreibt vor allem Qualitätskriterien, keine feste Satzschablone; entsprechend umformuliert (didaktische Formulierungsschablone statt Normsyntax) und Abschnittsüberschrift angepasst. Ebenfalls von allen drei Reviews bestätigt: 'soll (Muss) vs. sollte (Kann)' war fachlich falsch – korrekt ist muss (verbindlich/shall) / sollte (Empfehlung/should) / kann (Option/may); korrigiert. Ebenfalls von allen drei Reviews bestätigt: Merksatz 'Anforderung ohne Zahl ist keine Anforderung' war zu absolut (Gegenbeispiel: rein funktionale, testbare Anforderungen ohne Zahl) – entschärft zu 'ersetzen vage Adjektive durch beobachtbare/messbare Kriterien'. Von zwei Reviews mit Quellenbeleg bestätigt, eigenständig mit zweiter Recherche-Runde verifiziert: DIN-69905-Emphase war veraltet – aktuellere Fachquellen (2022-2026) zitieren überwiegend DIN 69901-5:2009 als Referenznorm, DIN 69905:1997 als historischen Ursprung; Emphase in Haupttext, Selbsttest, Cheatsheet und YAML umgekehrt. Von zwei Reviews bestätigt: Constraint-vs-NFR-Abgrenzung 'von außen auferlegt vs. selbst gesetzt' war fachlich unsauber (beide können von unterschiedlichen Quellen stammen) – korrekt ist die Abgrenzung nach Funktion: Constraint begrenzt den Lösungsraum, NFR beschreibt Qualität der Funktionserfüllung; in Haupttext, Prüfungsfalle 3, Selbsttest 4 und Cheatsheet konsistent korrigiert. Echter Fachfehler gefunden und behoben: 'Passwörter verschlüsselt (gehasht)' vermischte zwei unterschiedliche Konzepte – Hashing ist keine Verschlüsselung (nicht umkehrbar vs. umkehrbar mit Schlüssel), explizit klargestellt. Rechtliche Pflichtenheft-Aussage relativiert (nicht jedes Softwareprojekt automatisch Werkvertrag, Wirkung hängt von konkreter Vertragsgestaltung ab). Kano-Modell um Hinweis auf weitere Kategorien (Indifferent/Reverse/Questionable) ergänzt. Cheatsheet um Stakeholder und Traceability ergänzt. Lastenheft/Pflichtenheft-Zeitpunkt-Tabelle und Agile-Dokumentation-Ausblick weniger starr formuliert (typischer statt zwingender Ablauf bzw. 'ergänzen oder teilweise ersetzen' statt 'ersetzen'). Eine Review schlug vor, 'AP1 (schriftlich) + Fachgespräch' im Kopf zu ändern, da das Fachgespräch üblicherweise zur AP2 gehört – nicht übernommen, da dies exakt der im wiki-fiae-Skill vorgegebenen Standardformulierung entspricht und durchgängig in allen bisherigen LF8-Artikeln so verwendet wurde; Änderung hier hätte Inkonsistenz zur restlichen Artikelserie erzeugt, nicht Konsistenz."
  - runde: 3
    datum: 2026-09-11
    ergebnis: "Eigene Abschlussprüfung (kein externer Review): gesamte Datei durchgelesen, vier echte Konsistenzreste gefunden und behoben – genau das 'Haupttext korrigiert, Nebenstelle vergessen'-Muster, vor dem der Workflow selbst warnt. Merksatz in Abschnitt 11 trug noch die alte, in Runde 2 sonst überall korrigierte Constraint/NFR-Unterscheidung; Cheatsheet-ISO-25010-Eintrag war noch die alte 6-Merkmale-Kurzfassung mit 'Usability' statt 'Interaction Capability'; Selbsttest 5 verwendete ebenfalls noch 'Usability'; Selbsttest 7 trug noch die alte absolute Atomaritätsregel ('niemals und/oder'), die in Abschnitt 4.2 bereits entschärft worden war. Alle vier nachgezogen, zusätzlich Cheatsheet-Atomar-Eintrag als Faustregel gekennzeichnet. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 3 Runden (1 externe Prüfrunde mit 3 Reviews + 1 eigene Abschlussprüfung, 2026-09-11) – Freigabe durch Autor:in bestätigt"
```