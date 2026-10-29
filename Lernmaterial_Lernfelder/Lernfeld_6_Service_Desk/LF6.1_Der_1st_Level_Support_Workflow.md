# LF6.1 – Der 1st-Level-Support-Workflow

*Vom Anruf bis zur Unterschrift – wie eine Anfrage professionell durch den Support läuft*

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 45–60 Minuten
> **Status:** Final
> **Stand:** 2026

---

## 📌 IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Wie unterscheidest du Störung (Incident) und Serviceanfrage (Service Request)? | [1. Anfrageeingang](#1-anfrageeingang-und-qualifizierung) |
| 2 | Wie berechnest du Priorität und SLA-Fristen? | [1.2 Priorisierung & SLA](#12-priorisierung-und-sla-fristen) |
| 3 | Welche Sicherheitsprüfung machst du vor Inbetriebnahme eines Geräts? | [2. Physische Bereitstellung](#2-physische-bereitstellung-und-durchführung) |
| 4 | Was gehört in ein rechtssicheres Übergabeprotokoll? | [3.2 Übergabeprotokoll](#32-das-übergabeprotokoll) |
| 5 | Was ist eine CMDB und wofür brauchst du sie? | [3.1 CMDB](#31-cmdb-configuration-management-database) |

---

## 1. Anfrageeingang und Qualifizierung

> Eine Anfrage ist erst dann ein gutes Ticket, wenn der 2nd Level sie lösen kann, ohne dich noch einmal fragen zu müssen.

### 1.1 Störung vs. Serviceanfrage

Der wichtigste Unterschied im gesamten Lernfeld – und eine klassische IHK-Fangfrage, weil beide Fälle oft ähnlich klingen.

| Aspekt | Störung (Incident) | Serviceanfrage (Service Request) | IHK-Relevanz |
|---|---|---|---|
| Definition | Unerwartetes Ereignis, das den Betrieb stört | Formelle Anfrage nach etwas Standardisiertem | 🔴 |
| Ziel | Schnellste Wiederherstellung | Standardisierte Bereitstellung | 🔴 |
| Beispiel | Server ausgefallen, Drucker druckt nicht | Passwort-Reset, neuer Laptop, Zugriffsrecht | 🔴 |
| Charakter | Reaktiv, dringend, ungeplant | Proaktiv, geplant, risikoarm | 🟡 |
| Prozess | Erkennen → Melden → Beheben → Dokumentieren | Portal-Einreichung → Genehmigung → Erfüllung | 🟡 |

**Die Prüfungsfalle:** Eine Störung wird oft als Serviceanfrage getarnt formuliert ("Ich brauche einen neuen PC, der alte geht nicht mehr an"). Das ist **keine** Serviceanfrage – es ist primär eine Störung, die erst repariert werden muss, bevor über Ersatz nachgedacht wird.

> **IHK-Typfrage:** *"Ein Mitarbeiter meldet: 'Mein Monitor zeigt nur noch bunte Streifen.' Handelt es sich um einen Incident oder Service Request?"*
> **Musterantwort:** Incident – es ist ein unerwartetes, ungeplantes Ereignis, das den normalen Betrieb stört. Ziel ist die schnellste Wiederherstellung, nicht die Bereitstellung eines Standard-Services.

### 1.2 Priorisierung und SLA-Fristen

Priorität = **Auswirkung (Impact)** × **Dringlichkeit (Urgency)**. Nicht die Hierarchie der Person entscheidet, sondern der Effekt auf den Geschäftsbetrieb.

```
        Dringlichkeit →
Auswirkung    Niedrig   Mittel   Hoch
    ↓
   Hoch        P2        P1       P1
   Mittel      P3        P2       P1
   Niedrig     P4        P3       P2
```

| Priorität | Reaktionszeit | Lösungszeit | Status-Updates | IHK-Relevanz |
|---|---|---|---|---|
| P1 – Kritisch | 15–30 Min. | 2–4 Std. | Alle 30–60 Min. | 🔴 |
| P2 – Hoch | 1–2 Std. | 6–12 Std. | Alle 4 Std. | 🔴 |
| P3 – Mittel | 4–8 Std. | 1–3 Tage | Täglich | 🟡 |
| P4 – Niedrig | 1–2 Tage | 5–10 Tage | Wöchentlich | 🟡 |

**Wichtig für die Fristberechnung:** SLA-Zeiten laufen meist nur innerhalb der **Servicezeit** (z. B. Mo–Fr, 8–18 Uhr). Ein Ticket, das Freitag 14 Uhr eingeht mit 24h-SLA, läuft nicht Samstag ab, sondern erst am nächsten Werktag entsprechend weiter.

> **IHK-Typfrage:** *"Ein Ticket mit 24h-SLA geht Freitag um 14:00 Uhr ein, Servicezeiten sind Mo–Fr 8–18 Uhr. Wann läuft die Frist ab?"*
> **Musterantwort:** 4 Stunden verbleiben am Freitag (bis 18 Uhr), die restlichen 20 Stunden verteilen sich auf die folgenden Werktage – die Frist läuft dann am Dienstag gegen 18 Uhr ab. Bei einem 24/7-SLA-Vertrag wäre sie dagegen schon Samstag 14 Uhr fällig.

### 1.3 Der Ticket-Lebenszyklus

1. **Erstellung** – Anfrage über Kanal (Mail, Telefon, Portal), erhält Ticket-ID
2. **Kategorisierung & Priorisierung (Triage)** – Typ + Dringlichkeit bestimmen
3. **Zuweisung** – an passendes Team (z. B. 1st Level, Hardware, Identity Management)
4. **Bearbeitung** – Untersuchung, Dokumentation, Kommunikation
5. **Warten auf Rückmeldung** – falls Infos vom Kunden fehlen
6. **Lösung** – Fix implementiert, Kunde informiert
7. **Abschluss** – Kunde bestätigt oder Auto-Close nach Frist
8. **Nachbereitung** – Analyse für Problem Management

**In Deutschland gebräuchliche Ticketsysteme:** Zammad, OTOBO, Jira Service Management, Matrix42, USU – meist On-Premises oder in zertifizierten deutschen Rechenzentren wegen DSGVO.

### 1.4 Die 6W-Checkliste

Ein Ticket, das diese 6 Fragen beantwortet, kann der 2nd Level sofort bearbeiten:

| Frage | Beispiel |
|---|---|
| **Wer** ist betroffen? | Einzelner Nutzer oder ganze Abteilung? |
| **Was** funktioniert nicht? | Fehlermeldung wortwörtlich mitschreiben |
| **Wann** ist es passiert? | Uhrzeit, Datum, Häufigkeit |
| **Wo** tritt der Fehler auf? | Rechnername, Standort, Homeoffice |
| **Wie** kam es dazu? | z. B. "nach Update von XY" |
| **Womit** wurde es schon versucht? | Eigene Lösungsversuche des Nutzers |

### 1.5 Fragetechnik: Das Trichtermodell

> Stell deine Fragen wie einen Trichter: erst weit und offen, dann enger und genauer.

1. **Offene Fragen** (Informationen sammeln) – "Was genau ist passiert?" (kein "Warum?" – klingt vorwurfsvoll)
2. **Konkrete Nachfragen** – "Seit wann tritt das auf? Was wurde vorher geändert?"
3. **Geschlossene Fragen** (Absicherung) – "Leuchtet die Lampe grün?" (Ja/Nein, gut für Checklisten)

**Drei goldene Regeln:** Aktives Zuhören (Wichtiges mit eigenen Worten wiederholen), kein Fachchinesisch, Dokumentation ist Pflicht.

---

## 2. Physische Bereitstellung und Durchführung

> Bevor ein Gerät läuft, muss es sicher sein – erst danach wird es ergonomisch eingerichtet.

### 2.1 VDE-Sichtprüfung

| Konzept | Erklärung | IHK-Relevanz |
|---|---|---|
| DIN EN 50678 (ex-VDE 0701) | Prüfung nach Reparatur/Änderung | 🟡 |
| DIN EN 50699 (ex-VDE 0702) | Wiederholungsprüfung | 🟡 |
| Sichtprüfung | Erster & essenzieller Schritt jeder Prüfung | 🔴 |

**Checkliste der Sichtprüfung:** Gehäuse (Risse, Verformung), Netzleitung (Isolationsschäden, Zugentlastung), Netzstecker (verbogene Stifte, Hitzespuren), Schalter/Kontrollleuchten, Sicherheitskennzeichnung, Kühlöffnungen frei.

**Wichtige Grundsätze:**
- "Prüfen mit allen Sinnen" – auch ertasten (fester Sitz) und riechen (Überhitzung)
- Nur durch Elektrofachkraft oder elektrotechnisch unterwiesene Person (EuP)
- Mängel → Gerät gilt als unsicher → muss repariert werden, bevor es in Betrieb geht

> **IHK-Typfrage:** *"Warum reicht bei einem reinen RAM-Wechsel meist die Sichtprüfung, bei Arbeiten am Netzteil aber nicht?"*
> **Musterantwort:** Der RAM-Wechsel berührt nicht die elektrische Sicherheit des Gehäuses/230V-Kreises. Sobald am Netzteil oder der internen Verkabelung gearbeitet wird, sind Messmethoden gesetzlich vorgeschrieben – zur Haftungsbegrenzung im Schadensfall.

### 2.2 Ergonomie am Arbeitsplatz

Seit 2016 nicht mehr die alte BildscharbV, sondern **ASR A6 "Bildschirmarbeit"** (Teil der ArbStättV).

| Regel | Wert | IHK-Relevanz |
|---|---|---|
| Sehabstand | 50–70 cm | 🟡 |
| Monitor-Oberkante | Auf Augenhöhe | 🔴 |
| Blickrichtung | Parallel zum Fenster (nicht direkt hinein/mit Rücken dazu) | 🔴 |
| Kabelmanagement | Strom/Daten getrennt, keine Stolperfallen (DGUV) | 🟡 |

**Merksatz für die Fensterausrichtung:** Steht das Fenster links, blickt man beim Arbeiten nach rechts auf den Monitor – nie mit dem Rücken oder direkt zum Fenster, wegen Blendung/Reflexion.

---

## 3. Dokumentation und Übergabe

> Dein Lösungstext ist deine Visitenkarte für die Wissensdatenbank – "Erledigt" hilft niemandem.

### 3.1 CMDB (Configuration Management Database)

Nicht nur "PC existiert", sondern: **PC gehört Benutzer X** und **ist Teil von Dienstleistung Y**.

| Element | Bedeutung | IHK-Relevanz |
|---|---|---|
| CI (Configuration Item) | Einzelner Baustein: Hardware, Software, Doku, Personen | 🔴 |
| Beziehungen (Dependencies) | Zeigt, welcher Service von welchem Server/welcher Software abhängt | 🔴 |
| Attribute | Standort, Version, Eigentümer, Garantie | 🟡 |

**Unterschied zu ITAM:** ITAM betrachtet den **finanziellen** Lebenszyklus (Kosten, Abschreibung), die CMDB die **operative** Konfiguration und Beziehungen.

**Nutzen:** Schnellere Ursachensuche (Incident/Problem Management), Auswirkungsanalyse vor Changes, revisionssichere Compliance-Dokumentation.

### 3.2 Das Übergabeprotokoll

Ab der Unterschrift greift die **Beweislastumkehr** – der Benutzer haftet ab dann bei grober Fahrlässigkeit (je nach Unternehmensrichtlinie). Zusätzlich bestätigt es die Sicherheitsunterweisung.

**Pflichtinhalte:**
1. Kennzeichnung (Tagging) – Inventar- und Seriennummer aller Geräte
2. Aktualisierung der Bestandsdaten – Benutzer-Zuordnung, Status "Aktiv"
3. Protokollerstellung – Geräte, Zubehör, Zustand
4. Einweisung & Unterschrift – Einschalten, Anmelden, Helpdesk-Nummer
5. Ticket-Abschluss – Zeitaufwand erfassen, Status "Geschlossen"

### 3.3 Der Lösungstext

| Schlecht | Gut |
|---|---|
| "Erledigt" | "Monitor getauscht, S/N 1234 gegen 5678 ersetzt, Funktionstest erfolgreich" |

Ein präziser Lösungstext ist die Grundlage jeder späteren Wissensdatenbank (KCS, siehe LF6.4) und beschleunigt künftige Fälle mit demselben Muster.

---

## ✅ Selbsttest

| Frage | Kurzantwort |
|---|---|
| 1. Was unterscheidet Incident und Service Request grundlegend? | Incident = ungeplant/reaktiv, Ziel Wiederherstellung. Service Request = geplant/standardisiert, Ziel Bereitstellung. |
| 2. Wie berechnet sich die Priorität? | Auswirkung (Impact) × Dringlichkeit (Urgency) |
| 3. Was prüft die VDE-Sichtprüfung primär? | Äußere Mängel: Gehäuse, Kabel, Stecker, Kühlöffnungen – vor jeder messtechnischen Prüfung |
| 4. Wozu dient die Beweislastumkehr im Übergabeprotokoll? | Ab Unterschrift haftet der Benutzer bei grober Fahrlässigkeit; bestätigt Sicherheitsunterweisung |
| 5. Was ist der Kernunterschied zwischen CMDB und ITAM? | CMDB = operative Konfiguration/Beziehungen. ITAM = finanzieller Lebenszyklus (Kosten, Abschreibung) |

---

## 📋 IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Incident | Ungeplante Störung des normalen Betriebs |
| Service Request | Standardisierte, geplante Anfrage eines Nutzers |
| SLA | Vereinbarte Reaktions- und Lösungszeit mit dem Kunden |
| Impact / Urgency | Auswirkung / Dringlichkeit – Basis der Priorisierung |
| P1–P4 | Prioritätsstufen von kritisch bis niedrig |
| CMDB | Datenbank für Configuration Items und ihre Beziehungen |
| CI | Configuration Item – einzelner Baustein der CMDB |
| VDE-Sichtprüfung | Äußere Mängelkontrolle vor Inbetriebnahme eines Geräts |
| ASR A6 | Aktuelle Regel zur Bildschirmarbeitsplatz-Ergonomie |
| Beweislastumkehr | Haftungsübergang an den Nutzer ab Unterschrift im Protokoll |

---

## 🎯 Prüfungstaktik

| Aufgabentyp | Formulierung im Fachgespräch | Was die IHK hören will |
|---|---|---|
| Klassifizierung | "Ist das ein Incident oder ein Service Request?" | Klare Begründung mit den Merkmalen (reaktiv/ungeplant vs. proaktiv/standardisiert) |
| Priorisierung | "Welches Ticket bearbeitest du zuerst?" | Verweis auf Impact × Urgency, nicht auf Hierarchie |
| Sicherheit | "Was prüfst du, bevor der PC läuft?" | VDE-Sichtprüfung nennen, Konsequenz bei Mängeln erklären |
| Dokumentation | "Warum ist die Unterschrift im Protokoll wichtig?" | Beweislastumkehr + Sicherheitsunterweisung nennen |

---

## 💬 Merk-Sätze für die mündliche Prüfung

> "Ein Incident ist immer ungeplant – ein Service Request ist immer geplant. Das ist die Trennlinie."

> "Priorität entscheidet sich an der Auswirkung auf den Betrieb, nicht an der Position des Melders."

> "Die Sichtprüfung kommt vor jeder Messung – ohne sie darf gar nicht weitergeprüft werden."

> "Ein guter Lösungstext beschreibt, was getan wurde – nicht, dass etwas getan wurde."

---

```yaml
lernfeld: LF6.1
titel: Der 1st-Level-Support-Workflow
teil: 1 von 5
quellen:
  - Einleitung für 1st LvL Support
  - LF6.1.1 Anfrageeingang und Qualifizierung
  - LF6.1.2 Physische Bereitstellung und Durchführung
  - LF6.1.3 Dokumentation und Übergabe
status: final
stand: 2026
```
