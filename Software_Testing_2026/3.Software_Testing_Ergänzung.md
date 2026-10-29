# Software Testing – Ergänzungen für Umschüler

> **Ergänzungsdokument** zu „Software Testing 2026: Qualitätssicherung in Praxis und Ausbildung"  
> Zielgruppe: FIAE & FISI | Fokus: IHK-Prüfungsrelevanz

---

## Inhaltsverzeichnis

1. [Testarten – Black-Box, White-Box, Grey-Box](#1-testarten--black-box-white-box-grey-box)
2. [Das V-Modell – Testphasen im Überblick](#2-das-v-modell--testphasen-im-überblick)
3. [Testdokumentation – IHK-konformer Testbericht](#3-testdokumentation--ihk-konformer-testbericht)
4. [Hinweis: Korrektur im Hauptdokument](#4-hinweis-korrektur-im-hauptdokument)

---

## 1. Testarten – Black-Box, White-Box, Grey-Box

In der IHK-Prüfung wirst du nach dem Unterschied dieser drei Testarten gefragt – und danach, welche Methode für welche Situation geeignet ist.

### Black-Box-Test

Der Tester kennt den **internen Code nicht**. Er sieht nur: Eingabe rein → Ausgabe raus. Getestet wird ausschließlich das Verhalten aus Anwendersicht.

```
Eingabe  ──►  [ ??? Blackbox ??? ]  ──►  Ausgabe
```

**Methoden (prüfungsrelevant):**

| Methode | Wann einsetzen? | Beispiel |
|---|---|---|
| Äquivalenzklassenbildung | Viele ähnliche Eingabewerte | Altersfeld: gültig (18–99), ungültig (<18 oder >99) |
| Grenzwertanalyse | Fehler an Bereichsgrenzen | Teste 17, 18, 99, 100 – nicht 50 |
| Zustandsbasierter Test | Bei Zustandsautomaten / Workflows | Bestellung: offen → bezahlt → versendet |
| Entscheidungstabellentest | Viele Bedingungskombinationen | Versandkosten: Gewicht UND Zielland UND Expressversand? |

> 💡 **Prüfungstipp FIAE:** Äquivalenzklassen und Grenzwerte sind die am häufigsten gestellten Rechenaufgaben in der schriftlichen AP2. Übe, die Klassen schriftlich aufzulisten und mindestens einen Repräsentanten pro Klasse zu benennen.

---

### White-Box-Test

Der Tester hat **vollständigen Einblick in den Quellcode**. Ziel ist es, alle Programmzweige, Schleifen und Bedingungen gezielt durchzutesten.

**Methoden (prüfungsrelevant):**

| Methode | Was wird gemessen? | Formel |
|---|---|---|
| Anweisungsüberdeckung C₀ | Wie viele Zeilen wurden ausgeführt? | ausgeführte Anweisungen / alle Anweisungen × 100 % |
| Zweigüberdeckung C₁ | Wie viele Ja/Nein-Zweige wurden durchlaufen? | ausgeführte Zweige / alle Zweige × 100 % |
| Pfadüberdeckung C₂ | Wie viele vollständige Ausführungspfade? | sehr aufwendig, selten vollständig erreichbar |

> 💡 **Merksatz:** C₁ ist stärker als C₀ – wer 100 % Zweigüberdeckung hat, hat automatisch auch 100 % Anweisungsüberdeckung. Umgekehrt gilt das **nicht**.

---

### Grey-Box-Test

Eine **Mischform**: Der Tester kennt die Datenbankstruktur oder die API-Schnittstelle, aber nicht den eigentlichen Anwendungscode. Typisch bei Integrationstests zwischen Systemen.

**Beispiel:** Ein Tester prüft, ob eine Bestellung korrekt in der Datenbank gespeichert wird – er kennt das Datenbankschema, aber nicht den Java-Code dahinter.

---

### Schnellvergleich für die Prüfung

| Merkmal | Black-Box | White-Box | Grey-Box |
|---|---|---|---|
| Codekenntnisse nötig? | Nein | Ja | Teilweise |
| Perspektive | Anwender | Entwickler | Tester mit Systemwissen |
| Typische Phase | Systemtest, Abnahmetest | Unit-Test, Modultest | Integrationstest |
| IHK-Relevanz FIAE | Hoch | Sehr hoch | Mittel |
| IHK-Relevanz FISI | Mittel | Niedrig | Hoch |

---

## 2. Das V-Modell – Testphasen im Überblick

Das V-Modell ist das **wichtigste Prozessmodell für Qualitätssicherung** in der IHK-Prüfung. Es zeigt, welche Testebene zu welcher Entwicklungsphase gehört.

```
Anforderungsanalyse  ────────────────────►  Abnahmetest
       │                                         │
  Grobentwurf  ──────────────────────►  Systemtest
       │                                    │
  Feinentwurf  ───────────────────►  Integrationstest
       │                               │
  Implementierung  ──────────►  Modultest (Unit-Test)
                        │
                  [Code schreiben]
```

Die **linke Seite** beschreibt Entwicklungsschritte (von oben nach unten).  
Die **rechte Seite** beschreibt Testschritte (von unten nach oben).  
Jede Teststufe **verifiziert** die gegenüberliegende Entwicklungsphase.

---

### Die vier Testebenen im Detail

#### Modultest (Unit-Test)

**Was wird getestet?** Einzelne Funktionen oder Klassen – isoliert vom Rest des Systems.

**Wer testet?** Entwickler (FIAE) selbst, direkt nach dem Schreiben.

**Werkzeuge:** JUnit (Java), NUnit (.NET), pytest (Python)

**Beispiel:**

```java
@Test
public void testVersandkostenUnterGrenze() {
    assertEquals(4.99, berechneVersand(50.00), 0.001);
}

@Test
public void testVersandkostenKostenlos() {
    assertEquals(0.00, berechneVersand(100.00), 0.001);
}
```

---

#### Integrationstest

**Was wird getestet?** Das Zusammenspiel mehrerer Module oder Systeme. Werden Daten korrekt übergeben?

**Typische Fehler:** Falsches Datenformat an der Schnittstelle, fehlende Fehlerbehandlung bei Verbindungsabbrüchen.

**FISI-Relevanz:** Prüfen, ob ein neu eingebundener Server korrekt mit dem Active Directory kommuniziert.

**Strategien:**

| Strategie | Vorgehen |
|---|---|
| Top-Down | Von der Benutzeroberfläche in Richtung Datenbank testen. Noch nicht fertige Untermodule werden durch *Stubs* (Platzhalter) ersetzt. |
| Bottom-Up | Von der Datenbank nach oben testen. Übergeordnete Module werden durch *Test-Treiber* simuliert. |

---

#### Systemtest

**Was wird getestet?** Das gesamte System gegen die ursprünglichen Anforderungen. Funktioniert das Produkt als Ganzes?

**Wer testet?** Ein **unabhängiges Testteam** – nie die Entwickler selbst (Betriebsblindheit!).

**Enthält auch:**

- **Lasttest:** Wie verhält sich das System unter hoher Nutzerzahl?
- **Stresstest:** Was passiert, wenn Ressourcen knapp werden (RAM voll, Festplatte fast voll)?
- **Sicherheitstest (FISI):** Penetrationstests, Port-Scans, Überprüfung auf bekannte CVEs.

---

#### Abnahmetest

**Was wird getestet?** Ob das System die **vertraglichen Anforderungen** des Kunden erfüllt. Dieser Test wird oft **zusammen mit dem Kunden** durchgeführt.

**Ergebnis:** Ein unterzeichnetes **Abnahmeprotokoll** – rechtlich relevant!

**FISI-Praxisbeispiel:** Nach der Installation eines neuen Servers prüft der Kunde anhand einer Checkliste, ob alle vereinbarten Dienste (DHCP, DNS, Dateifreigaben) funktionieren und unterschreibt das Protokoll.

> 💡 **Prüfungstipp:** Das V-Modell wird oft als Lückentextaufgabe abgefragt. Lerne die Paarungen auswendig: Anforderungsanalyse ↔ Abnahmetest, Grobentwurf ↔ Systemtest, Feinentwurf ↔ Integrationstest, Implementierung ↔ Modultest.

---

## 3. Testdokumentation – IHK-konformer Testbericht

> **Achtung:** Fehlende oder lückenhafte Testdokumentation ist einer der häufigsten Gründe für Punktabzüge in der Projektdokumentation (GAP2). Der Prüfungsausschuss erwartet Nachvollziehbarkeit – nicht nur das Ergebnis, sondern den **gesamten Testprozess**.

---

### Was gehört in eine vollständige Testdokumentation?

Eine IHK-konforme Testdokumentation besteht aus zwei Teilen:

**Teil 1 – Testplan** (vor dem Testen schreiben)

| Abschnitt | Inhalt |
|---|---|
| Testziel | Was soll sichergestellt werden? („Korrekte Berechnung der Versandkosten gemäß Anforderung 3.2") |
| Teststrategie | Welche Testart? (Black-Box, White-Box) Welche Methode? (Äquivalenzklassen, Grenzwerte) |
| Testumgebung | Betriebssystem, Java-Version, Testframework, Datenbankversion |
| Testabdeckung | Welche Anforderungen / Funktionen werden abgedeckt? |

**Teil 2 – Testprotokoll** (während/nach dem Testen ausfüllen)

| Abschnitt | Inhalt |
|---|---|
| Testfall-ID | Eindeutige Nummer (z. B. TC-001) |
| Beschreibung | Was wird getestet? |
| Vorbedingung | Welcher Zustand muss vorher herrschen? |
| Eingabe | Konkrete Testwerte |
| Erwartetes Ergebnis | Was soll passieren? |
| Tatsächliches Ergebnis | Was ist passiert? |
| Status | Bestanden / Fehlgeschlagen |
| Bemerkung | Fehlerbeschreibung bei Fehlschlag |

---

### Beispiel: Ausgefülltes Testprotokoll

**Funktion:** `berechneVersand(double bestellwert)` – Versandkosten: 4,99 € unter 100 €, kostenlos ab 100 €.

| TC-ID | Beschreibung | Eingabe | Erwartet | Ergebnis | Status |
|---|---|---|---|---|---|
| TC-001 | Normalfall unter Grenze | 50,00 € | 4,99 € | 4,99 € | ✅ Bestanden |
| TC-002 | Grenzwert knapp unter kostenlos | 99,99 € | 4,99 € | 4,99 € | ✅ Bestanden |
| TC-003 | Grenzwert genau kostenlos | 100,00 € | 0,00 € | 0,00 € | ✅ Bestanden |
| TC-004 | Grenzwert knapp über kostenlos | 100,01 € | 0,00 € | 0,00 € | ✅ Bestanden |
| TC-005 | Ungültige Eingabe (negativ) | -5,00 € | Exception | Exception | ✅ Bestanden |
| TC-006 | Grenzwert genau 0 € | 0,00 € | 4,99 € | 4,99 € | ✅ Bestanden |

---

### Testbericht-Abschluss (Zusammenfassung)

Am Ende der Dokumentation gehört eine kurze Zusammenfassung:

```
Testbericht – Zusammenfassung
==============================
Getestete Funktion:  berechneVersand()
Anzahl Testfälle:    6
Bestanden:           6
Fehlgeschlagen:      0
Anweisungsüberdeckung (C₀): 100 %
Zweigüberdeckung (C₁):      100 %

Bewertung: Alle Testfälle bestanden.
           Die Funktion verhält sich spezifikationskonform.
Freigabe:  [Datum] [Unterschrift]
```

> 💡 **Prüfungstipp FIAE:** Deine Projektdokumentation muss mindestens ein ausgefülltes Testprotokoll mit mindestens einem Negativtest (ungültige Eingabe) enthalten. Ohne Negativtest gilt die Teststrategie als unvollständig.

> 💡 **Prüfungstipp FISI:** Bei Systemintegrationsprojekten ersetzt das **Abnahmeprotokoll** das Testprotokoll. Es muss die geprüften Dienste, Prüfmethode (z. B. `ping`, `nslookup`, `nmap`), erwartetes und tatsächliches Ergebnis sowie eine Kundenunterschrift enthalten.

---

## 4. Hinweis: Korrektur im Hauptdokument

Im Hauptdokument („Software Testing 2026") enthält **Übung 2** eine unvollständige Begründung bei der C₀-Antwort.

**Betroffene Stelle:** Übung 2, Antwort zu Frage 1

**Bisher:**
> „Ein Testfall (z. B. `alter = 20`) reicht für C₀ – alle Zeilen werden ausgeführt."

**Korrektur – vollständige Begründung:**
> „Ein Testfall (z. B. `alter = 20`) reicht für C₀. Alle 4 ausführbaren Anweisungen werden damit durchlaufen: `int erlaubt = 0`, `if (alter >= 18)` (Bedingungsprüfung), `erlaubt = 1` (if-Zweig), `return erlaubt`. C₀ = 4/4 × 100 % = **100 %**."

**Warum wichtig?** In der Prüfung wird nicht nur das Ergebnis, sondern die **Herleitung** bewertet. Wer nur schreibt „ein Testfall reicht", ohne die Anweisungen aufzuzählen, riskiert halbe Punktzahl.

---
