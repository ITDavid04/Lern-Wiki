# LF8.6 – Code-Qualität, Statische/Dynamische Sicherheitstests & Test-Strategien

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1 (schriftlich), Transferfragen in AP2 und Fachgespräch möglich
> **Lernzeit:** Ca. 100–130 Minuten reines Lesen, +80–110 Minuten mit Aufgaben – abhängig von Vorkenntnissen und Bearbeitungstiefe
> **Status:** Final
> **Stand:** 2026
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was unterscheidet Formatting, Linting und Static Code Analysis, und wie erzwingt ein Quality Gate definierte Qualitätskriterien? | [→ 1. Code-Qualität & SAST](#1-code-qualität-linting-und-sast) |
| 2 | Was unterscheidet SAST von DAST, und wie schützen CORS/HTTP-Security-Header eine laufende Anwendung? | [→ 2. DAST & Runtime-Sicherheit](#2-dast-und-runtime-sicherheit) |
| 3 | Was unterscheidet einen Stub von einem Mock, und warum sollten Unit-Tests keine unkontrollierten Zugriffe auf externe Systeme durchführen? | [→ 3. Test Doubles](#3-test-doubles-mocking-vs-stubbing) |
| 4 | Wie ergänzen sich automatisiertes Integrationstesten und exploratives Testen, und was gehört in ein aussagekräftiges Abnahmeprotokoll? | [→ 4. Integrations- & Exploratives Testen](#4-integrations--und-exploratives-testen) |
| 5 | Wie greifen Quality Gates, DAST-Scans, Test Doubles und Sign-off in einer durchgängigen CI/CD-Pipeline ineinander? | [→ 5. Der Verifikations-Zyklus](#5-der-verifikations-zyklus-in-der-cicd-pipeline) |

---

## 1. Code-Qualität, Linting und SAST

> **Grundprinzip:** In einer Werkstatt gibt es mehrere Kontrollstufen, bevor ein Werkstück ausgeliefert wird – die optische Endkontrolle prüft nur das Erscheinungsbild, die Funktionsprüfung testet auf Fehlfunktion, und ein strukturelles Materialgutachten prüft die Statik. Formatting, Linting und Static Code Analysis übernehmen genau diese drei unterschiedlichen Rollen im Code.

### 1.1 Formatting vs. Linting vs. Static Code Analysis

| Ebene | Fokus | Beispiel-Tool | IHK-Relevanz |
| --- | --- | --- | --- |
| **Code Formatting** | Rein optisches Erscheinungsbild (Einrückung, Anführungszeichen, Zeilenumbrüche) – soll das Programmverhalten nicht verändern | Prettier | 🔴 |
| **Code Linting** | Programmatische Auffälligkeiten und potenzielle Bugs im Quellcode (ungenutzte Variablen, unerreichbarer Code, doppelt deklarierte Funktionen) | ESLint, Ruff, Flake8 | 🔴 |
| **Static Code Analysis** | Tiefere, abstrakte Auswertung über einen Syntaxbaum: Metriken wie kognitive Komplexität, Duplizierung, Sicherheitslücken – Plattformen wie SonarQube führen diese Ergebnisse zusätzlich mit einer *durch Testausführung ermittelten und importierten* Code-Coverage zusammen (Coverage selbst wird nicht durch statische Analyse berechnet) | SonarQube, SonarCloud | 🔴 |

> **IHK-Typfrage:** *"Zeigen Sie an einem Beispiel, wie ein Linter einen Laufzeitfehler verhindern kann, während ein Formatter nur die optische Konsistenz sicherstellt."*
> **Musterantwort:** Ein Formatter würde z. B. `if(x==y){return true}` lediglich in eine einheitlich eingerückte, mit Leerzeichen versehene Form bringen – die Logik bleibt unverändert. Ein Linter dagegen erkennt inhaltliche Auffälligkeiten wie unerreichbaren Code nach einem `return`-Statement oder in JavaScript den unsicheren Vergleichsoperator `==` statt `===`, der durch implizite Typumwandlung zu unerwarteten Vergleichsergebnissen und damit zu einem fachlichen Fehler führen kann – ein Formatter würde beides unverändert lassen, da beide Fälle syntaktisch korrekt sind.

### 1.2 SAST, Code Smells und technische Schulden

**Static Application Security Testing (SAST)** ist eine White-Box-Testmethode: Sie analysiert den Quellcode selbst, bevor die Anwendung gebaut oder ausgeführt wird, um Sicherheitslücken zu identifizieren.

| Begriff | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Code Smell** | Merkmal im Code, das auf ein tieferes architektonisches Problem hindeutet (Duplizierter Code, überlange Funktionen, riesige Klassen) – kein akuter Bug, aber erschwert Wartbarkeit | 🔴 |
| **Technische Schulden (Technical Debt)** | Metapher für die implizierten Kosten künftiger Nacharbeit, die entstehen, wenn jetzt eine schnelle, minderwertige Lösung statt einer sauberen Architektur gewählt wird | 🔴 |
| **SAST-Nutzen** | Scannt automatisiert nach bekannten Schwachstellen (hartcodierte Zugangsdaten, unsichere reguläre Ausdrücke); Analyseplattformen wie SonarQube schätzen für gefundene Probleme zusätzlich einen Behebungsaufwand (technische Schulden in Stunden) | 🔴 |

### 1.3 Quality Gates (am Beispiel SonarQube)

Professionelle Analyseplattformen erlauben, **Quality Gates** zu definieren – vordefinierte Schwellenwerte, die ein Projekt bestehen muss, bevor gemergt werden darf:

```text
[ Code-Änderung / Commit ]
           |
           v
[ Statischer Scanner / SAST + importierter Testreport ]
           |
           +---> Auswertung: Coverage (aus Testreport), Duplizierung (%), Komplexität, Bugs, Security
           |
           v
[ Quality-Gate-Auswertung ]
           |
           +---> BESTANDEN: Merge/Deploy erlaubt
           +---> DURCHGEFALLEN: Pipeline blockiert, Team benachrichtigt
```

Typische Quality-Gate-Bedingungen:

- **Neue Code-Coverage:** muss ≥ 80 % sein
- **Duplizierte Zeilen:** müssen ≤ 3 % sein
- **Security Vulnerabilities:** müssen exakt 0 sein

> **IHK-Typfrage:** *"Ein Entwickler reicht einen Pull Request mit hartcodiertem Datenbank-Passwort und einem gegen ReDoS (Regular Expression Denial of Service) anfälligen regulären Ausdruck ein. Wie würde ein SAST-Tool diesen Code analysieren?"*
> **Musterantwort:** Das SAST-Tool scannt den Quellcode gegen eine Regelbibliothek bekannter Schwachstellenmuster – ein hartcodiertes Passwort wird als "Hardcoded Credentials"-Finding markiert, der riskante reguläre Ausdruck als potenzielles ReDoS-Muster (z. B. verschachtelte Quantifizierer). Beide Findings werden mit Schweregrad und geschätztem Behebungsaufwand (technische Schulden in Stunden) im Quality-Gate-Report ausgewiesen; bei aktivierter "Security Vulnerabilities = 0"-Bedingung blockiert das den Merge automatisch, und das Team erhält eine automatisierte Rückmeldung im Pull Request.

---

## 2. DAST und Runtime-Sicherheit

> **Grundprinzip:** SAST ist wie eine Bauplan-Prüfung, bevor das Haus gebaut wird – DAST ist wie ein Einbruchstest am fertigen Gebäude: Ein Prüfer versucht von außen, Fenster und Türen zu öffnen, ohne die Baupläne zu kennen.

### 2.1 SAST vs. DAST

Während SAST den passiven Quellcode prüft, ist **DAST (Dynamic Application Security Testing)** eine Black-Box-Methode: Sie analysiert eine *laufende* Anwendung von außen, ohne Zugriff auf den Quellcode – vergleichbar mit einem Angreifer, der bösartige Payloads, fehlerhafte Anfragen und Fuzzing-Vektoren gegen aktive Netzwerk-Ports, APIs und Web-Oberflächen schickt.

| Merkmal | SAST (Statisch) | DAST (Dynamisch) |
| --- | --- | --- |
| Perspektive | White-Box (Innen nach außen) | Black-Box (Außen nach innen) |
| Ziel | Quellcode, teilweise kompilierter Code | Laufende Anwendung |
| Findet | Unsichere Datenflüsse, riskante Codekonstruktionen, bestimmte Implementierungsfehler | Laufzeitbezogene Schwachstellen und Fehlkonfigurationen (potenziell oder bestätigt ausnutzbar) |
| Zeitpunkt | Compile-Zeit / Pipeline | Laufzeit / nach Deployment |

> **Abgrenzung zu SCA:** Die Suche nach bekannten Schwachstellen (CVEs) in eingesetzten **Drittanbieter-Bibliotheken** ist eine eigene Prüfkategorie, **Software Composition Analysis (SCA)** – nicht SAST. Manche Plattformen bieten beide Funktionen an, fachlich bleiben es getrennte Verfahren: SAST prüft den eigenen Code, SCA die verwendeten fremden Komponenten, DAST das Laufzeitverhalten.

> Manche Laufzeitprobleme kann SAST nicht zuverlässig erkennen – etwa tatsächlich ausgelieferte HTTP-Header oder eine erst in der Deployment-Umgebung entstehende CORS-Fehlkonfiguration. Statische Werkzeuge können zwar bestimmte Konfigurationsmuster im Code finden (z. B. fest codierte, offensichtlich unsichere CORS-Einstellungen), das tatsächliche Verhalten der laufenden, ausgelieferten Anwendung prüft aber nur DAST. Deshalb ergänzen sich SAST und DAST, statt sich zu ersetzen.

### 2.2 Aktives vs. passives Scanning

Ein verbreitetes Open-Source-Werkzeug in diesem Bereich ist **ZAP** – früher häufig als "OWASP ZAP" bezeichnet; das Projekt hat OWASP 2023 verlassen (Details siehe Quellenangabe). ZAP prüft laufende Anwendungen mit zwei unterschiedlichen Methoden:

| Methode | Verhalten | Risiko | IHK-Relevanz |
| --- | --- | --- | --- |
| **Passives Scanning** | Beobachtet nur den fließenden Netzwerkverkehr, verändert keine Anfragen – prüft z. B. auf fehlende `HttpOnly`/`Secure`-Cookie-Flags, schwache Security-Header, geleakte Serverinformationen | Geringes scanbedingtes Risiko, da Anfragen/Antworten nicht verändert werden | 🔴 |
| **Aktives Scanning** | Konstruiert und sendet aktiv bösartige Anfragen (SQL-Injection, XSS, Path Traversal, Parameter Tampering) | **Kann Datenkorruption oder Systemabstürze verursachen** – gehört grundsätzlich in eine isolierte Staging-/Testumgebung; gegen Produktionssysteme nur in ausdrücklich autorisierten, eng begrenzten Ausnahmefällen mit Schutz- und Abbruchmaßnahmen | 🔴 |

### 2.3 Runtime-Sicherheitsgrenzen: CORS & HTTP-Header

- **CORS (Cross-Origin Resource Sharing):** Ein HTTP-basierter Mechanismus, mit dem ein Server dem Browser mitteilt, welche fremden Ursprünge auf eine Ressource zugreifen dürfen – CORS lockert damit **kontrolliert** die browsereigene **Same-Origin Policy**, die Cross-Origin-Zugriffe standardmäßig einschränkt. CORS verhindert nicht, dass eine Anfrage überhaupt gesendet wird; es steuert vor allem, ob das anfragende JavaScript die Antwort auslesen darf. Für Anfragen mit Credentials (Cookies) darf `Access-Control-Allow-Origin` nicht `*` sein – Browser blockieren diese Kombination ohnehin; das eigentlich gefährliche Muster ist meist ein Server, der den angefragten `Origin`-Header ungeprüft zurückspiegelt und gleichzeitig Credentials erlaubt.

| HTTP-Security-Header | Zweck | IHK-Relevanz |
| --- | --- | --- |
| `Content-Security-Policy` (CSP) | Schränkt ein, von wo Skripte/Styles/Bilder geladen werden dürfen – mindert XSS | 🔴 |
| `Strict-Transport-Security` (HSTS) | Zwingt Browser, ausschließlich verschlüsselt per HTTPS zu kommunizieren | 🔴 |
| `X-Frame-Options` | Beschränkt mit `DENY` (kein Framing) oder `SAMEORIGIN` (nur eigene Herkunft), ob eine Seite in ein `<iframe>` eingebettet werden darf – mindert Clickjacking. Moderne Anwendungen steuern das zusätzlich oder bevorzugt über CSP `frame-ancestors` | 🟡 |

> **IHK-Typfrage:** *"Warum funktioniert `Access-Control-Allow-Origin: *` nicht für Anfragen mit Credentials, und welche CORS-Fehlkonfiguration kann stattdessen private Nutzerdaten gefährden?"*
> **Musterantwort:** Browser verweigern die Kombination aus `Access-Control-Allow-Origin: *` und `Access-Control-Allow-Credentials: true` grundsätzlich – bei Anfragen mit Credentials muss der Server stattdessen einen konkreten, erlaubten Origin zurückgeben. Gefährlich wird es, wenn ein Server den angefragten `Origin`-Header ungeprüft dynamisch zurückspiegelt und gleichzeitig Credentials erlaubt: Dann kann jede beliebige bösartige Webseite als vermeintlich erlaubter Origin behandelt werden und im Namen eines eingeloggten Nutzers geschützte Antworten auslesen.

---

## 3. Test Doubles: Mocking vs. Stubbing

> **Grundprinzip:** Ein Stub ist wie ein Brühwürfel in der Küche – er liefert ein vorhersehbares, "eingedostes" Ergebnis, ohne dass wirklich stundenlang echte Brühe gekocht werden muss. Ein Mock ist eher wie ein Küchenchef, der genau protokolliert, ob die Kommis exakt 200 g Butter und nicht mehr verwendet haben – es geht um die Kontrolle des *Vorgangs*, nicht nur um das Ergebnis.

### 3.1 Testisolation und die Gefahr unkontrollierter externer Netzwerkaufrufe

**Unit-Tests** müssen schnell, deterministisch und wiederholbar sein. Läuft ein Unit-Test gegen echte externe Abhängigkeiten (Live-APIs, entfernte Datenbanken), verletzt das diese Eigenschaften:

| Problem | Beschreibung | IHK-Relevanz |
| --- | --- | --- |
| **Flakiness** | Ist die externe API offline, schlägt die Testsuite fehl – selbst wenn der eigene Code fehlerfrei ist | 🔴 |
| **Geschwindigkeit** | Netzwerklatenzen verlangsamen die Testausführung erheblich | 🟡 |
| **Nebenwirkungen** | Tests könnten versehentlich Datenmüll in eine echte Produktionsdatenbank schreiben oder kostenpflichtige externe API-Aufrufe auslösen | 🔴 |

Die Lösung: Externe Abhängigkeiten werden in **Unit-Tests** durch **Test Doubles** isoliert. Das gilt nicht für automatisierte Tests generell: **Integrationstests** (Kapitel 4.1) sollen und müssen bewusst über echte Schnittstellen mit *kontrollierten* Testinstanzen kommunizieren – nur produktive Fremdsysteme oder unkontrollierte Live-APIs sind dabei zu vermeiden.

### 3.2 Stubs vs. Mocks: Zustand vs. Verhalten

"Mock" wird umgangssprachlich oft als Sammelbegriff für jeden Test Double verwendet – fachlich wird aber strikt unterschieden:

```text
                  +--------------------------------+
                  |          Test Doubles           |
                  +--------------------------------+
                 /                                  \
     [ Stubs ]                                    [ Mocks ]
     - Zustandsverifikation                       - Verhaltensverifikation
     - liefert vorgefertigte Antworten             - prüft Interaktionen
     - "Wie verhält sich das System,                - "Hat das System die richtige
        wenn die DB X zurückgibt?"                     Methode mit den richtigen
                                                        Parametern aufgerufen?"
```

| Test Double | Zweck | IHK-Relevanz |
| --- | --- | --- |
| **Stub** | Liefert vorgefertigte ("eingedoste") Antworten auf Methodenaufrufe – simuliert Zustand, steuert den Testablauf | 🔴 |
| **Mock** | Verifiziert Interaktionen: welche Methoden wie oft und mit welchen Parametern aufgerufen wurden | 🔴 |

```typescript
// Hinweis zur Terminologie: Viele Mocking-Frameworks bezeichnen ein aufzeichnendes
// Test Double wie unten umgangssprachlich als "Mock". In der strengeren, von Fowler
// geprägten Terminologie ist ein Objekt, das Aufrufe nachträglich protokolliert und
// erst danach geprüft wird, eher ein Spy (siehe Deep-Dive). Ein "echtes" Mock im engeren
// Sinn wird bereits vor der Ausführung mit den erwarteten Interaktionen programmiert.
class EmailServiceMock {
    private sendCallsCount = 0;
    private lastRecipient = "";

    public sendEmail(to: string, subject: string) {
        this.sendCallsCount++;
        this.lastRecipient = to;
    }

    public verifyWasSentTo(recipient: string): boolean {
        return this.sendCallsCount === 1 && this.lastRecipient === recipient;
    }
}
```

> **IHK-Typfrage:** *"Ein Alarmsystem löst bei Überschreiten eines Temperaturschwellwerts eine E-Mail-Benachrichtigung über einen `NotificationService` aus. Sie möchten testen, dass die E-Mail genau einmal mit der korrekten Empfängeradresse gesendet wird. Stub oder Mock?"*
> **Musterantwort:** Mock – hier geht es nicht um einen simulierten Rückgabewert (Zustand), sondern um die Verifikation, *dass* und *wie* eine Interaktion stattgefunden hat (genau ein Aufruf, korrekter Empfänger). Ein `NotificationServiceMock` zeichnet Aufrufanzahl und Parameter auf, ohne einen echten Netzwerkaufruf zu tätigen, und stellt eine Prüfmethode (`verifyWasSentTo`) zur Verfügung.

---

## 4. Integrations- und Exploratives Testen

> **Grundprinzip:** Automatisierte Tests sind wie ein fester Gießplan im Gewächshaus – zuverlässig, wiederholbar, aber blind für alles, was außerhalb des Plans passiert. Exploratives Testen ist die Gärtnerin, die zusätzlich durch die Reihen geht und nach Schädlingen sucht, die kein Plan vorhergesehen hat.

### 4.1 Automatisiertes Integrationstesten

Während Unit-Tests einzelne Klassen/Funktionen isoliert prüfen, verifizieren **Integrationstests**, dass mehrere Komponenten, Microservices, Datenbanken oder Systeme korrekt als Gesamtsystem zusammenspielen.

| Testart | Prüft | Beispiel-Tools | IHK-Relevanz |
| --- | --- | --- | --- |
| **API-Integrationstest** | Ob API-Endpunkte Anfragen korrekt verarbeiten, Geschäftslogik durchlaufen und Datenbanken lesen/schreiben | Pytest mit HTTP-Client | 🔴 |
| **UI-Integrationstest** | Ob einzelne UI-Bausteine im Zusammenspiel mit (teils gemockter) Logik korrekt auf Zustandsänderungen/Dateneingaben reagieren | Vitest mit Testing Library (Komponentenebene) | 🔴 |
| **End-to-End-Test (E2E)** | Ob die Anwendung als Ganzes – vollständiger Browser, reale HTTP-Aufrufe gegen eine Testumgebung – korrekt funktioniert; eine eigene, umfassendere Teststufe als der reine UI-Integrationstest | Playwright | 🟡 |

### 4.2 Exploratives Testen und Testing Charters

Automatisierte Tests können nur Szenarien prüfen, die Entwickler:innen bereits antizipiert und codiert haben. **Exploratives Testen** ist ein menschengetriebener, kreativer Prozess aus gleichzeitigem Lernen, Testdesign und Testausführung – Tester:innen untersuchen das laufende System gezielt auf unerwartete Grenzfälle, logische Lücken und Bedienprobleme.

Um dabei nicht in chaotisches "Ad-hoc-Klicken" abzugleiten, werden Sessions über eine **Testing Charter** strukturiert:

- **Explore:** [Zielbereich/Feature]
- **With:** [Ressourcen, Rollen, Tools]
- **To Discover:** [konkrete Information, Schwachstellen, Usability-Probleme]

Dokumentiert werden Session-Dauer (üblich: 60–90 Minuten), die eingeschlagenen Pfade, gefundene Bugs (mit Reproduktionsschritten) und UX-Auffälligkeiten.

### 4.3 Abnahmeprotokoll (Sign-Off)

Rechtlich entscheidend ist die **Abnahme** selbst, nicht zwingend ein bestimmtes Dokument – eine Abnahme kann je nach Vertrag ausdrücklich, konkludent oder unter bestimmten gesetzlichen Voraussetzungen auch fingiert erfolgen. Das **Abnahmeprotokoll** dokumentiert das Ergebnis dieser Abnahme: den geprüften Leistungsstand, bekannte Mängel, Vorbehalte, Fristen und die Erklärungen der Parteien. Ein von beiden Seiten unterschriebenes Protokoll hat eine wichtige **Beweisfunktion**, ist aber nicht in jedem Fall die alleinige Voraussetzung für eine wirksame Abnahme.

Ein professionelles Abnahmeprotokoll enthält typischerweise:

- **Projekt-Metadaten:** Name, Version, Datum, Beteiligte
- **Testzusammenfassung:** bestandene/fehlgeschlagene Testfälle, offene Bugs, verbleibende Risiken
- **Dokumentierter Status:** z. B. Abnahme ohne festgestellte Mängel, Abnahme unter Dokumentation unwesentlicher Mängel/Vorbehalte, oder begründete Verweigerung der Abnahme
- **Unterschriften/Erklärungen:** beider Parteien, mit wichtiger Beweisfunktion für den dokumentierten Stand

> Diese drei Statusangaben sind eine verbreitete **praktische Dokumentationsform**, keine abschließende gesetzliche Kategorisierung. Wegen unwesentlicher Mängel darf eine Abnahme im deutschen Werkvertragsrecht (§ 640 BGB) grundsätzlich nicht verweigert werden; die Vergütung wird nach § 641 BGB grundsätzlich mit der Abnahme fällig. Für die Prüfung reicht das praktische Grundverständnis – bei rechtlichen Detailfragen ist im Zweifel der konkrete Vertrag bzw. juristischer Rat maßgeblich.

> **IHK-Typfrage:** *"Nennen Sie drei in der Praxis übliche Statusangaben eines Abnahmeprotokolls und erläutern Sie deren typische Auswirkungen."*
> **Musterantwort:** (1) **Abnahme ohne festgestellte Mängel** – die Leistung wird abgenommen, weitere Rechtsfolgen (u. a. Fälligkeit der Vergütung) richten sich nach Vertrag und Gesetz. (2) **Abnahme unter Dokumentation unwesentlicher Mängel/Vorbehalte** – die Abnahme erfolgt trotzdem, Mängel und Behebungsfristen werden protokolliert (eine Abnahme darf wegen unwesentlicher Mängel grundsätzlich nicht verweigert werden). (3) **Begründete Verweigerung der Abnahme** – die Leistung wird zunächst nicht abgenommen, der Auftragnehmer muss in der Regel nachbessern. Diese drei Statusangaben sind eine praktische Dokumentationsform, keine abschließende gesetzliche Kategorisierung.

---

## 5. Der Verifikations-Zyklus in der CI/CD-Pipeline

> **Grundprinzip:** Wie an einem Fließband mit mehreren Qualitätskontrollstationen durchläuft Code auf dem Weg zur Produktion mehrere unabhängige Prüfstufen – jede mit einer anderen Perspektive auf mögliche Fehler.

Die in diesem Artikel behandelten Bausteine sind kein Sammelsurium unabhängiger Themen, sondern typische Stationen einer durchgängigen Verifikationskette:

```text
[ Commit / Pull Request ]
           |
           v
[ SAST + Quality Gate ] --- FAIL ---> Pipeline blockiert (Kapitel 1)
           | PASS
           v
[ Unit-Tests (Test Doubles) + Integrationstests (kontrollierte Testinstanzen) ] --- FAIL ---> Pipeline blockiert (Kapitel 3, 4.1)
           | PASS
           v
[ Deployment auf Staging-Umgebung ]
           |
           v
[ DAST-Scan (passiv + aktiv) ] --- FAIL bei Medium/High ---> Deployment blockiert (Kapitel 2)
           | PASS
           v
[ Exploratives Testen (Testing Charter) ] (Kapitel 4.2)
           |
           v
[ Abnahmeprotokoll / Sign-Off ] (Kapitel 4.3)
           |
           v
[ Produktions-Deployment ]
```

Wichtig für die Prüfung: **Automatisierte Gates (SAST/DAST/Tests) und menschliches exploratives Testen ersetzen sich nicht gegenseitig.** Automatisierte Prüfungen sind schnell, wiederholbar und decken bekannte Muster ab; exploratives Testen findet, wonach niemand explizit gesucht hat. Ein vollständiges Qualitätssicherungskonzept für kritische Systeme (z. B. Finanztransaktions-APIs) kombiniert typischerweise beide Ebenen, bevor ein Abnahmeprotokoll unterschrieben wird.

---

## 6. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Formatting und Linting sind dasselbe | Formatting ändert nur das Erscheinungsbild, Linting erkennt inhaltliche/logische Probleme – ein Formatter kann keinen Bug verhindern |
| 2 | Ein Code Smell ist automatisch ein Bug | Ein Code Smell deutet auf ein architektonisches Problem hin, ist aber kein akuter Fehler – er erschwert nur künftige Wartung |
| 3 | SAST findet alle Sicherheitslücken | SAST prüft nur den Quellcode – Laufzeit-spezifische Lücken (Header-Fehlkonfiguration, aktive CORS-Bypässe) sind nur per DAST erkennbar |
| 4 | Aktives DAST-Scanning ist gegen jede Umgebung sicher einsetzbar | Aktives Scanning kann Datenkorruption/Abstürze verursachen – nur gegen isolierte Staging-/Testumgebungen, nie gegen Produktionssysteme |
| 5 | "Mock" und "Stub" sind austauschbare Begriffe | Ein Stub liefert nur vorgefertigte Antworten (Zustandsverifikation), ein Mock prüft zusätzlich, *ob* und *wie* eine Interaktion stattfand (Verhaltensverifikation) |
| 6 | Automatisierte Tests dürfen grundsätzlich keine echten Netzwerkaufrufe machen | Das gilt für **Unit-Tests** (Isolation nötig). **Integrationstests** dürfen und sollen bewusst über echte Schnittstellen mit kontrollierten Testinstanzen kommunizieren – vermieden werden müssen nur unkontrollierte Live-Systeme/Produktivdaten |
| 7 | Exploratives Testen ist unstrukturiertes "Herumklicken" | Session-Based Test Management mit einer Testing Charter (Explore/With/To Discover) strukturiert exploratives Testen gezielt, ohne die Kreativität einzuschränken |
| 8 | Ein Abnahmeprotokoll ist selbst das rechtlich bindende Element, und seine drei Statuswerte sind gesetzlich festgelegt | Rechtlich entscheidend ist die Abnahme selbst (die auch konkludent erfolgen kann) – das Protokoll dokumentiert sie mit wichtiger Beweisfunktion. Die drei Statuswerte sind eine praktische, keine gesetzliche Kategorisierung |
| 9 | Automatisierte Tests und exploratives Testen sind austauschbar | Beide decken unterschiedliche Fehlerarten ab (bekannte vs. unerwartete Szenarien) und ergänzen sich, statt sich zu ersetzen |

---

## 7. Deep-Dive-Ausblick (freiwillig)

- **Kognitive Komplexität vs. zyklomatische Komplexität** (→ Kapitel 1.3, Quality Gates): Warum kognitive Komplexität tief verschachtelte `if`-Strukturen stärker bestraft als klassische zyklomatische Komplexität und dadurch näher an der tatsächlichen menschlichen Verständlichkeit von Code liegt.
- **Spy als dritter Test-Double-Typ** (→ Kapitel 3.2, Mocking/Stubbing): Ein Spy zeichnet tatsächlich erfolgte Methodenaufrufe zur späteren Prüfung auf – oft (aber nicht zwingend) durch Umschließen eines echten Objekts, sodass reale Geschäftslogik zusätzlich ausgeführt wird. Entscheidendes Merkmal ist die *nachträgliche* Prüfung aufgezeichneter Aufrufe, im Unterschied zum Mock, der meist *vorab* mit erwarteten Interaktionen programmiert wird.
- **Session-Based-Testing-Werkzeuge** (→ Kapitel 4.2, Exploratives Testen): Wie Tools wie Rapid Reporter oder Browser-Erweiterungen das Protokollieren von Screenshots, Notizen und Konsolenfehlern während einer Explorationssession erleichtern.
- **Automatisierte DAST-Quality-Gates** (→ Kapitel 5, Verifikations-Zyklus): Wie ein headless DAST-Scan bei jedem Staging-Deployment automatisch angestoßen wird und einen strukturierten JUnit/JSON-Report liefert, der die Pipeline bei Funden ab Schweregrad "Medium" blockiert.

---

## 8. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Was prüft ein Linter, was ein Formatter nicht prüft? | Programmatische Auffälligkeiten/potenzielle Bugs (nicht nur optisches Erscheinungsbild) |
| 2 | Was ist eine "technische Schuld"? | Metapher für den impliziten Nacharbeitsaufwand, der durch eine schnelle statt einer sauberen Lösung entsteht |
| 3 | Nenne zwei typische Quality-Gate-Bedingungen. | z. B. Coverage ≥ 80 %, Duplizierte Zeilen ≤ 3 %, Security Vulnerabilities = 0 |
| 4 | Was unterscheidet passives von aktivem DAST-Scanning? | Passiv beobachtet nur den Verkehr, ohne Anfragen zu verändern (geringes scanbedingtes Risiko), aktiv sendet bösartige Anfragen (kann Schaden verursachen) |
| 5 | Wofür steht CSP, und was bewirkt es? | Content-Security-Policy – schränkt ein, von wo Skripte/Styles/Bilder geladen werden dürfen, mindert XSS |
| 6 | Was verifiziert ein Mock im Gegensatz zu einem Stub? | Ob und wie eine Interaktion (Methodenaufruf, Parameter, Häufigkeit) stattgefunden hat, statt nur einen Rückgabewert zu liefern |
| 7 | Nenne zwei Probleme, wenn Unit-Tests echte externe APIs aufrufen. | z. B. Flakiness bei API-Ausfall, Nebenwirkungen (Datenmüll, Kosten), langsamere Testausführung |
| 8 | Was sind die drei Bestandteile einer Testing Charter? | Explore (Zielbereich), With (Ressourcen/Tools), To Discover (Entdeckungsziel) |
| 9 | Nenne drei in der Praxis übliche Statusangaben eines Abnahmeprotokolls. | Abnahme ohne festgestellte Mängel, Abnahme unter Dokumentation unwesentlicher Mängel/Vorbehalte, begründete Verweigerung der Abnahme (praktische Kategorisierung, keine gesetzliche) |
| 10 | Warum ersetzen automatisierte Tests kein exploratives Testen? | Automatisierte Tests prüfen nur bereits antizipierte Szenarien – exploratives Testen findet unerwartete, nicht codierte Grenzfälle |
| 11 | Ein Team möchte eine Login-Funktion testen, die intern einen `TokenService` aufruft, um ein Zugriffstoken zu generieren. Der Test soll prüfen, dass bei falschem Passwort `TokenService.generate()` *nicht* aufgerufen wird. Stub oder Mock, und warum? | Mock – geprüft wird eine Interaktion (Nichtaufruf einer Methode unter einer Bedingung), nicht nur ein simulierter Rückgabewert |

---

## 9. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **SAST** | White-Box-Sicherheitsanalyse des Quellcodes vor Ausführung |
| **DAST** | Black-Box-Sicherheitsanalyse einer laufenden Anwendung von außen |
| **Code Smell** | Hinweis auf architektonisches Problem, kein akuter Bug |
| **Technical Debt** | Implizierter künftiger Nacharbeitsaufwand durch schnelle Lösungen |
| **Quality Gate** | Vordefinierte Metrik-Schwellenwerte, die ein Merge/Deploy blockieren können |
| **Stub** | Test Double mit vorgefertigten Antworten – Zustandsverifikation |
| **Mock** | Test Double, der Interaktionen protokolliert – Verhaltensverifikation |
| **Flakiness** | Unzuverlässige Tests, oft durch externe Abhängigkeiten verursacht |
| **Testing Charter** | Strukturierungsrahmen für explorative Testsessions (Explore/With/To Discover) |
| **Abnahmeprotokoll** | Dokumentiert das Ergebnis einer Abnahme mit wichtiger Beweisfunktion – die rechtliche Wirkung ergibt sich aus Abnahme, Vertrag und Gesetz, nicht allein aus dem Dokument |

---

## 10. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Begriffsabgrenzung | "Erläutern Sie den Unterschied zwischen X und Y" | Klare Kriterien + konkretes Beispiel (z. B. Linter vs. Formatter, Stub vs. Mock, SAST vs. DAST) |
| Konfigurationsaufgabe | "Entwerfen Sie eine Quality-Gate-Konfiguration für …" | Konkrete Metriken, Operatoren und Schwellenwerte benennen, nicht nur allgemein "gute Codequalität" fordern |
| Test-Double-Auswahl | "Würden Sie hier einen Stub oder einen Mock verwenden?" | Begründung anhand Zustands- vs. Verhaltensverifikation, nicht pauschal "Mock" als Sammelbegriff |
| Sicherheitsbegründung | "Warum erkennt SAST diese Schwachstelle nicht?" | Bezug auf Laufzeit-Charakter der Lücke (Header, CORS) statt nur "SAST ist unvollständig" |
| Prozess-/Abnahmefrage | "Was gehört in ein Abnahmeprotokoll?" | Alle vier Bestandteile nennen (Metadaten, Testzusammenfassung, Abnahmestatus, Unterschriften), nicht nur "Unterschrift" |

---

## 11. Merksätze für das Fachgespräch

> Formatter vereinheitlichen die Darstellung, Linter erkennen regelbasierte Auffälligkeiten, weitergehende statische Analyse bewertet zusätzliche Qualitäts- und Sicherheitsmerkmale – drei verschiedene Fragen, drei verschiedene Werkzeuge.

> SAST liest den Bauplan, DAST testet das fertige Gebäude von außen – beide finden unterschiedliche Dinge und ersetzen sich nicht.

> Ein Stub sagt "hier ist die Antwort", ein Mock fragt "hast du mich richtig benutzt?" – Zustand vs. Verhalten.

> Automatisierte Tests finden, was man erwartet hat – exploratives Testen findet, was niemand erwartet hat.

> Ein Abnahmeprotokoll ist kein Gütesiegel für Fehlerfreiheit, sondern dokumentiert die erfolgte Abnahme, den festgestellten Leistungsstand und bekannte Mängel mit wichtiger Beweisfunktion – die rechtliche Bindung entsteht durch die Abnahme selbst, nicht allein durch das Dokument.

---

```yaml
dokument: LF8.6-wiki-artikel
lernfeld: LF8.6
titel: "Code-Qualität, Statische/Dynamische Sicherheitstests & Test-Strategien"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-07
quellen_intern:
  - "LF8.6.1: Static Code Analysis, Linting & SAST.md"
  - "LF8.6.2: DAST (Dynamic Application Security Testing) & Runtime Security.md"
  - "LF8.6.3: Mocking vs. Stubbing in Distributed Systems.md"
  - "LF8.6.4: Automated Integration Testing & Exploratory Testing.md"
quellen_fachlich:
  - titel: "ZAP-Projekt – Namensänderung und Trägerschaft"
    herausgeber: "ZAP-Projekt / Software Security Project (Linux Foundation) / Checkmarx"
    status: "ZAP hat OWASP im August 2023 verlassen und ist seither kein OWASP-Projekt mehr (nur noch 'ZAP', seit 2024 'ZAP by Checkmarx'); 'OWASP ZAP' ist eine verbreitete, aber veraltete Bezeichnung"
  - titel: "SonarQube/SonarCloud Quality Gates Dokumentation"
    herausgeber: "SonarSource"
    status: "etabliertes, aktuelles Konzept für automatisierte Code-Qualitätsschwellen"
  - titel: "OWASP Top 10 / OWASP Web Security Testing Guide"
    herausgeber: "OWASP Foundation"
    status: "aktuelle Referenz für SAST/DAST-Grundlagen, CORS, HTTP-Security-Header"
  - titel: "Martin Fowler – Mocks Aren't Stubs"
    herausgeber: "martinfowler.com"
    status: "Standardreferenz zur Test-Double-Terminologie"
review_historie:
  - runde: 1
    datum: 2026-09-07
    ergebnis: "Erstdraft mit integrierter Web-Verifikation erstellt – dabei wichtigen, im Rohmaterial durchgehend veralteten Fund korrigiert: 'OWASP ZAP' heißt seit 2023 nur noch 'ZAP' (Projekt hat OWASP verlassen, seit 2024 'ZAP by Checkmarx'). Eigene Review nach Style-Guide-Checkliste direkt eingearbeitet: Typische Prüfungsfallen und Deep-Dive-Ausblick von Anfang an vorhanden, Analogien aus vier verschiedenen Domänen (Handwerk, Kochen, Gärtnerei, Logistik/Fließband) statt Wiederholung, zusätzlicher Synthese-Abschnitt 5 verknüpft alle vier Unterthemen explizit zu einem CI/CD-Verifikationszyklus (im Rohmaterial nicht als eigene Datei vorhanden, aber aus den vorhandenen Pipeline-Diagrammen der Sub-Themen zusammengeführt, keine neuen Fakten erfunden)"
  - runde: 2
    datum: 2026-09-08
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet, gewichtet nach fachlicher Substanz. Wichtigster Fund: echter innerer Widerspruch behoben – Kapitel 3.1 verbot pauschal Netzwerkaufrufe in 'automatisierten Tests', während Kapitel 4.1 explizit Integrationstests mit echten HTTP-Aufrufen beschreibt; jetzt korrekt auf Unit-Tests begrenzt. Weitere Korrekturen: Coverage nicht als statisch berechnete Metrik dargestellt (kommt aus importiertem Testreport), SAST von SCA abgegrenzt, CORS korrekt als Lockerung der Same-Origin-Policy statt als eigenständiger Blockmechanismus erklärt, Abnahmeprotokoll-Abschnitt grundlegend BGB-konform überarbeitet (Abnahme statt Dokument ist rechtlich entscheidend, drei Statuswerte als praktische statt gesetzliche Kategorisierung gekennzeichnet), Mock-Beispiel/Spy-Deep-Dive terminologisch nach Fowler bereinigt (Beispiel ist strenggenommen ein Spy), Vitest/Playwright-Rollen differenziert, X-Frame-Options um DENY/SAMEORIGIN/CSP frame-ancestors präzisiert, passives Scanning und Produktionsscans nicht mehr absolut formuliert, Duplizierungs-Schwellenwert auf SonarQube-Konvention ≤ korrigiert, ZAP-Markenerklärung im Fließtext gekürzt. Umfangreiche Ergänzungsvorschläge einer Review (Spy-Codebeispiel, Security-Header-Konfigurationsbeispiele, Testing-Charter-Beispiel) als optionale Scope-Erweiterung bewusst nicht übernommen"
  - runde: 3
    datum: 2026-09-08
    ergebnis: "Finale Review (3 Reviews) geprüft: von zwei unabhängigen Reviews übereinstimmend gemeldeten Rest-Widerspruch behoben – Pipeline-Diagramm in Kapitel 5 sagte weiterhin pauschal 'Integrationstests mit Test Doubles', obwohl Kapitel 3.1 das in Runde 2 bereits auf Unit-Tests begrenzt hatte. Weitere Konsistenz-Nacharbeit: Kernfrage 3 und Selbsttest 3/4 an die in Runde 2 korrigierten Formulierungen (Unit-Test-Bezug, ≤3%, 'geringes Risiko' statt 'risikofrei') nachgezogen, Merksatz zu Formatter/Linter entschärft, Merksatz Abnahmeprotokoll an die BGB-konforme Kapitel-4.3-Fassung angeglichen ('Abnahme selbst ist bindend, nicht das Dokument'), UI-Integrationstest und End-to-End-Test als getrennte Teststufen dargestellt (Vitest/Testing-Library vs. Playwright), CORS-Typfrage-Prämisse an die bereits korrekte Musterantwort angepasst. Erneut gemeldete Markdown-Schäden ([...]-Platzhalter, abgeschnittene Tabelle/Selbsttest) beim Abgleich mit der tatsächlichen Datei nicht bestätigt – nicht übernommen"
  - runde: 4
    datum: 2026-09-08
    ergebnis: "Eigene Abschlussprüfung (kein externer Review): drei letzte Konsistenzreste gefunden und behoben, die trotz Runde 3 übersehen wurden – Kernfrage 1 hatte Genus-Fehler ('eine Quality Gate' statt 'ein Quality Gate') und vage Formulierung ('sauberen Code' statt 'definierte Qualitätskriterien'), Kernfrage 4 sagte noch 'rechtssicheres Abnahmeprotokoll' und widersprach damit der bewusst zurückhaltenden BGB-Formulierung in Kapitel 4.3 ('aussagekräftiges Abnahmeprotokoll'), DAST-Tabelle stellte Funde als generell 'aktiv ausnutzbare Schwachstellen' dar statt als potenziell/bestätigt ausnutzbar, SAST-Nutzen-Zeile stellte Berechnung technischer Schulden als allgemeine SAST-Eigenschaft statt als plattformspezifische Zusatzfunktion (SonarQube) dar. YAML, Anchor-Links und Gliederung final programmatisch validiert – keine weiteren Fachfehler gefunden"
freigabe: "Final gesetzt nach 4 Runden (3 externe Reviews + 1 eigene Abschlussprüfung, 2026-09-08) – Freigabe durch Autor:in bestätigt"
```