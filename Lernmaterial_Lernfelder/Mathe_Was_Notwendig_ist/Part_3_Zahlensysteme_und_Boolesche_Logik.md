# Zahlensysteme & Boolesche Logik

> **Zielgruppe:** Umschüler FIAE/FISI, 1./2. Lehrjahr
> **Prüfungsrelevanz:** 🟡 Grundlagenwissen mit möglichem Einsatz in AP1 und weiteren technischen Prüfungsaufgaben. Zahlensysteme, Bitoperationen und Boolesche Logik sind wichtige IT-Grundlagen, die wiederkehrend in praktischen Aufgaben auftauchen (Speicherberechnung, Subnetting/IP-Adressierung, Dateirechte, Bedingungslogik in Programmen). Die konkrete Prüfungsrelevanz einzelner Inhalte richtet sich nach dem jeweils aktuellen Prüfungskatalog.
> **Lernzeit:** 60–75 Min.
> **Status:** Final
> **Stand:** 2026-09-16
>
> **Hinweis zur Überschneidung:** Der Kern dieses Artikels (Zahlensysteme, Logikgatter) ist inhaltlich bereits in **LF2.1 – Die Logik der Maschinen** abgedeckt (dort mit Hardware-/CPU-Rahmung: Von-Neumann-Architektur, Befehlszyklus). Dieser Artikel steht bewusst zusätzlich im Mathe-Ordner als eigenständige, kompakte Referenz ohne Hardware-Kontext, ergänzt um **Daten & Codierung** (ASCII/UTF-8), das in LF2.1 nicht behandelt wird. Bei Widersprüchen zwischen beiden Artikeln gilt LF2.1 als Pflegeautorität für Zahlensysteme/Logikgatter.

**Legende (redaktionelle Einschätzung, keine offizielle IHK-Gewichtung):** 🔴 unmittelbar auf typische Prüfungsaufgaben anwendbar · 🟡 wichtiges Verständnis-/Transferwissen · 🟢 vertiefendes Kontextwissen

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Wie rechnet man zwischen Dual-, Hexadezimal- und Dezimalsystem um, und wozu wird Hex in der Praxis genutzt? | [1](#1-zahlensysteme) |
| 2 | Wie funktionieren die Grundverknüpfungen AND, OR und NOT, und was macht NAND/NOR zu "universellen" Gattern? | [2](#2-boolesche-logik) |
| 3 | Was ist der Unterschied zwischen ASCII und UTF-8, und warum reicht ASCII nicht für alle Sprachen? | [3](#3-daten--codierung) |

---

## 1. Zahlensysteme

> **Grundprinzip:** Menschen rechnen im Dezimalsystem, weil sie zehn Finger haben. Computer arbeiten mit zwei unterscheidbaren elektrischen Pegeln, die als `0` und `1` interpretiert werden – deshalb eignet sich das Dualsystem besonders für digitale Schaltungen. Hexadezimal ist dabei kein drittes System, das Computer "verstehen" – es ist eine für Menschen lesbarere Kurzschreibweise für Dualzahlen.

### 1.1 Stellenwertsysteme im Vergleich

| System | Basis | Ziffern | Typische Verwendung |
|---|---|---|---|
| Dezimal | 10 | 0–9 | Alltag |
| Dual (Binär) | 2 | 0, 1 | Interne Repräsentation in der Hardware |
| Hexadezimal | 16 | 0–9, A–F | Kompakte, menschenlesbare Darstellung von Bitmustern beliebiger Länge (z. B. Farbcodes, Speicheradressen, MAC-Adressen) |

Jede Stelle in einem Stellenwertsystem hat einen Wert, der einer Potenz der Basis entspricht. Im Dezimalsystem ist die Zahl 347 = 3×10² + 4×10¹ + 7×10⁰. Im Dualsystem funktioniert das identisch, nur mit Basis 2.

🟢 **Nice to know:** Eine einzelne Dualstelle heißt **Bit**. **8 Bit ergeben 1 Byte** – die gebräuchlichste Speichereinheit, in der z. B. ein einzelnes ASCII-Zeichen abgelegt wird (siehe Abschnitt 3.2).

### 1.2 Umrechnung Dual → Dezimal

```text
1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰
      = 8 + 0 + 2 + 1
      = 11₁₀
```

### 1.3 Umrechnung Dezimal → Dual

Fortlaufende Division durch 2, die Reste (von unten nach oben gelesen) ergeben die Dualzahl:

```text
13 ÷ 2 = 6 Rest 1
 6 ÷ 2 = 3 Rest 0
 3 ÷ 2 = 1 Rest 1
 1 ÷ 2 = 0 Rest 1

Von unten nach oben gelesen: 13₁₀ = 1101₂
```

### 1.4 Umrechnung Dual ↔ Hexadezimal

Da 16 = 2⁴ ist, entspricht **genau eine Hex-Ziffer exakt vier Dualstellen** (einem "Nibble") – deshalb lässt sich zwischen Dual und Hex direkt blockweise umrechnen, ohne über Dezimal zu gehen.

| Dezimal | Dual | Hex |
|---:|---:|---:|
| 0 | `0000` | `0` |
| 1 | `0001` | `1` |
| 2 | `0010` | `2` |
| 3 | `0011` | `3` |
| 4 | `0100` | `4` |
| 5 | `0101` | `5` |
| 6 | `0110` | `6` |
| 7 | `0111` | `7` |
| 8 | `1000` | `8` |
| 9 | `1001` | `9` |
| 10 | `1010` | `A` |
| 11 | `1011` | `B` |
| 12 | `1100` | `C` |
| 13 | `1101` | `D` |
| 14 | `1110` | `E` |
| 15 | `1111` | `F` |

```text
1011 1110₂  →  in 4er-Blöcke teilen: 1011 | 1110
            →  1011₂ = 11₁₀ = B₁₆ ; 1110₂ = 14₁₀ = E₁₆
            →  1011 1110₂ = BE₁₆
```

Ist die Dualzahl kein Vielfaches von 4 Stellen lang, wird links mit Nullen aufgefüllt, ohne den Wert zu verändern (z. B. `101101₂` → `0010 1101₂`).

> **Wichtig für die Prüfung:** Bei Hex↔Dual **immer in 4er-Blöcken (Nibbles) denken** – das ist schneller und fehlerärmer als der Umweg über Dezimal. 🔴

### 1.5 Umrechnung Dezimal ↔ Hexadezimal (direkt)

Anders als oft angenommen, ist für Dezimal↔Hex **kein Umweg über Dual nötig** – die direkte Umrechnung funktioniert wie bei Dezimal↔Dual, nur mit Basis 16 statt Basis 2.

**Dezimal → Hex** (fortlaufende Division durch 16):

```text
45 ÷ 16 = 2 Rest 13   (13 = D)
 2 ÷ 16 = 0 Rest 2

Von unten nach oben gelesen: 45₁₀ = 2D₁₆
```

**Hex → Dezimal** (Stellenwerte mit Basis 16 aufsummieren):

```text
2D₁₆ = 2×16¹ + D×16⁰
     = 2×16 + 13×1
     = 32 + 13
     = 45₁₀
```

> **Wichtig für die Prüfung:** Es gibt **zwei gültige Wege** für Dezimal↔Hex – direkt durch 16 dividieren, oder über Dual als Zwischenschritt. Beide führen zum selben Ergebnis. Bei einer vorgegebenen Dezimalzahl ist die direkte Division durch 16 oft zweckmäßig; liegt die Zahl bereits dual vor, bietet sich stattdessen die Umrechnung über 4er-Blöcke an. 🔴

### 1.6 Bitoperationen

| Operation | Bedeutung | Beispiel (4 Bit) |
|---|---|---|
| AND (`&`) | 1, wenn **beide** Bits 1 sind | `1010 & 1100 = 1000` |
| OR (`\|`) | 1, wenn **mindestens ein** Bit 1 ist | `1010 \| 1100 = 1110` |
| XOR (`^`) | 1, wenn die Bits **unterschiedlich** sind | `1010 ^ 1100 = 0110` |
| NOT (`~`) | Kippt jedes Bit | `~1010 = 0101` (bei 4 Bit) |

> **Wichtig für die Prüfung:** Das Ergebnis von `NOT` hängt von der betrachteten **Bitbreite** ab – `~1010` ergibt bei 4 Bit `0101`, bei 8 Bit dagegen `~00001010 = 11110101`. Ohne Angabe der Bitbreite ist `NOT` nicht eindeutig bestimmt. 🟡

🟡 **Praxisbezug – Unix-Dateirechte:** Rechte werden als Bitmuster kodiert: `r=4=100₂`, `w=2=010₂`, `x=1=001₂`. Für die `chmod`-Ziffer werden die **Stellenwerte der gesetzten Bits** addiert (nicht die Bits selbst, die ja nur 0 oder 1 sind):

```text
rw- = 110₂ = 6
r-x = 101₂ = 5
r-- = 100₂ = 4

chmod 654 datei   (Besitzer: rw-, Gruppe: r-x, Andere: r--)
```

Auch Subnetzmasken bei der IP-Adressierung beruhen auf demselben Bitmuster-Prinzip.

> **IHK-Typfrage:** *"Gegeben sind die 4-Bit-Muster A = 1100 und B = 1010. Berechnen Sie A AND B, A OR B und A XOR B."*
> **Musterantwort:**
> ```text
>   1100  (A)
> & 1010  (B)
> ------
>   1000
> ```
> A AND B = `1000` (nur an der äußersten linken Stelle sind beide Bits 1), A OR B = `1110` (an jeder Stelle, an der mindestens ein Bit 1 ist), A XOR B = `0110` (an den Stellen, an denen sich A und B unterscheiden).

---

## 2. Boolesche Logik

> **Grundprinzip:** Ein Lichtschalter ist ein einfaches Modell für zwei Zustände: an oder aus. Boolesche Logik ist die Mathematik genau solcher Zwei-Zustands-Systeme – und weil digitale Schaltungen ebenfalls mit zwei unterscheidbaren elektrischen Pegeln arbeiten (vgl. Abschnitt 1), ist Boolesche Algebra deren mathematische Grundlage.

### 2.1 Die drei Grundverknüpfungen

| Verknüpfung | Symbol | Wahrheitstabelle |
|---|---|---|
| AND (UND) | `∧` | `1∧1=1`, sonst `0` |
| OR (ODER) | `∨` | `0∨0=0`, sonst `1` |
| NOT (NICHT) | `¬` | `¬1=0`, `¬0=1` |

**Vollständige Wahrheitstabelle für AND und OR:**

| A | B | A AND B | A OR B |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

### 2.2 NAND, NOR und XOR

| Verknüpfung | Bedeutung | Wahrheitstabelle |
|---|---|---|
| NAND | NOT(A AND B) | Nur `0`, wenn A **und** B beide 1 sind |
| NOR | NOT(A OR B) | Nur `1`, wenn A **und** B beide 0 sind |
| XOR | Exklusives ODER – 1, wenn A und B **unterschiedlich** sind | `0⊕0=0`, `0⊕1=1`, `1⊕0=1`, `1⊕1=0` |

> **Wichtig für die Prüfung:** NAND und NOR heißen **universelle Gatter** (funktional vollständig), weil sich **jede** beliebige logische Verknüpfung (AND, OR, NOT, XOR usw.) ausschließlich aus NAND-Gattern (oder ausschließlich aus NOR-Gattern) aufbauen lässt. Das vereinfacht Entwurf und Standardisierung digitaler Schaltungen – reale moderne Chips verwenden trotzdem meist unterschiedliche, optimierte Bauelemente statt ausschließlich eines einzigen Gattertyps. 🟡

### 2.3 Boolesche Ausdrücke und De-Morgan-Bezug

```text
WENN (Nutzer.istAktiv UND NICHT Nutzer.istGesperrt)
    DANN Zugriff gewähren
```

🟢 **Querverweis:** Die Regeln zum Umformen negierter Ausdrücke (De-Morgan-Regeln) werden in **Part 2 – Mengenlehre, Dreisatz & De-Morgan-Regeln** dieser Serie ausführlich behandelt.

> **IHK-Typfrage:** *"Erstellen Sie die Wahrheitstabelle für den Ausdruck A XOR (NOT B)."*
> **Musterantwort:**
>
> | A | B | NOT B | A XOR (NOT B) |
> |---|---|---|---|
> | 0 | 0 | 1 | 1 |
> | 0 | 1 | 0 | 0 |
> | 1 | 0 | 1 | 0 |
> | 1 | 1 | 0 | 1 |
>
> Der Ausdruck ist wahr, wenn A und (NOT B) unterschiedliche Werte haben.

---

## 3. Daten & Codierung

> **Grundprinzip:** Ein Computer speichert grundsätzlich nur Zahlen (Bitmuster) – damit daraus lesbarer Text wird, braucht es eine vereinbarte **Zuordnungstabelle** zwischen Zahl und Zeichen. Genau das ist eine Zeichenkodierung.

### 3.1 Speichergrößen: SI vs. IEC

| Präfix | Bedeutung | Wert |
|---|---|---|
| Kilobyte (formal korrekt: kB) | SI-Präfix, Basis 1000 | 1.000 Byte |
| Kibibyte (KiB) | IEC-Präfix, Basis 1024 | 1.024 Byte |

🟡 **Stolperstein:** "KB" statt "kB" ist umgangssprachlich weit verbreitet, formal aber nicht korrekt. Dass eine "1 TB"-Festplatte im Dateimanager oft weniger anzeigt, hat zwei Ursachen zusammen: Hersteller rechnen die Kapazität meist **dezimal** (1 TB = 1.000.000.000.000 Byte), während viele Betriebssystem-Anzeigen **binär** rechnen (in 1024er-Schritten) und dabei oft trotzdem mit "GB"/"TB" statt korrekt "GiB"/"TiB" beschriften.

### 3.2 ASCII

**ASCII** (American Standard Code for Information Interchange) definiert 128 Codes mit 7 Bit (`0000000`–`1111111`) – Groß-/Kleinbuchstaben des englischen Alphabets, Ziffern, Satzzeichen und Steuerzeichen. Beispiel: Der Buchstabe `A` hat den Dezimalwert 65, als 7-Bit-Code `1000001₂`. Gespeichert wird ein Zeichen in der Praxis meist in einem vollen 8-Bit-Byte – dabei wird links eine führende Null ergänzt: `01000001₂` = `41₁₆`.

> **Wichtig für die Prüfung:** ASCII reicht **nicht** für Umlaute (ä, ö, ü), Sonderzeichen anderer Sprachen oder Emojis – dafür braucht es eine erweiterte Kodierung. 🔴

### 3.3 Unicode und UTF-8

**Unicode** definiert Codepoints für Zeichen und Symbole aus zahlreichen Schriftsystemen sowie für Steuer-, Formatierungs- und weitere Sonderzeichen. **UTF-8** ist die gebräuchlichste Art, diese Codepoints als Bytes zu speichern: Es ist eine Variable-Länge-Kodierung, die 1 bis 4 Byte **pro Codepoint** verwendet. (Ein für Menschen sichtbares Zeichen kann in seltenen Fällen aus mehreren Codepoints bestehen, z. B. ein Grundbuchstabe plus ein kombinierendes Akzentzeichen – für diesen Artikel nicht weiter vertieft.)

| Zeichenbereich | Beispiele | UTF-8-Länge |
|---|---|---|
| ASCII-Bereich | englische Buchstaben, Ziffern, grundlegende Satz-/Steuerzeichen | 1 Byte |
| Weitere europäische Zeichen | z. B. `ä`, `ö`, `ü` | meist 2 Byte |
| Viele weitere Unicode-Zeichen | z. B. viele chinesische Schriftzeichen | meist 3 Byte |
| Zeichen außerhalb der Basisebene | z. B. viele Emojis | 4 Byte |

> **Wichtig für die Prüfung:** UTF-8 ist **abwärtskompatibel zu ASCII** – jedes gültige ASCII-Zeichen ist in UTF-8 identisch kodiert (1 Byte). Das ist ein wesentlicher Grund für die weite Verbreitung von UTF-8 als Standard im Web. Die tatsächliche Byte-Länge eines Zeichens richtet sich nach seinem Unicode-Codepoint, nicht nach Sprache oder "Exotik" – die Tabelle oben zeigt typische Bereiche, keine feste Regel pro Sprache. 🔴

> **IHK-Typfrage:** *"Warum kann ein deutschsprachiger Text mit Umlauten in UTF-8 mehr Speicherplatz benötigen als ein gleich langer Text, der ausschließlich aus ASCII-Zeichen besteht?"*
> **Musterantwort:** ASCII-Zeichen (Buchstaben ohne Umlaute, Ziffern) benötigen in UTF-8 genau 1 Byte. Zeichen wie ä, ö, ü gehören nicht zum ASCII-Zeichensatz und werden in UTF-8 mit meist 2 Byte kodiert. Ein Text mit vielen Umlauten benötigt deshalb bei gleicher Zeichenanzahl mehr Speicherplatz als ein Text, der ausschließlich aus ASCII-Zeichen besteht.

---

## 4. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
|---|---|---|
| 1 | Hex↔Dual-Umrechnung muss über Dezimal erfolgen | Direkt über 4er-Blöcke (Nibbles) umrechnen – schneller und fehlerärmer |
| 1b | Dezimal↔Hex geht nur über den Umweg Dual | Auch direkt durch fortlaufende Division durch 16 möglich – beide Wege sind gültig |
| 2 | NAND ist nur eine abgeleitete Verknüpfung ohne besondere Bedeutung | NAND (und NOR) sind universelle Gatter – jede Logik lässt sich allein daraus aufbauen |
| 3 | "KB" und "KiB" sind dasselbe | kB = 1.000 Byte (SI), KiB = 1.024 Byte (IEC) – umgangssprachlich wird oft "KB" für beides verwendet |
| 4 | ASCII reicht für alle Texte, die ein Computer speichern muss | ASCII deckt nur 128 Codes ab – Umlaute, andere Schriften und Emojis brauchen Unicode/UTF-8 |
| 5 | UTF-8 verwendet für jedes Zeichen dieselbe Byte-Anzahl | UTF-8 ist eine Variable-Länge-Kodierung (1–4 Byte je nach Codepoint), aber abwärtskompatibel zu ASCII |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Stellenwertsystem | Jede Stelle entspricht einer Potenz der Basis (Dezimal: 10er, Dual: 2er, Hex: 16er) |
| Bit / Byte | Eine Dualstelle = 1 Bit; 8 Bit = 1 Byte |
| Hex↔Dual | 1 Hex-Ziffer = 4 Dualstellen (ein Nibble) – blockweise umrechnen |
| Dezimal↔Hex | Direkt durch/mit 16 möglich, alternativ über Dual als Zwischenschritt |
| AND/OR/NOT/XOR | Grundverknüpfungen der Booleschen Logik bzw. Bitoperationen |
| NAND/NOR | Universelle Gatter – jede Logik daraus aufbaubar |
| kB vs. KiB | 1.000 Byte (SI, formal "kB") vs. 1.024 Byte (IEC, "KiB") |
| ASCII | 7-Bit-Kodierung, 128 Codes: Buchstaben, Ziffern, Satz-/Steuerzeichen |
| UTF-8 | Variable-Länge-Unicode-Kodierung (1–4 Byte je Codepoint), abwärtskompatibel zu ASCII |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
|---|---|---|
| Zahlensystem umrechnen | "Rechnen Sie X in Dual-/Hexadezimalschreibweise um" | Nachvollziehbarer Rechenweg (Divisionsreste bzw. 4er-Blöcke), nicht nur das Endergebnis |
| Wahrheitstabelle erstellen | "Erstellen Sie die Wahrheitstabelle für..." | Alle Eingangskombinationen vollständig auflisten, auch bei zusammengesetzten Ausdrücken |
| Kodierung erklären | "Warum benötigt X mehr Speicherplatz als Y?" | Konkreten Byte-Unterschied nennen, nicht nur "weil es mehr Zeichen sind" |

---

## Merk-Sätze fürs Fachgespräch

> Hex ist keine eigene Maschinensprache – es ist eine für Menschen lesbarere Kurzform für Dualzahlen, vier Bit pro Hex-Ziffer.

> NAND und NOR sind universell: Aus einem einzigen Gattertyp lässt sich jede beliebige Logikschaltung bauen.

> kB und KiB klingen ähnlich, meinen aber unterschiedliche Werte – 1.000 vs. 1.024 Byte.

> UTF-8 ist abwärtskompatibel zu ASCII: ASCII-Zeichen brauchen 1 Byte, andere Unicode-Zeichen je nach Codepoint 2 bis 4 Byte.

---

```yaml
dokument: Zahlensysteme-Boolesche-Logik-wiki-artikel
lernfeld: "Priorität-1-Thema aus Mathe-Prioritätenplan (Part 3 der Serie 'Mathe_Was_Notwendig_ist')"
titel: "Zahlensysteme & Boolesche Logik"
typ: "Typ A – Kompakter Prüfungs-Wiki (FIAE/FISI-übergreifend, IT-Grundlagen mit AP1-Bezug)"
status: final
stand: 2026-09-16
quellen_intern:
  - "Priorität-1-Thema aus dem Mathe-Prioritätenplan. Bewusste, transparent dokumentierte teilweise Überschneidung mit LF2.1 - Die Logik der Maschinen (dort bereits Final, Hardware-/CPU-Rahmung): Auftraggeber hat nach eigener Analyse entschieden, dass eine zusätzliche eigenständige Referenz im Mathe-Ordner trotz Überschneidung sinnvoll ist ('wird auch wenn es eventuell doppelt kein Schaden verursachen'). LF2.1 bleibt Pflegeautorität für Zahlensysteme/Logikgatter bei Widersprüchen."
  - "Echter Mehrwert gegenüber LF2.1: Abschnitt 3 (Daten & Codierung, ASCII/UTF-8) - dieses Thema ist in LF2.1 nicht enthalten, hier erstmals im Wiki abgedeckt"
  - "Querverweis zu Part 2 (Mengenlehre/Dreisatz/De-Morgan) für die dort ausführlich behandelten De-Morgan-Regeln, statt Wiederholung"
quellen_fachlich:
  - titel: "Grundlagen der Zahlensysteme, Booleschen Algebra, ASCII/Unicode/UTF-8"
    herausgeber: "Etabliertes Informatik-Standardwissen"
    status: "Stabile, unstrittige technische Grundlagen - keine gesonderte Web-Verifikation nötig. ASCII (7-Bit, 128 Codes), UTF-8 als Variable-Länge-Kodierung pro Codepoint mit ASCII-Abwärtskompatibilität, SI- vs. IEC-Präfixe (kB=1000 Byte vs. KiB=1024 Byte) sind langjährig etablierte, unveränderte technische Standards"
review_historie:
  - runde: 1
    datum: 2026-09-15
    ergebnis: "Erstdraft erstellt. Bewusst als eigenständige Referenz im Mathe-Ordner konzipiert, trotz inhaltlicher Überschneidung mit dem bereits finalen LF2.1 - auf ausdrücklichen Wunsch des Auftraggebers, der die Dopplung als unschädlich bewertet hat. Um Redundanz nicht komplett unproduktiv zu machen, bewusst ohne Hardware-/CPU-Rahmung (die ist LF2.1s Alleinstellungsmerkmal) und um einen echten neuen Abschnitt (ASCII/UTF-8/Daten & Codierung) erweitert, der im Wiki bisher nirgends vorkommt. Kein Rohmaterial vorhanden - aus eigenem Wissen erstellt."
  - runde: 2
    datum: 2026-09-15
    ergebnis: "3 Reviews eingearbeitet. Wichtigster Fund (alle 3 Reviews unabhängig, als Fachfehler markiert): Die Aussage 'Dezimal↔Hex führt meist kein Weg an einer Zwischenumrechnung vorbei' war schlicht falsch - direkte Division durch 16 funktioniert genauso wie bei Dezimal↔Dual. Neuer Abschnitt 1.5 mit direkter Dezimal→Hex- UND Hex→Dezimal-Umrechnung ergänzt (vorher fehlte Hex→Dezimal komplett, obwohl die Kernfrage explizit 'zwischen allen drei Systemen' verlangte). Nibble-Referenztabelle (0-F) ergänzt. Weitere mehrfach bestätigte Korrekturen: ASCII-Beispiel vermischte 7-Bit-Code und 8-Bit-Byte-Darstellung, jetzt sauber getrennt. UTF-8-Typfrage war logisch inkonsistent ('derselbe Text in reinem ASCII' - Umlaute können dort gar nicht existieren), umformuliert auf Vergleich zwischen zwei verschiedenen Texten. 'Je exotischer das Zeichen'-Merksatz durch Codepoint-basierte Erklärung ersetzt. Tippfehler 'block- weise' behoben. Transistor-Erklärung präzisiert (elektrische Pegel statt vereinfachtem Strom-an/aus-Bild). NAND/NOR-Chipfertigungsaussage entschärft (reale Chips nutzen nicht nur einen Gattertyp). KB/kB-Erklärung präzisiert: zwei getrennte Ursachen (Hersteller rechnet dezimal, OS zeigt binär mit oft falscher Bezeichnung) statt nur 'fälschliche Beschriftung'. AP1-Prüfungsrelevanz-Behauptung vorsichtiger formuliert. Bitoperationen-Abschnitt überarbeitet: NOT-Bitbreiten-Abhängigkeit explizit erklärt, chmod-Beispiel konkretisiert statt pauschaler Behauptung, veraltete redundante Typfrage (Zahlenumrechnung, jetzt in 1.4/1.5 behandelt) durch echte Bitoperationen-Aufgabe ersetzt. '1 Byte = 8 Bit' als fehlende Grundlage ergänzt. Cheatsheet und Prüfungsfallen entsprechend konsistent nachgezogen."
  - runde: 3
    datum: 2026-09-16
    ergebnis: "3 weitere Reviews eingearbeitet (überwiegend Bestätigung von Runde 2, keine neuen Fachfehler gefunden). Größter echter Fund (1 Review, klar begründet): chmod-Erklärung sagte 'Summe der gesetzten Bits' - die Bits selbst sind aber nur 0 oder 1, addiert werden die Stellenwerte (4/2/1). Präzisiert. UTF-8 'pro Zeichen' zu 'pro Codepoint' korrigiert (2 Reviews) - ein sichtbares Zeichen kann aus mehreren Codepoints bestehen, außerdem war das Cheatsheet selbst schon inkonsistent ('je Codepoint') zum Fließtext ('pro Zeichen'). 'Position 1' in der Bitoperations-Musterantwort war mehrdeutig (von links/rechts? bei 0 oder 1 beginnend?) - durch stellenweise Untereinander-Darstellung mit eindeutiger Richtungsangabe ersetzt. Transistor-Erklärung in Abschnitt 2 (Boolesche Logik) war noch nicht an die in Runde 2 bereits präzisierte Fassung in Abschnitt 1 angeglichen - nachgezogen. kB/KB-Schreibweise durchgängig auf formal korrektes 'kB' vereinheitlicht (Merksatz, YAML). ASCII '128 Zeichen' zu '128 Codes' präzisiert (Steuerzeichen sind keine sichtbaren Zeichen). 'Direkter Weg bei größeren Zahlen oft schneller'-Pauschalisierung durch situationsabhängige Empfehlung ersetzt. Zwei Vorschläge (Umbenennung 'IHK-Typfrage' und 'Was die IHK hören will') bewusst nicht übernommen - beides sind feste, projektweit in allen fertigen Wiki-Artikeln dieser Sammlung identisch verwendete Konventionen; eine Änderung nur hier hätte Inkonsistenz geschaffen (dieselbe Begründung wie bereits beim Pseudocode-Artikel in Runde 3 dokumentiert)."
  - runde: 4
    datum: 2026-09-16
    ergebnis: "Eigene Abschlussprüfung: Zwei Reste gefunden - Prüfungsfalle 4 trug noch '128 Zeichen' statt '128 Codes' (überall sonst in Runde 3 korrigiert), YAML-typ-Feld trug noch 'AP1-Grundlagen' obwohl die Prüfungsrelevanz-Aussage im Kopf bereits in Runde 2 bewusst vorsichtiger formuliert wurde ('möglicher Einsatz in AP1'). Beide angeglichen. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 4 Runden (3 externe Prüfrunden + 1 eigene Abschlussprüfung, 2026-09-16) – Freigabe durch Autor:in bestätigt. Part 3 der Serie Mathe_Was_Notwendig_ist."
```