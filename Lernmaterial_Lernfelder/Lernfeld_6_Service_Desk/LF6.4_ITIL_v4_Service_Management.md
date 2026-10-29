# LF6.3b – ITIL v4 Service Management

*Serviceanfragen, Störungen, Metriken und der Katalog – wie ITIL Ordnung in den Support bringt*

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 60–75 Minuten
> **Status:** Final
> **Stand:** 2026

---

## 📌 IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Was ist eine "Standard-Änderung" und warum ist sie risikoarm? | [1.2 Standard-Änderungen](#12-standard-änderungen-standard-changes) |
| 2 | Was unterscheidet funktionale von hierarchischer Eskalation? | [2.2 Eskalation](#22-eskalation-funktional-vs-hierarchisch) |
| 3 | Wie hängen Incident und Problem Management zusammen? | [2.3 Incident vs. Problem Management](#23-incident-vs-problem-management) |
| 4 | Was ist der Unterschied zwischen SLR, SLA, SLI und OLA? | [3.1 SLR, SLA, SLI, OLA](#31-die-vier-begriffe-im-überblick) |
| 5 | Warum gibt es Business-Sicht und technische Sicht im Servicekatalog getrennt? | [4.2 Zwei Sichten](#42-warum-zwei-getrennte-sichten) |

---

## 1. Serviceanfragen nach ITIL v4

> Eine Serviceanfrage ist Routine – aber Routine ohne Prozess wird schnell zu Chaos.

### 1.1 Der Standard-Workflow

Serviceanfrage → Ticket-Erstellung → SLA-Zuordnung → Weiterleitung an zuständige Stelle → Bearbeitung → Abschluss.

**Wichtiger Sicherheitshinweis bei Self-Service (z. B. Passwort-Reset):** Bei einer Passwort-Vergessen-Funktion sollte die Antwort **immer gleich aussehen** ("Link wurde versendet"), egal ob das Konto existiert oder nicht. Das schützt gegen **User Enumeration** – sonst könnte ein Angreifer durch unterschiedliche Antworten herausfinden, welche E-Mail-Adressen im System existieren.

### 1.2 Standard-Änderungen (Standard Changes)

| Merkmal | Beschreibung | IHK-Relevanz |
|---|---|---|
| Definition | Automatisierte Routineaufgabe ohne Einfluss auf normale Geschäftsprozesse | 🔴 |
| Grundlage | SOP (Standard Operating Procedure) – einmalig genehmigt | 🔴 |
| Beispiele | Passwort-Reset, Installation von Standard-Software | 🟡 |
| Risiko | Gering, da dokumentiert und getestet | 🟡 |

**Wichtig:** Führt eine Standard-Änderung wiederholt zu Störungen, muss das **Change Management** sie neu bewerten – möglicherweise wird eine höhere Genehmigungsstufe nötig.

> **IHK-Typfrage:** *"Warum darf ein Passwort-Reset automatisiert ohne Einzelgenehmigung ablaufen, eine neue Server-Firewall-Regel aber nicht?"*
> **Musterantwort:** Ein Passwort-Reset ist eine dokumentierte, getestete Standard-Änderung mit geringem Risiko und einmaliger Vorab-Genehmigung (SOP). Eine Firewall-Regel kann die Sicherheit oder Verfügbarkeit kritischer Systeme beeinflussen und braucht daher eine individuelle Prüfung im normalen Change-Prozess.

### 1.3 Genehmigungsverfahren am Beispiel Hardware-Bestellung

1. Mitarbeiter stellt Anforderung
2. System prüft: im Katalog vorhanden? Budget ausreichend?
3. Kostenstellenverantwortlicher prüft geschäftlichen Nutzen, IT prüft technische Kompatibilität
4. Bei hohem Wert: zusätzliche Freigabe durch den Einkauf
5. Bestellung beim Händler (bei positiver Entscheidung)
6. Vollständige Protokollierung (Revisionssicherheit)

### 1.4 Das Serviceanfrage-Portal

Ein Self-Service-Portal steigert die Effizienz durch: Standardisierung über einen Hardware-/Software-Katalog, automatische Weiterleitung an die richtige Stelle, Status-Transparenz für den Anfragenden, CMDB-Aktualisierung ohne manuellen Zusatzaufwand.

---

## 2. Störungsmanagement nach ITIL v4

> Incident Management löscht das Feuer. Problem Management sucht und beseitigt die Feuerquelle.

### 2.1 Priorisierung wiederholt: Impact × Urgency

(Details siehe LF6.1 – hier zusätzlich der Blick auf Eskalation und die Incident/Problem-Trennung.)

### 2.2 Eskalation: funktional vs. hierarchisch

| Eskalationsart | Richtung | Grund | IHK-Relevanz |
|---|---|---|---|
| **Funktional** (horizontal) | 1st-Level → 2nd-Level-Spezialist | Fachwissen des aktuellen Bearbeiters reicht nicht | 🔴 |
| **Hierarchisch** (vertikal) | 1st-Level → Vorgesetzter | Entscheidungsbefugnis fehlt (z. B. Kunde will Preisnachlass) | 🔴 |

**Häufiger Fehler in der Praxis:** Zu spätes oder zu zögerliches Eskalieren – führt zu unnötigen Verzögerungen und verletzten SLA-Fristen.

> **IHK-Typfrage:** *"Ein Kunde fordert eine Sonderregelung außerhalb des Vertrags. Welche Eskalation ist nötig?"*
> **Musterantwort:** Hierarchische (vertikale) Eskalation – hier fehlt nicht das Fachwissen, sondern die Entscheidungsbefugnis. Der Fall geht an einen Vorgesetzten mit der nötigen Freigabestufe.

### 2.3 Incident vs. Problem Management

| Aspekt | Incident Management | Problem Management | IHK-Relevanz |
|---|---|---|---|
| Ziel | Schnellstmögliche Wiederherstellung | Nachhaltige Ursachenbeseitigung | 🔴 |
| Mittel | Workaround / Quick-Fix | Root-Cause-Analyse, dauerhafte Lösung | 🔴 |
| Zeithorizont | Kurzfristig | Mittel- bis langfristig | 🟡 |

**Beispiel:** Login schlägt fehl, wenn das Passwort ein `&` enthält (Regressionsfehler nach Update).
- **Incident Management:** Workaround anbieten – Passwort ohne `&` neu vergeben, Info-Banner auf der Login-Seite, funktionale Eskalation ans Backend-Team.
- **Problem Management:** Ursache im Code beheben (korrekte Maskierung des Zeichens), damit der Fehler gar nicht mehr auftritt.

> Merksatz: **Incident bekämpft das Symptom, Problem bekämpft die Ursache.**

### 2.4 Pflichtangaben einer Störungsmeldung

Nach dem Muster **Wer – Was – Wann – Wie – Wie**:

| Kategorie | Beispielfragen |
|---|---|
| Wer | Wer meldet, wie erreichbar, welche Abteilung? |
| Was | Konkreter Fehler, betroffene Hardware/Software, Logs/Screenshots vorhanden? |
| Wann | Zeitpunkt, sporadisch oder dauerhaft? |
| Wie (Entstehung) | Was wurde vorher getan, genaue Rekonstruktion? |
| Wie (Auswirkung) | Wie viele betroffen, wie stark die Auswirkung auf Arbeitsprozesse? |

---

## 3. Metriken und Vereinbarungen (SLR, SLA, SLI, OLA)

> SLR ist der Wunsch, SLA das Versprechen, SLI die Messung, OLA die interne Abstimmung, die das Versprechen überhaupt einhaltbar macht.

### 3.1 Die vier Begriffe im Überblick

| Begriff | Bedeutung | Beispiel | IHK-Relevanz |
|---|---|---|---|
| **SLR** (Requirement) | Was der Kunde braucht (Wunschliste) | "Buchhaltung braucht 99 % Verfügbarkeit" | 🔴 |
| **SLA** (Agreement) | Was vertraglich zugesichert wird | Vertrag mit Reaktions-/Lösungszeiten | 🔴 |
| **SLI** (Indicator) | Was tatsächlich gemessen wird | Uptime in %, Latenz in ms | 🔴 |
| **OLA** (Operational) | Interne Vereinbarung zwischen IT-Teams | Backup-Team liefert in 2h zu | 🔴 |

**Merksätze:**
> SLA ist das Gesicht zum Kunden. OLA ist der Handschlag zwischen Kollegen. UC ist die Unterschrift beim externen Lieferanten.

| Vergleich | SLA | OLA | UC (Underpinning Contract) |
|---|---|---|---|
| Vertragspartner | Provider ↔ Kunde | Interne Abteilungen | Provider ↔ externer Dienstleister |
| Rechtsstatus | Rechtlich bindend (bei externen Kunden) | Betriebsintern | Rechtlich bindender Vertrag |

### 3.2 SLI-Beispiele für "Internet-Zugang"

1. **Verfügbarkeit in %** – (erfolgreiche Anfragen / Gesamtanfragen) × 100
2. **Latenz in ms** – Round-Trip-Time (z. B. Ping)
3. **Datenübertragungsrate in Mbit/s** – gemessen per Testtransfer

### 3.3 Verfügbarkeitsberechnung – die IHK-Rechenaufgabe

**Beispiel: 99,5 % Verfügbarkeit, Servicezeit Mo–Fr 8–18 Uhr**

```
Servicezeit/Woche = 10h × 5 Tage = 50h
Servicezeit/Monat = 50h × 4 Wochen = 200h = 12.000 Min.
Erlaubter Ausfall = 12.000 Min. × 0,5 % = 60 Min./Monat
```

**Gleiche Verfügbarkeit bei 24/7-Betrieb:**

```
Monat = 30 Tage × 24h = 720h
Erlaubter Ausfall = 720h × 0,5 % = 3,6h = 216 Min./Monat
```

> **Merke:** Dieselbe Prozentzahl bedeutet bei 24/7-Diensten eine deutlich größere erlaubte Ausfallzeit in Minuten als bei einem Dienst mit reduzierter Servicezeit – weil die Bezugsgröße (Gesamtzeit) größer ist.

> **IHK-Typfrage:** *"Ein Server hat 99,9 % SLA bei 24/7-Betrieb. Wie viele Minuten Ausfall sind im Monat erlaubt?"*
> **Musterantwort:** Rechenweg: Monat = 720h = 43.200 Min. → 43.200 × 0,1 % = 43,2 Min./Monat erlaubte Ausfallzeit.

### 3.4 Warum ein OLA notwendig ist

Ein SLA verspricht z. B. "Wiederherstellung in 4h" – das kann der Provider aber nur einhalten, wenn **mehrere interne Teams** zeitlich abgestimmt zusammenarbeiten:

| Team | Zeitbudget | Verbleibend |
|---|---|---|
| 1st-Level (Qualifizierung) | 30 Min. | 3h 30 Min. |
| Fachabteilung (Behebung) | 2h | 1h 30 Min. |
| Qualitätssicherung (Test) | 30 Min. | 1h Puffer |

Ohne OLA-Abstimmung zwischen diesen Teams wäre das SLA gegenüber dem Kunden nicht realistisch einhaltbar. Wiederholte Überschreitungen führen zur Nachbesserung im Rahmen von **CSI (Continuous Service Improvement)**.

---

## 4. Der Dienstleistungskatalog

> Ein Servicekatalog, der Business-Sprache und Technik-Jargon mischt, funktioniert für niemanden richtig.

### 4.1 Zweck und Aufbau

Ein moderner, webbasierter Servicekatalog hat Frontend (Bestelloberfläche, nach RBAC je Abteilung sortiert) und Backend (meist CMDB-gekoppelt: Freigabe, Genehmigung, Bestellung, Status-Tracking).

### 4.2 Warum zwei getrennte Sichten?

| Grund | Erklärung | IHK-Relevanz |
|---|---|---|
| Zielgruppen-Konflikt | Business-User will schnellen "Bestellen"-Button, IT-Spezialist braucht präzise technische Anweisungen | 🔴 |
| Unterschiedliche Lebenszyklen | Business-Sicht stabil (bleibt "E-Mail-Service"), technische Sicht hochdynamisch (heute Exchange, morgen Cloud) | 🔴 |
| Vertraulichkeit | Technische Details (Versionsnummern, Lizenzkosten) sind sicherheitsrelevant und gehören nicht ins öffentliche Portal | 🟡 |

**Die Lösung: Verknüpfung statt Mischung** – moderne ITSM-Systeme verknüpfen Business-Ansicht (oben) mit technischer Service Map (unten) per 1:N-Beziehung, statt beides in einem Text zu vermengen.

| Ebene | Beispielinhalt |
|---|---|
| Oben (User) | "Ich brauche Zugriff auf das ERP-System." |
| Mitte (Logik) | System prüft Berechtigung/Kostenstelle automatisch |
| Unten (Technik) | Workflow schreibt Nutzer in AD-Gruppe `GRP_ERP_FIN_WRITE` |

> **IHK-Typfrage:** *"Warum steht im Kunden-Servicekatalog nicht 'VPN-Tunnel via Cisco AnyConnect, Port 443', sondern 'Wir ermöglichen mobiles Arbeiten'?"*
> **Musterantwort:** Der Business-User braucht keine technischen Details, um eine Entscheidung zu treffen – zu viele Fachbegriffe erzeugen "Information Overload" und schrecken ab. Die technische Formulierung ist für den IT-Mitarbeiter in der verknüpften technischen Sicht hinterlegt, nicht im kundennahen Portal.

### 4.3 Top-down vs. Bottom-up bei der Katalog-Erstellung

| Methode | Ausgangspunkt | Vorteil |
|---|---|---|
| Top-down | Kundensicht (welche Services braucht der Kunde?) | Stellt sicher, dass alle kundenrelevanten Services erfasst sind |
| Bottom-up | Vorhandene Infrastruktur | Deckt auf, welche Infrastruktur eventuell nicht mehr benötigt wird |

### 4.4 Vier typische Katalog-Kategorien

| Kategorie | Zielgruppe | Fokus |
|---|---|---|
| Business-Service-Katalog | Mitarbeiter/Anwender | Nutzen, Verfügbarkeit, Kosten |
| Technischer Service-Katalog | IT-Mitarbeiter/Admins | Konfiguration, Wartung, Support |
| Compliance/Security-Katalog | Sicherheitsbeauftragte, Recht | DSGVO, Zugriffsberechtigung, SLA |
| Strategischer Service-Katalog | IT-Leitung, Controlling | Investitionsplanung, Portfolio |

### 4.5 Prozess zur Aufnahme eines neuen Dienstes

Bedarf/Nachfrage prüfen → Dienst klassifizieren → Servicebeschreibung Kundensicht → Servicebeschreibung IT-Sicht → Nutzungsbedingungen → ggf. gestuftes SLA-Paket (Bronze/Silber/Gold) → Test-/Pilotbetrieb → offizielle Freigabe → Aufnahme in den Katalog.

---

## ✅ Selbsttest

| Frage | Kurzantwort |
|---|---|
| 1. Warum ist eine gleichlautende Antwort bei "Passwort vergessen" wichtig, egal ob das Konto existiert? | Schutz gegen User Enumeration – verhindert, dass Angreifer existierende Konten identifizieren |
| 2. Funktionale oder hierarchische Eskalation bei fehlendem Fachwissen? | Funktional (horizontal) – zum 2nd-Level-Spezialisten |
| 3. Was ist der Kernunterschied zwischen Incident und Problem Management? | Incident = schnelle Symptombehandlung (Workaround), Problem = nachhaltige Ursachenbeseitigung |
| 4. Was regelt ein OLA im Gegensatz zu einem SLA? | OLA regelt interne Zusammenarbeit zwischen IT-Teams, SLA das externe Versprechen an den Kunden |
| 5. Warum werden Business- und technische Sicht im Servicekatalog getrennt? | Unterschiedliche Zielgruppen, unterschiedliche Änderungsgeschwindigkeit, Vertraulichkeit technischer Details |

---

## 📋 IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Standard Change | Vorab genehmigte, risikoarme Routineänderung (SOP-basiert) |
| Funktionale Eskalation | Weiterleitung an fachlich kompetenteren Mitarbeiter |
| Hierarchische Eskalation | Weiterleitung an Vorgesetzten mit Entscheidungsbefugnis |
| Workaround | Kurzfristige Symptombehandlung ohne Ursachenbeseitigung |
| SLR | Service Level Requirement – Kundenanforderung |
| SLA | Service Level Agreement – vertragliches Versprechen |
| SLI | Service Level Indicator – tatsächlich gemessener Wert |
| OLA | Operational Level Agreement – interne Team-Vereinbarung |
| UC | Underpinning Contract – Vertrag mit externem Dienstleister |
| CSI | Continuous Service Improvement – Nachbesserung bei wiederholten SLA-Verstößen |

---

## 🎯 Prüfungstaktik

| Aufgabentyp | Formulierung im Fachgespräch | Was die IHK hören will |
|---|---|---|
| Eskalationsentscheidung | "Wohin eskalierst du diesen Fall?" | Klare Trennung funktional (Wissen fehlt) vs. hierarchisch (Befugnis fehlt) |
| Incident/Problem | "Ist das ein Incident oder ein Problem?" | Symptombehandlung vs. Ursachenbeseitigung, beide nennen |
| SLA-Rechnung | "Wie viel Ausfallzeit ist bei X % erlaubt?" | Rechenweg zeigen: Servicezeit × (1 - Verfügbarkeit) |
| Katalog-Design | "Warum siehst du als Kunde keine Servernamen im Katalog?" | Zielgruppentrennung, Vertraulichkeit, Verknüpfung statt Mischung |

---

## 💬 Merk-Sätze für die mündliche Prüfung

> "Ein Workaround löscht das Feuer. Erst das Problem Management beseitigt die Feuerquelle."

> "Funktional eskaliert man wegen fehlendem Wissen, hierarchisch wegen fehlender Befugnis."

> "SLA ist das Versprechen nach außen, OLA ist die Abstimmung, die dieses Versprechen überhaupt möglich macht."

> "Der Kunde will einen Bestellen-Button sehen, der Techniker eine Portnummer – deshalb trennt man beide Sichten."

---

```yaml
lernfeld: LF6.3b
titel: ITIL v4 Service Management
teil: 4 von 5
quellen:
  - LF6.3.4 Serviceanfragen nach ITIL v4
  - LF6.3.5 Störungsmanagement nach ITIL v4
  - LF6.3.6 Metriken und Vereinbarungen (SLA, SLR, SLI, OLA)
  - LF6.3.7 Der Dienstleistungskatalog
status: final
stand: 2026
```
