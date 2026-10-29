# LF5.4 – Writing the Logic

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 80–100 Minuten für das erste Durcharbeiten, +60–80 Minuten mit Selbsttest und Wiederholung (viel Code zum Nachvollziehen)
> **Status:** Final
> **Stand:** 2026-09-11
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.
>
> **Hinweis zur Abgrenzung:** UML-Klassendiagramme und OOP-Design-Patterns werden in LF8.1 ausführlich vertieft. Dieser Artikel legt die **Grundlagen**, auf denen LF8.1 aufbaut (Sprachparadigmen, Python-Syntax, Bash, Docker) – wiederholt aber nicht die dortigen Vertiefungen.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Welche Programmierparadigmen gibt es, und wann passt welches? | [→ 1. Sprachen & Paradigmen](#1-sprachen-und-paradigmen) |
| 2 | Wie ist ein Bash-Skript aufgebaut, und wie macht man es ausführbar? | [→ 2. Bash-Automatisierung](#2-bash-automatisierung) |
| 3 | Wie funktioniert prozedurale Programmierung in Python? | [→ 3. Python prozedural](#3-python-prozedural) |
| 4 | Wie werden Klassen und Objekte in Python umgesetzt? | [→ 4. Python objektorientiert](#4-python-objektorientiert) |
| 5 | Was unterscheidet einen Container von einer virtuellen Maschine, und wie ist ein Dockerfile aufgebaut? | [→ 5. Docker](#5-containerisierung-mit-docker) |

---

## 1. Sprachen und Paradigmen

> **Grundprinzip:** Ein Rezept kann eine Schritt-für-Schritt-Anleitung sein ("zuerst Zwiebeln anbraten, dann Fleisch dazu"), oder es kann beschreiben, welches Endergebnis herauskommen soll, ohne die genaue Reihenfolge festzulegen. Genau diese unterschiedlichen "Denkweisen", wie man ein Problem in Anweisungen übersetzt, nennt man in der Programmierung Paradigmen – die Programmiersprache ist nur das Werkzeug, das Paradigma ist die Philosophie dahinter.

### 1.1 Aktuelle Sprachlandschaft

Programmiersprachen-Rankings wie der **TIOBE-Index** ändern sich laufend – für die Prüfung zählt eher das grundsätzliche Einsatzgebiet als der exakte Rangplatz. Stand September 2026 (TIOBE-Index):

| Sprache | Typisches Einsatzgebiet | IHK-Relevanz |
| --- | --- | --- |
| **Python** | Datenanalyse, KI, Backend-Automatisierung (aktuell mit Abstand Platz 1) | 🔴 |
| **C** | Systemnahe, ressourcenkritische Software, Embedded | 🟡 |
| **C++** | Performante Anwendungen, Spiele, systemnahe Software | 🟡 |
| **Java** | Große Unternehmenssysteme, Backend-Anwendungen | 🟡 |
| **C#** | .NET-Backend, Desktop-Anwendungen, Spieleentwicklung | 🟡 |
| **JavaScript** | Web-Frontend, Node.js-Backend | 🟡 |
| **TypeScript** | Typisiertes JavaScript, vor allem für größere Web-/Backend-Projekte | 🟡 |
| **Rust** | Speichersicherheit ohne Garbage Collector, Systemprogrammierung | 🟢 |

> **Hinweis zur Aktualität:** Rangfolgen wie der TIOBE-Index schwanken monatlich und sollten nicht auswendig gelernt werden – für die Prüfung reicht das grundsätzliche Verständnis, welche Sprache für welches Einsatzgebiet typisch ist. Wichtig auch: Der TIOBE-Index misst **Popularität/Sichtbarkeit** (u. a. Suchmaschinen-Treffer) – er ist kein Qualitätsranking und misst nicht direkt, wie viele Projekte oder Codezeilen tatsächlich mit einer Sprache geschrieben werden.

### 1.2 Drei wichtige Programmierparadigmen

| Paradigma | Kernidee | Beispielsprachen | IHK-Relevanz |
| --- | --- | --- | --- |
| **Imperativ/prozedural** | Problemlösung als Folge von Anweisungen, Bedingungen, Schleifen und Funktionen; Ablauf und Zustandsänderungen stehen im Mittelpunkt (prozedural ist eine verbreitete Ausprägung des imperativen Paradigmas) | C, Bash | 🔴 |
| **Objektorientiert (OOP)** | Daten und Funktionen werden in Objekten gebündelt; modelliert reale Entitäten | Java, C# | 🔴 |
| **Funktional** | Berechnung wird möglichst als Zusammenspiel von Funktionen beschrieben; veränderlicher Zustand und Seiteneffekte werden möglichst reduziert | Haskell, Elixir | 🟡 |

> **Wichtig für die Prüfung:** Viele moderne Sprachen wie Python und JavaScript sind **Multiparadigmen-Sprachen** – sie unterstützen prozedurale, objektorientierte und teilweise funktionale Elemente gleichzeitig. Das ist kein Widerspruch, sondern Flexibilität: Welches Paradigma im Konkreten genutzt wird, entscheidet die Entwicklerin je nach Problem.

> **Typische Prüfungsfalle:** Nicht jedes Problem sollte objektorientiert gelöst werden. Ein einfaches 20-Zeilen-Skript ist oft einer aufwendigen Klassenhierarchie mit fünf Klassen vorzuziehen – OOP lohnt sich vor allem bei komplexen, wiederverwendbaren Strukturen mit Zustand.

> **IHK-Typfrage:** *"Welches Paradigma wird typischerweise verwendet, wenn ein Systemadministrator ein Bash-Skript zur Serverwartung schreibt, und warum passt das gut?"*
> **Musterantwort:** Ein Bash-Skript zur Serverwartung ist typischerweise **prozedural**: Es führt eine Abfolge konkreter Befehle von oben nach unten aus (z. B. "prüfe Speicherplatz, dann lösche alte Logs, dann starte den Dienst neu"). Für diese Art von Aufgabe – eine klare, lineare Abfolge von Systembefehlen ohne komplexe Datenmodellierung – ist der objektorientierte Ansatz unnötig aufwendig; die prozedurale Denkweise bildet den tatsächlichen Ablauf direkt und verständlich ab.

---

## 2. Bash-Automatisierung

> **Grundprinzip:** Ein Backrezept ohne Überschrift "Rezept" wird von der Küchenmaschine nicht erkannt – bei einem Bash-Skript ist die erste Zeile (die Shebang) genau diese Kennzeichnung: Sie sagt dem Betriebssystem, mit welchem "Koch" (Interpreter) die folgenden Anweisungen ausgeführt werden sollen.

### 2.1 Aufbau eines Bash-Skripts

Bash (**B**ourne **A**gain **Sh**ell) ist auf vielen Linux-Systemen installiert und häufig als interaktive Standardshell eingerichtet; auf schlankeren Systemen kommen teils andere Shells zum Einsatz. Bash-Scripting ist prozedurale Programmierung, direkt auf das Betriebssystem angewendet.

```bash
#!/bin/bash
# Die Shebang: sagt Linux, welcher Interpreter genutzt werden soll

SERVER_PORT=8080
# Variable ohne Leerzeichen um das "="!

echo "Server läuft auf Port $SERVER_PORT"
```

| Element | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Shebang** (`#!/bin/bash`) | Erste Zeile, legt den Interpreter fest | 🔴 |
| **Variable** (`NAME="Wert"`) | Keine Leerzeichen um das `=`; Zugriff mit `$NAME` | 🔴 |
| **Rechte** (`chmod +x script.sh`) | Nötig, wenn das Skript **direkt** mit `./script.sh` gestartet werden soll | 🔴 |
| **Direkter Aufruf** (`./script.sh`) | Der `./`-Präfix zeigt, dass die Datei im aktuellen Verzeichnis gemeint ist; benötigt Ausführungsrecht und wertet die Shebang aus | 🟡 |
| **Interpreter-Aufruf** (`bash script.sh`) | Alternative **ohne** Ausführungsrecht – der Interpreter wird hier explizit angegeben, die Shebang spielt dabei keine Rolle | 🟢 |
| **Exit-Codes** (`exit 0` / `exit 1`) | `0` = fehlerfrei, alles andere = Fehler – essenziell für automatisierte CI/CD-Pipelines | 🟡 |

> **Typische Prüfungsfallen:**
> - Leerzeichen um das `=` bei Variablenzuweisung (`VAR = "value"`) führt zu einem Fehler – korrekt ist `VAR="value"`.
> - `chmod +x` vergessen → beim **direkten** Aufruf `./script.sh` in der Regel "Permission denied". Der Aufruf `bash script.sh` funktioniert dagegen auch ohne Ausführungsrecht, da hier explizit der Interpreter aufgerufen wird.
> - Ein Skript im aktuellen Verzeichnis einfach mit `script.sh` statt `./script.sh` aufrufen zu wollen, funktioniert nicht – Linux sucht sonst nur in den Verzeichnissen des PATH.

> **IHK-Typfrage:** *"Warum ist es riskant, ein Bash-Skript aus dem Internet herunterzuladen und direkt mit Root-Rechten auszuführen?"*
> **Musterantwort:** Ein Bash-Skript kann beliebige Systembefehle enthalten, die mit den Rechten des ausführenden Nutzers laufen. Mit Root-Rechten hat das Skript vollen Zugriff auf das gesamte System – es könnte Dateien löschen, Hintertüren einrichten, Daten exfiltrieren oder das System für Angriffe missbrauchen, ohne dass der Nutzer den Code vorher gelesen oder verstanden hat. Vor dem Ausführen sollte der Skriptinhalt geprüft werden, und Root-Rechte sollten nur vergeben werden, wenn sie tatsächlich zwingend nötig sind (Prinzip der geringsten Rechte).

---

## 3. Python prozedural

> **Grundprinzip:** In manchen Sprachen zeigen geschweifte Klammern { }, wo ein Codeblock beginnt und endet – bei Python übernimmt die Einrückung selbst diese Aufgabe. Das erzwingt sauberen, einheitlich formatierten Code, kann aber bei Vermischung von Leerzeichen und Tabs zu Fehlern führen.

### 3.1 Grundlegende Syntax

```python
def greet(name):
    print(f"Hallo {name}")

age = 20
if age >= 18:
    print("Volljährig")
else:
    print("Minderjährig")

for number in [1, 2, 3]:
    print(number)
```

| Konzept | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Einrückung** | Eine konsistente Einrückung definiert den Codeblock (statt `{}`); üblicher Python-Stil (PEP 8) sind 4 Leerzeichen pro Ebene, zwingend ist aber nur die Konsistenz. Falsche/inkonsistente Einrückung → `IndentationError` | 🔴 |
| **Dynamische Typisierung** | Datentyp wird nicht deklariert, ergibt sich aus dem zugewiesenen Wert | 🔴 |
| **Kontrollstrukturen** | `if/else`, `for item in liste:`, `while bedingung:` | 🔴 |
| **Funktionen** | `def funktionsname(parameter):` kapselt wiederverwendbare Logik | 🔴 |

> **Typische Prüfungsfalle:** Tabs und Leerzeichen sollten bei der Einrückung nicht gemischt werden. Eine inkonsistente Mischung kann zu einem `TabError` führen (nicht jede Mischung sofort – entscheidend ist, ob die Einrückungsebene dadurch uneindeutig wird). Moderne IDEs (z. B. VS Code) können so konfiguriert werden, dass die Tabulatortaste automatisch 4 Leerzeichen einfügt – sinnvoll, aber von der jeweiligen Konfiguration abhängig.

> **IHK-Typfrage:** *"Warum schlägt dieser Code fehl: `if True:` in Zeile 1, `print(\"It is true\")` in Zeile 2, aber ohne Einrückung?"*
> **Musterantwort:** In Python definiert die Einrückung den zugehörigen Codeblock einer Kontrollstruktur wie `if`. Da die zweite Zeile nicht eingerückt ist, erkennt Python sie nicht als Teil des `if`-Blocks – das Ergebnis ist ein `IndentationError`, weil Python nach einem Doppelpunkt zwingend einen eingerückten Block erwartet. Die korrekte Version wäre `if True:` gefolgt von einer eingerückten Zeile `    print("It is true")`.

---

## 4. Python objektorientiert

> **Grundprinzip:** Eine Bauzeichnung für ein Auto ist noch kein Auto – erst wenn nach dieser Zeichnung tatsächlich ein Fahrzeug gebaut wird, existiert ein konkretes, fahrbares Exemplar. Die Zeichnung ist die **Klasse**, das gebaute Auto ist das **Objekt** (die Instanz).

### 4.1 Klassen, Objekte und `__init__()`

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._isbn = None  # Konvention: "privat", nicht technisch erzwungen

    def display(self):
        print(f"{self.title} von {self.author}")

my_book = Book("Der Prozess", "Kafka")
my_book.display()  # Ausgabe: Der Prozess von Kafka
```

| Konzept | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Klasse vs. Objekt** | Klasse = Bauplan (z. B. `Book`), Objekt = konkrete Instanz (z. B. `my_book`) | 🔴 |
| **`__init__`-Methode** | Initialisierungsmethode, häufig vereinfachend als "Konstruktor" bezeichnet – wird automatisch aufgerufen, um eine bereits erzeugte neue Instanz zu initialisieren (die eigentliche Objekterzeugung übernimmt technisch `__new__`) | 🔴 |
| **`self`** | Üblicher erster Parameter einer **Instanzmethode**, verweist auf das konkrete Objekt und wird beim Methodenaufruf automatisch übergeben (Ausnahmen: `@classmethod` nutzt `cls`, `@staticmethod` braucht kein `self`) | 🔴 |
| **Kapselung (Konvention)** | Python kennt kein echtes `private` – ein führender Unterstrich (`self._attribut`) signalisiert nur konventionell "nicht von außen anfassen" | 🟡 |

> **Wichtig für die Prüfung:** Der Unterstrich vor `_isbn` ist **keine technische Zugriffsbeschränkung** – von außen könnte trotzdem auf `my_book._isbn` zugegriffen werden. Es ist eine reine Konvention unter Entwickler:innen, die Absicht "nicht direkt verwenden" auszudrücken.

> **Typische Prüfungsfalle:** Wird bei einer gewöhnlichen Instanzmethode der Parameter für die Instanz vergessen, führt der übliche Aufruf über ein Objekt (`objekt.methode()`) zu einem `TypeError` – beim Aufruf wird die Instanz automatisch als erstes Argument übergeben, auch wenn `self` dort nicht mit angegeben wird.

> **IHK-Typfrage:** *"Erklären Sie den Unterschied zwischen 'Klasse' und 'Objekt' anhand einer Alltagsmetapher, und schreiben Sie eine passende Python-Klasse."*
> **Musterantwort:** Eine Klasse ist wie ein Kuchenrezept – sie beschreibt, welche Zutaten (Attribute) und Zubereitungsschritte (Methoden) nötig sind, ist aber selbst kein Kuchen. Ein Objekt ist der tatsächlich gebackene Kuchen – eine konkrete, essbare Instanz, die nach dem Rezept entstanden ist. Man kann aus demselben Rezept beliebig viele Kuchen backen, so wie man aus einer Klasse beliebig viele Objekte erzeugen kann. Beispiel:
> ```python
> class Cake:
>     def __init__(self, flavor):
>         self.flavor = flavor
>
> chocolate_cake = Cake("Schokolade")
> ```

---

## 5. Containerisierung mit Docker

> **Grundprinzip:** Ein möbliertes Apartment mit eigener Küche, eigenem Bad und eigenen vier Wänden simuliert ein komplettes Haus (das entspricht einer virtuellen Maschine – schwer, aber komplett unabhängig). Ein WG-Zimmer dagegen teilt sich Küche und Bad mit den Mitbewohnern, ist aber viel schneller bezugsfertig und braucht weniger Platz (das entspricht einem Container – leicht, weil er sich den Kernel des Host-Systems teilt).

### 5.1 Container vs. virtuelle Maschine

| Merkmal | Virtuelle Maschine (VM) | Container |
| --- | --- | --- |
| **Kernel** | Eigener, vollständiger Guest-Kernel über einem Hypervisor | Teilt sich den Kernel des Host-Betriebssystems |
| **Ressourcenbedarf** | Eher hoch (vollständiges Gastbetriebssystem mit eigenem Kernel) | Meist geringer (enthält nur App + exakte Abhängigkeiten) |
| **Typische Startzeit** | Eher langsamer, häufig Sekunden bis Minuten | Meist deutlich schneller, häufig wenige Sekunden oder weniger |

> **Vereinfachte Darstellung:** Native Linux-Container auf einem Linux-Host teilen sich direkt dessen Kernel. Unter Windows/macOS betreibt Docker Desktop Linux-Container dagegen innerhalb einer Linux-VM – die Container teilen sich dann den Kernel dieser VM, nicht unmittelbar den Windows-/macOS-Kernel.

### 5.2 Dockerfile, Image und Container

| Begriff | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Dockerfile** | Das Rezept – eine Textdatei mit Bauanweisungen (`FROM`, `COPY`, `CMD`) | 🔴 |
| **Image** | Der fertig gebackene Kuchen – ein unveränderliches Template, erzeugt durch `docker build` | 🔴 |
| **Container** | Die laufende Instanz – gestartet durch `docker run` auf einem Image | 🔴 |

```dockerfile
FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY code.py .

CMD ["python", "code.py"]
```

> **Praxistipp:** Die Reihenfolge ist bewusst gewählt – `requirements.txt` wird **vor** dem eigentlichen Anwendungscode kopiert und installiert. Ändert sich nur der Code (nicht die Abhängigkeiten), kann Docker den bereits gebauten Installations-Layer aus dem Cache wiederverwenden, statt alle Pakete erneut zu installieren – das beschleunigt wiederholte Builds erheblich.

```bash
docker build -t my-app .
docker run my-app
```

> **Typische Prüfungsfalle:** Image und Container werden oft verwechselt. Man **baut** ein Image (das statische Template), man **startet** einen Container (den laufenden Prozess) – aus demselben Image lassen sich beliebig viele Container gleichzeitig starten.

> **Wichtig für die Prüfung – Docker Engine vs. Docker Desktop:** Die eigentliche Container-Engine (**Docker Engine**, früher auch "Docker CE" genannt, Apache-2.0-Lizenz) ist quelloffen und bleibt frei nutzbar. **Docker Desktop** – die grafische Oberfläche für Windows/macOS/Linux – unterliegt dagegen eigenen Lizenzbedingungen (Docker Subscription Service Agreement): kostenlos für private Nutzung, Bildung, nicht-kommerzielle Open-Source-Projekte und kleine Unternehmen (weniger als 250 Mitarbeitende **und** weniger als 10 Mio. USD Jahresumsatz), kostenpflichtig sobald eine der beiden Schwellen überschritten wird; für Behörden gelten gesonderte, grundsätzlich kostenpflichtige Bedingungen. Die genauen, aktuell gültigen Konditionen sollten im Zweifel direkt bei Docker geprüft werden, da sich Lizenzmodelle ändern können.

> **IHK-Typfrage:** *"Warum gilt ein zustandsloses (stateless) Design als Best Practice für Anwendungen in Docker-Containern?"*
> **Musterantwort:** Container sollen leicht ersetzt, neu erstellt und horizontal skaliert werden können. Daten im beschreibbaren Dateisystem eines Containers bleiben bei einem bloßen `docker stop`/`docker start` desselben Containers normalerweise erhalten, sind aber fest an genau diesen einen Container gebunden. Wird der Container entfernt oder durch eine neue Instanz (z. B. bei einem Update) ersetzt, gehen diese Daten verloren. Ein zustandsloses Design speichert wichtige Daten deshalb außerhalb des austauschbaren Containers (z. B. in einer externen Datenbank oder einem Docker-Volume), sodass der Container selbst jederzeit ersetzbar bleibt, ohne Daten zu verlieren. Das erleichtert horizontale Skalierung (mehrere identische Container gleichzeitig) und automatisiertes Deployment erheblich.

---

## 6. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Jedes Problem sollte objektorientiert gelöst werden, weil OOP "moderner" ist | Ein einfaches Skript ist oft einer komplexen Klassenhierarchie vorzuziehen – das Paradigma sollte zum Problem passen |
| 2 | Bash-Variablen dürfen wie in anderen Sprachen mit Leerzeichen um das "=" geschrieben werden | `VAR = "value"` erzeugt einen Fehler – korrekt ist `VAR="value"` ohne Leerzeichen |
| 3 | Ein führender Unterstrich in Python (`self._attribut`) macht ein Attribut technisch unzugänglich | Das ist nur eine Konvention – von außen ist der Zugriff weiterhin möglich, Python hat kein echtes `private` |
| 4 | Ein Docker-Image und ein Docker-Container sind dasselbe | Ein Image ist das statische Template (gebaut mit `docker build`), ein Container die laufende Instanz davon (gestartet mit `docker run`) |
| 5 | Docker ist grundsätzlich kostenpflichtig | Docker Engine ist frei und quelloffen (Apache-2.0); Docker Desktop kann je nach Nutzung und Unternehmensgröße kostenpflichtig sein. Daneben bietet Docker weitere eigenständige kostenpflichtige Dienste an (z. B. Docker Hub Pro/Team) |

---

## 7. Deep-Dive-Ausblick (freiwillig)

- **Funktionale Programmierung im Detail** (→ Abschnitt 1.2): Pure Functions, Vermeidung von Seiteneffekten, warum sich funktionale Pipelines gut für komplexe Datentransformationen eignen.
- **Rust und Memory Safety** (→ Abschnitt 1.1): Warum Rust ohne Garbage Collector speichersicher sein kann, im Vergleich zu C/C++.
- **Vererbung und Polymorphismus in Python** (→ Abschnitt 4): Vertiefte OOP-Konzepte werden in LF8.1 behandelt.
- **docker-compose** (→ Abschnitt 5): Orchestrierung mehrerer Container/Dienste inkl. Port- und Volume-Mapping in einer `docker-compose.yml`.

> 🔍 **Hinweis zur Selbstrecherche:** Programmiersprachen-Rankings (TIOBE, Stack Overflow Survey) ändern sich laufend – für eine aktuelle Einschätzung lohnt sich ein Blick auf tiobe.com oder die aktuelle Stack-Overflow-Developer-Survey, statt sich auf die hier genannten Werte zu verlassen.

---

## 8. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Nenne drei in diesem Artikel behandelte Programmierparadigmen. | Imperativ/prozedural, objektorientiert, funktional (es gibt noch weitere, z. B. deklarativ, logisch, ereignisorientiert) |
| 2 | Was bedeutet "Multiparadigmen-Sprache"? | Eine Sprache (z. B. Python, JavaScript), die mehrere Paradigmen gleichzeitig unterstützt |
| 3 | Was macht die Shebang-Zeile in einem Bash-Skript? | Legt fest, mit welchem Interpreter das Skript ausgeführt wird (`#!/bin/bash`) |
| 4 | Welcher Befehl macht eine Datei unter Linux ausführbar? | `chmod +x dateiname.sh` |
| 5 | Wodurch werden Codeblöcke in Python definiert? | Durch konsistente Einrückung, nicht durch geschweifte Klammern; 4 Leerzeichen pro Ebene sind PEP-8-Konvention, keine zwingende Syntax |
| 6 | Was ist der Unterschied zwischen einer Klasse und einem Objekt? | Klasse = Bauplan; Objekt = konkrete Instanz, die nach diesem Bauplan erzeugt wurde |
| 7 | Was passiert, wenn `self` in einer Python-Methode vergessen wird? | Ein `TypeError` beim Aufruf der Methode |
| 8 | Was unterscheidet einen Container von einer virtuellen Maschine? | Container teilen sich (bei nativem Linux-Host) den Host-Kernel und sind dadurch leichtgewichtiger; VMs betreiben ein vollständiges Gastbetriebssystem mit eigenem Kernel auf virtualisierter Hardware |
| 9 | Womit wird ein Docker-Image erzeugt, womit ein Container gestartet? | Image: `docker build`; Container: `docker run` |
| 10 | Ist Docker Engine kostenpflichtig? | Nein, Docker Engine ist frei und quelloffen (Apache-2.0); Docker Desktop unterliegt dagegen eigenen Lizenzbedingungen, die je nach Nutzung/Unternehmensgröße kostenpflichtig sein können |

---

## 9. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Prozedural** | Problemlösung durch Anweisungen, Bedingungen, Schleifen und Funktionen; Ablauf im Mittelpunkt |
| **Objektorientiert (OOP)** | Daten und Funktionen in Objekten gebündelt |
| **Funktional** | Berechnung als Funktionsauswertung, vermeidet veränderlichen Zustand |
| **Shebang** | `#!/bin/bash` – legt den Skript-Interpreter fest |
| **chmod +x** | Macht eine Datei unter Linux ausführbar |
| **Exit-Code** | `0` = Erfolg, sonst Fehler – wichtig für CI/CD |
| **Einrückung (Python)** | Definiert Codeblöcke statt `{}`; 4 Leerzeichen pro Ebene sind PEP-8-Konvention, zwingend ist nur die Konsistenz |
| **`__init__`** | Initialisiert eine neu erzeugte Instanz (häufig vereinfachend "Konstruktor" genannt) |
| **`self`** | Verweist in einer Methode auf das konkrete Objekt |
| **Dockerfile / Image / Container** | Bauanleitung / statisches Template / laufende Instanz |
| **Docker Engine vs. Desktop** | Engine (Apache-2.0) frei; Desktop je nach Nutzung/Unternehmensgröße kostenpflichtig |

---

## 10. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die Prüfung hören will |
| --- | --- | --- |
| Paradigma zuordnen | "Welches Paradigma passt zu Problem X?" | Konkrete Begründung anhand der Problemstruktur, nicht nur die Bezeichnung |
| Bash-Syntax anwenden | "Schreiben Sie ein Skript, das..." | Shebang nicht vergessen, korrekte Variablensyntax ohne Leerzeichen |
| Python-Code schreiben | "Implementieren Sie eine Klasse/Funktion für..." | Korrekte Einrückung, bei Klassen `__init__` und `self` nicht vergessen |
| Docker-Konzepte erklären | "Was unterscheidet X von Y?" | Klare Begriffstrennung (Image/Container, VM/Container) mit Beispiel |

---

## 11. Merksätze für das Fachgespräch

> Die Sprache ist das Werkzeug, das Paradigma ist die Philosophie dahinter.

> Kein Leerzeichen um das Gleichheitszeichen – Bash ist da gnadenlos.

> Einrückung ist in Python keine Kosmetik, sondern Syntax.

> Die Klasse ist das Rezept, das Objekt ist der gebackene Kuchen.

> Man baut ein Image, man startet einen Container – nie andersherum.

---

```yaml
dokument: LF5.4-wiki-artikel
themenfeld: "LF5.4 - Writing the Logic"
titel: "Writing the Logic"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-11
quellen_intern:
  - "LF5.4.1: Language Landscape & Paradigms.md"
  - "LF5.4.2: OS Automation.md"
  - "LF5.4.3: Python Fundamentals (Procedural).md"
  - "LF5.4.4: Object-Oriented Python.md"
  - "LF5.4.5: Containerization with Docker CE.md"
  - "Zusätzliche deutschsprachige Rechercheunterlagen vom Auftraggeber (siehe LF5.1-Historie)"
quellen_fachlich:
  - titel: "TIOBE-Index September 2026 (Sprachranking)"
    herausgeber: "TIOBE Software (Primärquelle, tiobe.com)"
    status: "web-verifiziert, Stand September 2026: Python #1 (17,76%, fallend aber dominant), C #2, C++ #3 (vor Java), Java #4, C# #5, JavaScript #6, Rust hält Platz 10; TIOBE misst laut eigener Beschreibung Popularität/Sichtbarkeit, kein Qualitäts-/Verbreitungsranking - Rohmaterial hatte 'Trend 2024/2025' aktualisiert auf aktuellen Stand mit Hinweis auf monatliche Schwankungen"
  - titel: "Docker Engine Licensing (Apache-2.0) und Docker Desktop Subscription Terms"
    herausgeber: "Docker Inc. (Primärquelle, docs.docker.com)"
    status: "web-verifiziert anhand offizieller Docker-Dokumentation; Docker Engine Open Source/Apache-2.0, Docker Desktop kostenlos für Privatnutzung/Bildung/kleine Unternehmen (<250 Mitarbeitende UND <10 Mio. USD Jahresumsatz), kostenpflichtige Subscription bei Überschreiten einer Schwelle sowie für Behörden - im Rohmaterial nicht thematisiert, als praxisrelevante Ergänzung aufgenommen"
review_historie:
  - runde: 1
    datum: 2026-09-11
    ergebnis: "Erstdraft erstellt. Rohmaterial (LF5.4.1-5, User-Story/Bloom-Format) deckte Sprachen/Paradigmen, Bash-Grundlagen, Python prozedural/OOP und Docker-Containerisierung gut ab, mit Code-Beispielen ergänzt (Bash, Python, Dockerfile), analog zum Code-Stil aus LF8.1. Zwei aktuelle Web-Funde eingearbeitet: (1) Sprachranking im Rohmaterial war als 'Trend 2024/2025' beschriftet - auf TIOBE-Index September 2026 aktualisiert, mit Hinweis auf monatliche Schwankungen statt starrer Rangliste; (2) Docker-Lizenzierung war im Rohmaterial nicht thematisiert - wichtige praxisrelevante Unterscheidung Docker CE/Engine (frei) vs. Docker Desktop (für Großunternehmen kostenpflichtig seit 2021) ergänzt, da das für Auszubildende, die später in Unternehmen mit Docker arbeiten, praktisch relevant ist. Bewusster Hinweis zur Abgrenzung von LF8.1 im Kopf ergänzt (UML/OOP-Design-Patterns dort vertieft, hier nur Grundlagen), da LF8 laut Auftraggeber explizit auf LF5 aufbaut. Auf Deutsch verfasst, Code-Kommentare ebenfalls auf Deutsch für Konsistenz. Eigene Review nach Style-Guide-Checkliste direkt eingearbeitet: Typische Prüfungsfallen und Deep-Dive-Ausblick von Anfang an vorhanden, Analogien aus mehreren Domänen (Rezept/Kochphilosophie, Backrezept/Shebang, Bauzeichnung/Auto, Kuchenrezept/Klasse, WG-Zimmer/Container)."
  - runde: 2
    datum: 2026-09-11
    ergebnis: "Externe Prüfung (2 Reviews) eingearbeitet. Wichtigster Fund, von einer Review sehr gründlich mit Docker-Primärquelle belegt: Die Aussage, ein Container verliere bei jedem Neustart automatisch seinen Zustand, war fachlich falsch – Daten im beschreibbaren Layer bleiben bei einem bloßen 'docker stop'/'docker start' desselben Containers normalerweise erhalten, gehen erst beim Entfernen/Ersetzen des Containers verloren; korrigiert, da dieser Unterschied für das Verständnis von Stateless-Design wichtig ist. Von beiden Reviews bestätigt: Python-Einrückung 'genau 4 Leerzeichen' war als zwingende Syntax dargestellt, tatsächlich ist nur die Konsistenz zwingend, 4 Leerzeichen sind PEP-8-Konvention - korrigiert in Haupttext, Selbsttest und Prüfungsfalle. Ebenfalls von beiden Reviews bestätigt: 'Leerzeichen/Tabs mischen = fataler Fehler' war zu dramatisch/unscharf - präzisiert zu spezifischem TabError bei uneindeutiger Einrückung. Ebenfalls von beiden Reviews bestätigt: '__init__' als reiner 'Konstruktor' war technisch ungenau (Objekterzeugung übernimmt __new__, __init__ initialisiert) - präzisiert in Haupttext und Cheatsheet. Ebenfalls von beiden Reviews bestätigt: Docker-Lizenzierung brauchte Präzisierung - 'Docker CE' als Hauptbezeichnung veraltet (heute 'Docker Engine'), Schwellenwerte als UND-Verknüpfung korrigiert, Hinweis auf Government-Entities-Sonderregelung ergänzt, 'nur Docker Desktop kann kostenpflichtig sein' als riskante Formulierung entschärft. Ebenfalls von beiden Reviews bestätigt: Container-Startzeiten 'Minuten/Sekunden' zu kategorisch - auf 'typische' Werte relativiert. Ein von einer Review sehr präzise begründeter Fachpunkt übernommen: 'self' gilt nur für Instanzmethoden, nicht für Klassenmethoden (cls) oder statische Methoden - präzisiert. Ebenfalls übernommen: chmod +x ist nur für den direkten Aufruf './script.sh' zwingend nötig, 'bash script.sh' funktioniert auch ohne Ausführungsrecht - Bash-Tabelle und Prüfungsfalle entsprechend erweitert. TIOBE-Tabelle: kombinierte Zeilen (C++/Java, C#/JavaScript/TypeScript) aufgetrennt, da unterschiedliche Einsatzgebiete unnötig vermischt wurden; TypeScript korrekt separat statt fälschlich gleichrangig mit C#/JS dargestellt; Hinweis ergänzt, dass TIOBE Popularität misst, kein Qualitäts-/Verbreitungsranking ist. Dockerfile idiomatischer umgebaut (WORKDIR vor COPY, Dependencies vor Code kopiert für besseres Build-Caching) - von beiden Reviews übereinstimmend vorgeschlagen. Bash-Standardaussage entschärft ('weit verbreitet' statt pauschal 'Standard'). Eine Review behauptete erneut Claude-Chat-Links im Dokument - beim Abgleich mit der tatsächlichen Datei (grep über gesamten Inhalt) nicht bestätigt, nicht übernommen (bekanntes Muster). Umfangreiche weitere Detailvorschläge (Mermaid-Diagramm für Docker-Workflow, zusätzliche Übungsaufgaben mit Code-Analyse, strukturierter YAML-Quellenblock mit Einzelfeldern, sichtbarer Quellenabschnitt im Artikeltext, Analogie-Diversifizierung, sofortige Vereinheitlichung des Genderstils) als optional eingestuft und nicht in dieser Runde übernommen, um die kompakte Form zu erhalten."
  - runde: 3
    datum: 2026-09-11
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet. Alle drei Reviews bestätigen: keine harten Fachfehler mehr. Von zwei Reviews unabhängig bestätigt, aus Runde 2 übersehen: Die Definitionen von 'Prozedural (imperativ)' ('von oben nach unten', 'Daten und Funktionen getrennt') und 'Funktional' ('vermeidet' Zustand) waren weiterhin zu absolut/unpräzise - jetzt korrigiert (prozedural als Ausprägung des imperativen Paradigmas, funktional mit 'möglichst reduziert' statt 'vermeidet'), konsistent in Haupttext, Cheatsheet und Selbsttest 1. Ebenfalls von zwei Reviews bestätigt: Überschrift 'Die drei Hauptparadigmen' suggerierte eine abschließende Taxonomie - zu 'Drei wichtige Programmierparadigmen' abgeschwächt, Selbsttest 1 entsprechend angepasst (Hinweis auf weitere Paradigmen wie deklarativ/logisch/ereignisorientiert). Ebenfalls von zwei Reviews bestätigt: YAML-Quellen widersprachen dem Anspruch auf Primärquellen (TechRepublic statt TIOBE direkt, Wikipedia/Softline/Software-Express/USU statt Docker-Dokumentation) - auf echte Primärquellen umgestellt (tiobe.com, docs.docker.com). Ein sehr präziser Einzelfund einer Review übernommen: Tempus-Fehler bei den LF8.1-Verweisen - da LF8 laut Auftraggeber explizit auf LF5 aufbaut, war 'wurden bereits in LF8.1 behandelt' falsch (suggeriert, LF8.1 käme zeitlich vorher) - korrigiert zu 'werden in LF8.1 behandelt/vertieft', an zwei Stellen (Kopf-Hinweis, Deep-Dive). Weitere Präzisierungen: Überschrift 4.1 von missverständlich 'und Konstruktor' zu eindeutig 'und __init__()' geändert; Prüfungsfalle 5 zur Docker-Lizenz war holprig formuliert ('aber nicht ausschließlich...') - entwirrt und um konkretes Beispiel (Docker Hub Pro/Team) ergänzt; Container-Kernel-Aussage um Windows/Mac-VM-Nuance ergänzt (Docker Desktop nutzt dort eine Linux-VM, Container teilen sich deren Kernel, nicht unmittelbar den Host-Kernel); Docker-Startzeit 'unter einer Sekunde' war zu konkret - auf 'wenige Sekunden oder weniger' relativiert, VM-Ressourcenbedarf-Beschreibung von 'simuliert komplette Hardware' auf präziseres 'vollständiges Gastbetriebssystem mit eigenem Kernel' geändert, konsistent in Tabelle und Selbsttest 8. 'Docker-Dreifaltigkeit'-Überschrift in neutraleres 'Dockerfile, Image und Container' geändert. Weitere Detailvorschläge (strukturierter YAML-Block mit Einzelfeldern pro Quelle, sichtbarer Quellenabschnitt im Artikeltext, python -m pip statt pip, Name-Mangling-Vertiefung, Fußnote zu docker commit als Ausnahme vom Image-zuerst-Workflow) als optional eingestuft und nicht übernommen, um die kompakte Form zu erhalten."
  - runde: 4
    datum: 2026-09-11
    ergebnis: "Eigene Abschlussprüfung (kein externer Review): gesamte Datei durchgelesen, ein kleiner Konsistenzrest gefunden – Cheatsheet-Eintrag zur Einrückung trug noch die alte Formulierung ohne die in Haupttext und Selbsttest bereits korrigierte PEP-8/Konsistenz-Nuance, nachgezogen. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 4 Runden (3 externe Prüfrunden + 1 eigene Abschlussprüfung, 2026-09-11) – Freigabe durch Autor:in bestätigt"
```