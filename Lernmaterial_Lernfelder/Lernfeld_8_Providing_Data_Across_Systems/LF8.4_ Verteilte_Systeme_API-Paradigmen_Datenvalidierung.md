# LF8.4 – Verteilte Systeme, API-Paradigmen & Datenvalidierung

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1 (schriftlich), Transferfragen in AP2 und Fachgespräch möglich
> **Lernzeit:** Ca. 100–130 Minuten reines Lesen, +70–100 Minuten mit Aufgaben – abhängig von Vorkenntnissen und Bearbeitungstiefe
> **Status:** Final
> **Stand:** 2026
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was passiert im HTTP-Request-Response-Zyklus, und warum ist Statelessness die Grundlage für horizontale Skalierbarkeit? | [→ 1. API-Grundlagen](#1-api-grundlagen-und-statelessness) |
| 2 | Was unterscheidet SOAP (WSDL, XML) von REST (JSON, HTTP-Verben) architektonisch, und wann setzt man welches ein? | [→ 2. SOAP vs. REST](#2-traditionelle-vs-ressourcenorientierte-apis-soap-und-rest) |
| 3 | Wie funktionieren gRPC (Protocol Buffers, HTTP/2) und GraphQL (Schema/Resolver), und welches Problem klassischer REST-APIs lösen sie? | [→ 3. gRPC & GraphQL](#3-high-performance--query-driven-apis-grpc-und-graphql) |
| 4 | Warum reicht Client-seitige Validierung nicht aus, und was unterscheidet Compile-Time-Typsicherheit von Runtime-Validierung? | [→ 4. Validierungsgrenzen](#4-datenvalidierungsgrenzen-zod-und-pydantic) |
| 5 | Welche konkreten Angriffsflächen (Injection, CORS-Fehlkonfiguration) muss eine API-Sicherheitsstrategie adressieren? | [→ 5. API-Sicherheit](#5-api-sicherheit-als-querschnittsthema) |

---

## 1. API-Grundlagen und Statelessness

> **Grundprinzip:** Eine API ist der schriftliche Vertrag zwischen zwei unabhängigen Systemen – solange beide Seiten sich an den Vertrag halten, ist es egal, in welcher Sprache oder Technologie die jeweils andere Seite gebaut ist.

### 1.1 Die Rolle von APIs in verteilten Systemen

Moderne Anwendungen bestehen selten aus einem einzigen, monolithischen Programm. Stattdessen sind sie als **verteilte Systeme** aufgebaut: unabhängige Dienste, die über ein Netzwerk miteinander kommunizieren. Eine **API (Application Programming Interface)** definiert dabei den formalen Vertrag zwischen diesen Diensten – erlaubte Anfragen, erwartete Antworten, Datenformate und Protokolle. Dadurch können Teams entkoppelt arbeiten: Ein Frontend-Team baut die Oberfläche in React/TypeScript, ein Backend-Team die Datenhaltung in Python – solange beide sich an den vereinbarten API-Vertrag halten.

### 1.2 Der HTTP-Request-Response-Zyklus

| Bestandteil der Anfrage | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **HTTP-Methode (Verb)** | Gewünschte Aktion: `GET` (lesen), `POST` (erstellen), `PUT` (vollständig ersetzen), `PATCH` (teilweise aktualisieren), `DELETE` (löschen) | 🔴 |
| **URI** | Pfad zur angefragten Ressource, z. B. `/api/v1/sensoren` | 🔴 |
| **Headers** | Metadaten, z. B. `Content-Type: application/json`, `Authorization: Bearer <token>` | 🔴 |
| **Body (Payload)** | Die gesendeten Nutzdaten, meist JSON | 🟡 |

| Bestandteil der Antwort | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Status Code** | Ergebnis der Anfrage (siehe Tabelle unten) | 🔴 |
| **Headers** | Metadaten zur Antwort | 🟡 |
| **Body (Payload)** | Die zurückgegebenen Daten | 🟡 |

| Statuscode | Bedeutung |
| --- | --- |
| `200 OK` / `201 Created` | Erfolg |
| `400 Bad Request` | Anfrage syntaktisch fehlerhaft |
| `401 Unauthorized` | Authentifizierung fehlt oder ist ungültig (nicht: fehlende Berechtigung) |
| `403 Forbidden` | Identität ist bekannt, Zugriff aber nicht erlaubt |
| `404 Not Found` | Ressource existiert nicht |
| `422 Unprocessable Entity` | Anfrage syntaktisch lesbar, aber fachlich/semantisch ungültig (typisch bei Validierungsfehlern) |
| `500 Internal Server Error` | Serverseitiger Fehler |

> **IHK-Typfrage:** *"Erklären Sie den semantischen Unterschied zwischen einem `4xx`- und einem `5xx`-Statuscode."*
> **Musterantwort:** `4xx` signalisiert einen Client-Fehler – die Anfrage selbst war fehlerhaft (z. B. ungültige Daten, fehlende Berechtigung). `5xx` signalisiert einen Server-Fehler – die Anfrage war grundsätzlich korrekt, aber der Server konnte sie nicht verarbeiten (z. B. Absturz, Datenbankfehler). Diese Unterscheidung ist wichtig, um zu wissen, ob der Client (z. B. seine Eingabe) oder der Server (z. B. sein Zustand) die Fehlerursache ist.

### 1.3 Statelessness (Zustandslosigkeit)

**Definition:** Der Server darf zwischen Anfragen keinen Kontext oder keine Sitzungsinformationen über den Client speichern. Jede einzelne Anfrage muss alle Informationen enthalten, die der Server zur Verarbeitung benötigt.

**Warum das für Skalierbarkeit entscheidend ist:** Ist ein Server zustandslos, können Anfragen eines einzelnen Clients jederzeit von unterschiedlichen Servern beantwortet werden (z. B. über einen Load Balancer), ohne dass der Client etwas davon bemerkt.

```text
[ Client ] --- Anfrage 1 (mit Auth-Token + Daten) ---> [ Server A ]
[ Client ] --- Anfrage 2 (mit Auth-Token + Daten) ---> [ Server B (A ist ausgefallen) ]
```

Da der Server keinen Zustand speichert, muss der "Zustand" der Interaktion vollständig auf Client-Seite verwaltet und bei jeder Anfrage mitgeschickt werden – typischerweise über Header (z. B. JWT-Tokens) oder den Payload.

> **IHK-Typfrage:** *"Warum verletzt das Speichern einer Login-Sitzungsdatei direkt auf der lokalen Festplatte eines Webservers die Statelessness, und wie schränkt das die horizontale Skalierbarkeit ein?"*
> **Musterantwort:** Die Sitzungsdatei bindet den Client an genau diesen einen Server – ein Load Balancer könnte Folgeanfragen nicht mehr beliebig an andere Server verteilen, ohne die Sitzung zu verlieren. Das verhindert horizontale Skalierung (Hinzufügen weiterer, austauschbarer Server), da jeder Server "seine" Clients kennen müsste.

### 1.4 Interaktionen visuell modellieren

Für die Modellierung dynamischer Client-Server-Abläufe (z. B. Authentifizierungs-Handshakes, Validierungsschritte, Fehler-Schleifen) eignen sich **UML-Sequenzdiagramme** – anders als die in LF8.3 behandelten Aktivitätsdiagramme (die den Kontrollfluss *eines* Prozesses zeigen), stellen Sequenzdiagramme den zeitlichen Nachrichtenaustausch *zwischen mehreren Beteiligten* (Client, API-Gateway, Validierungsschicht, Datenbank) dar. Vertiefung dazu siehe Deep-Dive-Ausblick.

---

## 2. Traditionelle vs. ressourcenorientierte APIs: SOAP und REST

> **Grundprinzip:** SOAP ist wie ein notariell beglaubigter Vertrag – jedes Detail ist vorab fixiert. REST ist wie ein loses Gentlemen's Agreement über Standardregeln (HTTP-Verben) – flexibler, aber weniger streng abgesichert.

### 2.1 SOAP (Simple Object Access Protocol)

SOAP ist ein stark strukturiertes, vom W3C entwickeltes Protokoll für Web Services.

- **Contract-First:** SOAP wird häufig nach dem Contract-First-Prinzip eingesetzt – die exakte Struktur aller verfügbaren Methoden, Datentypen und Parameter wird vorab in einem XML-basierten Dokument namens **WSDL (Web Services Description Language)** festgelegt. WSDL unterstützt dieses Vorgehen; zwingend vorgeschrieben ist es durch SOAP selbst nicht, in der Praxis aber der Regelfall.
- **Payload:** SOAP-Nachrichten werden als XML-Struktur übertragen, verpackt in einen **SOAP Envelope** (Header für Metadaten/Sicherheit, Body für die eigentlichen Daten).
- **Transport:** Meist über HTTP, protokollunabhängig auch über SMTP oder TCP möglich.
- **Enterprise-Features:** SOAP selbst bietet **keine automatisch eingebauten ACID-Transaktionen** – über zusätzliche WS-*-Standards (z. B. **WS-Security** für Nachrichtensicherheit, WS-AtomicTransaction für verteilte Transaktionen) lassen sich aber Sicherheits- und Transaktionsgarantien standardisiert integrieren. Das macht SOAP in Kombination mit diesen Erweiterungen attraktiv für Bank-/Finanzsysteme – die Garantie entsteht jedoch durch die Erweiterung, nicht durch SOAP allein. XML-Parsing und der Envelope-Overhead führen zudem zu höherer CPU-Last und langsameren Übertragungszeiten.

### 2.2 REST (Representational State Transfer)

REST ist ein architektonischer Stil als leichtgewichtige Alternative zu SOAP.

- **Ressourcenorientiert:** Statt entfernte Methoden aufzurufen, interagieren Clients mit Ressourcen (identifiziert über URIs) mittels Standard-HTTP-Verben.
- **Payload:** Meist **JSON**, kann aber auch XML, Text oder HTML sein.
- **Constraints:** Basiert auf sechs REST-Constraints. Client-Server-Trennung, Statelessness, Cacheability, Uniform Interface und Layered System bilden den Kern; **Code-on-Demand ist optional**. In der Praxis setzen viele als "REST-API" bezeichnete Schnittstellen nicht alle Constraints vollständig um.

| Merkmal | SOAP (Webservice) | REST (API-Stil) |
| --- | --- | --- |
| Format | Ausschließlich XML | JSON, XML, Text, HTML |
| Charakter | Striktes Protokoll (W3C-Standard) | Architekturstil (keine feste Spezifikation) |
| Schnittstellenbeschreibung | WSDL (strikter Vertrag) | OpenAPI/Swagger (JSON), optional |
| Performance | Tendenziell langsamer (hoher XML-Overhead) | Tendenziell schneller (leichtgewichtiges JSON) |
| Kopplung | Eng (Contract-First) | Lose |

> **Hinweis zur Einordnung:** "Schneller" und "langsamer" sind Tendenzaussagen für typische Einsatzszenarien – ein schlecht designtes REST-API kann trotzdem langsamer sein als ein optimiertes SOAP-System. Die Entscheidung hängt vom konkreten Anwendungsfall ab (siehe Prüfungstaktik).

> **IHK-Typfrage:** *"Warum wird SOAP für transaktionssichere Finanzsysteme bevorzugt, während REST der Standard für moderne mobile Anwendungen ist?"*
> **Musterantwort:** SOAP eignet sich für Enterprise-Szenarien, weil sich Sicherheits- und Transaktionsmechanismen über standardisierte WS-*-Erweiterungen integrieren lassen (nicht automatisch durch SOAP allein) – wichtig, wenn dies vertraglich vorausgesetzt wird. REST ist dagegen leichtgewichtig, schnell zu entwickeln und ressourcenschonend – wichtiger für mobile Clients mit begrenzter Bandbreite und Akkulaufzeit, wo Entwicklungsgeschwindigkeit und geringer Overhead stärker zählen als aufwendig konfigurierbare Transaktionsgarantien.

---

## 3. High-Performance & Query-Driven APIs: gRPC und GraphQL

> **Grundprinzip:** gRPC optimiert die *Übertragung* (kompakt, binär, schnell), GraphQL optimiert die *Abfrage* (Client bestimmt selbst, welche Felder er braucht).

### 3.1 gRPC (gRPC Remote Procedure Calls)

> Kleine Prüfungsfalle in eigener Sache: "gRPC" wird oft als "Google Remote Procedure Call" aufgelöst – offiziell steht das "g" aber selbstreferenziell für "gRPC" selbst (laut gRPC-eigener FAQ). Fachlich korrekt bleibt: gRPC wurde von Google entwickelt und ist heute Open Source.

- **Transport:** Klassisches gRPC basiert auf **HTTP/2** – ermöglicht bidirektionales Streaming, Multiplexing (mehrere Anfragen über eine einzige Verbindung) und Header-Kompression. Varianten wie gRPC-Web benötigen für den Browser-Einsatz zusätzliche Vermittlungsschichten.
- **RPC-Arten:** gRPC unterstützt vier Aufrufmuster: **Unary** (eine Anfrage, eine Antwort – wie klassisches REST), **Server-Streaming**, **Client-Streaming** und **bidirektionales Streaming**. Diese Streaming-Fähigkeit ist ein zentraler Unterschied zu klassischem REST.
- **Serialisierung:** **Protocol Buffers (Protobuf)** als binäres Format statt textbasiertem JSON – dadurch deutlich kompaktere Payloads und schnelleres Parsen.
- **Contract-First:** Eine `.proto`-Datei definiert Dienste und Nachrichtenstrukturen; Compiler-Tools generieren daraus automatisch typsichere Client-/Server-Stubs in mehreren Sprachen.

```protobuf
// Beispiel: sensor.proto
syntax = "proto3";

message SensorRequest {
  int32 sensor_id = 1;
}

message SensorResponse {
  double value = 1;
  string status = 2;
}

service SensorService {
  rpc GetSensorData (SensorRequest) returns (SensorResponse);
}
```

### 3.2 GraphQL

- **Gelöstes Problem:** Klassische REST-APIs leiden häufig unter **Over-Fetching** (mehr Daten als benötigt) oder **Under-Fetching** (mehrere Anfragen nötig, um verknüpfte Daten zu erhalten).
- **Client-definierte Abfragen:** Der Client fragt über einen einzigen Endpunkt genau die Felder ab, die er braucht. Das **reduziert** Over- und Under-Fetching strukturell deutlich – vollständig beseitigt wird es nicht automatisch, da die tatsächliche Effizienz von Schema-Design und Resolvern abhängt.
- **Schema & Resolver:** Der Server definiert ein stark typisiertes Schema (SDL). **Resolver** sind serverseitige Funktionen, die die Daten für jedes angefragte Feld liefern.
- **Kehrseite – das N+1-Problem:** Ein naiv implementierter Resolver für eine Liste (z. B. "alle Kurse") kann pro Listenelement eine eigene Datenbankabfrage auslösen (1 Abfrage für die Liste + N Abfragen für die Details) – das kann die Performance stärker belasten als ein einzelner, gut designter REST-Call. Lösungsansätze wie Batching/DataLoader-Muster verhindern das.

```graphql
# Beispiel: schema.graphql
type Sensor {
  id: ID!
  name: String!
  readings(limit: Int): [Reading!]!
}

type Reading {
  value: Float!
  timestamp: String!
}

type Query {
  getSensor(id: ID!): Sensor
}
```

### 3.3 Einordnung: REST vs. gRPC vs. GraphQL

```text
REST:     [ Client ] --GET /users/5--------> [ Server ]   -> ganzer "users"-Datensatz
                                                              (evtl. zu viele/zu wenige Felder)

gRPC:     [ Client ] --GetUser(id=5)-------> [ Server ]   -> kompaktes Protobuf-Objekt
          (binär, HTTP/2, feste .proto-Struktur)

GraphQL:  [ Client ] --{ user(id:5){name} }-> [ Server ]   -> nur "name", sonst nichts
          (Client bestimmt Felder pro Anfrage selbst)
```

| Kriterium | REST | gRPC | GraphQL |
| --- | --- | --- | --- |
| Payload-Format | JSON (textbasiert) | Protobuf (binär) | JSON (textbasiert) |
| Typischer Einsatz | Öffentliche Web-/Mobile-APIs | Interne Microservice-Kommunikation, Streaming | Flexible Client-Abfragen, mehrere Frontend-Typen |
| Over-/Under-Fetching | Anfällig dafür | Kein Thema (klar definierte RPC-Aufrufe) | Deutlich reduziert, aber abhängig von Resolver-Design (N+1-Risiko) |
| Lernkurve | Niedrig | Mittel (Protobuf-Toolchain nötig) | Mittel (Schema-Design, Resolver-Logik) |

> **IHK-Typfrage:** *"Erklären Sie, wie GraphQLs Client-definierte Abfragen das Over-Fetching-Problem klassischer REST-APIs lösen."*
> **Musterantwort:** Bei REST liefert ein Endpunkt eine feste, serverseitig definierte Datenstruktur – der Client bekommt oft mehr Felder, als er benötigt (Over-Fetching), oder muss mehrere Endpunkte kombinieren (Under-Fetching). Bei GraphQL spezifiziert der Client in der Abfrage selbst genau die benötigten Felder; der Resolver liefert nur diese – dadurch werden beide Probleme strukturell deutlich reduziert. Vollständig verschwinden sie nicht automatisch: Ein unsauber implementierter Resolver kann z. B. das N+1-Problem erzeugen (pro Listenelement eine eigene Datenbankabfrage).

---

## 4. Datenvalidierungsgrenzen: Zod und Pydantic

> **Grundprinzip:** "Vertraue niemals Client-Eingaben" – Client-seitige Validierung verbessert die Nutzererfahrung, Server-seitige Validierung schützt die Systemintegrität. Beides ist nötig, aber nur eines ist sicherheitsrelevant.

### 4.1 Warum Validierungsgrenzen durchsetzen?

In verteilten Systemen überqueren Daten nicht vertrauenswürdige Netzwerkgrenzen. Client-seitige Validierung (z. B. in einem React-Formular) lässt sich leicht umgehen (Postman, curl, Proxys). **Backend-seitige Validierung** ist deshalb der eigentliche Schutzwall der Systemintegrität – sie schützt Geschäftslogik, Datenbank und nachgelagerte Prozesse vor fehlerhaften Daten und Injection-Angriffen.

### 4.2 Compile-Time-Typsicherheit vs. Runtime-Validierung

| Aspekt | Compile-Time-Typsicherheit (z. B. TypeScript) | Runtime-Validierung (z. B. Zod, Pydantic) | IHK-Relevanz |
| --- | --- | --- | --- |
| Wann geprüft? | Während der Entwicklung/Kompilierung | Zur Laufzeit, bei jedem eingehenden Datensatz | 🔴 |
| Nach der Kompilierung? | Typen verschwinden vollständig (**Type Erasure**) | Prüfung bleibt aktiv, unabhängig vom Kompilierzeitpunkt | 🔴 |
| Schützt vor externen Daten? | Nein – kompilierte Typen prüfen keine Laufzeitdaten von außen | Ja – genau dafür entwickelt | 🔴 |

> **IHK-Typfrage:** *"Warum ist Runtime-Schema-Validierung auch dann notwendig, wenn eine Anwendung zur Compile-Zeit vollständig typsicher ist?"*
> **Musterantwort:** TypeScript-Typen existieren nur während der Entwicklung – nach dem Kompilieren zu JavaScript sind sie durch Type Erasure vollständig verschwunden und stehen zur Laufzeit nicht mehr als Prüfmechanismus zur Verfügung. Sendet eine externe API zur Laufzeit einen String statt einer erwarteten Zahl, findet keine automatische TypeScript-Prüfung mehr statt – der Wert kann unbemerkt weiterverarbeitet werden und erst später (z. B. bei einer Berechnung oder in Framework-Code) zu Fehlern oder unerwartetem Verhalten führen. Nur eine Runtime-Prüfung (Zod/Pydantic) kann Daten, die *nach* der Kompilierung ins System gelangen, direkt an der Systemgrenze validieren.

### 4.3 Zod (TypeScript) – Stand 2026: Zod 4.x ist die aktuelle Hauptversion

```typescript
import { z } from "zod";

// Seit Zod 4 werden Format-Validatoren wie z.email()/z.uuid() als
// Top-Level-Funktionen empfohlen. Die verketteten Formen (z.string().email())
// funktionieren in vielen Zod-4-Versionen weiterhin, gelten laut
// Migrationsdokumentation aber als veraltet.
// z.strictObject() lehnt zusätzlich unbekannte Felder ab (statt sie stillschweigend
// zu ignorieren) – relevant, wenn nur explizit erlaubte Felder akzeptiert werden sollen.
const UserSchema = z.strictObject({
  id: z.uuid(),
  username: z.string().min(3).max(20),
  email: z.email(),
  age: z.number().int().min(18).optional()
});

// Compile-Time-Typ aus dem Schema ableiten
type User = z.infer<typeof UserSchema>;

// Zur Laufzeit parsen und validieren
try {
  const validUser = UserSchema.parse(incomingJson);
} catch (error) {
  // strukturierter Validierungsfehler
}
```

### 4.4 Pydantic (Python) – Stand 2026: Pydantic V2 ist seit 2023 stabil und weiterhin die aktuelle Hauptversion

```python
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, ValidationError

# Hinweis: EmailStr benötigt das Extra-Paket "email-validator"
# (Installation: pip install pydantic[email])

class UserModel(BaseModel):
    id: UUID
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr
    age: int | None = Field(default=None, ge=18)

try:
    valid_user = UserModel.model_validate(incoming_json)
except ValidationError as e:
    print(e.json())
```

---

## 5. API-Sicherheit als Querschnittsthema

> **Grundprinzip:** Sicherheit ist kein separater Schritt am Ende, sondern eine Eigenschaft, die durch alle vorherigen Abschnitte hindurchzieht – vom Protokoll (WS-Security) über die Transportebene (HTTPS) bis zur Validierungsgrenze (Zod/Pydantic).

| Ebene | Maßnahme | Betrifft primär | IHK-Relevanz |
| --- | --- | --- | --- |
| Nachrichtenebene | WS-Security (Verschlüsselung/Signaturen im XML-Header) | SOAP | 🟡 |
| Transportebene | HTTPS/TLS-Verschlüsselung der gesamten Verbindung | REST, gRPC, GraphQL | 🔴 |
| Autorisierung | Token-basierte Auth (z. B. Bearer-Token/JWT) | Alle zustandslosen APIs | 🔴 |
| Cross-Origin-Zugriff | Korrekt konfigurierte **CORS**-Policy (Cross-Origin Resource Sharing) | Browserbasierte REST/GraphQL-Clients | 🔴 |
| Eingabedaten | Backend-seitige Schema-Validierung (Zod/Pydantic) als verpflichtende Schutzschicht gegen fehlerhafte und unerwartete Eingaben | Alle APIs | 🔴 |

**Warum Client-seitige Validierung als alleinige Sicherheitsmaßnahme nicht ausreicht:** Ein Angreifer kann das Frontend vollständig umgehen und Anfragen direkt über Tools wie curl oder Postman an die API senden. Serverseitige Validierung kann er dabei nicht *umgehen* wie das Frontend – der Server prüft jede eingehende Anfrage unabhängig davon, welcher Client sie geschickt hat. Sie ist damit die zentrale, durchsetzbare Sicherheitsschicht (Abschnitt 4), auch wenn sie allein noch keine vollständige Sicherheit garantiert: Schema-Validierung kann unerwartete Eingaben strukturell ablehnen, verhindert aber allein keine kontextabhängigen Injection-Angriffe – gegen SQL-Injection helfen zusätzlich parametrisierte Datenbankabfragen, gegen XSS korrektes Output-Encoding, und gegen unautorisierte Aktionen zusätzliche Berechtigungsprüfungen.

> **IHK-Typfrage:** *"Warum ist eine korrekt konfigurierte CORS-Policy sicherheitsrelevant, und was passiert bei einer Fehlkonfiguration?"*
> **Musterantwort:** CORS ist ein **browserseitig durchgesetzter** Mechanismus – der Server sendet lediglich Header, die dem Browser mitteilen, welche fremden Ursprünge (Domains) zugreifen dürfen; die eigentliche Durchsetzung übernimmt der Browser. Eine gefährliche Fehlkonfiguration liegt z. B. vor, wenn der Server den `Origin`-Header unzureichend prüft, beliebige Ursprünge dynamisch zurückspiegelt und gleichzeitig `Access-Control-Allow-Credentials: true` setzt – dann kann eine fremde Webseite unter Umständen authentifizierte Browseranfragen im Namen des Nutzers auslösen. Wichtig: CORS schützt nicht vor direkten Anfragen außerhalb des Browsers (curl, Postman, eigene Programme) und ersetzt weder Authentifizierung noch CSRF-Schutz.

---

## 6. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Statelessness bedeutet "der Client speichert nichts" | Das Gegenteil: Der **Server** speichert nichts – der Client muss den gesamten benötigten Zustand bei jeder Anfrage mitschicken |
| 2 | SOAP ist "veraltet und wird nicht mehr benutzt" | SOAP ist in bestimmten Enterprise-/Finanzkontexten weiterhin aktiv im Einsatz – "traditionell" heißt nicht "obsolet" |
| 3 | SOAP bietet automatisch ACID-Transaktionen | SOAP selbst garantiert das nicht – Transaktionssicherheit entsteht erst durch zusätzliche WS-*-Erweiterungen (z. B. WS-AtomicTransaction) |
| 4 | REST-APIs müssen JSON zurückgeben | REST schreibt kein Format zwingend vor (auch XML, Text, HTML möglich) – JSON ist nur die in der Praxis dominierende Wahl |
| 5 | REST und JSON sind dasselbe | REST ist ein Architekturstil, JSON nur das gebräuchlichste (aber nicht einzige) Format dafür |
| 6 | gRPC ist "einfach schnelleres REST" | gRPC ist ein eigenständiges RPC-Framework mit eigenem Transport (HTTP/2) und Serialisierungsformat (Protobuf) – kein REST-Derivat |
| 7 | GraphQL ersetzt REST komplett und beseitigt Over-/Under-Fetching vollständig | GraphQL reduziert beides strukturell deutlich, aber nicht automatisch (siehe N+1-Problem) – die Wahl hängt vom Anwendungsfall ab |
| 8 | TypeScript allein reicht für sichere Datenverarbeitung | TypeScript-Typen existieren nur zur Compile-Zeit (Type Erasure) – externe Laufzeitdaten benötigen zusätzlich Runtime-Validierung (Zod) |
| 9 | Client-seitige Validierung ist "unnötig", wenn es Backend-Validierung gibt | Client-seitige Validierung bleibt wichtig für UX (sofortiges Feedback) – sie ersetzt aber nie die sicherheitsrelevante Backend-Validierung |
| 10 | CORS schützt den Server vor Angriffen generell | CORS ist eine **browserseitig durchgesetzte** Maßnahme, die steuert, welche Webseiten per Browser zugreifen dürfen – sie schützt nicht vor direkten Anfragen außerhalb des Browsers (z. B. curl) und ersetzt keine Authentifizierung/CSRF-Schutz |

---

## 7. Deep-Dive-Ausblick (freiwillig)

- **HTTP/2-Multiplexing** (→ Kapitel 1, HTTP-Grundlagen): Wie HTTP/2 mehrere Anfragen/Antworten gleichzeitig über eine einzige TCP-Verbindung sendet (Multiplexing) und dadurch Head-of-Line-Blocking auf HTTP-Ebene vermeidet – Grundlage für gRPC-Streaming.
- **UML-Sequenzdiagramme** (→ Kapitel 1.4): Wie Lifelines, Aktivierungsbalken und Nachrichtenpfeile den zeitlichen Ablauf von Client-Server-Interaktionen inklusive Fehlerfällen (z. B. `422 Unprocessable Entity`, Timeouts) darstellen.
- **Enterprise Integration Patterns / API-Gateways** (→ Kapitel 2, SOAP vs. REST): Wie API-Gateways als "Übersetzer" zwischen modernen REST/JSON-Clients und Legacy-SOAP/XML-Backends fungieren.
- **HTTP/3 (QUIC)** (→ Kapitel 3.1, gRPC): Wie das neuere HTTP/3-Protokoll das TCP-eigene Head-of-Line-Blocking auflöst, von dem auch HTTP/2-basiertes gRPC unter schlechten Netzwerkbedingungen betroffen sein kann.
- **Type Coercion** (→ Kapitel 4, Validierung): Chancen und Risiken automatischer Typkonvertierung in Zod/Pydantic (z. B. String `"123"` → Zahl `123`) – praktisch, aber bei zu laxer Konfiguration eine mögliche Fehlerquelle.

---

## 8. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Was muss laut Statelessness-Prinzip bei jeder Anfrage mitgeschickt werden? | Alle Informationen, die der Server zur Verarbeitung benötigt (z. B. Auth-Token, Daten) |
| 2 | Welches Dokument definiert bei SOAP den strikten Vertrag zwischen Client und Server? | WSDL (Web Services Description Language) |
| 3 | Nenne zwei der sechs REST-Constraints. | z. B. Statelessness, Uniform Interface, Client-Server, Cacheability, Layered System, Code-on-Demand |
| 4 | Welches Serialisierungsformat verwendet gRPC, und warum ist es schneller als JSON? | Protocol Buffers (Protobuf) – binäres statt textbasiertes Format, dadurch kompakter und schneller zu parsen |
| 5 | Was ist der Unterschied zwischen Over-Fetching und Under-Fetching? | Over-Fetching: mehr Daten als benötigt; Under-Fetching: mehrere Anfragen nötig für verknüpfte Daten |
| 6 | Was bedeutet "Type Erasure" bei TypeScript? | Typinformationen existieren nur zur Compile-Zeit und verschwinden nach dem Kompilieren zu JavaScript vollständig |
| 7 | Warum ist Client-seitige Validierung als alleinige Sicherheitsmaßnahme unzureichend? | Sie lässt sich umgehen (z. B. über curl/Postman direkt an die API) |
| 8 | Welche Bibliothek wird typischerweise für Runtime-Validierung in Python-Backends verwendet? | Pydantic |
| 9 | Was regelt eine CORS-Policy? | Welche fremden Ursprünge (Domains) per Browser auf die API zugreifen dürfen |
| 10 | Nenne einen Vorteil von HTTP/2 gegenüber HTTP/1.1 für die API-Kommunikation. | Multiplexing – mehrere Anfragen/Antworten über eine einzige TCP-Verbindung, kein Head-of-Line-Blocking mehr auf HTTP-Ebene. **Wichtig:** Das TCP-eigene Head-of-Line-Blocking bleibt bestehen – geht ein TCP-Paket verloren, können weiterhin mehrere Streams betroffen sein (siehe Deep-Dive HTTP/3) |
| 11 | Ein Sensor-System muss extrem viele kleine Nachrichten mit minimaler Latenz übertragen. Welches API-Paradigma ist eine plausible Wahl, und warum? | gRPC ist eine naheliegende Option – binäre Protobuf-Serialisierung und HTTP/2-Multiplexing minimieren Overhead und Latenz gegenüber textbasiertem JSON/REST. Die endgültige Wahl hängt aber zusätzlich von Faktoren wie Client-Vielfalt und vorhandener Infrastruktur ab (z. B. wäre MQTT bei reiner Sensor-zu-Broker-Kommunikation ebenfalls denkbar) |

---

## 9. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Statelessness** | Server speichert keinen Client-Kontext zwischen Anfragen |
| **WSDL** | XML-Vertragsdokument, das eine SOAP-Schnittstelle strikt vorab definiert |
| **REST-Constraints** | Sechs Architekturprinzipien, u. a. Statelessness, Uniform Interface, Cacheability |
| **Protobuf** | Binäres Serialisierungsformat von gRPC – kompakter und schneller als JSON |
| **Over-/Under-Fetching** | Zu viele bzw. zu wenige Daten pro REST-Anfrage – von GraphQL strukturell vermieden |
| **Type Erasure** | Verschwinden von Compile-Time-Typinformationen nach dem Kompilieren |
| **Runtime-Validierung** | Prüfung eingehender Daten zur Laufzeit (Zod/Pydantic), unabhängig von Compile-Time-Typen |
| **CORS** | Browser-Mechanismus, der Cross-Origin-Zugriffe auf eine API steuert |
| **WS-Security** | Sicherheitsstandard für SOAP-Nachrichten (Verschlüsselung/Signaturen im XML-Header) |
| **JWT** | Signiertes Tokenformat, häufig für zustandsarme Authentifizierung/Autorisierung verwendet – ersetzt nicht automatisch sichere Token-Verwaltung oder Widerrufsmechanismen |
| **Idempotenz** | Mehrfache Ausführung führt zum gleichen beabsichtigten Endzustand wie eine einmalige Ausführung – Antwortstatus/Nebenwirkungen müssen dabei nicht identisch sein (z. B. liefert ein zweites `DELETE` oft `404` statt `200`, der Endzustand "gelöscht" bleibt aber gleich). Typischerweise gelten `GET`, `PUT`, `DELETE` als idempotent; `POST` typischerweise nicht |

---

## 10. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Begriffsabgrenzung | "Erläutern Sie den Unterschied zwischen SOAP und REST" | Klare Kriterien (Format, Kopplung, Contract-First vs. ressourcenorientiert), keine reine Meinungsaussage |
| Architekturentscheidung | "Welches API-Paradigma empfehlen Sie für Szenario X?" | Abwägung mit mind. zwei Kriterien (z. B. Latenzanforderung, Client-Vielfalt, Browserfähigkeit, vorhandene Infrastruktur), begründete Entscheidung – keine Technologie ist "grundsätzlich die beste" |
| Sicherheitsbegründung | "Warum reicht Client-seitige Validierung nicht aus?" | Konkreter Umgehungsweg nennen (curl/Postman), nicht nur "ist unsicher" |
| Schema-/Vertragsentwurf | "Entwerfen Sie ein Zod-/Pydantic-Schema für …" | Korrekte Typen, Constraints (min/max, Formate) und Pflichtfeld-Kennzeichnung |
| Transferfrage | "Wie würden Sie die API bei 10x mehr gleichzeitigen Nutzern skalieren?" | Bezug auf Statelessness + horizontale Skalierung (Load Balancer, austauschbare Server), nicht nur "mehr Server" |

---

## 11. Merksätze für das Fachgespräch

> Eine API ist ein Vertrag, keine Vermutung – der Server darf nur das annehmen, was der Vertrag (Schema) explizit erlaubt.

> Statelessness heißt: Der Server vergisst dich bei jeder Anfrage neu – deshalb muss der Client sich selbst "erinnern" und alles Nötige mitschicken.

> SOAP und REST unterscheiden sich nicht nur im Format (XML/JSON), sondern in der Denkweise: Methoden aufrufen vs. Ressourcen adressieren.

> gRPC macht die Übertragung schnell, GraphQL macht die Abfrage präzise – beides sind unterschiedliche Antworten auf unterschiedliche Probleme.

> Client-seitige Validierung ist Komfort, Backend-Validierung ist Sicherheit – und nur Letzteres kann nicht umgangen werden.

---

```yaml
dokument: LF8.4-wiki-artikel
lernfeld: LF8.4
titel: "Verteilte Systeme, API-Paradigmen & Datenvalidierung"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-07
quellen_intern:
  - "LF8.4.1: API Fundamentals & Statelessness.md"
  - "LF8.4.2: Traditional & Resource-Oriented APIs.md"
  - "LF8.4.3: High-Performance & Query-Driven APIs.md"
  - "LF8.4.4: Data Validation Boundaries (Zod & Pydantic).md"
quellen_fachlich:
  - titel: "Zod (npm-Paket)"
    herausgeber: "Colin McDonnell / npm-Registry"
    status: "Zod 4.x aktuelle Hauptversion, stabil seit Mai 2025 (exakte Patch-Version bei Bedarf gegen npm/Doku erneut prüfen)"
  - titel: "Pydantic Version Policy"
    herausgeber: "Pydantic-Team"
    status: "Pydantic V2 stabil seit 2023, weiterhin aktuelle Hauptversion (Stand 2026)"
  - titel: "Protocol Buffers (proto3)"
    herausgeber: "Google"
    status: "aktuelles IDL/Serialisierungsformat für gRPC"
  - titel: "HTTP/2 (RFC 9113) / HTTP/3 (RFC 9114)"
    herausgeber: "IETF"
    status: "aktuelle Transportprotokoll-Standards"
  - titel: "gRPC FAQ (grpc.io)"
    herausgeber: "gRPC-Projekt / CNCF"
    status: "offizielle Klarstellung zur Namensauflösung ('gRPC Remote Procedure Calls')"
review_historie:
  - runde: 1
    datum: 2026-09-07
    ergebnis: "Erstdraft mit integrierter Web-Verifikation (Zod-/Pydantic-Versionsstand) und eigener Review nach Style-Guide-Checkliste erstellt – inkl. Typische Prüfungsfallen und Deep-Dive-Ausblick von Anfang an"
  - runde: 2
    datum: 2026-09-07
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet: gRPC-Namensauflösung korrigiert (verifiziert, echter Fehler), SOAP-ACID-Überbehauptung entschärft, CORS-Beispiel technisch korrigiert (Wildcard+Credentials funktioniert nicht wie ursprünglich dargestellt), Zod-Codebeispiel auf aktuelle Top-Level-Validatoren aktualisiert, fehlenden ValidationError-Import im Pydantic-Beispiel behoben, GraphQL Over-/Under-Fetching-Aussage samt N+1-Problem präzisiert, HTTP/2-HOL-Blocking-Aussage um TCP-Ebene ergänzt, REST-Constraints/Code-on-Demand als optional gekennzeichnet, Statuscodes 403/422 und PATCH-Methode ergänzt, JWT-Definition entschärft, Vergleichsdiagramm REST/gRPC/GraphQL ergänzt (Skill-Pflichtelement 'Zyklus-/Vergleichsdiagramme')"
  - runde: 3
    datum: 2026-09-07
    ergebnis: "Finale Review (3 Reviews) geprüft: Statuscode-Tabelle sauber in zwei Tabellen aufgeteilt (statt leerer Erstspalten-Zeilen), Idempotenz-Definition auf Endzustand statt identische Antwort präzisiert, REST-Constraints als 'Kern, in der Praxis oft nicht vollständig umgesetzt' statt 'verpflichtend' formuliert, SOAP-Contract-First als typisches statt zwingendes Vorgehen dargestellt, Injection-Schutz über SQL hinaus verallgemeinert (auch XSS/Autorisierung), gRPC-Namenserklärung didaktisch gekürzt, Zod-Beispiel um z.strictObject()-Hinweis ergänzt und Kommentar entschärft. Hinweis: Ein Review meldete beschädigte Tabellen/YAML – beim Abgleich mit der tatsächlichen Datei nicht bestätigt (vermutlich Übertragungsartefakt beim Reviewer), daher nicht blind übernommen, aber das zugrunde liegende Strukturproblem (Statuscode-Tabelle) war real und wurde behoben"
freigabe: "Final gesetzt nach 3 Review-Runden (2026-09-07) – Freigabe durch Autor:in bestätigt"
```