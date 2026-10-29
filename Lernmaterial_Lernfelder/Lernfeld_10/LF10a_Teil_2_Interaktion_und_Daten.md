# LF10a Teil 2 – Interaktion & Daten

> **Zielgruppe:** Umschüler FIAE, 2. Lehrjahr (Aufbaustufe)
> **Prüfungsrelevanz:** Schwerpunkt AP2 im Prüfungsbereich "Planen eines Softwareproduktes" (schriftlich, 90 Minuten, 10% Gewichtung) – insbesondere "Programmspezifikationen anwendungsgerecht festlegen" und "Maßnahmen zur Qualitätskontrolle planen und durchführen". Projektbezogene Inhalte (Interaktionslogik, Validierung, Datenanbindung) können außerdem im Fachgespräch relevant werden, sofern sie Teil der eigenen betrieblichen Projektarbeit sind.
> **Lernzeit:** Ca. 2,5–3 Stunden Lesen/Durcharbeiten, +1,5–2 Stunden für Zustandsmodell-/Validierungs-Übungen
> **Status:** Final
> **Stand:** 2026-09-14
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.
>
> **Hinweis zur Abgrenzung:** Zweiter Teil der dreiteiligen LF10a-Serie (Teil 1: Konzeption & Struktur; Teil 2: Interaktion & Daten; Teil 3: Sicherheit, Test & Abnahme). Baut auf den Architekturmustern und UI-Zuständen aus Teil 1 auf – hier werden sie technisch mit JavaScript/DOM umgesetzt.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Wie hängen DOM, Ereignis und Anwendungszustand zusammen, und warum ist `submit` robuster als `click`? | [→ 1. Interaktion und UI-Zustände](#1-interaktion-und-ui-zustände) |
| 2 | Was unterscheidet syntaktische, semantische und feldübergreifende Validierungsregeln, und warum ist Clientvalidierung keine Sicherheitsgrenze? | [→ 2. Validierung und Fehlerrückmeldung](#2-validierung-und-fehlerrückmeldung) |
| 3 | Was gehört in einen Datenvertrag, und welche Zustände braucht eine asynchrone Datenanbindung mindestens? | [→ 3. Datenanbindung und API-Zustände](#3-datenanbindung-und-api-zustände) |

---

## 1. Interaktion und UI-Zustände

> **Grundprinzip:** Ein Fahrkartenautomat, bei dem der Bildschirm, die Kartenausgabe und die Geldrückgabe jeweils unabhängig voneinander "wissen", was gerade passiert, kann leicht widersprüchliche Zustände anzeigen – Karte ausgegeben, aber Bildschirm zeigt noch "bitte warten". Erst eine gemeinsame, zentrale Zustandsquelle verhindert das.

### 1.1 DOM, Ereignis und Zustand

Das **DOM (Document Object Model)** bildet die HTML-Seite als Baum aus Objekten ab, den JavaScript lesen und verändern kann. Ein **Ereignis** (Event) signalisiert, dass etwas passiert ist, durch die Nutzerin oder das System (`click`, `submit`, `input`, `keydown`). Der **UI-Zustand** sagt, in welcher fachlichen Lage sich die Oberfläche gerade befindet, zum Beispiel "leer", "lädt" oder "gespeichert".

Jede Interaktion lässt sich als Übergang lesen: alter Zustand und Ereignis, eventuell mit Bedingung, ergeben einen neuen Zustand mit sichtbarer Rückmeldung. Beispiel: Ein Formular steht auf "Entwurf". Schickt jemand gültige Daten ab, wechselt es zu "wird gespeichert", der Speichern-Button wird gesperrt und ein Hinweis zeigt, dass gerade gespeichert wird.

> **Wichtig für die Prüfung:** Was gerade im DOM steht, ist **kein** Zustandsmodell. Ändern verschiedene Funktionen jede für sich Klassen, Texte und Attribute, zeigt die Seite irgendwann zwei Dinge gleichzeitig, die nicht zusammenpassen. Deshalb gibt es einen ausdrücklich geführten Zustand im Code, und die Anzeige wird daraus erzeugt. Andersherum geht es schief. 🔴

### 1.2 Ereignisbehandlung strukturieren

Keine HTML-Inlinehandler (`onclick="…"`) – ein **Listener** wird im JavaScript registriert. Empfohlene Trennung in drei Schritte: (1) **DOM lesen** (Eingaben/Ziel ermitteln), (2) **Zustand ändern** (fachliche Entscheidung), (3) **darstellen** (sichtbare UI aktualisieren).

```js
form.addEventListener("submit", handleSubmit);

function handleSubmit(event) {
  event.preventDefault();
  if (!(event.target instanceof HTMLFormElement)) return;
  const data = new FormData(event.target);
  state.action = event.submitter?.name ?? "default"; // bei mehreren Submit-Buttons
  state.saving = true;
  render();
}
```

Bei mehreren Submit-Buttons mit unterschiedlicher Bedeutung liefert `event.submitter` den konkret verwendeten Button – die zentrale Verarbeitung bleibt dabei am Formular, ohne die Bedeutung des jeweiligen Submitters zu verlieren.

> **Wichtig für die Prüfung:** Ein Formular wird über `submit` verarbeitet statt über den `click` einer bestimmten Schaltfläche – aber nicht, weil `click` die Eingabetaste grundsätzlich verpasst: Beim impliziten Absenden löst der Browser laut HTML-Standard zuerst ein `click`-Event auf dem Standard-Submit-Button aus, bevor das `submit`-Event auf dem Formular feuert. Ein einzelner `click`-Listener auf dem Standard-Button erreicht die Eingabetaste in einfachen Formularen also durchaus. `submit` ist trotzdem die robustere Stelle, weil die Logik an die **Formularaktion** statt an einen einzelnen Submitter gebunden wird: Das deckt mehrere Submit-Buttons, `form.requestSubmit()` und spätere Strukturänderungen zuverlässiger ab als ein Listener auf genau einer Schaltfläche. Programmatisches `form.submit()` (ohne "request") löst weder `click` noch `submit` aus und umgeht die native Constraint-Validierung – dafür ist `form.requestSubmit()` die passendere Wahl. 🔴

### 1.3 Bibliothek, Modul und Framework

| Begriff | Kernidee | IHK-Relevanz |
| --- | --- | --- |
| **Bibliothek** | Stellt wiederverwendbare Funktionen bereit – der Anwendungscode ruft sie gezielt auf | 🔴 |
| **Modul** | Kapselt zusammengehörigen Code und stellt definierte Schnittstellen/Exporte bereit | 🟡 |
| **Framework** | Gibt Anwendungsrahmen und zentrale Abläufe vor – ruft an festgelegten Stellen den Anwendungscode auf | 🔴 |

"Vorhanden" bedeutet nicht automatisch "geeignet". Bei jeder Abhängigkeit werden dokumentiert: Zweck im Projekt, Version/Quelle, Lizenz, Wartungs-/Abhängigkeitsfolgen, Einfluss auf Semantik/Barrierefreiheit, begründete Alternative.

> **Wichtig für die Prüfung:** Bibliothek und Framework sind **nicht dasselbe**. Eine Bibliothek benutzt du: Dein Code ruft ihre Funktionen auf, wann er will. Ein Framework gibt den Rahmen vor und ruft deinen Code an festgelegten Stellen auf. Das nennt man "Inversion of Control". In der Praxis verschwimmt die Grenze manchmal, dann zählt, wie du das Paket in deinem Projekt einsetzt. 🔴

### 1.4 Rückmeldung, Live-Region und Fokusführung

Regeln für den Fokus: Öffnet sich ein Dialog, landet der Fokus auf seinem ersten sinnvollen Element. Schließt er sich, kehrt der Fokus zu dem Button zurück, der ihn geöffnet hat. Gibt es mehrere Fehler, hilft eine Fehlerübersicht beim Einstieg. Nach einer erfolgreichen Aktion springt der Fokus nicht unerwartet weg. Die Fokusmarkierung bleibt immer sichtbar. Verschwindet das Element mit dem Fokus oder wird es gesperrt, setzt du den Fokus bewusst auf ein passendes Nachbarelement.

> **IHK-Typfrage:** *"Ein Team registriert für einen Speichern-Button einen `click`-Listener statt eines `submit`-Listeners auf dem umgebenden Formular. Ist das fachlich robust, und wie sollte die Implementierung geändert werden?"*
> **Musterantwort:** Ein `click`-Listener auf dem Standard-Submit-Button erreicht die Eingabetaste in einfachen Formularen durchaus, da der Browser beim impliziten Absenden zuerst ein `click`-Event auf diesem Button auslöst. Die Bindung ist aber an genau diese eine Schaltfläche geknüpft statt an die Formularaktion selbst – bei mehreren Submit-Buttons mit unterschiedlicher Bedeutung, bei programmatischem `form.requestSubmit()` oder bei späteren Strukturänderungen des Formulars ist das nicht zuverlässig genug. Die Implementierung sollte deshalb einen `submit`-Listener auf dem `<form>`-Element registrieren und `event.preventDefault()` aufrufen, um das native Neuladen zu verhindern; dadurch werden native Validierung, Tastaturbedienung und unterschiedliche Submitter einheitlich behandelt.

---

## 2. Validierung und Fehlerrückmeldung

> **Grundprinzip:** Ein Türsteher, der Ausweise nur oberflächlich anschaut (Clientvalidierung), verhindert vielleicht die meisten Probleme – aber wer wirklich verlässlich draußen bleiben soll, braucht eine Kontrolle, die sich nicht umgehen lässt (Servervalidierung). Beide Ebenen haben unterschiedliche Aufgaben.

### 2.1 Regelarten und Durchsetzungsort

Drei Regelarten beschreiben, **was** geprüft wird – der Durchsetzungsort beschreibt separat, **wo** verbindlich geprüft werden muss:

| Regelart | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Syntaktisch** | Form/Wertebereich, z. B. Pflichtfeld, maximale Länge | 🔴 |
| **Semantisch** | Fachliche Bedeutung, z. B. Enddatum nicht vor Startdatum | 🔴 |
| **Feldübergreifend** | Beziehung mehrerer Werte (oft zugleich eine semantische Regel) | 🟡 |

Jede Regel wird vor der Implementierung dokumentiert: betroffenes Feld, fachlicher Zweck, gültige/ungültige Beispiele, erwartete Meldung, Zuständigkeit Client/Server.

> **Wichtig für die Prüfung:** "Serverseitig" ist **keine weitere Regelart** neben den anderen, sondern sagt, **wo** eine Regel geprüft wird. Im Client gibt es schnelles Feedback, auf dem Server die verbindliche Entscheidung, und dieselbe Regel, ob Format, Bedeutung oder Abhängigkeit zwischen Feldern, steht oft an beiden Stellen. Prüfungen im Browser machen die Bedienung angenehmer, schützen aber **nichts**: Browsercode lässt sich ändern, und Anfragen lassen sich auch ganz ohne Browser direkt ans Backend schicken. Jede sicherheits- oder geschäftsrelevante Regel muss zusätzlich serverseitig durchgesetzt werden (vertieft in LF10a Teil 3). 🔴

### 2.2 Native HTML-Validierung zuerst

HTML bringt schon viel mit: `required`, passende `type`-Werte sowie `min`, `max`, `minlength`, `maxlength` und `pattern`. Browser und Handy-Tastaturen kennen diese Angaben, deshalb gehören sie **nicht einfach per `novalidate` abgeschaltet**. Für manche Fachregeln reichen sie trotzdem nicht, etwa wenn ein Feld vom Wert eines anderen abhängt. Eigenes JavaScript ergänzt dann genau diese Lücke.

### 2.3 Fachliche Regeln und Race Conditions

```js
function validatePeriod(start, end) {
  if (!start || !end) return null;
  if (end < start) return "Das Enddatum darf nicht vor dem Startdatum liegen.";
  return null;
}
```

Von einer **Race Condition** spricht man, wenn das Ergebnis davon abhängt, welcher von mehreren parallel laufenden Vorgängen zuerst fertig wird. Prüft ein Feld seine Eingabe asynchron beim Server, kann die Antwort zu einer alten Eingabe nach der zur neuen eintreffen und sie überschreiben. Abhilfe: veraltete Anfragen abbrechen, jede Anfrage nummerieren und nur die Antwort verwenden, die zur aktuellen Eingabe gehört.

### 2.4 Gute Fehlermeldungen und Testwerte

Eine Fehlermeldung hilft, wenn sie sagt, (1) was nicht stimmt, (2) wie man es richtig macht und (3), falls wichtig, was sonst passiert. "Ungültig" hilft niemandem, "Wähle 1 bis 10 Tickets." schon. Alles, was schon richtig eingegeben war, **bleibt stehen**, und Fehler sind nicht nur an der Farbe erkennbar.

Bei einem Wertebereich testet man meist mindestens fünf Werte (Grenzwertanalyse): einen unterhalb der Untergrenze, die Untergrenze selbst, einen typischen Wert aus der Mitte, die Obergrenze selbst und einen oberhalb. Bei 1 bis 10 Tickets also 0, 1, 5, 10 und 11. **Negativtests** zeigen, dass falsche Eingaben abgelehnt werden, **Grenztests** prüfen genau die Kanten zwischen erlaubt und verboten, **Korrekturtests**, ob man nach einem Fehler weitermachen kann, ohne Eingaben zu verlieren. **Modellbasiertes Testen** leitet die Testfälle planmäßig aus einem vereinfachten Modell ab, etwa aus der Regelmatrix. Ausgeführt werden müssen die Tests trotzdem.

> **IHK-Typfrage:** *"Ein Formular zeigt bei ungültiger Eingabe nur die Meldung 'Fehler'. Bewerten Sie das und schlagen Sie eine bessere Meldung für ein Feld 'Anzahl Tickets (1–10)' vor."*
> **Musterantwort:** Mit "Fehler" weiß niemand, was falsch ist oder was zu ändern wäre. Besser: "Wähle 1 bis 10 Tickets." Der Satz zeigt in einem Zug, dass der Wert außerhalb des erlaubten Bereichs liegt und welcher Bereich gilt. Die Meldung sollte technisch mit dem Feld verbunden sein (z. B. über `aria-describedby`), und der bereits eingegebene, fehlerhafte Wert sollte erhalten bleiben statt das Feld zu leeren.

---

## 3. Datenanbindung und API-Zustände

> **Grundprinzip:** Ein Kellner, der Bestellungen direkt an zufällige Küchenmitarbeiter weiterreicht statt über eine feste Ausgabestelle, macht die Küche unnötig kompliziert auszutauschen. Eine feste Ausgabestelle (Zugriffsschicht) lässt die Küche im Hintergrund wechseln, ohne dass sich am Bestellvorgang etwas ändert.

### 3.1 Datenvertrag

Ein **Datenvertrag** legt fest, welche Daten in welcher Form und mit welcher Bedeutung zwischen Oberfläche und Datenquelle fließen. Ein Beispiel-JSON allein ist noch keiner. Pro Feld gehören mindestens dazu: Name und was er fachlich bedeutet, Datentyp und Format, Pflicht oder optional. Ein Beispielwert und der Hinweis, wo die UI das Feld zeigt, helfen beim Bauen und Testen, gehören aber eher zur UI-Beschreibung. Damit die Anbindung robust wird, regelt der Vertrag auch leere Werte, Fehlerantworten und was passiert, wenn Daten nicht zum Vertrag passen. Mit dem Datenbankschema hat er **nichts** zu tun: Er beschreibt nur die vereinbarte Schnittstelle und nur das, was für diesen Zweck gebraucht wird.

### 3.2 Fixture, Mock-Service und Test-API

| Variante | Stärke | Grenze | IHK-Relevanz |
| --- | --- | --- | --- |
| **Fixture** | Einfach, offline, reproduzierbar | Simuliert Transport/Schreibvorgänge nur begrenzt | 🔴 |
| **Mock-Service** | Spielt gezielt echte Situationen nach, auch Fehler und Verzögerung | Muss erst gebaut und dann gepflegt werden | 🟡 |
| **Test-API** | Echte Übertragung, echter Vertrag | Muss erreichbar sein, braucht eine Testumgebung und unbedenkliche Testdaten | 🟡 |

Produktive Endpunkte und Produktionszugangsdaten gehören nicht in Test-Fixtures oder unkontrollierte Lernumgebungen. Externe/fremde Systeme dürfen nur verwendet werden, wenn ihre Nutzung ausdrücklich vorgesehen und autorisiert ist und geeignete, dafür bestimmte Testdaten verwendet werden.

### 3.3 Zugriffsschicht (Repository) und Bezug zu Teil 1

```js
export async function listBookings() { /* Transportdetail */ }
export async function createBooking(input) { /* Transportdetail */ }
```

Diese Zwischenschicht heißt oft **Repository**. Die UI ruft dort Funktionen mit fachlichen Namen auf, etwa `ladeOffeneAuftraege()`, und muss nicht wissen, ob die Daten gerade aus einer Fixture, einem Mock-Service oder einer Test-API kommen. Mit den Mustern aus Teil 1 passt das gut zusammen: In der Drei-Schichten-Architektur sitzt die UI in der Präsentationsschicht, die Fachlogik in der Logikschicht und das Speichern in der Datenschicht. Client-Server sagt, welches System welche Rolle übernimmt und wie sie über eine Schnittstelle reden. MVC ordnet obendrein die Aufgaben innerhalb einer Anwendung. **Den Datenvertrag und eine saubere Trennung zwischen UI und Backend braucht es trotzdem, kein Muster nimmt dir das ab.**

### 3.4 Asynchrone Zustände und die `fetch()`-Falle

```js
async function loadItems() {
  renderState("loading");
  try {
    const response = await fetch("./fixtures/items.json");
    if (!response.ok) {
      renderState("technical-error", { status: response.status });
      return;
    }
    let items;
    try {
      items = await response.json();
    } catch {
      renderState("contract-error"); // Antwort ist kein gültiges JSON
      return;
    }
    if (!Array.isArray(items)) {
      renderState("contract-error"); // Antwort ist JSON, aber kein Array
      return;
    }
    renderState(items.length ? "data" : "empty", items);
  } catch (error) {
    renderState("technical-error"); // z. B. Netzwerk-/Transportfehler oder bewusster Abbruch (siehe AbortController, Abschnitt 3.5)
  }
}
```

Der äußere `catch`-Block fängt technische Probleme wie Netzwerkfehler ab. HTTP-Fehlerstatus und Vertragsverletzungen (ungültiges JSON, falsche Struktur) werden davon getrennt und jeweils dem passenden Zustand zugeordnet – ein vereinfachtes Lernbeispiel könnte mehrere technische Unterfälle zunächst zusammenfassen, sollte das aber transparent machen statt sie unbemerkt zu vermischen.

**Bei einer Datenabfrage** (wie im Beispiel oben) benötigt die UI mindestens: **Laden**, **Daten vorhanden**, **keine Daten vorhanden**, **Vertragsverletzung** (`contract-error`), **technischer/unbekannter Fehler** – je nach Anwendung kommt ein **erwartbarer fachlicher Fehler** hinzu. **Bei einer Datenübermittlung** (Schreibvorgang) werden typischerweise eigene Zustände wie `saving` (verhindert Mehrfachübermittlung), `success` und ein fachlicher `business-error` benötigt – das sind zwei unterschiedliche, wenn auch verwandte Zustandsmaschinen. Jeder Zustand nennt den nächsten sinnvollen Schritt.

> **Wichtig für die Prüfung:** Das Promise von `fetch()` wird **auch bei 404 oder 500 erfüllt**, abgelehnt wird es nur bei Netzwerkfehlern. Du musst also selbst `response.ok` abfragen, sonst behandelt dein Code eine Fehlerantwort wie Erfolg. Danach prüfst du, ob die Antwort zum Datenvertrag passt (im Beispiel: Ist `items` wirklich ein Array?). Passt sie nicht, bekommt das einen eigenen Zustand (`contract-error`) und wird **nicht** als leere Liste angezeigt. "Keine Daten" heißt: Die Anfrage hat geklappt, es gibt nur nichts. "Fehler" heißt: Wir wissen nicht, was da wäre. Beides verlangt andere nächste Schritte. 🔴

### 3.5 Race Conditions, optimistische UI und Verantwortungsgrenzen

Klickt sich jemand schnell durch Filter, kann eine langsame Antwort zum alten Filter das Ergebnis zum neuen überschreiben. Dagegen helfen `AbortController`, eine Anfrage-ID oder der Abgleich mit dem gerade gesetzten Filter. Eine **optimistische UI** zeigt den Erfolg schon an, bevor der Server ihn bestätigt hat. Das fühlt sich flott an, braucht aber einen Plan, wie die Anzeige bei einem Fehler zurückgenommen wird. Bei wichtigen Aktionen wartet man besser auf die Bestätigung (pessimistisch). Optimistische UI ist eine Vertiefung, keine Pflichtannahme.

Wer ist beim Testen wofür zuständig? Die **UI** für klare Zustände, Schutz vor Fehleingaben und die Möglichkeit, es nochmal zu versuchen. Das **Backend** für die verbindlichen Fachregeln, das Speichern und die Rechteprüfung. Der **Betrieb** dafür, dass alles erreichbar ist, überwacht und protokolliert wird. Der **Fachprozess** für Entscheidungen und die Frage, wer bei Problemen eingreift.

> **IHK-Typfrage:** *"Eine Liste zeigt bei einer leeren Kategorie denselben Bildschirm wie bei einem Netzwerkfehler. Bewerten Sie das."*
> **Musterantwort:** Das ist problematisch, weil beide Situationen unterschiedliche Ursachen und unterschiedliche sinnvolle nächste Schritte haben. Bei einer leeren Kategorie war die Anfrage erfolgreich – es gibt schlicht keine Einträge, ein sinnvoller nächster Schritt wäre z. B. "Kategorie wechseln" oder "Filter zurücksetzen". Bei einem Netzwerkfehler ist unbekannt, ob überhaupt Daten existieren – der sinnvolle nächste Schritt ist "Erneut versuchen". Werden beide Fälle gleich dargestellt, kann eine Person fälschlich glauben, es gebe tatsächlich keine Daten, obwohl nur die Anfrage gescheitert ist (oder umgekehrt unnötig einen Fehler vermuten). Die beiden Zustände "keine Daten vorhanden" und "technischer Fehler" müssen deshalb unterscheidbar dargestellt werden.

---

## 4. Zusammenspiel der Konzepte in LF10a Teil 2

Die drei Module bilden zusammen die technische Umsetzung der in Teil 1 konzipierten Struktur: **Interaktion und UI-Zustände** (Abschnitt 1) liefern das Zustandsmodell, mit dem Ereignisse nachvollziehbar verarbeitet werden. **Validierung** (Abschnitt 2) stellt sicher, dass nur sinnvolle Daten in dieses Zustandsmodell gelangen – mit der wichtigen Einschränkung, dass Clientvalidierung allein nicht genügt. **Datenanbindung** (Abschnitt 3) verbindet das Zustandsmodell mit einer austauschbaren, gekapselten Datenquelle und definiert, welche zusätzlichen Zustände (Laden, Fehler, Vertragsverletzung) dabei entstehen. Die Architekturmuster aus Teil 1 (Drei-Schichten, Client-Server, MVC) ziehen sich als Ordnungsrahmen durch alle drei Module – das Repository-Pattern aus Abschnitt 3.3 **ergänzt** diese Muster um eine gekapselte Zugriffsschicht für Daten, statt einfach eine "Anwendung" von ihnen zu sein: Drei-Schichten beschreibt strukturelle Aufteilung, Client-Server die Verteilung, MVC die Verantwortung innerhalb der Anwendung, Repository die Abstraktion des Datenzugriffs – sie spielen zusammen, ohne in einer festen Hierarchie zueinander zu stehen. Die durchgängige Warnung "Ausgeblendet/Client-geprüft ist nicht geschützt/sicher" aus Teil 1 setzt sich hier fort und wird in Teil 3 (Rollen, Datenschutz, sichere UI) vertieft.

---

## 5. Typische Prüfungsfallen

| # | Falle | Richtigstellung | IHK-Relevanz |
| --- | --- | --- | --- |
| 1 | Was im DOM steht, ist der Zustand | Der Zustand wird im Code ausdrücklich geführt, und die Anzeige folgt daraus, nicht andersherum | 🔴 |
| 2 | Ein `click`-Listener auf die Speichern-Schaltfläche deckt das Formular vollständig ab | Erreicht die Eingabetaste beim Standard-Button meist durchaus, bindet die Logik aber an genau diesen Submitter statt an die Formularaktion – bei mehreren Buttons oder `requestSubmit()` unzuverlässig | 🔴 |
| 3 | Bibliothek und Framework sind austauschbare Begriffe | Bibliothek: Anwendungscode ruft auf; Framework: ruft eigenen Code an vorgesehenen Stellen auf | 🔴 |
| 4 | Clientvalidierung ist eine vertrauenswürdige Sicherheits- oder Autorisierungsgrenze | Sie verbessert nur die Bedienung – Code im Browser kann umgangen werden, sicherheitsrelevante Regeln müssen serverseitig gelten | 🔴 |
| 5 | Native HTML-Validierung sollte durch eigene Logik ersetzt werden | Native Funktionen sind in Browser/Tastatur integriert und sollten nicht pauschal per `novalidate` abgeschaltet werden | 🟡 |
| 6 | Ein typischer gültiger Wert reicht als Test | Fehler stecken besonders oft genau an den Grenzen des erlaubten Bereichs, deshalb braucht es Grenzwerttests | 🟡 |
| 7 | `fetch()` wirft bei jedem HTTP-Fehler eine Exception | Viele Fehlerstatus erfüllen das Promise regulär – `response.ok` muss separat geprüft werden | 🔴 |
| 8 | Leere Liste und Fehler kann man gleich anzeigen | Die leere Liste ist ein Ergebnis, beim Fehler gibt es keins; Nutzer:innen brauchen in beiden Fällen einen anderen Hinweis, wie es weitergeht | 🔴 |
| 9 | Ein Beispiel-JSON reicht als Datenvertrag | Es fehlen Bedeutung, Format, Pflichtfelder und Fehlerfälle, also bleibt unklar, wie die UI auf Abweichungen reagiert | 🟡 |

---

## 6. Vertiefung und Ausblick (freiwillig – für den ersten Durchgang nicht erforderlich)

- **Optimistische UI im Detail**: Konkrete Rücknahmestrategien (Rollback, Re-Sync) bei fehlgeschlagener Bestätigung durch die Datenquelle.
- **`AbortController` im Detail**: Wie laufende `fetch()`-Anfragen gezielt abgebrochen werden, um Race Conditions zu vermeiden.
- **Modellbasiertes Testen im Detail**: Wie aus einer Regelmatrix systematisch eine vollständige, überschneidungsfreie Testfallmenge abgeleitet wird.
- **State-Management-Bibliotheken**: Wie umfangreichere Anwendungen das in Abschnitt 1 beschriebene Zustandsprinzip mit dedizierten Werkzeugen strukturieren.
- **Web Components und Zugriffsschichten**: Wie sich das Repository-Pattern aus Abschnitt 3.3 mit gekapselten UI-Komponenten kombinieren lässt.

---

## 7. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Was ist ein UI-Zustand, und warum reicht der sichtbare DOM als Modell nicht aus? | Die fachlich relevante Situation der Oberfläche; der DOM kann bei unabhängigen Änderungen widersprüchliche Situationen anzeigen |
| 2 | Warum ist `submit` robuster als ein `click`-Listener auf eine Schaltfläche, obwohl `click` die Eingabetaste beim Standard-Button meist auch erreicht? | Bindet an die Formularaktion statt an einen einzelnen Submitter – deckt mehrere Submit-Buttons, `requestSubmit()` und Strukturänderungen zuverlässiger ab |
| 3 | Was unterscheidet Bibliothek und Framework? | Bibliothek: Anwendungscode ruft auf; Framework: ruft eigenen Code an vorgesehenen Stellen auf |
| 4 | Nenne drei Regelarten bei der Validierung, und was ist der Durchsetzungsort? | Syntaktisch, semantisch, feldübergreifend – Durchsetzungsort (client- oder serverseitig) ist eine separate Dimension, keine vierte Regelart |
| 5 | Warum ist Clientvalidierung keine Sicherheitsgrenze? | Code im Browser kann verändert/umgangen werden, Eingaben können direkt ans Backend gesendet werden |
| 6 | Nenne fünf typische Testwerte für einen Wertebereich. | Knapp unter Grenze, auf unterer Grenze, normaler gültiger Wert, auf oberer Grenze, knapp über Grenze |
| 7 | Was gehört mindestens in einen Datenvertrag, und was ist eher optionale Ergänzung? | Mindestens: Name/Bedeutung, Datentyp/Format, Pflicht/optional; Beispielwert und UI-Verwendung erleichtern die Umsetzung, sind aber eher UI-Spezifikation als Kernbestandteil |
| 8 | Warum reicht `response.ok` allein nicht, um Datenkorrektheit sicherzustellen? | Es prüft nur den HTTP-Status, nicht ob der Antwortkörper dem Datenvertrag entspricht (dafür: eigener `contract-error`-Zustand) |
| 9 | Was unterscheidet Race Condition bei Validierung und bei Datenanbindung im Kern? | Beide entstehen, wenn das Ergebnis vom zeitlichen Ablauf nebenläufiger Vorgänge abhängt – bei Validierung kann eine veraltete Prüfantwort, bei Datenanbindung eine veraltete Ladeantwort den aktuellen Zustand überschreiben; Lösung jeweils über Abbruch, Sequenz-/Anfrage-ID oder Vergleich mit aktuellem Zustand |

---

## 8. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **DOM/Ereignis/Zustand** | Objektstruktur / Aktion-Meldung / fachlich relevante Situation |
| **Listener** | Im JavaScript registrierte Reaktion auf ein Ereignis (kein Inline-Handler) |
| **submit vs. click** | `submit` bindet an die Formularaktion (mehrere Submitter, `requestSubmit()`), `click` nur an eine Schaltfläche – Enter erreicht click beim Standard-Button meist trotzdem |
| **Bibliothek / Framework** | Wird aufgerufen / ruft eigenen Code auf (Inversion of Control) |
| **Clientvalidierung ≠ Sicherheit** | Nur Bedienkomfort – sicherheitsrelevante Regeln müssen serverseitig gelten |
| **Native HTML-Validierung** | `required`, `min`/`max`, `pattern` – nicht pauschal per `novalidate` abschalten |
| **Race Condition** | Ergebnis hängt von Reihenfolge nebenläufiger Vorgänge ab – Lösung: Abbruch/ID/Vergleich |
| **Datenvertrag** | Bedeutung, Typ, Pflichtstatus, Fehlerfälle – mehr als Beispiel-JSON |
| **Fixture / Mock-Service / Test-API** | Statisch offline / steuerbar simuliert / echter Transport in Testumgebung |
| **Repository-Pattern** | Zugriffsschicht mit fachlich benannten Operationen, kapselt Datenquelle |
| **response.ok** | Prüft nur HTTP-Status, nicht Datenvertrag-Konformität |
| **contract-error** | Eigener Zustand für Vertragsverletzung, nicht gleich "keine Daten" |
| **Optimistische UI** | Erfolg vor endgültiger Bestätigung angezeigt – braucht Rücknahmestrategie |

---

## 9. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die Prüfung hören will |
| --- | --- | --- |
| Ereignisbehandlung bewerten | "Bewerten Sie diese Listener-Registrierung" | Konkrete scheiternde Bedienwege benennen, nicht nur "das ist schlecht" |
| Validierungsregel einordnen | "Welche Art von Regel ist X?" | Syntaktisch/semantisch/feldübergreifend korrekt zuordnen, Durchsetzungsort (Client/Server) getrennt davon benennen |
| Fehlermeldung verbessern | "Verbessern Sie diese Meldung" | Problem + erwartete Korrektur konkret benennen, keine vage Formulierung |
| API-Zustand einordnen | "Welcher Zustand liegt hier vor?" | Zwischen leer/Fehler/Vertragsverletzung sauber unterscheiden, Begründung liefern |
| Architekturbezug herstellen | "Wo gehört diese Komponente hin?" | Bezug zu Drei-Schichten/Client-Server/MVC aus Teil 1 explizit herstellen |

---

## 10. Merksätze für das Fachgespräch

> Ein Ereignis ist fertig behandelt, wenn Zustand, Anzeige und der nächste mögliche Schritt zueinander passen.

> Gute Validierung sagt nicht nur "falsch", sondern auch, wie es richtig geht.

> Clientvalidierung ist Komfort, nicht Sicherheit – die verbindliche Regel gilt serverseitig.

> Robust wird eine Datenanbindung erst, wenn Datenvertrag, Zustände und Zuständigkeiten zusammen geplant werden.

> Leer und fehlerhaft sind zwei verschiedene Geschichten – beide brauchen ihren eigenen nächsten Schritt.

---

```yaml
dokument: LF10a-Teil2-wiki-artikel
lernfeld: "LF10a Teil 2 (Module 10a.5-10a.7)"
titel: "Interaktion & Daten"
typ: "Typ A – Kompakter Prüfungs-Wiki (FIAE-fokussiert)"
status: final
stand: 2026-09-14
quellen_intern:
  - "LF10a Interaktion/UI-Zustände, Validierung/Fehlerrückmeldung, Datenanbindung/API-Zustände)"
  - "Bewusster Rückbezug zu LF10a Teil 1 (Architekturmuster, UI-Zustände) statt Wiederholung - Repository-Pattern als ergänzende Zugriffsschicht, nicht als Anwendung der dort eingeführten Muster"
  - "Offizielle FIAE-AP2-Bezeichnung 'Planen eines Softwareproduktes' aus Teil-1-Korrektur übernommen (bereits web-verifiziert)"
quellen_fachlich:
  - titel: "WHATWG HTML Living Standard, WHATWG Fetch Standard"
    herausgeber: "WHATWG"
    status: "Rohmaterial verlinkt Primärquellen; fetch()/response.ok-Verhalten und AbortController sind stabile Web-Plattform-Standards, keine Web-Verifikation nötig"
  - titel: "Architekturmuster (Repository-Pattern, Drei-Schichten/Client-Server/MVC aus LF10a Teil 1), Validierungs-/Teststrategien"
    herausgeber: "Rohmaterial + etabliertes Software-Engineering-Standardwissen"
    status: "stabile Konzepte, keine Web-Verifikation nötig"
review_historie:
  - runde: 1
    datum: 2026-09-14
    ergebnis: "Erstdraft erstellt aus den recherchierten Quellen. Als ein zusammenhängender Artikel (Teil 2 von 3) verfasst. Bewusste Rückbezüge zu Teil 1 (Architekturmuster, UI-Zustände, offizielle AP2-Bezeichnung) statt Wiederholung. Von Anfang an vorsichtig und kontextbezogen formuliert, basierend auf den Lektionen aus Teil 1 und den LF7/LF9-Review-Historien (keine Absolutheiten ohne Einschränkung, konsistente Cheatsheet-/Selbsttest-Formulierungen von Beginn an)."
  - runde: 2
    datum: 2026-09-14
    ergebnis: "3 Reviews eingearbeitet. Wichtigster Fund (2 Reviews, eigenständig web-verifiziert via HTML-Spec): 'click scheitert bei Enter'-Aussage war zu absolut - beim impliziten Absenden löst der Browser laut HTML-Standard zuerst ein click-Event auf dem Standard-Submit-Button aus, bevor submit feuert. submit bleibt trotzdem robuster, aber aus anderen Gründen (mehrere Submitter, requestSubmit(), Strukturänderungen) - an vier Stellen korrigiert (Wichtig-Block, Typfrage, Prüfungsfalle, Selbsttest, Cheatsheet). Zweitwichtigster Fund (2 Reviews, gut begründet): 'vier Regelarten' vermischte Regelart mit Durchsetzungsort - 'serverseitig' ist kein Regeltyp auf gleicher Ebene wie syntaktisch/semantisch/feldübergreifend, sondern eine separate Dimension - Abschnitt 2.1 umstrukturiert. Dritter Fund (1 Review, klare interne Inkonsistenz): API-Zustände als 'sechs' benannt, aber contract-error im Code macht sieben - korrigiert, Codebeispiel zusätzlich verbessert (HTTP-Fehler/JSON-Parse-Fehler/Array-Vertragsverletzung sauber getrennt statt im catch-Block vermischt). Weitere Korrekturen: Repository-Pattern nicht mehr als 'Anwendung' der Architekturmuster dargestellt, sondern als Ergänzung ohne Hierarchie; AP1-Erwähnung aus Kopf entfernt (Artikelinhalt ist AP2-spezifisch); Fixture/Mock/Test-API-Absolutheit ('fremde Systeme grundsätzlich ausgeschlossen') abgeschwächt; Moduldefinition präzisiert; Selbsttest 9 (Race Condition) allgemeiner und korrekter gefasst. Zum wiederholten Mal behauptete eine Review Claude-Chat-Links im Dokument - beim Abgleich nicht bestätigt."
  - runde: 3
    datum: 2026-09-14
    ergebnis: "3 Reviews eingearbeitet. Zwei interne Inkonsistenzen aus Runde 2 nachgezogen (Prüfungstaktik nannte noch 'serverseitig' als Regelart, YAML-Quellenblock noch 'konkrete Anwendung' statt 'ergänzende Zugriffsschicht' fürs Repository-Pattern). Fetch-Beispiel: irreführender 'Timeout'-Kommentar korrigiert (fetch() hat keinen eingebauten Timeout-Mechanismus) und um event.submitter ergänzt (macht die 'mehrere Submitter'-Aussage im Code sichtbar). API-Zustände konzeptionell in Lese- und Schreib-Zustandsmaschine getrennt statt einer vermischten Liste (u. a. weil 'erfolgreiche Übermittlung' im gezeigten loadItems()-Beispiel gar nicht vorkommt). Fokusregel präzisiert (sichtbarer Indikator vs. Fokus-Ersatz beim Entfernen als zwei getrennte Aspekte). 'Fünf Testklassen' zu 'fünf Testwerten' präzisiert (keine feste allgemeine Kategorie). Datenvertrag-Definition erweitert (Fehler-/Leerwertverhalten ergänzt, UI-Sichtbarkeit als optional statt Kernbestandteil gekennzeichnet). Zum wiederholten Mal (jetzt mehrfach über mehrere Runden) behauptete eine Review sehr konkret Claude-Chat-Links und einen abgeschnittenen YAML-Block - beide Behauptungen beim Abgleich erneut nicht bestätigt."
  - runde: 4
    datum: 2026-09-14
    ergebnis: "Eigene Abschlussprüfung: Abschnittsüberschrift 2.4 trug noch 'Testklassen' statt der in Runde 3 korrigierten 'Testwerte' - nachgezogen. Selbsttest 7 listete 'Beispielwert, Verwendung in der UI' noch als Kernbestandteil des Datenvertrags, obwohl 3.1 das gerade als optionale Ergänzung statt Kernbestandteil präzisiert hatte - angeglichen. Keine weiteren Fachfehler gefunden."
  - runde: 5
    datum: 2026-09-14
    ergebnis: "Nachträgliche Ergänzung auf Wunsch des Auftraggebers (Konsistenz-Nacharbeit, analog zu LF10a Teil 1 und Teil 3): IHK-Relevanz-Markierungen (🔴/🟡/🟢) tatsächlich in den Fließtext eingebaut - Begriffstabellen (Bibliothek/Modul/Framework, Regelarten, Fixture/Mock-Service/Test-API, Prüfungsfallen) sowie alle Wichtig-für-die-Prüfung-Blöcke markiert. Von 1 auf 24 tatsächliche Markierungen. Keine inhaltlichen Änderungen, rein ergänzende Markierung."
freigabe: "Final gesetzt nach 4 Runden (3 externe Prüfrunden + 1 eigene Abschlussprüfung, 2026-09-14) – Freigabe durch Autor:in bestätigt. Runde 5: nachträgliche Markierungs-Ergänzung, Inhalt unverändert final."
```