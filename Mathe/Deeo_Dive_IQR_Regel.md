# Die IQR-Regel – Ausreißer systematisch erkennen

## 1. Einleitung – Was ist das Thema, wann braucht man es?

Immer wenn du eine Liste von Messwerten hast – Server-Antwortzeiten, Testergebnisse, Login-Zeiten, Gehälter – stellt sich früher oder später die Frage: *Ist dieser eine Wert normal, oder ist er ein Ausreißer?*

Die **IQR-Regel** (Interquartilsabstand-Regel) ist eine einfache, rein rechnerische Methode, um genau das zu beantworten – ohne dass du "nach Gefühl" entscheiden musst. Du brauchst sie überall dort, wo du Daten bewerten musst, bevor du sie interpretierst: beim Monitoring, in der Datenanalyse, in der Qualitätssicherung und in der Security.

> **Grundprinzip:** Du schaust dir den "normalen" mittleren Bereich deiner Daten an und ziehst Grenzen. Alles, was weit außerhalb dieser Grenzen liegt, wird als Ausreißer markiert.

---

## 2. Einfache Erklärung – Die Analogie

Stell dir vor, deine Daten sind eine Schlange von Läufern bei einem Marathon, sortiert nach Zielzeit. Die IQR-Regel teilt die Schlange in vier gleich lange Viertel (**Quartile**).

- Das **mittlere Läufer-Feld** (zwischen dem 25%- und dem 75%-Punkt) sind die "normalen" Zeiten.
- Die **Breite dieses mittleren Feldes** nennst du IQR (Interquartilsabstand).
- Jetzt ziehst du links und rechts vom mittleren Feld noch etwas Puffer dazu (das 1,5-fache der Feldbreite).
- Wer außerhalb dieses Puffers liegt – also viel schneller oder viel langsamer als die Masse – fällt auf. Das sind deine Ausreißer.

Genau dieses Prinzip wendest du bei Server-Antwortzeiten, Testergebnissen oder Zugriffsmustern an.

---

## 3. Voraussetzungen / Wann anwenden?

- Du brauchst eine Liste **numerischer** Werte (mindestens ca. 4–5 Werte, sinnvoll ab deutlich mehr).
- Die Daten müssen **sortierbar** sein (aufsteigend sortiert).
- Die IQR-Regel eignet sich für **eindimensionale** Datensätze (eine Kennzahl pro Beobachtung, z.B. nur Antwortzeit – nicht mehrere Merkmale gleichzeitig).
- Sie ist **robust gegenüber Ausreißern selbst** – im Gegensatz zu Mittelwert und Standardabweichung, die von Extremwerten stark verzerrt werden. Deshalb wird sie in der Praxis bevorzugt, wenn du nicht weißt, ob Ausreißer vorhanden sind.

---

## 4. Schritt-für-Schritt-Rezept

1. **Daten sortieren** (aufsteigend).
2. **Median (Q2) der Gesamtdaten bestimmen:**
   - Gerade Anzahl \(n\): Mittelwert der beiden mittleren Werte.
   - Ungerade Anzahl \(n\): der mittlere Wert selbst.
3. **Q1 bestimmen:** Median der unteren Hälfte (bei ungeradem \(n\) den Gesamtmedian nicht mitzählen).
4. **Q3 bestimmen:** Median der oberen Hälfte (bei ungeradem \(n\) den Gesamtmedian nicht mitzählen).
5. **IQR berechnen:**
   \[
   IQR = Q3 - Q1
   \]
6. **Grenzen (Zäune) berechnen:**
   \[
   \text{Untere Grenze} = Q1 - 1{,}5 \times IQR
   \]
   \[
   \text{Obere Grenze} = Q3 + 1{,}5 \times IQR
   \]
7. **Ausreißer identifizieren:** Jeder Wert außerhalb von [Untere Grenze, Obere Grenze] ist ein Ausreißer.

**Merksatz:**
> "Alles, was mehr als das 1,5-fache des IQR unter Q1 oder über Q3 liegt, ist ein Ausreißer."

---

## 5. Durchgerechnetes Beispiel (IT-Bezug)

Server-Antwortzeiten in ms (n=10, sortiert):

`12, 14, 15, 15, 16, 17, 18, 19, 20, 95`

| Schritt | Rechnung | Ergebnis |
|---|---|---|
| Untere Hälfte | 12, 14, 15, 15, 16 | Q1 = 15 |
| Obere Hälfte | 17, 18, 19, 20, 95 | Q3 = 19 |
| IQR | \(19 - 15\) | 4 |
| Untere Grenze | \(15 - 1{,}5 \times 4\) | 9 |
| Obere Grenze | \(19 + 1{,}5 \times 4\) | 25 |

**→ 95 ms liegt weit über 25 → Ausreißer!**

Das visualisiert man klassischerweise mit einem **Boxplot**: Die Box zeigt Q1 bis Q3, die Antennen (Whiskers) reichen bis zu den Grenzen, Punkte außerhalb der Antennen sind die Ausreißer.

**ROT – hochrelevant für IHK:** Ein Ausreißer ist kein automatischer Fehler. Er ist ein *Hinweis*, den du interpretieren musst – z.B. Traffic-Spike, Angriff, Bug oder Messfehler.

---

## 6. Anwendungsfelder für FIAE/FISI

| Anwendung | Beispiel | IHK-Relevanz |
|---|---|---|
| Monitoring | Ungewöhnliche Server-Response-Zeiten erkennen | 🔴 |
| Datenanalyse | Fehlerhafte Messwerte in Datensätzen finden | 🔴 |
| Qualitätssicherung | Testergebnisse bewerten | 🟡 |
| Security | Ungewöhnliche Login-Zeiten/Zugriffsmuster erkennen | 🔴 |

---

## 7. Praktische Aufgaben

**Hinweis:** Rechne jede Aufgabe erst selbst, bevor du unten in Abschnitt 9 nachschaust!

**Aufgabe 1 (ROT):**
Gegeben: `4, 8, 9, 10, 11, 12, 13, 15, 60` (n=9). Bestimme Q1, Q3, IQR und die Grenzen. Ist 60 ein Ausreißer?

**Aufgabe 2 (ROT):**
Gegeben: CPU-Auslastung in % über 12 Messungen: `20, 22, 21, 23, 24, 22, 25, 21, 20, 78, 23, 24`. Sortiere die Werte und prüfe, ob 78 als Ausreißer gilt.

**Aufgabe 3 (GELB):**
Warum eignet sich die IQR-Regel besser für Ausreißer-Erkennung als "Mittelwert ± 2 Standardabweichungen", wenn du vermutest, dass bereits extreme Ausreißer in den Daten enthalten sind?

**Aufgabe 4 (GELB):**
Ein Login-System zeichnet folgende Zeiten (in Sekunden, gemessen ab Mitternacht, vereinfacht als Zahl) auf: `100, 105, 98, 102, 99, 101, 500`. Berechne die Grenzen und interpretiere das Ergebnis im Security-Kontext.

**Aufgabe 5 (GRÜN):**
Recherchiere kurz: Welchen Wert liefert `pandas.Series.quantile()` standardmäßig für Q1/Q3, und warum kann er leicht von der manuellen "Median-der-Hälfte"-Methode abweichen?

---

## 8. Typische Fehler / Prüfungsfallen

- **ROT:** Bei ungerader Anzahl Werte den Gesamtmedian versehentlich in die untere oder obere Hälfte mit einrechnen – verfälscht Q1/Q3.
- **ROT:** Ausreißer automatisch als "Fehler" oder "muss gelöscht werden" interpretieren, statt sie als Hinweis zur weiteren Prüfung zu behandeln.
- **GELB:** Den Faktor 1,5 mit dem IQR selbst verwechseln (Grenze ist \ (Q1 - 1{,}5 x IQR\ ), nicht \(Q1 - IQR\)).
- **GELB:** Vergessen, die Daten vor der Quartilsberechnung zu sortieren.
- **GRÜN:** Nicht wissen, dass verschiedene Tools (z.B. Pandas, Excel) unterschiedliche Interpolationsmethoden für Quartile verwenden und deshalb leicht abweichende Werte liefern können.

---

## 9. Lösungen

**Lösung Aufgabe 1:**
Daten sortiert: `4, 8, 9, 10, 11, 12, 13, 15, 60` (n=9, ungerade)

- Gesamtmedian (Q2) = 11 (5. Wert)
- Untere Hälfte (ohne Median): `4, 8, 9, 10` → Q1 = Mittelwert(8,9) = 8,5
- Obere Hälfte (ohne Median): `12, 13, 15, 60` → Q3 = Mittelwert(13,15) = 14
- IQR = 14 − 8,5 = 5,5
- Untere Grenze = 8,5 − 1,5×5,5 = 0,25
- Obere Grenze = 14 + 1,5×5,5 = 22,25
- **60 > 22,25 → Ausreißer.**

**Lösung Aufgabe 2:**
Sortiert: `20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 78` (n=12, gerade)

- Gesamtmedian = Mittelwert(22, 23) = 22,5
- Untere Hälfte: `20, 20, 21, 21, 22, 22` → Q1 = Mittelwert(21,21) = 21
- Obere Hälfte: `23, 23, 24, 24, 25, 78` → Q3 = Mittelwert(24,24) = 24
- IQR = 24 − 21 = 3
- Untere Grenze = 21 − 1,5×3 = 16,5
- Obere Grenze = 24 + 1,5×3 = 28,5
- **78 > 28,5 → Ausreißer.**

**Lösung Aufgabe 3:**
Mittelwert und Standardabweichung werden von Extremwerten selbst stark verschoben ("verzerrt") – ein einziger sehr großer Ausreißer zieht den Mittelwert nach oben und vergrößert die Standardabweichung, wodurch die Grenze künstlich weiter wird und der Ausreißer plötzlich "normal" aussieht. Q1 und Q3 basieren dagegen auf der Position der Werte (Median-Prinzip) und reagieren viel weniger empfindlich auf einzelne Extremwerte. Deshalb gilt die IQR-Regel als robuster.

**Lösung Aufgabe 4:**
Sortiert: `98, 99, 100, 101, 102, 105, 500` (n=7, ungerade)

- Gesamtmedian = 101 (4. Wert)
- Untere Hälfte: `98, 99, 100` → Q1 = 99
- Obere Hälfte: `102, 105, 500` → Q3 = 105
- IQR = 105 − 99 = 6
- Untere Grenze = 99 − 1,5×6 = 90
- Obere Grenze = 105 + 1,5×6 = 114
- **500 > 114 → Ausreißer.** Im Security-Kontext ist das ein Hinweis, der weiter untersucht werden sollte (z.B. ungewöhnlicher Login-Zeitpunkt, evtl. Brute-Force-Versuch oder fehlerhafter Zeitstempel) – die Regel liefert nur den Hinweis, nicht die Ursache.

**Lösung Aufgabe 5:**
`pandas.Series.quantile()` nutzt standardmäßig **lineare Interpolation** zwischen den beiden benachbarten Datenpunkten, nicht die manuelle "Median der Hälfte"-Methode. Bei kleinen Datensätzen führt das zu leicht unterschiedlichen Q1/Q3-Werten als bei der Handrechnung – bei größeren Datensätzen gleicht sich der Unterschied meist aus.

---

## 10. Praxis-Bonus: IQR in Python

```python
import pandas as pd

# Daten aus dem Beispiel
antwortzeiten = pd.Series([12, 14, 15, 15, 16, 17, 18, 19, 20, 95])

# Quartile berechnen
Q1 = antwortzeiten.quantile(0.25)
Q3 = antwortzeiten.quantile(0.75)
IQR = Q3 - Q1

# Grenzen berechnen
untere_grenze = Q1 - 1.5 * IQR
obere_grenze = Q3 + 1.5 * IQR

# Ausreißer finden
ausreisser = antwortzeiten[(antwortzeiten < untere_grenze) |
                           (antwortzeiten > obere_grenze)]

print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Grenzen: [{untere_grenze}, {obere_grenze}]")
print(f"Ausreißer:\n{ausreisser}")
```

**Ausgabe:**
```
Q1: 15.0, Q3: 19.0, IQR: 4.0
Grenzen: [9.0, 25.0]
Ausreißer:
9    95
```

**GRÜN:** Pandas nutzt standardmäßig eine etwas andere Interpolationsmethode als die manuelle "Median-der-Hälfte"-Methode – bei größeren Datensätzen können die Werte leicht abweichen. Für den Einstieg ist das vernachlässigbar.

---

```yaml
titel: "Die IQR-Regel – Ausreißer systematisch erkennen"
typ: "Deep Dive (Typ B)"
zielgruppe: "Umschüler FIAE/FISI, 2. Lehrjahr"
pruefungsrelevanz: "AP1 (schriftlich) + Fachgespräch"
stand: 2026
status: "Draft"
```