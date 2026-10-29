# LF6.3a – IT-Lifecycle & Bestandsverwaltung

*Von der Geburt bis zur Entsorgung – wie IT-Ressourcen strukturiert durchs Unternehmen wandern*

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 45–60 Minuten
> **Status:** Final
> **Stand:** 2026

---

## 📌 IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Was sind die Phasen des IT-Lebenszyklus (Hardware & Software)? | [1. Grundlagen des IT-Lebenszyklus](#1-grundlagen-des-it-lebenszyklus) |
| 2 | Technische vs. wirtschaftliche Lebensdauer – was hat Vorrang? | [1.2 Technische vs. wirtschaftliche Lebensdauer](#12-technische-vs-wirtschaftliche-lebensdauer) |
| 3 | Was bedeuten die 6 Buchstaben in IMAC-RD? | [2. Das IMAC-RD-Modell](#2-das-imac-rd-modell) |
| 4 | Wie läuft die datenschutzkonforme Entsorgung (Dispose) ab? | [2.2 Dispose: Datenlöschung](#22-dispose-datenlöschung-und-entsorgung) |
| 5 | Was ist der Unterschied zwischen Asset und CI? | [3.2 Asset vs. Configuration Item](#32-asset-vs-configuration-item) |

---

## 1. Grundlagen des IT-Lebenszyklus

> Ein Unternehmen ohne Lebenszyklus-Management ist wie ein Kapitän ohne Wartungsplan und ohne Seekarte.

### 1.1 Die Phasen im Überblick

| Bereich | Phasen | IHK-Relevanz |
|---|---|---|
| **Allgemein/Hardware** | Planung → Beschaffung → Implementierung → Betrieb → Optimierung → Aussonderung | 🔴 |
| **Software** | Anforderungsanalyse → Entwurf → Umsetzung → Testen → Auslieferung/Betrieb → Wartung | 🟡 |

**Analogie Hausbau (Software):** Analyse = Raumplanung/Budget, Entwurf = Architektenplan, Umsetzung = Maurerarbeit, Testen = Dichtigkeitsprüfung, Wartung = Jahre später neu anstreichen.

**Analogie Firmenauto (Hardware):** Planung = LKW oder Kleinwagen?, Beschaffung = Kauf beim Händler, Betrieb = Tanken/Ölwechsel/Reifen, Entsorgung = Verkauf/Verschrottung – aber vorher das Handschuhfach leeren (= Daten löschen!).

### 1.2 Technische vs. wirtschaftliche Lebensdauer

Das ist der zentrale Denkfehler, den die IHK gerne abfragt:

| Begriff | Bedeutung | Vorrang |
|---|---|---|
| Technische Lebensdauer | Wie lange ein Gerät physisch funktionieren **könnte** (z. B. 5 Jahre) | – |
| Wirtschaftliche Lebensdauer | Wann ein Austausch **sinnvoller** ist als Weiterbetrieb | 🔴 hat Vorrang |

**Warum die wirtschaftliche Lebensdauer meist gewinnt:** Ein Laptop könnte technisch 5 Jahre laufen – aber schon nach 2 Jahren kann ein Umstieg sinnvoller sein, wenn er Arbeitsprozesse spürbar beschleunigt. Zusätzlich: Sicherheitsupdates werden oft nur für aktuelle Hardware entwickelt, und Reparaturen alter Geräte werden irgendwann unwirtschaftlich, sobald die Reparaturkosten den Restwert übersteigen.

> **IHK-Typfrage:** *"Ein 3 Jahre alter Server läuft technisch noch einwandfrei. Wann würdest du ihn trotzdem austauschen?"*
> **Musterantwort:** Wenn die wirtschaftliche Lebensdauer erreicht ist – z. B. wenn der Hersteller keine Sicherheitsupdates mehr liefert, eine nötige Reparatur teurer wäre als eine Neuanschaffung, oder die Leistung für aktuelle Anforderungen nicht mehr ausreicht. Technische Funktionsfähigkeit allein rechtfertigt keinen Weiterbetrieb, wenn Sicherheit oder Wirtschaftlichkeit dagegensprechen.

### 1.3 Die drei Säulen des Lebenszyklus-Managements

| Säule | Inhalt | IHK-Relevanz |
|---|---|---|
| Wirtschaftlichkeit | Planbarkeit, Effizienz, Lizenzmanagement | 🔴 |
| Sicherheit & Compliance | Updates, DSGVO, Support-Ende | 🔴 |
| Qualität & Verfügbarkeit | Standardisierung, Vermeidung von Schatten-IT | 🟡 |

### 1.4 Bezug zur CIA-Triade

| Schutzziel | Bezug zum Lebenszyklus | Analogie |
|---|---|---|
| Verfügbarkeit | Rechtzeitiger Austausch vor Ausfall, Redundanzen (RAID) | Ein Rettungswagen nützt nichts in der Werkstatt |
| Integrität | Schutz vor Manipulation während Betrieb + Umsetzung | Ein versiegelter Brief |
| Vertraulichkeit | Sichere Löschung am Ende des Zyklus (Dispose) | Ein Flüstern – niemand sonst darf mithören |

**Typische vorzeitige Zyklus-Enden:** Kein Hersteller-Support mehr für Sicherheitsupdates, Reparatur teurer als Neuanschaffung, Prozessoptimierung durch neue Hardware, unannehmbare neue Lizenzbedingungen, Schutzziele (CIA) nicht mehr gewährleistbar.

---

## 2. Das IMAC-RD-Modell

> IMAC-RD beschreibt jede Standard-Serviceanfrage, die den physischen oder logischen Zustand eines Assets verändert.

### 2.1 Die 6 Phasen

| Buchstabe | Bedeutung | Beispiel | IHK-Relevanz |
|---|---|---|---|
| **I** – Install | Erstinstallation | Neuer Arbeitsplatz wird eingerichtet | 🔴 |
| **M** – Move | Standortwechsel | Abteilungsumzug | 🔴 |
| **A** – Add | Erweiterung | RAM-Upgrade | 🔴 |
| **C** – Change | Konfigurationsänderung/Austausch | Neue Softwareversion | 🟡 |
| **R** – Remove | Abbau, aber noch keine Entsorgung | Alter PC wird ausgebaut | 🔴 |
| **D** – Dispose | Datenlöschung + Entsorgung | Festplatte wird vernichtet | 🔴 |

**Wichtige Prüfungsfalle:** *Remove* ist **nicht** das Ende des Prozesses! Es beschreibt nur das fachgerechte Abbauen – die Komponente landet danach im Lager oder wird weitergeleitet. Erst *Dispose* ist der tatsächliche Abschluss.

### 2.2 Dispose: Datenlöschung und Entsorgung

Die kritischste Phase aus Datenschutzsicht – und beliebtes IHK-Thema.

| Methode | Wann | IHK-Relevanz |
|---|---|---|
| Soft Delete | **Nicht ausreichend** – Daten sind wiederherstellbar | 🔴 (als Fehler erkennen!) |
| Wiping (z. B. DoD 5220.22-M) | Mehrfaches Überschreiben mit Zufallsmustern | 🔴 |
| Physische Zerstörung | Bei hochsensiblen Daten – Festplatte wird geschreddert/unbrauchbar gemacht | 🟡 |

**Compliance-Pflicht:** Jede Löschung muss protokolliert werden (Löschprotokoll/Vernichtungszertifikat). Erfolgt die Entsorgung über eine externe Firma, ist ein **Auftragsverarbeitungsvertrag (AVV)** nach Art. 28 DSGVO zwingend erforderlich.

> **IHK-Typfrage:** *"Warum reicht das einfache Löschen von Dateien vor der Entsorgung einer Festplatte nicht aus?"*
> **Musterantwort:** Ein normales Löschen (Soft Delete) entfernt nur den Verweis auf die Daten, nicht die Daten selbst – sie sind mit entsprechenden Tools wiederherstellbar. DSGVO-konform ist erst mehrfaches Überschreiben (Wiping, z. B. DoD 5220.22-M) oder bei hochsensiblen Daten die physische Zerstörung, jeweils mit Löschprotokoll als Nachweis.

### 2.3 Beispiel: Add-Request (RAM-Upgrade)

Typischer Ablauf: Bedarfsanalyse (Kompatibilität, freier Steckplatz) → Ticket mit Begründung + Genehmigung → Bestellung → Wareneingangskontrolle → CMDB-Aktualisierung → Einbau → Funktionstest → Abschlussbericht → Ticket schließen. Alter RAM wird bei Zustand "i.O." ins Lager übernommen, sonst fachgerecht entsorgt (→ Dispose).

---

## 3. Bestandsverwaltung (ITAM)

> Ein Asset kostet Geld – ein Configuration Item verursacht im Fehlerfall Support-Aufwand. Diese Trennung ist der Kern von ITAM.

### 3.1 Zweck von ITAM

IT Asset Management fokussiert den **geschäftlichen Wert** und die **kaufmännische Verwaltung** von Hardware und Software.

| Ziel | Bedeutung | IHK-Relevanz |
|---|---|---|
| Kostenkontrolle | Abschreibung, TCO-Übersicht | 🔴 |
| Compliance | Lizenz-Nachverfolgung | 🔴 |
| Risikomanagement | Schatten-IT vermeiden | 🟡 |

### 3.2 Asset vs. Configuration Item

Die zentrale Unterscheidung dieses Kapitels – gehört zusammen mit dem CMDB-Wissen aus LF6.1.

| Aspekt | Asset (kaufmännisch) | CI (technisch) | IHK-Relevanz |
|---|---|---|---|
| Fokus | Geld, Kosten, Abschreibung | Betriebsbereitschaft, Beziehungen | 🔴 |
| Beispiel | "Monitor hat 250 € gekostet" | "Monitor hängt an PC 5, Büro 10, Arbeitsplatz 2" | 🔴 |
| Nutzen | Buchhaltung, Budgetplanung | Support kann sofort lokalisieren, Serienfehler erkennen | 🔴 |

> **IHK-Typfrage:** *"Ein Mitarbeiter meldet einen defekten Monitor. Warum reicht die reine Asset-Information (Kaufpreis, Abschreibung) dem Techniker nicht?"*
> **Musterantwort:** Der Techniker braucht die CI-Information: Wo genau hängt das Gerät (welcher PC, welches Büro, welcher Arbeitsplatz)? Nur so kann er zielgerichtet reagieren. Zusätzlich lässt sich über wiederkehrende CI-Meldungen erkennen, ob es sich um ein Serienproblem handelt – eine reine Kostenperspektive zeigt das nicht.

### 3.3 Asset-Attribute (Beispiel Monitor)

Kaufmännisch: Inventarnummer/Asset-Tag, Seriennummer, Hersteller, Anschaffungsdatum, Garantielaufzeit, Lieferant, Genehmiger.
Technisch (CI): Auflösung, Panel-Typ, Größe, Anschlüsse, Standort/aktueller Nutzer, Status (in Gebrauch/Lager/defekt).

### 3.4 Der Asset-Audit-Prozess

1. **Identifikation** – vorhandene Dokumentation nutzen oder Bestand neu aufnehmen
2. **Klassifizierung** – Zuordnung zu Gruppen (Hardware/Software)
3. **Abhängigkeiten dokumentieren** – z. B. welche Software auf welchem Gerät läuft
4. **Ownership festlegen** – jedes Asset braucht einen klaren Besitzer/Entscheider
5. Grundlage für die anschließende **Schutzbedarfsanalyse**

### 3.5 Lizenzmanagement als Teil von ITAM

Software-Lizenzen sind vertragsbasierte, werthaltige Assets – aber ohne passende Hardware wertlos. Lizenzmanagement verknüpft daher wirtschaftliche (keine ungenutzten Lizenzen bezahlen), technische (Hardware muss Software "ziehen" können) und Compliance-Aspekte (keine Über- oder Unterlizenzierung).

---

## ✅ Selbsttest

| Frage | Kurzantwort |
|---|---|
| 1. Was hat Vorrang: technische oder wirtschaftliche Lebensdauer? | Die wirtschaftliche Lebensdauer – Sicherheit, Kosten und Prozessoptimierung überstimmen reine technische Funktionsfähigkeit |
| 2. Warum ist Remove nicht das Ende von IMAC-RD? | Remove ist nur der Abbau; Entsorgung/Löschung erfolgt erst in der Dispose-Phase |
| 3. Warum reicht Soft Delete vor der Entsorgung nicht aus? | Daten sind mit Tools wiederherstellbar; nötig sind Wiping-Standards oder physische Zerstörung |
| 4. Was unterscheidet Asset und CI grundsätzlich? | Asset = kaufmännische Sicht (Kosten), CI = technische Sicht (Betrieb, Standort, Abhängigkeiten) |
| 5. Warum ist Ownership beim Asset-Audit wichtig? | Jedes Asset braucht einen klaren Verantwortlichen, der über Zugriff und Nutzung entscheidet |

---

## 📋 IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| IT-Lebenszyklus | Gesamte Zeitspanne von Planung bis Aussonderung einer IT-Ressource |
| Technische Lebensdauer | Wie lange ein Gerät physisch funktionieren könnte |
| Wirtschaftliche Lebensdauer | Wann ein Austausch wirtschaftlich sinnvoller ist – hat Vorrang |
| IMAC-RD | Install, Move, Add, Change, Remove, Dispose |
| Wiping | Mehrfaches Überschreiben von Datenträgern zur sicheren Löschung |
| AVV | Auftragsverarbeitungsvertrag nach Art. 28 DSGVO bei externer Entsorgung |
| ITAM | IT Asset Management – kaufmännische Verwaltung von IT-Ressourcen |
| Asset | Kaufmännisches Objekt: Kosten, Abschreibung, Garantie |
| CI | Configuration Item – technischer Baustein mit Betriebsbezug |
| Schatten-IT | Geräte/Software, die am ITAM-Prozess vorbei beschafft wurden |

---

## 🎯 Prüfungstaktik

| Aufgabentyp | Formulierung im Fachgespräch | Was die IHK hören will |
|---|---|---|
| Lebensdauer-Entscheidung | "Warum tauschst du ein noch funktionierendes Gerät aus?" | Wirtschaftliche vor technischer Lebensdauer, konkrete Gründe (Sicherheit, Kosten) |
| IMAC-RD-Zuordnung | "Zu welcher Phase gehört dieser Vorgang?" | Alle 6 Buchstaben sicher auflösen, Remove von Dispose trennen |
| Datenschutz bei Entsorgung | "Wie stellst du sicher, dass keine Daten übrig bleiben?" | Wiping/Zerstörung + Protokollierung + ggf. AVV nennen |
| Asset/CI-Unterscheidung | "Was brauchst du, um den Fehler zu lokalisieren?" | CI-Information (Standort/Beziehung), nicht die Kaufdaten |

---

## 💬 Merk-Sätze für die mündliche Prüfung

> "Technisch könnte ein Gerät noch laufen – wirtschaftlich entscheidet, ob es das auch soll."

> "Remove ist Abbauen, nicht Wegwerfen – erst Dispose beendet den Zyklus wirklich."

> "Ein Asset zeigt, was etwas gekostet hat. Ein CI zeigt, wo es steht und was davon abhängt."

> "Löschen heißt nicht Entfernen – erst Wiping oder Zerstörung macht Daten wirklich unwiederbringlich."

---

```yaml
lernfeld: LF6.3a
titel: IT-Lifecycle & Bestandsverwaltung
teil: 3 von 5
quellen:
  - LF6.3.1 Grundlagen des IT-Lebenszyklus
  - LF6.3.2 Das IMAC-RD-Modell
  - LF6.3.3 Bestandsverwaltung (ITAM)
status: final
stand: 2026
```
