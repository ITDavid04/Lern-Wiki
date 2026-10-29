# TypeScript Einstieg – Von Null auf Grundgerüst

> **Zielgruppe:** Umschüler FIAE/FISI ohne Java- oder TypeScript-Vorerfahrung
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch, Grundlage für LF8
> **Lernzeit:** Ca. 90–120 Minuten (in Etappen machbar)
> **Status:** Draft
> **Stand:** 2026

---

## Wie du dieses Dokument nutzt

Das ist bewusst in **Stufen** aufgebaut. Du musst nicht alles an einem Stück durchziehen:

- **Stufe 1** – absolute Basics, keine Vorkenntnisse nötig
- **Stufe 2** – Bausteine, mit denen du wirklich etwas baust
- **Stufe 3** – die Konzepte, die TypeScript von reinem JavaScript unterscheiden
- **Weiterführung** – wo du danach hinschauen solltest

Mach nach jeder Stufe eine Pause und probiere den Code wirklich aus, bevor du weitermachst. Verstehen kommt durch Tippen, nicht durch Lesen.

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|-------|-----------|
| 1 | Was ist TypeScript und wie unterscheidet es sich von JavaScript? | [→ 0. Was ist TypeScript überhaupt?](#0-was-ist-typescript-überhaupt) |
| 2 | Wie deklariert man Variablen mit Typ in TypeScript? | [→ 1.1 Variablen und Typen](#11-variablen-und-typen) |
| 3 | Wie sieht eine typisierte Funktion aus? | [→ 1.3 Funktionen](#13-funktionen) |
| 4 | Was ist ein Interface und wofür braucht man es? | [→ 2.2 Interfaces](#22-interfaces) |
| 5 | Wie sieht eine einfache Klasse mit Typisierung aus? | [→ 2.3 Klassen](#23-klassen) |

---

## 0. Was ist TypeScript überhaupt?

> TypeScript ist JavaScript – nur mit einer zusätzlichen Kontrollinstanz, die vor dem Ausführen prüft, ob die Daten zusammenpassen.

Stell dir vor, du packst Kisten für einen Umzug. JavaScript sagt: "Pack einfach alles rein, wir sortieren das später am Zielort." TypeScript sagt: "Jede Kiste bekommt vorher ein Schild, was reingehört – und wenn du versuchst, Geschirr in die Bücher-Kiste zu packen, meckert es sofort, bevor der Lkw überhaupt losfährt."

- TypeScript-Dateien enden auf `.ts`
- Der **TypeScript-Compiler** (`tsc`) übersetzt `.ts`-Code in normales `.js`, das der Browser oder Node.js tatsächlich ausführen kann
- Alles, was in reinem JavaScript funktioniert, funktioniert auch in TypeScript – TypeScript kommt nur zusätzlich mit Typangaben

**IHK-Relevanz:** 🔴 – "TypeScript ist ein Superset von JavaScript mit statischer Typprüfung" ist eine Standard-Definitionsfrage.

---

## STUFE 1 – Absolute Basics

### 1.1 Variablen und Typen

In JavaScript/TypeScript gibt es drei Wege, eine Variable anzulegen:

```typescript
let alter: number = 25;        // kann sich später ändern
const name: string = "Alex";   // ändert sich NIE wieder
var veraltet = "bitte nicht";  // alte Schreibweise, meide sie
```

**Merken:** Nutze `const`, wenn sich der Wert nie ändert (Standardfall). Nutze `let`, wenn er sich ändern soll. `var` ist ein Relikt aus alten JavaScript-Zeiten – in der Praxis und Prüfung so gut wie nie die richtige Antwort. 🔴

```typescript
const pi = 3.14159;
pi = 3.14; // ❌ Fehler: Cannot assign to 'pi' because it is a constant
```

Genau das ist der Sinn von `const`: TypeScript verhindert aktiv, dass du den Wert versehentlich später überschreibst.

Die wichtigsten Basis-Typen:

| Typ | Beispielwert | Bedeutung |
|-----|--------------|-----------|
| `number` | `42`, `3.14` | Zahlen (Ganzzahl und Kommazahl sind derselbe Typ) |
| `string` | `"Hallo"` | Text |
| `boolean` | `true` / `false` | Wahrheitswert |
| `any` | beliebig | „Egal welcher Typ" – **vermeiden**, hebt die Typprüfung auf |

```typescript
let temperatur: number = 21.5;
let stadtname: string = "Hamburg";
let istAktiv: boolean = true;
```

**Wichtig zu verstehen:** Du musst den Typ oft gar nicht hinschreiben. TypeScript erkennt ihn meistens selbst (**Typ-Inferenz**):

```typescript
let temperatur = 21.5;  // TypeScript weiß: das ist eine number
```

Beide Varianten (mit und ohne `: number`) sind korrekt. Explizite Typangaben sind vor allem bei Funktionsparametern und bei leeren Variablen ohne Startwert sinnvoll.

**IHK-Relevanz:** 🔴 – Typ-Inferenz vs. explizite Typangabe ist ein beliebter Prüfungspunkt.

---

### 1.2 Ausgaben und einfache Kontrollstrukturen

Etwas auf der Konsole ausgeben:

```typescript
console.log("Hallo Welt");
console.log(temperatur);
```

Bedingungen – funktionieren wie in fast jeder Sprache:

```typescript
if (temperatur > 25) {
  console.log("Es ist warm");
} else if (temperatur > 15) {
  console.log("Es ist mild");
} else {
  console.log("Es ist kalt");
}
```

Schleifen:

```typescript
// Zählschleife
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// Solange-Schleife
let zaehler = 0;
while (zaehler < 3) {
  console.log("Durchlauf", zaehler);
  zaehler++;
}
```

**Merken:** Blöcke werden immer mit `{ }` markiert, nicht durch Einrückung (anders als bei Python). Die Einrückung selbst ist rein kosmetisch – sie hilft dir beim Lesen, ändert aber nichts an der Logik. 🟡

---

### 1.3 Funktionen

Eine Funktion ist ein wiederverwendbares Stück Code, das Eingaben (Parameter) nimmt und etwas zurückgibt.

```typescript
function addiere(a: number, b: number): number {
  return a + b;
}

const ergebnis = addiere(3, 5); // ergebnis = 8
```

Lesart: `a: number, b: number` sind die Parameter mit ihren Typen. `: number` nach der Klammer ist der **Rückgabetyp** – was die Funktion am Ende zurückgibt.

Kurzschreibweise (Arrow Function) – macht genau dasselbe:

```typescript
const addiere = (a: number, b: number): number => {
  return a + b;
};
```

Funktion ohne Rückgabewert (z. B. nur eine Ausgabe):

```typescript
function begruesse(name: string): void {
  console.log(`Hallo, ${name}!`);
}
```

`void` bedeutet: "Diese Funktion gibt nichts zurück." Das `` `Hallo, ${name}!` `` ist ein **Template String** – Text mit eingebauten Variablen, erkennbar an den Backticks `` ` `` statt normaler Anführungszeichen.

**IHK-Relevanz:** 🔴 – Parametertypen, Rückgabetyp und `void` sind Standard-Klausurfragen.

### 1.4 Entscheidungshilfe: Was nehme ich wann?

| Ich will... | Dann nehme ich... |
|--------------|-------------------|
| Einen Wert, der sich nie wieder ändert | `const` |
| Einen Zähler oder eine Variable, die sich ändern soll | `let` |
| Eine Funktion, die etwas zurückgibt | Rückgabetyp angeben (z. B. `: number`) |
| Eine Funktion, die nur etwas ausführt (z. B. eine Ausgabe) | `void` als Rückgabetyp |

Diese kleine Tabelle beantwortet die häufigsten "was nehme ich hier"-Fragen aus Stufe 1 in einem Blick.

---

## STUFE 2 – Bausteine für echte Programme

### 2.1 Arrays und Objekte

Ein Array ist eine Liste von Werten desselben Typs:

```typescript
let zahlen: number[] = [1, 2, 3, 4];
let namen: string[] = ["Anna", "Ben", "Cem"];

zahlen.push(5);           // fügt 5 hinzu
console.log(zahlen[0]);   // gibt 1 aus – Zählung startet bei 0!
```

Ein Objekt bündelt zusammengehörige Daten unter einem Namen:

```typescript
let person = {
  name: "Alex",
  alter: 30,
  istAktiv: true,
};

console.log(person.name); // "Alex"
```

**IHK-Relevanz:** 🟡 – Array-Grundlagen und Zugriff über Index sind Basiswissen, aber selten allein Prüfungsschwerpunkt.

---

### 2.2 Interfaces

> Ein Interface ist ein Vertrag: Es legt fest, welche Eigenschaften ein Objekt haben MUSS – ohne selbst Code auszuführen.

Das Problem ohne Interface: Bei jedem `person`-Objekt müsstest du die Struktur neu hinschreiben und TypeScript kann nicht prüfen, ob du etwas vergessen hast. Mit Interface:

```typescript
interface Person {
  name: string;
  alter: number;
  istAktiv: boolean;
}

const alex: Person = {
  name: "Alex",
  alter: 30,
  istAktiv: true,
};
```

Wenn jetzt eine Eigenschaft fehlt oder der falsche Typ drinsteht, meldet TypeScript sofort einen Fehler – noch bevor der Code läuft. Genau das ist der Kernvorteil gegenüber JavaScript.

Ein Interface kann auch als Bauplan für Funktionsparameter dienen:

```typescript
function zeigePerson(p: Person): void {
  console.log(`${p.name} ist ${p.alter} Jahre alt`);
}
```

**IHK-Relevanz:** 🔴 – "Was ist ein Interface und wofür wird es genutzt?" ist eine der häufigsten Fachgespräch-Fragen zu TypeScript.

*(→ siehe Abschnitt 2.3 für Klassen – dort werden Interfaces oft als Bauplan für Objekte verwendet, die eine Klasse erzeugt)*

---

### 2.3 Klassen

> Eine Klasse ist ein Bauplan, aus dem du beliebig viele konkrete Objekte (Instanzen) erzeugen kannst – inklusive eigener Methoden (Funktionen, die zur Klasse gehören).

```typescript
class Auto {
  marke: string;
  tempo: number = 0;

  constructor(marke: string) {
    this.marke = marke;
  }

  beschleunigen(): void {
    this.tempo += 10;
    console.log(`${this.marke} fährt jetzt ${this.tempo} km/h`);
  }
}

const meinAuto = new Auto("VW");
meinAuto.beschleunigen(); // "VW fährt jetzt 10 km/h"
meinAuto.beschleunigen(); // "VW fährt jetzt 20 km/h"
```

Begriffe zum Merken:

| Begriff | Bedeutung |
|---------|-----------|
| `class` | Definiert den Bauplan |
| `constructor` | Läuft automatisch ab, wenn ein neues Objekt erzeugt wird (`new Auto(...)`) |
| `this` | Verweis auf "das aktuelle Objekt selbst" |
| Instanz | Ein konkretes Objekt, das aus der Klasse erzeugt wurde (hier: `meinAuto`) |
| Methode | Eine Funktion, die zu einer Klasse gehört (hier: `beschleunigen`) |

**Kurzschreibweise** – Zugriffsmodifizierer direkt im Constructor, sehr verbreitet in echtem TypeScript-Code. Es gibt zwei Varianten, je nachdem ob die Eigenschaft von außen sichtbar sein soll:

```typescript
// Mit "public" – Eigenschaften bleiben von außen sichtbar/veränderbar (Standardverhalten)
class Auto {
  constructor(public marke: string, public tempo: number = 0) {}
}

// Mit "private" – Eigenschaften sind NUR innerhalb der Klasse sichtbar
class Auto {
  constructor(private marke: string, private tempo: number = 0) {}

  beschleunigen(): void {
    this.tempo += 10;
  }
}
```

Beide Schreibweisen sind eine Abkürzung für die Langform von oben – TypeScript legt automatisch die Eigenschaft an und weist im Constructor den Wert zu, ohne dass du `this.marke = marke;` selbst schreiben musst.

**Merken:** `public` ist auch die Voreinstellung – lässt du den Modifizierer ganz weg, ist die Eigenschaft trotzdem öffentlich sichtbar. `private` schreibt man nur explizit dazu, wenn man bewusst Datenkapselung will. 🟡

**IHK-Relevanz:** 🔴 – Klassen, `constructor` und `this` sind Kernstoff, gerade weil objektorientierte Konzepte in fast jedem Lernfeld wiederkehren.

---

## STUFE 3 – Was TypeScript besonders macht

### 3.1 Union Types – mehr als ein möglicher Typ

Manchmal darf ein Wert mehrere Typen annehmen:

```typescript
function zeigeId(id: number | string): void {
  console.log(`Die ID ist: ${id}`);
}

zeigeId(42);      // erlaubt
zeigeId("A123");  // auch erlaubt
```

Das `|` bedeutet "oder". `id` darf entweder eine `number` oder ein `string` sein – aber nichts anderes.

**IHK-Relevanz:** 🟡 – Union Types tauchen zunehmend in modernem TypeScript-Code auf, sind aber (noch) kein AP1-Kernstoff.

### 3.2 Optionale Eigenschaften

Mit einem `?` markierst du, dass eine Eigenschaft nicht zwingend vorhanden sein muss:

```typescript
interface Person {
  name: string;
  alter: number;
  spitzname?: string; // optional
}

const bob: Person = { name: "Bob", alter: 40 }; // gültig, auch ohne spitzname
```

**IHK-Relevanz:** 🟡 – nützlich zu kennen, kommt im Fachgespräch häufiger vor als in der Klausur.

### 3.3 Strukturelle Typisierung (Kurzfassung)

> TypeScript fragt nicht "wie heißt der Typ", sondern "hat das Objekt die richtige Form".

```typescript
interface Punkt {
  x: number;
  y: number;
}

function zeigeAbstand(p: Punkt): void {
  console.log(Math.sqrt(p.x ** 2 + p.y ** 2));
}

// Funktioniert, obwohl "koordinate" nie als Punkt deklariert wurde:
const koordinate = { x: 3, y: 4 };
zeigeAbstand(koordinate);
```

Solange die Form (die Eigenschaften) passt, akzeptiert TypeScript das Objekt – unabhängig vom ursprünglichen Namen. Das nennt man **strukturelle Typisierung** oder "Duck Typing, nur schon vor der Ausführung geprüft".

**IHK-Relevanz:** 🔴 – ein Kernkonzept, das TypeScript von klassisch-typisierten Sprachen wie Java unterscheidet.

---

## Mini-Projekt: Bücherverwaltung

Jetzt kommen alle Bausteine aus Stufe 1–3 zusammen: Interface, Klasse mit `private`-Eigenschaft, Array, Methode, Template String und eine optionale Eigenschaft.

```typescript
// 📝 Zum Selbst-Abtippen und Ausprobieren:

interface Buch {
  titel: string;
  autor: string;
  seiten: number;
  gelesen?: boolean; // optional – siehe Stufe 3.2
}

class Bibliothek {
  private buecher: Buch[] = [];

  hinzufuegen(buch: Buch): void {
    this.buecher.push(buch);
  }

  listeAnzeigen(): void {
    this.buecher.forEach((b) =>
      console.log(`${b.titel} von ${b.autor} (${b.seiten} Seiten)`)
    );
  }
}

// Ausprobieren:
const meineBib = new Bibliothek();
meineBib.hinzufuegen({ titel: "TypeScript Basics", autor: "Max Mustermann", seiten: 200 });
meineBib.hinzufuegen({ titel: "Clean Code", autor: "Robert C. Martin", seiten: 464, gelesen: true });
meineBib.listeAnzeigen();
```

**Was hier aus welcher Stufe steckt:**

| Baustein | Stufe |
|----------|-------|
| `interface Buch` | 2.2 |
| `class Bibliothek`, `private buecher` | 2.3 |
| `Buch[]` (Array) | 2.1 |
| `hinzufuegen(buch: Buch): void` | 1.3 |
| `gelesen?: boolean` | 3.2 |
| `` `${b.titel} von ${b.autor}` `` | 1.3 (Template String) |

**Aufgabe zum Selbst-Üben:** Ergänze eine Methode `anzahlUngelesen(): number`, die zählt, wie viele Bücher noch kein `gelesen: true` haben. Nutze dafür `this.buecher.filter(...)`.

---

## Selbsttest

| # | Frage | Kurzantwort |
|---|-------|-------------|
| 1 | Was ist der Unterschied zwischen `let` und `const`? | `let` erlaubt spätere Änderung des Werts, `const` nicht |
| 2 | Was bedeutet `: void` nach einem Funktionskopf? | Die Funktion gibt keinen Wert zurück |
| 3 | Was macht ein Interface? | Legt fest, welche Eigenschaften/Typen ein Objekt haben muss – ohne selbst Code auszuführen |
| 4 | Wofür steht `this` in einer Klasse? | Verweis auf das aktuelle Objekt (die Instanz) selbst |
| 5 | Was bedeutet `id: number \| string`? | `id` darf entweder eine number oder ein string sein |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---------|-----------------|
| `tsc` | TypeScript-Compiler, übersetzt `.ts` zu `.js` und prüft Typen |
| Typ-Inferenz | TypeScript erkennt den Typ automatisch, ohne explizite Angabe |
| Interface | Vertrag, der die Struktur eines Objekts festlegt |
| Klasse | Bauplan für Objekte (Instanzen), kann Zustand und Methoden enthalten |
| Constructor | Methode, die beim Erzeugen einer neuen Instanz automatisch läuft |
| Union Type | Ein Typ, der mehrere mögliche Typen zulässt (`number \| string`) |
| Strukturelle Typisierung | „Passende Form = passender Typ", unabhängig vom Namen |
| `any` | Hebt die Typprüfung auf – in echtem Code und Prüfung möglichst vermeiden |

---

## Merk-Sätze für die mündliche Prüfung

> TypeScript ist JavaScript plus eine Typprüfung, die vor der Ausführung greift.

> `const` ist der Normalfall, `let` nur wenn sich der Wert wirklich ändern soll.

> Ein Interface prüft nur die Form eines Objekts – es führt selbst keinen Code aus.

> TypeScript prüft strukturell: Wenn die Form passt, ist der Typ egal, wie das Objekt ursprünglich genannt wurde.

---

## Weiterführung – wo es nach diesem Grundgerüst weitergeht

Wenn Stufe 1–3 sitzen, sind das die nächsten sinnvollen Themen (baut direkt darauf auf):

1. **Generics** (`<T>`) – Funktionen/Klassen, die mit beliebigen Typen arbeiten können
2. **Vererbung** (`extends`) – Klassen, die Eigenschaften/Methoden einer anderen Klasse übernehmen
3. **Enums** – benannte Konstanten-Gruppen (z. B. Status: `Aktiv`, `Inaktiv`, `Gesperrt`)
4. **async/await** – Umgang mit asynchronem Code (z. B. Daten von einer API laden)
5. **MVC/MTV-Architekturvergleich** – siehe dein bestehendes Wiki-Dokument "Python vs. TypeScript & MVC-Architekturen" – dort baut das Model-View-Controller-Beispiel direkt auf Klassen aus Abschnitt 2.3 auf

**Praktischer Tipp:** Installiere dir lokal Node.js und probiere die Codebeispiele selbst aus, statt nur zu lesen. Für die Prüfungsvorbereitung reicht das – du brauchst kein komplettes Framework-Setup, um diese Basics zu verinnerlichen.

**Setup in 3 Schritten** (Node.js muss bereits installiert sein):

```bash
npm init -y
npm install typescript ts-node --save-dev
npx ts-node deinedatei.ts
```

Damit kannst du jede `.ts`-Datei direkt ausführen, ohne den Kompilierungsschritt (`tsc`) manuell aufzurufen – `ts-node` macht das intern für dich (siehe dazu auch dein bestehendes MVC-Dokument, Abschnitt 1, zur Rolle von `ts-node`/Bun/Deno).

---

```yaml
titel: "TypeScript Einstieg – Von Null auf Grundgerüst"
typ: "A"
lernfeld: "LF8-Vorbereitung"
stichworte: [TypeScript, Basics, Einstieg, Variablen, Funktionen, Klassen, Interfaces]
zielgruppe: "ohne Java-/TypeScript-Vorerfahrung"
status: draft
stand: 2026
```
