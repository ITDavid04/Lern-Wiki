# LF4.2 (Teil A) – BSI-Grundschutz-Methodik: Strukturanalyse & Schutzbedarf

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1 (schriftlich), Transferfragen in AP2 und Fachgespräch möglich
> **Lernzeit:** Ca. 70–90 Minuten reines Lesen, +50–70 Minuten mit Aufgaben (Berechnungsaufgaben einplanen) – abhängig von Vorkenntnissen und Bearbeitungstiefe
> **Status:** Final
> **Stand:** 2026
> **Teil:** 1 von 2 – Strukturanalyse, Physische Sicherheit, Schutzbedarf (Teil B: Sichere Datenträger, TOM/Web-Sicherheit, Patch-Management, Incident Response)
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was ist ein Informationsverbund nach BSI-Standard 200-2, und welche Bereiche umfasst die Strukturanalyse? | [→ 1. Strukturanalyse](#1-strukturanalyse-was-müssen-wir-schützen) |
| 2 | Wie berechnet man den Energiebedarf von IT-Hardware und dimensioniert eine USV? | [→ 2. Physische Sicherheit & Energie](#2-physische-sicherheit-energiebedarf-und-green-it) |
| 3 | Was ist das Maximumprinzip, und wann weicht man mit Kumulations- oder Verteilungseffekt davon ab? | [→ 3. Schutzbedarfsfeststellung](#3-schutzbedarfsfeststellung-und-das-maximumprinzip) |

---

## 1. Strukturanalyse: Was müssen wir schützen?

> **Grundprinzip:** Ein Architekt zeichnet nicht einfach drauflos, sondern erfasst zuerst akribisch, was auf dem Grundstück bereits vorhanden ist und wie alles zusammenhängt – erst danach lässt sich sinnvoll planen. Die Strukturanalyse ist genau dieser Bestandsplan für die IT-Sicherheit.

### 1.1 Informationsverbund und die Bereiche der Strukturanalyse

Der **Informationsverbund** (BSI-Standard 200-2) beschreibt den Geltungsbereich (Scope) eines Sicherheitskonzepts – die Gesamtheit aller organisatorischen, personellen, physischen und technischen Komponenten, die einer bestimmten Aufgabe dienen.

Die Strukturanalyse nach BSI-Standard 200-2 erfasst dabei folgende Bereiche (didaktisch zu fünf Lernbereichen zusammengefasst – im BSI-Kompendium werden z. B. Kommunikationsverbindungen sowie Räume/Gebäude teils gesondert betrachtet):

| Bereich der Strukturanalyse | Beispiele | IHK-Relevanz |
| --- | --- | --- |
| **Geschäftsprozesse/Fachaufgaben und Informationen** | Auftragsabwicklung, Personalverwaltung, Kundendaten, Konstruktionspläne | 🔴 |
| **Anwendungen** | ERP-Systeme, CAD-Software, Webserver, Datenbanken | 🔴 |
| **Netze und Kommunikationsverbindungen** | LAN, WLAN, VPN, WAN-Strecken, Internetanbindungen, Standortkopplungen | 🟡 |
| **IT-, ICS- und IoT-Systeme** | Client-PCs, Virtualisierungs-Server, NAS, industrielle Steuerungen | 🔴 |
| **Räume und Gebäude** | Serverraum, Großraumbüro, Heimarbeitsplatz, Werkshalle | 🟡 |

> **Wichtig für die Prüfung:** Personen, Rollen und Verantwortlichkeiten (z. B. Benutzer, Administratoren) sind wichtige Angaben *innerhalb* der Strukturanalyse – sie werden z. B. bei der Erfassung von IT-Systemen konkret mit erhoben. Sie bilden aber **keinen eigenen, gleichrangigen Zielobjektbereich** neben Geschäftsprozessen, Anwendungen, IT-Systemen, Netzen und Räumen/Gebäuden. Ebenso gehören **Geschäftsprozesse/Fachaufgaben** explizit zur Strukturanalyse – ein häufig übersehener, aber prüfungsrelevanter Bereich.

### 1.2 Abhängigkeiten zwischen Zielobjekten

Eine Anwendung funktioniert nur, wenn alle darunterliegenden Schichten verfügbar sind:

```text
[ Geschäftsprozess/Information ] --> [ Anwendung ] --> [ IT-System ] --> [ Netz ] --> [ Raum/Gebäude ]
```

Fällt die unterste Schicht aus (z. B. der Serverraum durch Stromausfall), sind automatisch alle darüberliegenden Schichten betroffen.

> **IHK-Typfrage:** *"Warum genügt es nicht, nur die Server eines Unternehmens in die Strukturanalyse aufzunehmen?"*
> **Musterantwort:** Ein Server allein ist ohne die darüberliegenden Anwendungen und Geschäftsprozesse/Informationen sowie die darunterliegende Netz- und Raum-Infrastruktur nicht sinnvoll zu schützen – ein Sicherheitskonzept, das z. B. Räume, das Netz oder die eigentlichen Fachaufgaben ausklammert, hat blinde Flecken. Vollständigkeit über alle Bereiche der Strukturanalyse ist deshalb Grundvoraussetzung.

---

## 2. Physische Sicherheit, Energiebedarf und Green IT

> **Grundprinzip:** Ein Haushalt mit hohem Stromverbrauch braucht nicht nur eine ausreichend dimensionierte Sicherung, sondern auch einen Plan für den Fall, dass der Strom ausfällt – IT-Infrastruktur tickt hier genauso wie die heimische Elektrik, nur mit höheren Einsätzen.

### 2.1 Physische Risiken

| Risiko | Typische Gegenmaßnahme | IHK-Relevanz |
| --- | --- | --- |
| Brand | Rauchansaugsysteme, Gaslöschanlagen (z. B. Argon, Stickstoff) – geeignet nur für dafür ausgelegte, abgedichtete Räume mit eigenem Evakuierungskonzept | 🔴 |
| Wasser/Elementarschäden | Standortwahl, Abdichtung, Hochwasserschutz | 🟡 |
| Diebstahl/Einbruch | Zutrittskontrollen, Videoüberwachung (rechtlich zulässig, verhältnismäßig und organisatorisch geregelt), mechanische Schließsysteme | 🔴 |
| Stromausfall | USV, redundante Energiepfade, Notstromaggregate | 🔴 |

### 2.2 Elektrische Leistung und Energiebedarf

$$P = U \cdot I \quad \text{(Leistung = Spannung} \times \text{Stromstärke, in Watt)}$$

$$E = P \cdot t \quad \text{(Arbeit = Leistung} \times \text{Zeit, in Wattstunden/kWh)}$$

> **IHK-Typfrage/Rechenbeispiel:** *"Ein Serverraum enthält 5 Rack-Server (je 450 W), 2 NAS-Systeme (je 120 W) und 3 Netzwerk-Switches (je 45 W). Berechnen Sie die Gesamtleistung und die tägliche elektrische Arbeit."*
> **Musterantwort:** Gesamtleistung: (5 × 450 W) + (2 × 120 W) + (3 × 45 W) = 2.250 + 240 + 135 = **2.625 W ≈ 2,625 kW**. Tägliche elektrische Arbeit: 2,625 kW × 24 h = **63 kWh/Tag** (unter der Annahme, dass alle Geräte durchgehend mit ihrer angegebenen Nennleistung laufen – die tatsächliche Leistungsaufnahme schwankt in der Praxis je nach Auslastung).

### 2.3 USV-Dimensionierung

Eine unterbrechungsfreie Stromversorgung (USV) muss ausreichend Kapazität besitzen, um Systeme kontrolliert herunterzufahren oder einen definierten Überbrückungszeitraum zu überstehen.

> **Rechenbeispiel:** Für die 2,625 kW aus obigem Beispiel soll eine USV einen Netzausfall von 30 Minuten überbrücken.
> Benötigte Energie: 2.625 W × 0,5 h = **1.312,5 Wh**.
> Bei einer Batteriebank mit 48 V Systemspannung: 1.312,5 Wh ÷ 48 V = **≈ 27,3 Ah** rechnerischer Idealwert.
>
> **Wichtig:** Das ist nur die theoretische Mindestkapazität ohne Verluste, berechnet über die **Wirkleistung** (Watt). Eine reale USV-Auslegung muss zusätzlich den Wirkungsgrad von USV und Wechselrichter, die zulässige Entladetiefe, Batteriealterung und Leistungsfaktor berücksichtigen – und zur Auswahl der USV zusätzlich deren **Scheinleistung (in VA/kVA)**, nach der USV-Anlagen typischerweise dimensioniert werden. Eine USV muss also sowohl hinsichtlich Leistung als auch Batteriekapazität ausreichend bemessen sein; in der Praxis wird deshalb immer ein deutlicher Sicherheitsaufschlag eingeplant.

### 2.4 Kühlung und Green IT

**Kalt-/Warmgang-Einhausung:** Server werden so angeordnet, dass kühle Zuluft und warme Abluft strikt getrennt geführt werden – das reduziert den Kühlaufwand erheblich gegenüber einer unstrukturierten Raumklimatisierung.

**PUE (Power Usage Effectiveness):** Kennzahl für die Energieeffizienz eines Rechenzentrums.

$$\text{PUE} = \frac{\text{Gesamter Energieverbrauch}}{\text{Energieverbrauch der IT-Hardware}}$$

> Je näher der PUE-Wert an 1,0 liegt, desto geringer ist rechnerisch der relative Energieanteil für die **gesamte Nicht-IT-Infrastruktur** (Kühlung, USV-Verluste, Beleuchtung, Energieverteilung u. a.), nicht nur für Kühlung allein. PUE-Werte sollten aber nur bei vergleichbarer Messmethode und ähnlichen Betriebsbedingungen (Größe, Auslastung, Klimazone, Redundanzgrad) direkt miteinander verglichen werden – ein einzelner Zahlenvergleich ohne diesen Kontext kann in die Irre führen.

**Recycling:** Vor der Entsorgung müssen Datenträger unwiderruflich gelöscht werden (siehe Teil B, Abschnitt "Sichere Datenträger"); Altgeräte gehören in einen zertifizierten Recyclingprozess zur Rückgewinnung von Edelmetallen und fachgerechten Entsorgung von Schadstoffen (WEEE-Richtlinie/ElektroG).

---

## 3. Schutzbedarfsfeststellung und das Maximumprinzip

> **Grundprinzip:** Wie bei einem Familienerbe vererbt sich der "höchste Wert" nach unten: Trägt eine Anwendung besonders sensible Daten, "erbt" das System, auf dem sie läuft, automatisch diesen hohen Schutzbedarf – unabhängig davon, was sonst noch auf dem System läuft.

### 3.1 Die drei Schutzbedarfskategorien

| Kategorie | Beschreibung | IHK-Relevanz |
| --- | --- | --- |
| **Normal** | Schadensauswirkungen überschaubar, nicht existenzbedrohend | 🔴 |
| **Hoch** | Schadensauswirkungen können beträchtlich sein (erhebliche finanzielle Verluste, Verletzung gesetzlicher Anforderungen wie der DSGVO, weitreichende Imageschäden) | 🔴 |
| **Sehr hoch** | Katastrophale, existenzbedrohende Schäden (Gefahr für Leib und Leben, ruinöse Bußgelder, Betriebszusammenbruch) | 🔴 |

### 3.2 Maximumprinzip und Vererbung

Der Schutzbedarf eines IT-Systems richtet sich grundsätzlich nach der Anwendung mit dem **höchsten** Schutzbedarf, die darauf läuft – und zwar **je Schutzziel (Vertraulichkeit, Integrität, Verfügbarkeit) getrennt betrachtet**, nicht als ein pauschaler Gesamtwert:

```text
[ Anwendung A: Vertraulichkeit=normal, Integrität=hoch, Verfügbarkeit=normal ]
[ Anwendung B: Vertraulichkeit=hoch,   Integrität=normal, Verfügbarkeit=normal ]
                      \                              /
                       \                            /
      [ IT-System: Vertraulichkeit=hoch, Integrität=hoch, Verfügbarkeit=normal ]
      (Maximumprinzip: je Schutzziel einzeln das Maximum aus allen Anwendungen)
```

### 3.3 Ausnahmen vom Maximumprinzip

| Effekt | Wirkung | IHK-Relevanz |
| --- | --- | --- |
| **Kumulationseffekt** | Mehrere Anwendungen mit "normalem" Schutzbedarf laufen auf einem System – die Gesamtwirkung eines Ausfalls ist größer als die Wirkung eines einzelnen Objekts, der Schaden summiert sich zu "hoch". Schutzbedarf wird begründet **heraufgesetzt** | 🔴 |
| **Verteilungseffekt** | Eine Anwendung mit hohem Schutzbedarf ist auf mehrere IT-Systeme verteilt, wobei auf einem einzelnen System nur **unwesentliche Teilbereiche** der Anwendung laufen. Der hohe Schutzbedarf der Gesamtanwendung wirkt sich dadurch **relativierend** auf das Einzelsystem aus – er wird nicht automatisch vollständig übertragen. Ob und in welchem Umfang eine Herabsetzung gerechtfertigt ist, muss fachlich nachvollziehbar begründet werden, getrennt je Schutzziel | 🔴 |

> **Abgrenzung zu reiner Redundanz:** Eine redundante Spiegelung ist nicht automatisch ein Verteilungseffekt. Enthält *jeder* Knoten einer gespiegelten Datenbank weiterhin die vollständigen, hochschutzbedürftigen Daten, trägt jedes einzelne System weiterhin den vollen Schutzbedarf – eine Herabsetzung wäre hier nicht begründet. Der Verteilungseffekt greift nur, wenn tatsächlich nur ein unwesentlicher *Teil* der schutzbedürftigen Funktion oder Information auf dem einzelnen System liegt.

> **IHK-Typfrage:** *"Eine virtuelle Serverinstanz beherbergt drei Container: Wiki (Vertraulichkeit=normal, Integrität=normal, Verfügbarkeit=normal), Buchhaltung (Vertraulichkeit=hoch, Integrität=hoch, Verfügbarkeit=normal), Entwicklungsdatenbank (Vertraulichkeit=hoch, Integrität=normal, Verfügbarkeit=hoch). Ermitteln Sie den geerbten Schutzbedarf der Serverinstanz."*
> **Musterantwort:** Nach dem Maximumprinzip wird **je Schutzziel einzeln** das Maximum aus allen Containern übernommen: **Vertraulichkeit = hoch** (von Buchhaltung/Datenbank), **Integrität = hoch** (von Buchhaltung), **Verfügbarkeit = hoch** (von Datenbank). Die drei Werte werden dabei unabhängig voneinander ermittelt, nicht zu einem einzigen Gesamtwert zusammengefasst.

---

## 4. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Die Strukturanalyse kennt "Personen" als eigenen, gleichrangigen sechsten Bereich | Personen/Rollen werden zwar konkret miterfasst (z. B. bei IT-Systemen), bilden aber keinen eigenen, gleichrangigen Bereich neben Geschäftsprozessen, Anwendungen, IT-Systemen, Netzen und Räumen |
| 2 | Geschäftsprozesse/Fachaufgaben gehören nicht zur Strukturanalyse | Sie sind explizit einer der Kernbereiche der Strukturanalyse – ein häufig übersehener, aber prüfungsrelevanter Punkt |
| 3 | Der Schutzbedarf eines Systems ist der Durchschnitt der darauf laufenden Anwendungen | Das Maximumprinzip gilt: je Schutzziel das **Maximum**, nicht der Durchschnitt, und **für jedes Schutzziel getrennt** ermittelt |
| 4 | Kumulations- und Verteilungseffekt sind Standardfall, nicht Ausnahme | Beide sind begründete **Abweichungen** vom Regelfall (Maximumprinzip) – sie gelten nur bei nachvollziehbarer fachlicher Begründung |
| 5 | Jede redundante/gespiegelte Anwendung ist automatisch ein Fall des Verteilungseffekts | Nein – enthält jeder Knoten weiterhin die vollständigen, hochschutzbedürftigen Daten, greift der Verteilungseffekt nicht. Er gilt nur, wenn ein einzelnes System tatsächlich nur einen unwesentlichen *Teil* der Anwendung/Information trägt |
| 6 | Eine berechnete USV-Kapazität (z. B. in Ah) ist bereits die reale Bestellgröße | Die einfache Rechnung liefert nur den theoretischen Idealwert – Wirkungsgrad, Entladetiefe, Alterung und Sicherheitsaufschlag fehlen noch |
| 7 | PUE-Werte verschiedener Rechenzentren sind immer direkt vergleichbar | Nur bei vergleichbarer Messmethode und ähnlichen Betriebsbedingungen (Größe, Auslastung, Klima, Redundanz) aussagekräftig |

---

## 5. Deep-Dive-Ausblick (freiwillig)

- **BSI-Baustein-Mapping** (→ Abschnitt 1): Wie konkrete Zielobjekte (z. B. ein Remote-Arbeitsplatz) begründet einzelnen Bausteinen des IT-Grundschutz-Kompendiums zugeordnet werden (z. B. `SYS.2.1 Allgemeiner Client`, `INF.1 Allgemeines Gebäude`).
- **Abwärmenutzung & PUE-Vertiefung** (→ Abschnitt 2): Wie die Abwärme eines Rechenzentrums rechnerisch zur Gebäudeheizung genutzt werden kann.
- **Reale USV-Auslegung** (→ Abschnitt 2.3): Wie Wirkungsgrad, Entladetiefe, Batteriealterung und Scheinleistung (VA) in eine praxistaugliche USV-Dimensionierung einfließen.
- **DSGVO Art. 9 und Schutzbedarf** (→ Abschnitt 3): Warum besondere Kategorien personenbezogener Daten (Gesundheitsdaten, politische Meinungen) häufig zu einem erhöhten Schutzbedarf bei Vertraulichkeit/Integrität führen können – und warum die konkrete Einstufung dennoch anhand der möglichen Schadensauswirkungen begründet werden muss, nicht automatisch aus Art. 9 folgt.

---

## 6. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Nenne die Kernbereiche der BSI-Strukturanalyse. | Geschäftsprozesse/Fachaufgaben und Informationen, Anwendungen, Netze/Kommunikationsverbindungen, IT-/ICS-/IoT-Systeme, Räume/Gebäude |
| 2 | Sind Personen ein eigener Zielobjekt-Typ der Strukturanalyse? | Nein – Personen, Rollen und Verantwortlichkeiten werden durchaus konkret erfasst (z. B. bei Geschäftsprozessen, Anwendungen, IT-Systemen), bilden aber keinen eigenen, gleichrangigen Bereich neben diesen |
| 3 | Ein System hat 800 W Leistungsaufnahme. Wie viel elektrische Arbeit verrichtet es in 10 Stunden? | 800 W × 10 h = 8.000 Wh = 8 kWh |
| 4 | Was besagt das Maximumprinzip? | Der Schutzbedarf eines Systems entspricht dem höchsten Schutzbedarf der darauf laufenden Anwendungen, je Schutzziel einzeln betrachtet |
| 5 | Wann wird der Schutzbedarf trotz Maximumprinzip manuell heraufgesetzt? | Beim Kumulationseffekt – viele "normale" Anwendungen summieren sich zu einem höheren Gesamtschaden |
| 6 | Warum ist eine berechnete USV-Kapazität nur ein Ausgangswert? | Sie berücksichtigt noch keinen Wirkungsgrad, keine Entladetiefe, keine Batteriealterung und keinen Sicherheitsaufschlag |

---

## 7. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Informationsverbund** | Geltungsbereich eines Sicherheitskonzepts nach BSI-Standard 200-2 |
| **Strukturanalyse-Bereiche** | Geschäftsprozesse/Informationen, Anwendungen, Netze, IT-/ICS-/IoT-Systeme, Räume/Gebäude |
| **Maximumprinzip** | Schutzbedarf eines Systems = Maximum der Schutzbedarfe der darauf laufenden Anwendungen, je Schutzziel |
| **Kumulationseffekt** | Viele "normale" Risiken summieren sich zu höherem Gesamtschaden → Schutzbedarf hoch |
| **Verteilungseffekt** | Nur unwesentliche Teilbereiche einer Anwendung laufen auf dem Einzelsystem – der Schutzbedarf wirkt relativierend, wird aber nicht automatisch herabgesetzt. Nicht dasselbe wie reine Redundanz/Spiegelung |
| **PUE** | Power Usage Effectiveness – Kennzahl für Rechenzentrums-Energieeffizienz, nur bedingt zwischen Standorten vergleichbar |

---

## 8. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Strukturanalyse-Vollständigkeit | "Welche Bereiche muss eine Strukturanalyse erfassen?" | Alle fünf Kernbereiche nennen, Personen nicht als eigenen sechsten Typ auflisten |
| Berechnungsaufgabe | "Berechnen Sie die elektrische Arbeit/USV-Kapazität für …" | Vollständiger Rechenweg mit Einheiten; bei USV auf den Idealwert-Charakter hinweisen |
| Maximumprinzip-Anwendung | "Ermitteln Sie den geerbten Schutzbedarf von System X" | Jedes Schutzziel (Vertraulichkeit/Integrität/Verfügbarkeit) einzeln maximieren, Begründung angeben |

---

## 9. Merksätze für das Fachgespräch

> Eine Strukturanalyse, die Geschäftsprozesse oder einen anderen Kernbereich auslässt, hat von Anfang an eine Lücke – Vollständigkeit kommt vor Detailtiefe.

> Personen sind sicherheitsrelevant, aber kein eigener Zielobjekt-Typ – sie hängen an den Objekten, die sie nutzen oder verwalten.

> Das Maximumprinzip fragt nicht "im Schnitt", sondern "im schlimmsten Fall" – und das für jedes Schutzziel einzeln, nicht als ein Gesamturteil.

> Eine berechnete USV-Kapazität ist der Anfang der Auslegung, nicht das Ende – Wirkungsgrad und Sicherheitsaufschlag kommen noch dazu.

---

*Fortsetzung in Teil B: Sichere mobile Datenspeicher, TOM & Web-Sicherheit (OWASP), Patch-Management, Incident Response.*

---

```yaml
dokument: LF4.2A-wiki-artikel
lernfeld: LF4.2
teil: "1 von 2 (A: Strukturanalyse, Physische Sicherheit, Schutzbedarf)"
titel: "BSI-Grundschutz-Methodik: Strukturanalyse & Schutzbedarf"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-08
quellen_intern:
  - "LF4.2.1: Strukturanalyse - Was müssen wir schützen.md"
  - "LF4.2.2: Physische Sicherheit, Energiebedarf & Green IT.md"
  - "LF4.2.3: Schutzbedarfsfeststellung & das Maximumprinzip.md"
quellen_fachlich:
  - titel: "BSI-Standard 200-2: IT-Grundschutz-Methodik"
    herausgeber: "Bundesamt für Sicherheit in der Informationstechnik"
    status: "Version 1.0; Strukturanalyse-Bereiche gegen BSI-Kompendium/Online-Kurs korrigiert (Geschäftsprozesse/Fachaufgaben statt 'Personen' als sechster Bereich, Verteilungseffekt-Definition korrigiert). Vor Veröffentlichung gegen die zum Nutzungszeitpunkt aktuelle BSI-Fassung/Kompendium-Edition prüfen"
  - titel: "IT-Grundschutz-Kompendium"
    herausgeber: "Bundesamt für Sicherheit in der Informationstechnik"
    status: "aktuelle Edition bzw. aktuelle Errata vor Veröffentlichung prüfen"
review_historie:
  - runde: 1
    datum: 2026-09-08
    ergebnis: "Ursprünglich Teil eines gemeinsamen LF4.2-Artikels (7 Unterkapitel). Externe Review (3 Reviews) ergab: Artikel zu lang für einen Wiki-Beitrag – auf Nutzerwunsch in Teil A (dieser Artikel: Strukturanalyse, Physische Sicherheit, Schutzbedarf) und Teil B (Datenträger, TOM/OWASP, Patch-Management, Incident Response) aufgeteilt. Dabei fachliche Korrektur aus der gründlichsten Review (mit BSI-200-2-PDF-Zitat) übernommen: 'Personen' ist nach BSI-Standard 200-2 kein eigener, gleichrangiger sechster Zielobjekt-Typ der Strukturanalyse – korrigiert auf die tatsächlichen Bereiche (Geschäftsprozesse/Fachaufgaben und Informationen, Anwendungen, Netze, IT-/ICS-/IoT-Systeme, Räume/Gebäude), Geschäftsprozesse/Fachaufgaben als vorher fehlender, prüfungsrelevanter Bereich ergänzt. Maximumprinzip-Darstellung präzisiert: ausdrücklich als 'je Schutzziel einzeln', nicht als pauschaler Gesamtwert. USV-Berechnung als theoretischer Idealwert ohne Wirkungsgrad/Entladetiefe/Alterung gekennzeichnet. PUE-Vergleichsaussage relativiert (nur bei vergleichbarer Messmethode/Betriebsbedingungen aussagekräftig). Markdown-Fehler, die eine Review meldete, beim Abgleich mit der tatsächlichen Datei nicht bestätigt – nicht übernommen."
  - runde: 2
    datum: 2026-09-08
    ergebnis: "Externe Prüfung (4 Reviews) eingearbeitet, gewichtet nach Quellenqualität. Wichtigster Fund (Review mit BSI-Kompendium-Zitat): Verteilungseffekt fachlich korrigiert – bisherige Darstellung verwechselte reine Redundanz/Spiegelung mit dem tatsächlichen BSI-Konzept (nur unwesentliche Teilbereiche einer Anwendung auf dem Einzelsystem), explizite Abgrenzung zu Redundanz ergänzt. Weitere Korrekturen: Strukturanalyse-Bereiche als didaktische Zusammenfassung gekennzeichnet (BSI nennt granularere Einzelkategorien), Personen-Aussage entschärft (werden konkret miterfasst, sind aber kein eigener gleichrangiger Bereich), DSGVO nicht mehr als Schadensbeispiel sondern als Rechtsgrundlage formuliert, Art.-9-Aussage im Deep-Dive von 'zwingend' auf 'kann zu erhöhtem Schutzbedarf führen, muss aber begründet werden' abgeschwächt, Rechenbeispiel-Annahme (Dauerbetrieb bei Nennleistung) explizit gemacht, USV-Abschnitt um Watt-vs-VA-Unterscheidung erweitert, Gaslöschanlagen/Videoüberwachung um praktische Einschränkungen ergänzt, PUE-Formulierung auf 'gesamte Nicht-IT-Infrastruktur' statt nur 'Kühlung' präzisiert, YAML-Quellenangabe um Prüfhinweis auf aktuelle BSI-Fassung ergänzt"
  - runde: 3
    datum: 2026-09-08
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet: Verteilungseffekt-Formulierung weiter präzisiert – 'die Herabsetzung muss begründet werden' auf 'wirkt relativierend, wird nicht automatisch herabgesetzt' geändert (BSI beschreibt eher eine mögliche Relativierung als eine zwingende Herabsetzung), Cheatsheet-Eintrag entsprechend nachgezogen. Selbsttest-Antwort zu Personen präzisiert: 'werden im Zusammenhang mit den Objekten berücksichtigt' konnte als reine Nebenerwähnung missverstanden werden – jetzt klargestellt, dass Personen/Rollen konkret erfasst werden, nur eben nicht als eigener gleichrangiger Bereich. Teil-Kennzeichnung im Frontmatter klarer formuliert (beschreibt jetzt den eigenen statt nur den anderen Teil)."
  - runde: 4
    datum: 2026-09-08
    ergebnis: "Eigene Abschlussprüfung (kein externer Review): gesamte Datei durchgelesen, kleines Blockquote-Spacing-Problem im Schwesterartikel Teil B behoben (nicht in dieser Datei relevant), Konsistenz aller Kernaussagen (Verteilungseffekt, Personen, DSGVO) über Haupttext/Selbsttest/Cheatsheet/YAML bestätigt. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 4 Runden (3 externe Reviews + 1 eigene Abschlussprüfung, 2026-09-08) – Freigabe durch Autor:in bestätigt"
```