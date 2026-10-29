# LF8.1: Client-Server-Architektur & OOP Design Patterns

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1; mögliche Transferfragen in AP2 und Fachgespräch
> **Lernzeit:** Ca. 90–120 Min. reines Lesen/Wiederholen, 150–210 Min. mit Codeübungen
> **Status:** Final
> **Stand:** 2026

## 📋 IHK-Kernfragen

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was unterscheidet imperative von deklarativen Programmierparadigmen? | [→ 1. Paradigmen & MVC](#1-programmierparadigmen-client-server--mvc) |
| 2 | Wie funktioniert das MVC-Pattern und warum entkoppelt es Daten von Darstellung? | [→ 1. Paradigmen & MVC](#1-programmierparadigmen-client-server--mvc) |
| 3 | Welche wichtigen Security-Design-Prinzipien gibt es und wie wirken sie im Zusammenspiel? | [→ 2. Security-by-Design](#2-security-by-design--software-planung) |
| 4 | Was unterscheidet `interface`, `abstract class` und `class` in TypeScript strukturell? | [→ 3. OOP-Grundlagen TS](#3-objektorientierte-typescript-grundlagen) |
| 5 | Wie funktionieren Singleton- und Observer-Pattern und wofür setzt man sie ein? | [→ 4. Design Patterns](#4-design-patterns--polymorphismus) |

---

## 1. Programmierparadigmen, Client-Server & MVC

> **Grundprinzip:** Ein Programmierparadigma bestimmt, *wie* man ein Problem in Code übersetzt – nicht *was* das Problem ist.

### 1.1 Programmierparadigmen im Überblick

Wie in der Gärtnerei ein Beet entweder Schritt-für-Schritt nach Anweisung bepflanzt wird (imperativ: "grab hier, pflanz das") oder nach dem gewünschten Endergebnis geplant wird ("ich will hier eine blühende Fläche" – wie das erreicht wird, entscheidet der Gärtner situativ, deklarativ), kann man für eine grundlegende Einordnung zwischen imperativen und deklarativen Ansätzen unterscheiden. Die meisten realen Sprachen sind aber **multiparadigmatisch** – TypeScript etwa unterstützt objektorientierte, imperative und funktionale Stile gleichzeitig.

```text
                  [ Programmierparadigmen ]
                 /                         \
     [ Imperativ ]                          [ Deklarativ ]
     (Wie wird es gelöst?)                  (Was wird gelöst?)
     /        |       \                     /         \
[Strukturiert][Prozedural][OOP]     [Funktional]  [Logisch]
```

| Aspekt | Beschreibung | IHK-Relevanz |
| --- | --- | --- |
| **Strukturiert** | Verzicht auf `goto`, klare Kontrollstrukturen (`if/else`, Schleifen) | 🟡 Kontextwissen |
| **Prozedural** | Aufteilung in wiederverwendbare Funktionen/Prozeduren (z. B. C) | 🟡 Kontextwissen |
| **Objektorientiert (OOP)** | Strukturierung nach realen Objekten mit Attributen + Methoden | 🔴 Prüfungsstoff |
| **Funktional** | Berechnung durch Auswertung und Komposition von Funktionen, bevorzugt reine Funktionen (Ergebnis hängt nur von Eingaben ab) und unveränderliche Daten (z. B. Haskell) | 🟡 Kontextwissen |
| **Logisch** | Regelbasierte Fakten-Datenbank, Inferenzmaschine löst Anfragen (z. B. Prolog) | 🟢 Nice to know |

> **IHK-Typfrage:** *"Nennen Sie ein imperatives und ein deklaratives Paradigma und je eine passende Sprache."*
> **Musterantwort:** Imperative Programme beschreiben überwiegend die einzelnen Verarbeitungsschritte zur Lösung eines Problems – z. B. Objektorientierung in Java/TypeScript. Deklarative Programme beschreiben primär das gewünschte Ergebnis, die konkrete Ausführung bleibt dem System überlassen – ein für die Prüfung besonders eingängiges Beispiel ist **SQL** ("Was ich will" statt "Wie ich es hole").

### 1.2 Client-Server-Modell & die 6 REST-Constraints

**Client-Server-Modell (allgemein):** Der Client fordert über eine definierte Schnittstelle Dienste oder Ressourcen an, der Server verarbeitet die Anfrage und stellt eine Antwort bereit. Beide Rollen können unabhängig voneinander entwickelt und betrieben werden. Ein Client muss dabei keine grafische Oberfläche besitzen – auch ein Kommandozeilenprogramm, ein anderer Server oder ein IoT-Gerät kann Client sein.

**REST** ist darauf aufbauend **ein Architekturstil** für verteilte Systeme, der das Client-Server-Modell um weitere Bedingungen ergänzt – nicht jede Web-API ist automatisch REST-konform. Die 6 REST-Constraints nach Fielding:

| # | Constraint | Beschreibung | IHK-Relevanz |
| --- | --- | --- | --- |
| 1 | **Client-Server-Modell** | Strikte Trennung der Verantwortlichkeiten zwischen Anfragendem und Anbieter | 🔴 Prüfungsstoff |
| 2 | **Statelessness** | Jede Anfrage enthält alle zu ihrer Verarbeitung nötigen Infos; der Server braucht keinen zwischen Requests gespeicherten Client-Sitzungskontext | 🔴 Prüfungsstoff |
| 3 | **Caching** | Antworten müssen als cachebar/nicht-cachebar deklariert sein | 🟡 Kontextwissen |
| 4 | **Uniform Interface** | Einheitlicher Zugriff: Ressourcen-Identifikation, Manipulation über Repräsentationen, selbstbeschreibende Nachrichten, Hypermedia als Zustandssteuerung (HATEOAS) – HTTP-Verben (`GET`/`POST`/`PUT`/`DELETE`) sind nur die praktische Umsetzung davon | 🔴 Prüfungsstoff |
| 5 | **Layered System** | Client weiß nicht, ob er direkt mit dem Endserver oder einem Proxy spricht | 🟡 Kontextwissen |
| 6 | **Code on Demand** (optional) | Server kann ausführbaren Code (z. B. JS) an Client senden | 🟢 Nice to know |

**Wichtige HTTP-Statuscodes** (praktische Umsetzung des Uniform Interface):

| Code | Bedeutung | Typischer Einsatz |
| --- | --- | --- |
| 200 OK | Erfolg | `GET` erfolgreich |
| 201 Created | Ressource erstellt | `POST` erfolgreich |
| 400 Bad Request | Fehlerhafte Anfrage/Eingabe | Validierung fehlgeschlagen |
| 401 Unauthorized | Nicht authentifiziert | Kein/ungültiges Auth-Token |
| 403 Forbidden | Authentifiziert, aber keine Berechtigung | Fehlende Rolle/Rechte |
| 404 Not Found | Ressource nicht vorhanden | `GET` mit ungültiger ID |
| 500 Internal Server Error | Server-seitiger Fehler | Unerwarteter Backend-Fehler |

> **IHK-Typfrage:** *"Welchen Vorteil bietet Statelessness für die Skalierbarkeit eines Servers?"*
> **Musterantwort:** Da der Server keinen Client-Sitzungskontext zwischen Anfragen vorhalten muss, kann jede Anfrage von einer beliebigen Serverinstanz bearbeitet werden – das erleichtert Lastverteilung (Load Balancing) und horizontale Skalierung erheblich. **Achtung Verwechslungsgefahr:** Stateless heißt nicht "keine Daten speichern" – Ressourcen- und Datenbankzustände dürfen selbstverständlich serverseitig persistiert werden, nur eben kein Client-Sitzungszustand.

### 1.3 Das MVC-Pattern (Model-View-Controller)

```text
      +-----------------+
      |   Controller    | <----+ (Nutzereingabe)
      +-----------------+      |
        |             |        |
(aktualisiert)     (wählt aus) |
        v             v        |
  +-----------+     +--------+ |
  |   Model   |     |  View  | -+
  +-----------+     +--------+
```

| Komponente | Aufgabe | IHK-Relevanz |
| --- | --- | --- |
| **Model** | Datenstrukturen, Zustand, Geschäftslogik – unabhängig von der Darstellung | 🔴 Prüfungsstoff |
| **View** | Präsentiert Daten in der UI, fragt sie (in)direkt vom Model ab | 🔴 Prüfungsstoff |
| **Controller** | Nimmt Nutzereingaben entgegen, validiert sie, manipuliert das Model, wählt die View | 🔴 Prüfungsstoff |

**Security-Vorteil:** Die Trennung der Verantwortlichkeiten erleichtert es, Sicherheitsprüfungen gezielt zu platzieren – der Controller kann syntaktische Eingaben prüfen und Autorisierung anstoßen, fachliche Regeln verbleiben im Model bzw. in der Service-Schicht. **MVC verhindert Sicherheitslücken aber nicht automatisch:** Gegen XSS helfen zusätzlich kontextgerechtes Output-Encoding und sichere DOM-APIs, gegen unautorisierte Zustandsänderungen serverseitige Authentifizierung und Autorisierung.

> **IHK-Typfrage:** *"Warum hilft MVC gegen 'fat views'?"*
> **Musterantwort:** MVC ordnet Darstellungs-, Steuerungs- und Geschäftslogik unterschiedlichen Verantwortungsbereichen zu und *fördert* damit eine schlanke View – garantiert sie aber nicht automatisch. Eine schlanke, testbare View entsteht nur, wenn diese Trennung im Projekt konsequent durchgehalten wird.

---

## 2. Security-by-Design & Software-Planung

> **Grundprinzip:** Sicherheit ist kein nachträglicher Anstrich, sondern ein Fundament, das von der ersten Bauzeichnung an mitgeplant wird – wie ein Drainagesystem, das man vor der Bepflanzung verlegt, nicht danach.

### 2.1 Security-by-Design & Privacy-by-Design

Nachträgliche Sicherheitskorrekturen in eine bereits fertige, eng verzahnte Codebasis sind häufig deutlich teurer und fehleranfälliger, weil Architektur, Schnittstellen, Tests und bestehende Abhängigkeiten nachträglich angepasst werden müssen. **Security-by-Design** und **Privacy-by-Design** (u. a. gesetzlich verankert in DSGVO Art. 25 – Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen) verlangen, dass Sicherheit und Datenschutz bereits im ersten Architekturentwurf feste Anforderungen sind.

### 2.2 Sechs wichtige Security-Design-Prinzipien

> Es gibt keine allgemein kanonische "die 6 Prinzipien" – je nach Quelle variiert die Zusammenstellung und Anzahl. Die folgende Auswahl deckt die für die Prüfung wichtigsten ab.

| Prinzip | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Least Privilege** (Minimalprinzip) | Jede Komponente erhält nur die minimal nötigen Rechte | 🔴 Prüfungsstoff |
| **Separation of Privilege** | Kritische Aktionen brauchen mehrere unabhängige Bedingungen/Freigaben (z. B. Vier-Augen-Prinzip) | 🔴 Prüfungsstoff |
| **Complete Mediation** | Jeder Zugriff auf eine geschützte Ressource wird anhand der *aktuell* gültigen Berechtigungen geprüft – frühere Prüfentscheidungen dürfen nicht ungeprüft weiterverwendet werden (Caching nur mit sicherer Invalidierung) | 🟡 Kontextwissen |
| **Defense in Depth** | Mehrere voneinander unabhängige, sich ergänzende Sicherheitsebenen, sodass das Versagen einer Maßnahme nicht sofort zur vollständigen Kompromittierung führt | 🔴 Prüfungsstoff |
| **Fail-Safe Defaults** | Zugriff wird standardmäßig verweigert ("deny by default") und nur aufgrund ausdrücklicher Berechtigung erlaubt – ein Fehler darf nicht versehentlich zu zusätzlichen Rechten führen | 🔴 Prüfungsstoff |
| **Psychological Acceptability** | Sicherheit muss benutzerfreundlich sein, sonst wird sie umgangen | 🟡 Kontextwissen |

> **IHK-Typfrage:** *"Was bedeutet 'Fail-Safe Defaults' und warum ist es sicherheitskritisch?"*
> **Musterantwort:** Ein System arbeitet standardmäßig nach dem Prinzip "deny by default": Zugriff wird verweigert, sofern keine explizite Berechtigung vorliegt. Kann eine Berechtigung wegen eines Fehlers nicht zuverlässig geprüft werden, wird der Zugriff *nicht* freigegeben – so führt ein Ausfall nicht versehentlich zu zusätzlichen Rechten.

### 2.3 Client-Side Threat Modeling & OWASP-Kandidatenliste

Im Frontend (z. B. eine React-SPA) lauern eigene Risiken, die der klassische (Backend-lastige) OWASP Top 10 nicht abdeckt. OWASP führt dazu ein eigenes Projekt zu clientseitigen Sicherheitsrisiken – die dortige Liste ist ausdrücklich als **Kandidatenliste** gekennzeichnet, nicht als abgeschlossener Standard:

| Risiko | Beschreibung | IHK-Relevanz |
| --- | --- | --- |
| **DOM-based XSS** | Angreifer schleust Skripte direkt ins Client-seitige DOM ein | 🔴 Prüfungsstoff |
| **Client-Side Data Leakage** | Vertrauliche Daten (Session-Tokens, personenbezogene Daten) im Browser, in Logs oder Fehlermeldungen exponiert. Geheime API-Schlüssel gehören grundsätzlich auf eine vertrauenswürdige Serverseite – ein Geheimnis, das an beliebiges Browser-JS ausgeliefert wird, kann nicht dauerhaft geheim bleiben (öffentliche/"publishable" Keys sind davon zu unterscheiden) | 🔴 Prüfungsstoff |
| **Prototype Pollution** | Manipulation gemeinsam genutzter JS-Prototypen – kann Programmlogik, Berechtigungsprüfungen oder Standardwerte verändern und in Verbindung mit geeigneten "Gadgets" bis zur Codeausführung führen; zusätzliches JS-Risiko, nicht offiziell Teil der OWASP-Kandidatenliste | 🟢 Nice to know |

### 2.4 Sichere Client-Side-Datenspeicherung

| Speicherort | Sicherheitsprofil | IHK-Relevanz |
| --- | --- | --- |
| **LocalStorage / SessionStorage** | Per JS jederzeit lesbar → **niemals** Tokens/sensible Daten hier ablegen | 🔴 Prüfungsstoff |
| **Cookies (`HttpOnly`, `Secure`, `SameSite`)** | `HttpOnly` blockt JS-Zugriff, `Secure` erzwingt HTTPS, `SameSite=Lax/Strict` reduziert (nicht: eliminiert) CSRF-Risiko | 🔴 Prüfungsstoff |
| **IndexedDB** | Browser-Datenbank für größere Datenmengen; innerhalb derselben Origin grundsätzlich durch dort laufendes JavaScript erreichbar – daher keine langfristige Ablage von Auth-Geheimnissen; Verschlüsselung ist kein allgemeiner XSS-Schutz, da Schadcode oft auch auf Schlüssel/Klartext zugreifen kann | 🟡 Kontextwissen |

> **IHK-Typfrage:** *"Warum ist `HttpOnly` sicherer als `localStorage` für Auth-Tokens, und reicht es allein aus?"*
> **Musterantwort:** Ein `HttpOnly`-Cookie kann von JavaScript nicht über `document.cookie` ausgelesen werden – der direkte Diebstahl des Tokens bei XSS wird dadurch erschwert. `HttpOnly` verhindert aber weder XSS selbst noch, dass bereits eingeschleuster Code authentifizierte Aktionen auslöst (das ist ein anderes Angriffsszenario). Gegen **CSRF** (eine fremde Seite lässt den Browser eine Anfrage an die Zielanwendung senden) helfen zusätzlich `SameSite` und – je nach Architektur – ein CSRF-Token; `SameSite` ist eine zusätzliche Schutzschicht, kein vollständiger CSRF-Ersatz: `Set-Cookie: sessionId=abc123; HttpOnly; Secure; SameSite=Strict`.

---

## 3. Objektorientierte TypeScript-Grundlagen

> **Grundprinzip:** Die vier Säulen der OOP sind wie die Grundregeln im Gewächshausbau: Man zeigt nur das Nötige nach außen (Abstraktion), schützt das Innenleben (Kapselung), baut auf Bewährtem auf (Vererbung) und lässt gleiche Handgriffe je nach Pflanze unterschiedlich wirken (Polymorphismus).

### 3.1 Die vier Säulen der OOP

| Säule | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Abstraktion** | Komplexität verbergen, nur Wesentliches zeigen (abstrakte Klassen/Interfaces) | 🔴 Prüfungsstoff |
| **Kapselung (Encapsulation)** | Interner Zustand nur über kontrollierte öffentliche Methoden zugänglich | 🔴 Prüfungsstoff |
| **Vererbung (Inheritance)** | Neue Klassen bauen auf bestehenden auf (`extends`) | 🔴 Prüfungsstoff |
| **Polymorphismus** | Verschiedene Objekte reagieren auf denselben Methodenaufruf unterschiedlich | 🔴 Prüfungsstoff |

### 3.2 Sichtbarkeitsmodifikatoren, `readonly` und Kapselung

```typescript
class Vehicle {
    private id: string;          // Nur innerhalb von Vehicle sichtbar
    protected speed: number = 0; // Sichtbar in Vehicle + Subklassen
    readonly brand: string;      // Bei Typprüfung nach Initialisierung nicht neu zuweisbar

    constructor(brand: string) {
        this.id = Math.random().toString();
        this.brand = brand;
    }
}
```

| Modifier | Sichtbarkeit | IHK-Relevanz |
| --- | --- | --- |
| `public` (Default) | Von überall zugänglich | 🟡 Kontextwissen |
| `private` | Nur innerhalb der deklarierenden Klasse direkt zugänglich | 🔴 Prüfungsstoff |
| `protected` | Innerhalb der deklarierenden Klasse und ihrer Subklassen zugänglich | 🔴 Prüfungsstoff |
| `readonly` | Property darf bei der Typprüfung nach ihrer Initialisierung nicht neu zugewiesen werden | 🟡 Kontextwissen |

> **Prüfungsfalle:** `private`, `protected` **und** `readonly` sind reine TypeScript-**Compile-Zeit-Konstrukte** – keines davon schützt zur Laufzeit. `private`-Felder lassen sich z. B. über `obj["id"]` trotzdem auslesen; echten JS-Laufzeitschutz bieten erst native **Private Fields** mit `#`-Syntax (`#id`, seit TS 3.8). `readonly` ist zudem nur **flach**: Es verhindert nur die Neuzuweisung der Property selbst, nicht die Veränderung eines referenzierten Objekts:
> ```typescript
> class Garden {
>     readonly plants: string[] = [];
> }
> const g = new Garden();
> g.plants.push("Rose"); // erlaubt – das Array selbst bleibt veränderbar
> // g.plants = [];      // TypeScript-Fehler – neue Referenz nicht erlaubt
> ```

### 3.3 Class vs. Abstract Class vs. Interface

| Merkmal | Class | Abstract Class | Interface |
| --- | --- | --- | --- |
| **Laufzeitcode** | Ja | Ja | Nein |
| **Instanziierbar?** | Ja (`new`) | Nein | Nein |
| **Implementierung** | Konkrete Member | Konkrete + abstrakte Member gemischt | Beschreibt nur eine Typstruktur/einen Vertrag |
| **Beziehungen** | Eine Basisklasse per `extends`; mehrere Interfaces per `implements` | Eine Basisklasse per `extends`; mehrere Interfaces per `implements` | Kann mehrere Interfaces per `extends` erweitern |
| **Nach Kompilierung** | Erzeugt JS-Laufzeitcode; konkrete Ausgabe hängt vom Compiler-Target ab | Erzeugt JS-Laufzeitcode für konkrete Member; `abstract`-Modifier selbst ist reine Typinformation (JS erzwingt zur Laufzeit nicht, dass die Klasse nicht instanziiert wird) | Verschwindet vollständig (Type Erasure) |

> **Prüfungsfalle:** `implements` ist **keine Mehrfachvererbung** – eine Klasse *implementiert* damit mehrere Verträge (Interfaces), *erbt* aber weiterhin nur von einer einzigen Basisklasse (`extends`).

```typescript
abstract class DatabaseConnector {
    protected connectionString: string;
    constructor(connectionString: string) {
        this.connectionString = connectionString;
    }
    abstract connect(): boolean; // Muss von Subklassen implementiert werden
}

interface CanFly { fly(): void; }
interface CanSwim { swim(): void; }

class Duck implements CanFly, CanSwim {
    fly() { console.log("Fliege"); }
    swim() { console.log("Schwimme"); }
}
```

> **IHK-Typfrage:** *"Warum 'verschwindet' ein Interface nach der TypeScript-Kompilierung?"*
> **Musterantwort:** Interfaces dienen ausschließlich der statischen Typprüfung (Type Erasure) und erzeugen keinen JavaScript-Laufzeitcode. Klassen besitzen dagegen eine Laufzeitrepräsentation, deren konkrete JS-Ausgabe vom eingestellten Compiler-Target abhängt.

### 3.4 Beziehungen zwischen Klassen: Assoziation, Aggregation, Komposition

Diese UML-Beziehungstypen beschreiben, *wie* Klassen miteinander verbunden sind – häufig relevant bei Klassendiagramm-Aufgaben:

| Beziehung | Bedeutung | Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **Assoziation** | Allgemeine "kennt"/"nutzt"-Beziehung | `Student` kennt `Kurs` | 🟡 Kontextwissen |
| **Aggregation** | Teil-Ganzes-Beziehung (schwach) – Teile existieren auch unabhängig vom Ganzen | `Auto` hat `Reifen` (Reifen überleben das Auto) | 🟡 Kontextwissen |
| **Komposition** | Teil-Ganzes-Beziehung (stark) – Teile existieren nur mit dem Ganzen | `Haus` hat `Zimmer` (Zimmer verschwinden mit dem Haus) | 🟡 Kontextwissen |

---

## 4. Design Patterns & Polymorphismus

> **Grundprinzip:** Ein gutes Entwurfsmuster ist wie ein bewährtes Anzuchtverfahren – man erfindet es nicht bei jedem Projekt neu, sondern greift auf ein Muster zurück, das sich für ein wiederkehrendes Problem bewährt hat.

### 4.1 Polymorphismus im Detail

| Konzept | Beschreibung | IHK-Relevanz |
| --- | --- | --- |
| **Method Overriding** (Überschreiben) | Subklasse liefert eigene Implementierung einer geerbten Methode, Signatur bleibt gleich | 🔴 Prüfungsstoff |
| **Method Overloading** (Überladen) | Mehrere von außen sichtbare Aufrufsignaturen für dieselbe Methode; **eine gemeinsame Implementierung** verarbeitet alle Varianten (Overload Signatures) – bei einfachen Fällen ist oft ein Union Type die schlankere Lösung | 🟡 Kontextwissen |
| **Dynamic Binding** (Late Binding) | Laufzeit entscheidet anhand des tatsächlichen Objekttyps, welche Methode ausgeführt wird | 🔴 Prüfungsstoff |

```typescript
class Formatter {
    format(value: string): string;
    format(value: number): string;
    format(value: string | number): string { // gemeinsame Implementierung
        return String(value);
    }
}
```

### 4.2 Creational Pattern: Singleton

Stellt innerhalb eines definierten Laufzeit-/Modulkontexts einen zentralen Zugriff auf genau eine kontrolliert erzeugte Instanz bereit (z. B. Konfigurationsverwaltung, Logger-Fassade, Cache-Manager):

```typescript
class AppConfig {
    private static instance: AppConfig;
    private constructor() {} // Verhindert Instanziierung von außen

    public static getInstance(): AppConfig {
        if (!AppConfig.instance) {
            AppConfig.instance = new AppConfig();
        }
        return AppConfig.instance;
    }
}
```

> **Achtung:** Die Eindeutigkeit gilt nur *innerhalb eines Laufzeit-/Modulkontexts* – über mehrere Node-Prozesse, Worker oder Browser-Tabs hinweg können durchaus mehrere Instanzen entstehen. Eine Datenbankverbindung als Beispiel ist zudem ungenau: In der Praxis nutzt man meist einen **Connection Pool**, keine einzelne physische Verbindung.

> **IHK-Typfrage:** *"Warum ist ein globales `static`-Feld kein Ersatz für Singleton?"*
> **Musterantwort:** Ein statisches Feld allein garantiert noch keine Einmaligkeit, solange der Konstruktor öffentlich bleibt – dann könnte trotzdem jemand `new AppConfig()` aufrufen. Erst der **private Konstruktor** verhindert die direkte Instanziierung von außen; die statische `getInstance()`-Methode kontrolliert die Erzeugung.
>
> *Hinweis:* Das gezeigte Beispiel ist eine einfache verzögerte Initialisierung. Innerhalb eines einzelnen Event-Loop-Kontexts ist die synchrone Ausführung unproblematisch; mehrere Node-Prozesse oder Worker besitzen jedoch getrennte Instanzen.

### 4.3 Creational Pattern: Factory Method

Die Basisklasse definiert den Ablauf, eine Subklasse legt die konkrete Objekterzeugung fest – z. B. ein Logger, der je nach Umgebung Konsole oder Datei anspricht, ohne dass der aufrufende Code die konkrete Logger-Klasse kennt:

```typescript
interface Logger {
    log(message: string): void;
}

class ConsoleLogger implements Logger {
    log(message: string): void { console.log(message); }
}

abstract class Application {
    protected abstract createLogger(): Logger; // Factory Method

    run(): void {
        const logger = this.createLogger();
        logger.log("Anwendung gestartet");
    }
}

class DevelopmentApp extends Application {
    protected createLogger(): Logger {
        return new ConsoleLogger();
    }
}
```

> Die Factory Method folgt dem **Open-Closed-Prinzip** (Teil von SOLID): Neue Logger-Typen lassen sich durch neue `Application`-Subklassen ergänzen, ohne den bestehenden `Application`-Code zu ändern.

### 4.4 Behavioral Pattern: Observer

Definiert eine direkte 1-zu-n-Abhängigkeit: Das *Subject* kennt seine *Observer* und benachrichtigt sie bei Zustandsänderung selbst. Das unterscheidet Observer vom verwandten **Publish/Subscribe**-Prinzip, bei dem ein Event-Broker/Bus zwischen Publisher und Subscriber vermittelt und beide sich nicht direkt kennen.

```text
+------------------+                    +-------------------+
|     Subject      |                    |     Observer      |
+------------------+                    +-------------------+
| - observers      | <>---------------->| + update()        |
+------------------+                    +-------------------+
| + attach(obs)    |
| + detach(obs)    |
| + notify()       |
+------------------+
```

| Pattern | Typ | Einsatzzweck | IHK-Relevanz |
| --- | --- | --- | --- |
| **Singleton** | Creational | Kontrollierter zentraler Zugriff auf eine Instanz, z. B. Konfiguration, Logger-Fassade oder Connection-Pool-Manager | 🔴 Prüfungsstoff |
| **Factory Method** | Creational | Objekterzeugung entkoppeln, Subklasse entscheidet konkrete Klasse | 🔴 Prüfungsstoff |
| **Observer** | Behavioral | 1:n-Benachrichtigung, Subject kennt seine Observer direkt | 🔴 Prüfungsstoff |

> **IHK-Typfrage:** *"Wie skaliert Observer, wenn die Zahl der Subscriber von 10 auf 10.000 wächst?"*
> **Musterantwort:** Bei der hier gezeigten **synchronen** Implementierung durchläuft `notify()` alle registrierten Observer nacheinander – die Laufzeit ist typischerweise \(O(n)\), wobei \(n\) die Anzahl der Observer ist. `notify()` muss aber nicht zwingend synchron sein. Bei sehr großen Mengen kommen zusätzlich Fehlerisolation, Abmeldeverhalten, Speicherverbrauch und ggf. asynchrone Verarbeitung (Event-Queue/Batching) ins Spiel, um Blockierungen zu vermeiden.

---

## 🔄 Zusammenspiel der Konzepte in LF8.1

```text
Programmierparadigma (OOP)
        │
        ▼
  MVC-Architektur ──────► Security-by-Design
   (Model/View/Controller)   (Security-Prinzipien, Threat Modeling)
        │
        ▼
  TypeScript-Klassenskelett (Interfaces, Abstract Classes)
        │
        ▼
  Design Patterns (Singleton, Factory, Observer)
```

---

## ⚠️ Typische Prüfungsfallen

| Falle | Problem | Richtigstellung |
| --- | --- | --- |
| "Stateless heißt keine Daten speichern" | Verwechslung von Client-Sitzungszustand und Ressourcenzustand | Server darf Ressourcen-/DB-Zustand speichern, nur keinen Client-Sitzungskontext |
| "Ein Interface kann man instanziieren" | Interface mit Klasse verwechselt | Interface ist reine Typdefinition, kein `new` möglich |
| "`implements` = Mehrfachvererbung" | Terminologie verwechselt | `implements` = Vertrag erfüllen, `extends` = Vererbung (nur einfach) |
| "`private` schützt zur Laufzeit" | TS-Feature mit JS-Feature verwechselt | `private` ist Compile-Zeit-Konstrukt, echter Laufzeitschutz nur mit `#field` |
| "Jede Web-API ist REST" | REST mit Client-Server gleichgesetzt | REST ist ein Architekturstil, nicht jede API erfüllt alle 6 Constraints |
| "Singleton = statische Klasse" | Muster mit Sprachfeature verwechselt | Singleton kontrolliert Instanziierung aktiv über privaten Konstruktor |

## ✅ Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Was ist der Kernunterschied zwischen imperativ und deklarativ? | Imperativ = *wie* lösen, deklarativ = *was* lösen |
| 2 | Welche Komponente im MVC-Pattern prüft typischerweise das Format von Eingaben? | Der Controller – fachliche Regeln bleiben im Model/der Service-Schicht |
| 3 | Warum ist `localStorage` für Tokens unsicher? | Von JS/XSS jederzeit auslesbar, kein `HttpOnly`-Schutz |
| 4 | Was passiert nach der Kompilierung mit einem TS-Interface? | Es verschwindet komplett (Type Erasure) |
| 5 | Wofür sorgt der `private`-Konstruktor beim Singleton? | Verhindert die direkte Instanziierung von außen und ermöglicht die kontrollierte Erzeugung einer Instanz innerhalb des jeweiligen Laufzeitkontexts |
| 6 | Warum reicht `HttpOnly` allein nicht als Cookie-Schutz? | Verhindert nur das direkte Auslesen durch JavaScript; zusätzlich sind XSS-Schutz sowie je nach Architektur `SameSite` und CSRF-Tokens nötig |
| 7 | Ist `protected` in TypeScript zur Laufzeit geschützt? | Nein, wie `private` nur Compile-Zeit-Konstrukt |
| 8 | Was unterscheidet Observer von Publish/Subscribe? | Bei Observer kennt das Subject seine Observer direkt, bei Pub/Sub vermittelt ein Broker/Event-Bus |
| 9 | Nennen Sie ein Beispiel für Client-Server ohne grafische UI. | Kommandozeilenprogramm, IoT-Gerät, oder ein Server als Client eines anderen Servers |
| 10 | Welchen Vorteil bietet Factory Method gegenüber direktem `new`? | Der übergeordnete Ablauf hängt nur von einer Abstraktion ab; welche konkrete Klasse instanziiert wird, entscheidet eine Subklasse – der Ablauf selbst muss dafür nicht geändert werden |

---

## 📇 IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **MVC** | Architekturmuster: Model (Daten/Logik), View (Darstellung), Controller (Steuerung/Validierung) |
| **Statelessness** | Jede Anfrage ist unabhängig – der Server braucht keinen zwischen Requests gespeicherten Client-Sitzungskontext (Ressourcenzustand darf serverseitig persistiert werden) |
| **Least Privilege** | Minimalprinzip: nur nötigste Rechte vergeben |
| **Fail-Safe Defaults** | Zugriff standardmäßig verweigern ("deny by default"), nur ausdrücklich Erlaubtes freigeben |
| **HttpOnly-Cookie** | Verhindert den direkten Cookie-Zugriff über JavaScript – verhindert XSS selbst nicht |
| **Encapsulation** | Interner Zustand nur über kontrollierte Methoden erreichbar |
| **Type Erasure** | Interfaces verschwinden nach TS-Kompilierung |
| **Singleton** | Kontrollierter zentraler Zugriff auf eine Instanz innerhalb eines Laufzeitkontexts |
| **Observer** | Direkte 1:n-Benachrichtigung, Subject kennt seine Observer |
| **Publish/Subscribe** | Indirekte 1:n-Kommunikation über Broker/Event-Bus (Publisher kennt Subscriber nicht) |
| **Dynamic Binding** | Laufzeit entscheidet Methodenimplementierung anhand des Objekttyps |
| **Factory Method** | Creational Pattern: Subklasse entscheidet, welche konkrete Klasse instanziiert wird |
| **SameSite (Cookie)** | Cookie-Attribut, das Mitsenden bei Cross-Site-Requests einschränkt – reduziert CSRF-Risiko |

---

## 🎯 Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| K2 – Erklären | "Erläutern Sie den Unterschied zwischen X und Y" | Klare Abgrenzung mit Fachbegriffen, kein Beispiel-Ersatz für Definition |
| K3 – Anwenden | "Entwerfen Sie eine Klassenstruktur für…" | Konkrete Klassen/Interfaces mit Modifiern, keine reine Prosa |
| K4 – Analysieren | "Analysieren Sie, wie sich X unter Bedingung Y verhält" | Ursache-Wirkungs-Kette, Skalierungs-/Trade-off-Aussage |
| K5/K6 – Bewerten/Synthetisieren | "Bewerten Sie kritisch…" / "Entwerfen Sie ein Gesamtkonzept…" | Abwägung mehrerer Optionen + begründete Empfehlung |

---

## 🗣️ Merksätze fürs Fachgespräch

> "MVC trennt nicht nur Code – es trennt Verantwortlichkeiten. Wer das vermischt, baut sich seine eigenen Bugs."

> "Security-by-Design heißt: Sicherheit ist keine Zutat, die man später hinzufügt, sondern das Fundament, auf dem alles andere steht."

> "Ein Interface beschreibt einen Typvertrag ohne eigene Laufzeitimplementierung – zur Entwurfszeit ist er alles, zur Laufzeit existiert er nicht mehr."

> "Singleton kontrolliert die Instanzerzeugung, Observer verteilt Zustandsänderungen – beide reduzieren direkte Abhängigkeiten, aber auf unterschiedliche Weise."

---

```yaml
lernfeld: LF8.1
titel: "Client-Server-Architektur & OOP Design Patterns"
typ: "Kompakter Pruefungswiki (Typ A)"
quellen_intern:
  - LF8.1.1: Programming Paradigms, Software Architectures & MVC
  - LF8.1.2: Security-by-Design & Software Planning
  - LF8.1.3: Object-Oriented TypeScript Fundamentals
  - LF8.1.4: Software Design Patterns & Polymorphism in TypeScript
quellen_fachlich:
  - "Roy Fielding: Architectural Styles and the Design of Network-based Software Architectures (REST-Dissertation)"
  - "TypeScript Handbook (typescriptlang.org/docs)"
  - "OWASP Cheat Sheet Series (Session Management, XSS Prevention, HTML5 Security)"
  - "OWASP Client-Side Security Risks Project (Kandidatenliste)"
  - "DSGVO Art. 25 (Datenschutz durch Technikgestaltung)"
pruefungsrelevanz: "Grundlagen fuer AP1, Transferfragen moeglich in AP2 und Fachgespraech"
status: final
stand: 2026
optionale_deepdives:
  - "MVVM & Flux-Architektur im Web-Frontend (Bezug: 1.3 MVC)"
  - "Content Security Policy (CSP) als Defense-in-Depth-Layer (Bezug: 2.2 Defense in Depth)"
  - "TypeScript Utility Types (Readonly<T>, Partial<T>, Omit<T,K>) (Bezug: 3. OOP-Grundlagen)"
  - "SOLID-Prinzipien im Detail, insbesondere Dependency Inversion (Bezug: 4.3 Factory Method)"
  - "STRIDE als Threat-Modeling-Methode (Bezug: 2.1 Security-by-Design)"
```