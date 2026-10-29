# LF6.4 – Support-Kommunikation & Service-Qualität

*Wie du im Gespräch souverän bleibst, Qualität messbar machst und aus Fehlern ein System lernt*

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 60–75 Minuten
> **Status:** Final
> **Stand:** 2026

---

## 📌 IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Was sind die 4 Ebenen des Schulz-von-Thun-Modells im Support? | [1.1 Das Vier-Seiten-Modell](#11-das-vier-seiten-modell-schulz-von-thun) |
| 2 | Warum sind Killerphrasen im Support gefährlich? | [1.3 Killerphrasen](#13-killerphrasen-und-ihr-gegenmittel) |
| 3 | Wie berechnest du MTTR und FCR, und warum reicht MTTR allein nicht? | [2. Metriken](#2-messung-der-service-qualität) |
| 4 | Was bedeutet das UFFA-Prinzip bei KCS? | [3.1 KCS und UFFA](#31-kcs-und-das-uffa-prinzip) |
| 5 | Was passiert in den 4 Phasen des PDCA-Zyklus? | [4. PDCA-Zyklus](#4-kontinuierliche-verbesserung-pdca) |

---

## 1. Professionelle Support-Kommunikation

> Der Kunde sagt "Mein PC geht nicht" – aber er sendet gleichzeitig drei weitere Botschaften mit, die du hören musst.

### 1.1 Das Vier-Seiten-Modell (Schulz von Thun)

Jede Nachricht enthält laut Schulz von Thun vier Ebenen gleichzeitig:

| Ebene | Bedeutung | Beispiel: "Mein PC geht nicht, ihr seid unfähig!" | IHK-Relevanz |
|---|---|---|---|
| Sachinhalt | Reine Fakten | "PC geht nicht" | 🔴 |
| Selbstkundgabe | Was der Sprecher über sich offenbart | Frustriert, fühlt sich hilflos | 🔴 |
| Beziehungsebene | Wie die Beziehung definiert wird | Abwertung der Support-Leistung | 🔴 |
| Appell | Gewünschte Handlung | "Löst das Problem sofort" | 🔴 |

**Die zentrale Support-Regel:** Das **Beziehungsohr** ist bei verärgerten Kunden oft überreizt. Der Fehler wäre, eine Aussage auf der Sachebene ("Der Computer ist zu langsam") als persönlichen Angriff auf der Beziehungsebene zu deuten – oder umgekehrt, eine emotionale Aussage nur technisch zu beantworten, ohne die Emotion zu adressieren.

> **IHK-Typfrage:** *"Ein Kunde schreibt genervt: 'Warum dauert das schon wieder so lange?' Wie reagierst du nach dem Vier-Seiten-Modell?"*
> **Musterantwort:** Ich höre nicht nur die Sachebene (Bearbeitungsdauer), sondern auch die Selbstkundgabe (Frustration/Zeitdruck) und die Beziehungsebene (Vorwurf an den Support). Statt mich zu rechtfertigen, spiegle ich die Emotion ("Ich verstehe, dass die Wartezeit belastend ist") und liefere dann die Sachinformation zum aktuellen Status.

### 1.2 Aktives Zuhören: Paraphrasieren

Wiederholen des Gehörten mit eigenen Worten – zeigt dem Kunden "Ich habe dich verstanden" und deckt Missverständnisse früh auf.

**Gutes Paraphrasieren spiegelt auch den fachlichen Kern**, nicht nur die Emotion:

> Schlecht: *"Ich verstehe, dass Sie frustriert sind."* (nur Emotion)
> Gut: *"Sie sagen also, dass die Anmeldemaske bei Sonderzeichen streikt, obwohl der Release morgen ist? Das verstehe ich, das ist wirklich unter Zeitdruck."* (Fachkern + Emotion)

### 1.3 Killerphrasen und ihr Gegenmittel

| Begriff | Bedeutung | IHK-Relevanz |
|---|---|---|
| Killerphrase | Scheinargument, das den Dialog beendet, ohne inhaltlich zu antworten | 🔴 |
| Ziel einer Killerphrase | Macht ausüben, Veränderung abwehren, Zeit gewinnen | 🟡 |
| Gegenmittel | Rückfragen/Paraphrasieren, um die Phrase zu entlarven | 🔴 |

**Beispiele:** "Dafür bin ich nicht zuständig.", "Das haben wir hier noch nie so gemacht.", "Das liegt an Ihrer Hardware." (ungeprüft behauptet).

**Warum gefährlich:** Eine Killerphrase blockiert den Lösungsweg komplett – vergleichbar mit einem Deadlock: Beide Seiten warten, aber niemand bewegt sich, weil der Pfad blockiert ist.

### 1.4 Fragetechniken je Support-Level

| Level | Technik | Zweck | IHK-Relevanz |
|---|---|---|---|
| 1st Level | Trichtermodell (offen → geschlossen) | Schnelle Kategorisierung (Incident/Request), Standardlösungen | 🔴 |
| 2nd Level | 5-Why-Methode | Tiefere Ursachenanalyse bei komplexeren Problemen | 🟡 |
| 3rd Level | 6W-Fragen + System-Logs | Undokumentierte Probleme lösen, Wissen für untere Level dokumentieren | 🟡 |

**Zusatzwerkzeug: Skalierungsfragen** ("Auf einer Skala von 1–10, wie stark ist Ihr Arbeitsablauf blockiert?") objektivieren die Dringlichkeit für die Eskalationsentscheidung.

### 1.5 Warum gute Kommunikation die KPIs verbessert

| Effekt | Zusammenhang | IHK-Relevanz |
|---|---|---|
| Höhere FCR | Strukturierte Fragen + Wissensdatenbank verhindern unnötige Eskalationen | 🔴 |
| Niedrigere MTTR | Paraphrasieren vermeidet Missverständnisse, die Zeit kosten | 🔴 |
| Höheres CSAT | Aktives Zuhören signalisiert Ernstnehmen des Problems | 🟡 |
| Geringere Kosten | Weniger Eskalation an teurere 2nd/3rd-Level-Techniker | 🟡 |

---

## 2. Messung der Service-Qualität

> Eine schnelle Lösung ist nicht automatisch eine gute Lösung – erst zusammen mit Qualitätskennzahlen ergibt Geschwindigkeit Sinn.

### 2.1 Die "großen Drei" Kennzahlen

| Kennzahl | Formel | Aussage | IHK-Relevanz |
|---|---|---|---|
| **MTTR** (Mean Time To Repair) | Σ(Wiederherstellungszeit − Ticketeingang) / Anzahl behobener Vorfälle | Wie schnell wird entstört? | 🔴 |
| **FCR** (First Contact Resolution) | (beim Erstkontakt gelöste Tickets / Gesamttickets) × 100 | Wie gut ist das Frontline-Wissen? | 🔴 |
| **Ticketvolumen** | Gesamtanzahl Tickets in Zeitraum | Wie hoch ist die Last? | 🟡 |

**Rechenbeispiel MTTR** (5 Tickets: 30, 120, 15, 240, 60 Minuten):
```
Summe = 30 + 120 + 15 + 240 + 60 = 465 Min.
MTTR = 465 / 5 = 93 Min.
```

**Rechenbeispiel FCR** (200 Tickets, 80 direkt telefonisch gelöst):
```
FCR = 80 / 200 × 100 = 40 %
```

> **IHK-Typfrage:** *"Ein Team hat eine sehr niedrige MTTR, aber niedrige Kundenzufriedenheit (CSAT). Was bedeutet das?"*
> **Musterantwort:** Die niedrige MTTR zeigt nur, dass Tickets schnell geschlossen werden – nicht, dass das Problem nachhaltig gelöst wurde. Häufig deutet das auf Symptombekämpfung statt Ursachenbehebung hin (z. B. "Neustart hilft kurzfristig"). Eine niedrige MTTR ist nur aussagekräftig gut, wenn gleichzeitig die First Fix Rate hoch ist – sonst wird Quantität über Qualität gestellt.

### 2.2 Quantitativ vs. qualitativ

| Typ | Beispiel | IHK-Relevanz |
|---|---|---|
| Quantitativ | MTTR, FCR, Ticketvolumen, Backlog | 🔴 |
| Qualitativ | CSAT (Kundenzufriedenheit, meist Kurzumfrage) | 🟡 |

**Manipulationsrisiko:** Tickets werden schnell geschlossen und bei erneutem Auftreten neu geöffnet, um die MTTR künstlich zu verbessern ("Zahlen-Jagen") – das verschleiert die eigentliche Servicequalität.

---

## 3. Wissensmanagement (KCS)

> Der beste Wissensartikel entsteht nicht danach, sondern während der Ticketbearbeitung.

### 3.1 KCS und das UFFA-Prinzip

**KCS (Knowledge Centered Service):** Dokumentation entsteht direkt bei der Bearbeitung, nicht als nachträgliche Zusatzaufgabe.

| Schritt | Bedeutung | IHK-Relevanz |
|---|---|---|
| **U**se it | Vorhandenen Artikel bei der Lösung nutzen | 🔴 |
| **F**lag it | Veralteten/fehlerhaften Artikel markieren | 🔴 |
| **F**ix it | Artikel korrigieren | 🔴 |
| **A**dd it | Fehlenden Artikel neu anlegen | 🔴 |

### 3.2 Struktur eines guten Wiki-/FAQ-Artikels

1. Klarer, prägnanter Titel (System + Zweck)
2. Metadaten (Ersteller, Änderungsdatum, Status: Entwurf/Überprüft/Veraltet)
3. Symptombeschreibung
4. Ursache
5. Schritt-für-Schritt-Lösung (nummeriert, mit Code-Blöcken wo nötig)
6. Troubleshooting-Hinweise

### 3.3 Internes vs. externes Wissen

| Typ | Zielgruppe | Inhalt |
|---|---|---|
| Internes Wissen | Techniker | Detaillierte technische Schritte, Konfigurationen |
| Externes Wissen | Endanwender | Einfache Anleitung, keine internen Details |

### 3.4 Review-Prozess

Ein Artikel muss überarbeitet oder gelöscht werden, wenn: die zugrundeliegende Software-Version veraltet ist (z. B. Anleitung für Ubuntu 18.04 bei aktivem Einsatz von 24.04), die Lösung nicht mehr funktioniert, oder Duplikate mit widersprüchlichen Informationen entstehen ("Informationsfriedhof" – viele Artikel, aber schlecht auffindbar).

> **IHK-Typfrage:** *"Warum ist eine gute Verschlagwortung (Tagging) für ein Wiki genauso wichtig wie die Artikelqualität selbst?"*
> **Musterantwort:** Auch der beste Artikel nützt nichts, wenn er nicht gefunden wird. Ohne konsistente Tags/Metadaten entsteht bei wachsender Artikelzahl ein "Informationsfriedhof", in dem Techniker lieber neu recherchieren als suchen – das untergräbt den gesamten Zweck von KCS.

---

## 4. Kontinuierliche Verbesserung (PDCA)

> PDCA ist kein einmaliges Projekt, sondern ein Kreis, der sich wieder schließt, sobald ein neues Problem auftaucht.

### 4.1 Die vier Phasen

| Phase | Kernfrage | Inhalt | IHK-Relevanz |
|---|---|---|---|
| **P**lan | Was wollen wir erreichen? | Problem/Ist-Zustand beschreiben, Ziel + messbare Kennzahlen definieren | 🔴 |
| **D**o | Wie setzen wir es um? | Maßnahme im kleinen Rahmen (Pilot) testen, Daten sammeln | 🔴 |
| **C**heck | Hat es funktioniert? | Ergebnisse mit Zielen vergleichen | 🔴 |
| **A**ct | Was machen wir jetzt besser? | Bei Erfolg: Standardisieren. Bei Misserfolg: neuer Zyklus | 🔴 |

**Beispiel: "Zu viele Rückfragen bei Hardware-Bestellungen"**
- **Plan:** Ursache = ungenaue Bestellbeschreibungen. Ziel: Rückfragequote −50 %. Maßnahme: standardisiertes Bestellformular
- **Do:** Formular als PDF, 2–3 Wochen Testlauf in einer Abteilung
- **Check:** Rückfragen pro Bestellung verglichen, Feedback der Fachabteilung eingeholt
- **Act:** Bei Erfolg → Formular fest im Intranet verankern; bei Misserfolg → Analyse und neuer Zyklus

### 4.2 Das Ishikawa-Diagramm (6M-Methode)

Werkzeug zur systematischen Ursachensuche – sieht aus wie eine Fischgräte: Kopf = Problem, Gräten = Ursachenkategorien.

| Kategorie (M) | Bedeutung im IT-Kontext | Beispiel | IHK-Relevanz |
|---|---|---|---|
| Mensch | Fehler durch Personen/Qualifikation | Fehlbedienung, fehlende Schulung | 🔴 |
| Maschine | Hardware, Server, Endgeräte | Defekter RAM, überhitzte CPU | 🔴 |
| Material | Kabel, Datenträger, Rohdaten | Defektes LAN-Kabel, fehlerhafter DB-Dump | 🟡 |
| Methode | Arbeitsabläufe, Prozesse | Falsches Update-Verfahren, fehlende Backups | 🔴 |
| Mitwelt | Äußere Einflüsse | Stromausfall, hohe Luftfeuchtigkeit im RZ | 🟡 |
| Messung | Datenqualität, Monitoring | Falsch konfiguriertes Monitoring, ungenaue Logs | 🟡 |

**Ziel von Ishikawa ist immer die Ursachenermittlung, nicht die direkte Problemlösung** – erst danach greift PDCA zur eigentlichen Behebung.

> **IHK-Typfrage:** *"Warum reicht es nicht, ein Problem einfach schnell zu beheben, ohne PDCA zu durchlaufen?"*
> **Musterantwort:** Eine schnelle Behebung (vgl. Incident Management) beseitigt nur das Symptom. Ohne den Check-Schritt weißt du nicht, ob die Maßnahme wirklich wirkt, und ohne Act wird die Lösung nie standardisiert – das Problem kommt wieder. PDCA sorgt für nachhaltige, messbare Verbesserung statt einmaligem Zufallserfolg.

---

## ✅ Selbsttest

| Frage | Kurzantwort |
|---|---|
| 1. Welche vier Ebenen enthält jede Nachricht nach Schulz von Thun? | Sachinhalt, Selbstkundgabe, Beziehungsebene, Appell |
| 2. Warum sind Killerphrasen im Support problematisch? | Sie blockieren den Lösungsweg komplett, ohne inhaltlich zu antworten (Deadlock-Effekt) |
| 3. Was zeigt eine niedrige MTTR bei niedrigem CSAT? | Häufig Symptombekämpfung statt nachhaltiger Lösung – Quantität vor Qualität |
| 4. Wofür steht UFFA bei KCS? | Use it, Flag it, Fix it, Add it |
| 5. Was passiert in der Act-Phase bei PDCA, wenn das Ziel nicht erreicht wurde? | Der Zyklus wird erneut durchlaufen (zurück zu Plan) |

---

## 📋 IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Vier-Seiten-Modell | Sachinhalt, Selbstkundgabe, Beziehung, Appell in jeder Nachricht |
| Paraphrasieren | Gehörtes in eigenen Worten wiederholen, inkl. Fachkern |
| Killerphrase | Scheinargument, das den Dialog ohne Inhalt beendet |
| MTTR | Durchschnittliche Zeit bis zur Störungsbehebung |
| FCR | Anteil beim Erstkontakt gelöster Tickets |
| CSAT | Kundenzufriedenheit, meist per Kurzumfrage gemessen |
| KCS | Knowledge Centered Service – Doku entsteht während der Bearbeitung |
| UFFA | Use it, Flag it, Fix it, Add it |
| PDCA | Plan, Do, Check, Act – Zyklus kontinuierlicher Verbesserung |
| Ishikawa-Diagramm | Fischgräten-Diagramm zur strukturierten Ursachensuche (6M) |

---

## 🎯 Prüfungstaktik

| Aufgabentyp | Formulierung im Fachgespräch | Was die IHK hören will |
|---|---|---|
| Kommunikationsanalyse | "Was hört der Kunde/was sendest du in dieser Aussage?" | Alle vier Ebenen nach Schulz von Thun sauber benennen |
| Deeskalation | "Wie reagierst du auf einen wütenden Kunden?" | Paraphrasieren mit Fachkern, keine Killerphrasen |
| Kennzahlen-Interpretation | "Ist dieses Team gut, wenn MTTR niedrig ist?" | MTTR allein nicht ausreichend – FCR/CSAT mitdenken |
| Ursachenanalyse | "Wie gehst du bei einem wiederkehrenden Fehler vor?" | Ishikawa zur Ursachensuche, dann PDCA zur Umsetzung |

---

## 💬 Merk-Sätze für die mündliche Prüfung

> "Eine Nachricht hat vier Seiten – wer nur die Sachebene hört, überhört den eigentlichen Konflikt."

> "Eine Killerphrase beendet das Gespräch, aber nie das Problem."

> "MTTR sagt, wie schnell – FCR sagt, wie gut. Beide zusammen ergeben erst ein vollständiges Bild."

> "KCS heißt: Wissen entsteht nebenbei, nicht danach."

> "PDCA schließt sich nie endgültig – jedes Act ist der Anfang des nächsten Plan."

---

```yaml
lernfeld: LF6.4
titel: Support-Kommunikation & Service-Qualität
teil: 5 von 5
quellen:
  - LF6.4.1 Professionelle Support-Kommunikation
  - LF6.4.2 Messung der Service-Qualität (Metriken)
  - LF6.4.3 Wissensmanagement (KCS)
  - LF6.4.4 Kontinuierliche Verbesserung (PDCA)
status: final
stand: 2026
```
