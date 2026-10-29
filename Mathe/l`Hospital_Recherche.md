# L’Hospitalsche Regel (IT-Umschulung FIAE/FISI, 2. Lehrjahr)

## 1. Worum geht’s?

Die **L’Hospitalsche Regel** hilft dir, **Grenzwerte von Brüchen** zu berechnen, wenn beim Einsetzen etwas *Unbestimmtes* herauskommt, z. B.:

- 0/0  
- ∞/∞

Dann darfst du statt des ursprünglichen Bruchs **die Ableitungen** von Zähler und Nenner benutzen.

**Grundidee:**

```
lim   f(x)/g(x)  (mit Form 0/0 oder ∞/∞)  =  lim   f'(x)/g'(x)
x→a                                         x→a
```
sofern der rechte Grenzwert existiert (endlich oder uneigentlich +∞ bzw. –∞).  
Andernfalls kann die Regel keine Aussage treffen.

---

## 2. Einfache Erklärung (ohne Fachchinesisch)

Du willst wissen:

> Wie verhält sich das Verhältnis zweier Größen, wenn die Eingabe gegen einen bestimmten Wert geht?

**IT-Analogie (FIAE/FISI):**

- f(x): Anzahl der Operationen eines Algorithmus bei Eingabegröße x  
- g(x): Eingabegröße x selbst

Du kennst aus der **O-Notation**, dass dich oft interessiert, wie schnell die Operationen im Vergleich zur Eingabe wachsen.

In der Algorithmik ist meist das asymptotische Verhalten x → ∞ mit der Form ∞/∞ relevant.  
Der Fall 0/0 kann auftreten, wenn die Funktionen bei x = 0 beide den Wert null haben.

Statt auf die Werte von f und g zu schauen, betrachtest du ihre **Änderungsraten**:

- Wie schnell wächst f(x)? → Ableitung f'(x)  
- Wie schnell wächst g(x)? → Ableitung g'(x)

Die L’Hospital-Regel sagt:  
Wenn der ursprüngliche Bruch unbestimmt ist, darfst du den Grenzwert des Bruchs der **Änderungsraten** f'(x)/g'(x) verwenden.

---

## 3. Wann darf ich L’Hospital benutzen?

Du darfst L’Hospital verwenden, wenn:

1. Du betrachtest einen Grenzwert eines **Bruchs**:
   ```
   lim   f(x)/g(x)
   x→a
   ```

2. Beim Einsetzen von x = a entsteht:
   - 0/0 oder  
   - ∞/∞

3. f und g sind in einer Umgebung von a **differenzierbar**, und **g'(x) ≠ 0** in dieser Umgebung (außer eventuell im Punkt a selbst).

Dann gilt:

```
lim   f(x)/g(x)  =  lim   f'(x)/g'(x)
x→a                 x→a
```

**Wichtige Präzisierung:**  

- Der Grenzwert von f'(x)/g'(x) muss **existieren** – entweder als endliche Zahl oder uneigentlich als +∞ oder –∞.  
- Existiert er nicht (und geht auch nicht gegen ±∞), kann L’Hospital **keine Aussage** über den ursprünglichen Grenzwert machen.  
- Der ursprüngliche Grenzwert **kann trotzdem existieren**  
  (Beispiel: `lim_{x→∞} (x + sin x)/x = 1`, aber `lim_{x→∞} (1 + cos x)/1` existiert nicht und geht auch nicht gegen ±∞).

---

## 4. Schritt-für-Schritt-Rezept

1. **Grenzwert aufschreiben**
   ```
   lim   f(x)/g(x)
   x→a
   ```

2. **Probe: Einsetzen**
   - Setze x = a in Zähler und Nenner ein.  
   - Prüfe, ob 0/0 oder ∞/∞ entsteht.

3. **Ableiten**
   - Berechne f'(x).  
   - Berechne g'(x).

4. **Neuen Grenzwert berechnen**
   ```
   lim   f'(x)/g'(x)
   x→a
   ```

5. Falls der neue Grenzwert wieder eine unbestimmte Form liefert → **Regel erneut anwenden** (nach Prüfung, dass weiterhin g'(x) ≠ 0 in der Umgebung gilt) oder ggf. andere Methoden (Umformen, Kürzen) nutzen.

---

## 5. Praktische Aufgaben zum Selbsttesten

> **Hinweis:**  
> Erst alle Aufgaben **selbst rechnen**, dann unten im Lösungsabschnitt vergleichen.

### Aufgabe 1 (Basis, Trigonometrie)

Berechne:
```
lim   sin x / x
x→0
```

---

### Aufgabe 2 (Polynom-Bruch, ∞/∞; zwei Wege)

Berechne:
```
lim   (4x² – 1) / (2x² + 3)
x→∞
```

Versuche **zwei Lösungswege**:

1. Mit L’Hospital.  
2. Ohne L’Hospital, indem du Zähler und Nenner durch x² teilst.

---

### Aufgabe 3 (zweimal L’Hospital)

Berechne:
```
lim   (1 – cos x) / x²
x→0
```

---

### Aufgabe 4 (Exponentialfunktion)

Berechne:
```
lim   (eˣ – 1) / x
x→0
```

---

### Aufgabe 5 (Logarithmus, ∞/∞)

Berechne:
```
lim   ln x / x
x→∞
```

---

## 6. Wissenswerte Sidefacts (IHK-Relevanz: ROT / GELB / GRÜN)

> **Legende:**  
> **ROT** = sehr wichtig für IHK (hochrelevant)  
> **GELB** = mittelwichtig (hilfreich, aber selten direkt abgefragt)  
> **GRÜN** = nice to know (gut fürs Verständnis)

- **ROT:** Sauberes Ableiten ist Pflicht  
  - Ohne richtige Ableitung bringt dir L’Hospital nichts.  
  - Wichtige Standard-Ableitungen:
    - (xⁿ)' = n·xⁿ⁻¹  
    - (eˣ)' = eˣ  
    - (ln x)' = 1/x  
    - (sin x)' = cos x  
    - (cos x)' = –sin x

- **ROT:** Umgang mit Grenzwerten  
  - Grenzwerte sind Basis für Wachstumsverhalten von Funktionen, Laufzeitabschätzungen etc.  
  - Kommt indirekt in vielen Aufgaben vor (Funktionsverläufe, Extremwerte, Konvergenz).

- **GELB:** Erkennen unbestimmter Formen  
  - Du solltest sicher entscheiden können:
    - *Unbestimmt*: 0/0, ∞/∞  
    - *Nicht unbestimmt*: z. B. 2/0 (Polstelle), ∞/5 (Grenzwert = ∞).

- **GELB:** Mehrfaches Anwenden  
  - In komplexeren Aufgaben kann die Regel **mehrmals** benötigt werden.  
  - Gut, um bei Analysis-Aufgaben in der Prüfung zu punkten.

- **GRÜN:** Verbindung zur O-Notation / Algorithmik  
  - Grenzwerte helfen zu verstehen, welche Funktion „schneller wächst“ (z. B. ln x vs. x, x² vs. eˣ).  
  - Das ist eng verwandt mit dem, was du beim Vergleich von Laufzeiten O(log n), O(n), O(n²) machst.

- **GRÜN:** Historischer Hintergrund  
  - Benannt nach Guillaume de l’Hospital (französischer Mathematiker), Idee stammt von Johann Bernoulli.

---

## 7. Typische Fehler (Prüfungsfallen)

- **Fehler 1: L’Hospital angewendet ohne unbestimmte Form**  
  Beispiel: `lim_{x→1} x²/x = 1/1 = 1`  
  → direkt ausrechnen, keine L’Hospital-Regel nötig.  
  **Relevanz:** **GELB**

- **Fehler 2: Ableitung falsch oder unvollständig**  
  - Ein kleiner Ableitungsfehler zerstört das Ergebnis.  
  - Besonders wichtig bei eˣ, ln x, sin x, cos x.  
  **Relevanz:** **ROT**

- **Fehler 3: L’Hospital als „Wahrheitsmaschine“ missverstanden**  
  - Wenn der Grenzwert von f'(x)/g'(x) **nicht existiert** (und auch nicht uneigentlich ±∞ ist), kann L’Hospital **keine Aussage** über den ursprünglichen Grenzwert machen.  
  - Der ursprüngliche Grenzwert kann trotzdem existieren.  
    Beispiel: `lim_{x→∞} (x + sin x)/x = 1`, aber `lim_{x→∞} (1 + cos x)/1` existiert nicht (und geht auch nicht gegen ±∞).  
  **Relevanz:** **GELB**

---

## 8. Lösungen zu den Aufgaben (Kontrolle)

> **Empfehlung:** Erst wirklich selbst rechnen, dann hier vergleichen.

### Lösung zu Aufgabe 1

```
lim   sin x / x
x→0
```

1. Einsetzen: sin 0 = 0, x = 0 → 0/0.  
2. Ableiten:
   - f(x) = sin x ⇒ f'(x) = cos x  
   - g(x) = x ⇒ g'(x) = 1

```
lim   sin x / x  =  lim   cos x / 1  =  cos 0  =  1
x→0                x→0
```

**Ergebnis:** **1**

---

### Lösung zu Aufgabe 2

```
lim   (4x² – 1) / (2x² + 3)
x→∞
```

**Weg 1: L’Hospital**

1. Für x → ∞: Zähler → ∞, Nenner → ∞ → ∞/∞.  
2. Ableiten:
   - f(x) = 4x² – 1 ⇒ f'(x) = 8x  
   - g(x) = 2x² + 3 ⇒ g'(x) = 4x

```
lim   (4x² – 1) / (2x² + 3)  =  lim   8x / 4x
x→∞                            x→∞
```

Da x ≠ 0 (und x → ∞), kürzt sich x heraus:

```
8x / 4x = 8/4 = 2
```

Also:

```
lim   8x / 4x  =  2
x→∞
```

**Weg 2: Ohne L’Hospital (durch x² teilen)**

```
(4x² – 1) / (2x² + 3)  =  (4 – 1/x²) / (2 + 3/x²)
```

Für x → ∞ gilt 1/x² → 0, also:

```
lim   (4 – 0) / (2 + 0)  =  4/2  =  2
x→∞
```

**Ergebnis:** **2**

---

### Lösung zu Aufgabe 3

```
lim   (1 – cos x) / x²
x→0
```

1. Einsetzen: 1 – cos 0 = 0, x² = 0 → 0/0.  
2. Erste Ableitung:
   - f(x) = 1 – cos x ⇒ f'(x) = sin x  
   - g(x) = x² ⇒ g'(x) = 2x

```
lim   (1 – cos x) / x²  =  lim   sin x / (2x)
x→0                      x→0
```

Einsetzen: sin 0 = 0, 2·0 = 0 → wieder 0/0.

3. Zweite Ableitung:
   - sin x ⇒ cos x  
   - 2x ⇒ 2

```
lim   sin x / (2x)  =  lim   cos x / 2  =  cos 0 / 2  =  1/2
x→0                   x→0
```

**Ergebnis:** **1/2**

---

### Lösung zu Aufgabe 4

```
lim   (eˣ – 1) / x
x→0
```

1. Einsetzen: e⁰ – 1 = 0, x = 0 → 0/0.  
2. Ableiten:
   - f(x) = eˣ – 1 ⇒ f'(x) = eˣ  
   - g(x) = x ⇒ g'(x) = 1

```
lim   (eˣ – 1) / x  =  lim   eˣ / 1  =  e⁰  =  1
x→0                   x→0
```

**Ergebnis:** **1**

---

### Lösung zu Aufgabe 5

```
lim   ln x / x
x→∞
```

1. Für x → ∞: ln x → ∞, x → ∞ → ∞/∞.  
2. Ableiten:
   - f(x) = ln x ⇒ f'(x) = 1/x  
   - g(x) = x ⇒ g'(x) = 1

```
lim   ln x / x  =  lim   (1/x) / 1  =  lim   1/x  =  0
x→∞               x→∞                 x→∞
```

**Ergebnis:** **0**
```