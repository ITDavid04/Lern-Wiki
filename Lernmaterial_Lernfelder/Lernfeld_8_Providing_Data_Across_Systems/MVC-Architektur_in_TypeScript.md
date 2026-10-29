# MVC-Architektur in TypeScript

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP2 (schriftlich, Softwarearchitektur/Entwurfsmuster) + Fachgespräch
> **Lernzeit:** Ca. 45–60 Minuten
> **Status:** Final
> **Stand:** 2026

---


## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|-------|-----------|
| 1 | Was ist MVC und wozu dient die Trennung der drei Schichten? | [→ 1. Was ist MVC?](#1-was-ist-mvc) |
| 2 | Welche konkrete Aufgabe hat der Controller – und welche NICHT? | [→ 2. Thin Controller, Fat Model](#2-thin-controller-fat-model) |
| 3 | Wie unterscheidet sich Web-MVC vom klassischen (Desktop-)MVC? | [→ 3. Web-MVC vs. klassisches MVC](#3-web-mvc-vs-klassisches-mvc) |
| 4 | Welchen konkreten Vorteil bringt TypeScript in einer MVC-Architektur? | [→ 4. Warum TypeScript?](#4-warum-typescript) |
| 5 | Wie läuft eine einzelne Anfrage durch alle drei Schichten? | [→ 5. Codebeispiel & Ablauf](#5-codebeispiel--ablauf) |

---

## 1. Was ist MVC?

> **Grundprinzip:** MVC trennt Daten, Darstellung und Steuerung strikt voneinander – jede Schicht hat genau eine Verantwortung (Separation of Concerns).

**Analogie – Das Restaurant-Prinzip:**

* **View (Speisekarte & Teller):** Was der Kunde sieht und worüber er bestellt. In der IT: HTML-Seite, App-Screen oder JSON-Ausgabe.
* **Controller (Der Kellner):** Nimmt die Bestellung entgegen, leitet sie an die Küche weiter und bringt das fertige Essen zurück.
* **Model (Küche & Lager):** Zutaten (Datenbank) und Rezepte (Geschäftsregeln). Der Kunde geht nie selbst in die Küche.

### 1.1 Model, View, Controller im Detail

| Aspekt | Beschreibung | IHK-Relevanz |
|--------|---------------|:---:|
| **Model** | Verwaltet Zustände, führt Datenbankabfragen aus, setzt Fachlogik durch (z. B. Validierung) | 🔴 |
| **View** | Ausschließlich zuständig für die Darstellung der Daten – keine eigene Logik | 🔴 |
| **Controller** | Empfängt Eingaben (z. B. HTTP GET/POST), koordiniert Model-Abrufe, wählt passende View | 🔴 |
| Kopplung | Model kennt Controller/View nicht – nur die Richtung Controller → Model ist erlaubt | 🟡 |

> **IHK-Typfrage:** *„Nennen Sie die drei Bestandteile des MVC-Musters und ordnen Sie jedem eine Kernaufgabe zu."*
> **Musterantwort:** Model verwaltet Daten und Fachlogik, View übernimmt die Darstellung, Controller nimmt Eingaben entgegen und steuert den Ablauf zwischen Model und View.

---

## 2. Thin Controller, Fat Model

> **Grundprinzip:** Der Controller soll so wenig Geschäftslogik wie möglich enthalten und Aufgaben an Model bzw. Service-Klassen delegieren.

| Aspekt | Beschreibung | IHK-Relevanz |
|--------|---------------|:---:|
| Thin Controller | Enthält nur Steuerungslogik: Eingabe entgegennehmen, richtige Methode aufrufen, Ergebnis weiterreichen | 🔴 |
| Fat Model | Enthält die eigentliche Fachlogik (Validierung, Berechnungen, Datenzugriff) | 🔴 |
| Warum wichtig | Verhindert schwer wartbaren „Spaghetti-Code" und erleichtert Unit-Testing, da Model ohne Webserver/UI testbar ist | 🔴 |
| Team-Vorteil | Frontend-Team arbeitet an View, Backend-Team parallel an Model/Datenbank | 🟡 |

> **IHK-Typfrage:** *„Warum sollte Geschäftslogik nicht im Controller, sondern im Model liegen?"*
> **Musterantwort:** Weil der Controller sonst schwer testbar und unübersichtlich wird. Liegt die Logik im Model, kann sie unabhängig von Webserver und Benutzeroberfläche per Unit-Test geprüft werden, und mehrere Controller können dieselbe Logik wiederverwenden.

---

## 3. Web-MVC vs. klassisches MVC

> **Grundprinzip:** Im klassischen MVC informiert das Model die View selbst bei Änderungen (Observer Pattern). Im Web-MVC ist das Model passiv – der Controller holt aktiv die Daten.

**Klassisches Desktop-MVC (Observer Pattern) – Model benachrichtigt View aktiv:**

```

[Benutzer] ---> [ Controller ] ---> [ Model ]
                                        |
                                        v (Benachrichtigung)
                                    [  View  ]
```

**Web-MVC (Request/Response) – Model bleibt passiv, Controller holt aktiv ab:**

```

[Client] ---> (Request) ---> [ Controller ] ---> (Anfrage) ---> [ Model ]
   ^                              |                                  |
   |                              v                                  v (Daten)
   +--------- (Response) <--- [  View  ] <------------- (Rückgabe) --+
```

**Wichtig:** Nur im zweiten Diagramm läuft der Datenfluss so ab, wie es Web-Anwendungen (und damit auch das Codebeispiel in Abschnitt 5) tatsächlich umsetzen. Das Model kennt die View nicht – der Controller ist in beiden Diagrammen der einzige, der beide Seiten kennt.

| Aspekt | Klassisches MVC (z. B. Smalltalk-80, Desktop) | Web-MVC (z. B. Node.js/TypeScript) | IHK-Relevanz |
|--------|-----------------------------------------------|-------------------------------------|:---:|
| Model-Verhalten | Aktiv – benachrichtigt View bei Änderung | Passiv – wird vom Controller abgefragt | 🔴 |
| Kommunikationsweg | Model → View direkt möglich | Nur Controller → Model → Controller → View | 🔴 |
| Ursprung | 1978, Trygve Reenskaug, Xerox PARC, Smalltalk-80 | Abwandlung für zustandslose HTTP-Kommunikation | 🟢 |

---

## 4. Warum TypeScript?

> **Grundprinzip:** TypeScript erzwingt an den Schichtgrenzen von MVC exakt die Datenstrukturen, die vereinbart wurden – Fehler entstehen beim Kompilieren statt zur Laufzeit.

| Aspekt | Beschreibung | IHK-Relevanz |
|--------|---------------|:---:|
| Typsicherheit über Schichten | `Interfaces`/`Types` stellen sicher, dass das Model nur validierte Strukturen an den Controller übergibt | 🔴 |
| Frühe Fehlererkennung | Tippfehler in Feldnamen fallen beim Kompilieren auf, nicht erst beim Kunden | 🔴 |
| Testbarkeit | Entkoppelte, typisierte Schichten lassen sich isoliert per Unit-Test prüfen | 🟡 |
| Parallele Entwicklung | Interface als Vertrag zwischen Frontend- und Backend-Team | 🟢 |

> TypeScript-Interfaces bilden genau die Verträge ab, die das MVC-Prinzip der losen Kopplung verlangt: Model und View müssen sich nicht kennen, solange der Controller die typisierten Datenstrukturen einhält.

---

## 5. Codebeispiel & Ablauf

**`UserModel.ts`** – Daten & Fachlogik:

```typescript
export interface User {
  id: number;
  name: string;
  email: string;
}

export class UserModel {
  private users: User[] = [
    { id: 1, name: "David", email: "david@example.com" },
    { id: 2, name: "Lisa", email: "lisa@example.com" }
  ];

  public getAll(): User[] {
    return this.users;
  }

  public findById(id: number): User | undefined {
    return this.users.find(u => u.id === id);
  }
}
```

**`UserView.ts`** – Nur Darstellung:

```typescript
import { User } from "./UserModel";

export class UserView {
  // In einer echten Web-App würde die View hier HTML rendern oder ein
  // Template befüllen (z. B. res.send(view.render(user)) in Express).
  // Der String hier zeigt nur das Prinzip der reinen Darstellung.
  public renderUserDetail(user: User): string {
    return `[Profilansicht] ID: ${user.id} | Name: ${user.name} | E-Mail: ${user.email}`;
  }

  public renderError(message: string): string {
    return `[Fehler] ${message}`;
  }
}
```

**`UserController.ts`** – Steuerung (Thin Controller):

```typescript
import { UserModel } from "./UserModel";
import { UserView } from "./UserView";

export class UserController {
  constructor(
    private model: UserModel,
    private view: UserView
  ) {}

  public getUserProfile(id: number): string {
    const user = this.model.findById(id);

    if (!user) {
      return this.view.renderError(`Benutzer mit ID ${id} wurde nicht gefunden.`);
    }

    return this.view.renderUserDetail(user);
  }
}
```

### Ablauf einer Anfrage

1. Client ruft `getUserProfile(1)` auf (**Eingabe**).
2. **Controller** fragt das **Model** nach den Daten von ID `1`.
3. **Model** sucht typensicher und gibt das `User`-Objekt (oder `undefined`) zurück.
4. **Controller** reicht das Ergebnis an die **View** weiter – ohne selbst Fachlogik auszuführen.
5. **View** baut den fertigen String und liefert die Antwort an den Aufrufer zurück.

---

## Selbsttest

| Frage | Kurzantwort |
|-------|-------------|
| Welche Schicht darf niemals direkt von außen (Client) angesprochen werden? | Das Model – Zugriff läuft immer über den Controller |
| Was bedeutet „Fat Model"? | Fachlogik und Datenzugriff liegen im Model, nicht im Controller |
| Ist das Model in Web-MVC aktiv oder passiv? | Passiv – der Controller holt die Daten aktiv ab |
| Welchen Vorteil hat MVC für Unit-Tests? | Model kann isoliert ohne Webserver/UI getestet werden |
| Woher stammt MVC ursprünglich? | 1978, Trygve Reenskaug, Xerox PARC, Smalltalk-80 |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---------|-----------------|
| Model | Daten + Fachlogik, kennt View/Controller nicht |
| View | Reine Darstellung, keine Logik |
| Controller | Steuerung, koordiniert Model und View |
| Separation of Concerns | Trennung von Zuständigkeiten pro Schicht |

| Fat Model | Fachlogik konzentriert sich im Model |
| Observer Pattern | Model benachrichtigt View aktiv (klassisches MVC) |

**Ausblick: Verwandte Muster (optional, nicht Kern-IHK-Stoff)**

| Begriff | Kurzdefinition |
|---------|-----------------|
| MVVM* | ViewModel statt Controller, bidirektionales Data Binding (z. B. Angular/Vue) |
| MVP* | Presenter manipuliert View direkt (Desktop/ältere Android-Apps) |
| Clean/Hexagonal Architecture* | Erweiterung von MVC – Kernlogik unabhängig von Framework/DB |

*Wird in der Prüfungstaktik-Tabelle unten zur Abgrenzung von MVC benötigt – hier nur zum Nachschlagen.

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
|-------------|------------------------|--------------------------|
| Begriffserklärung | „Erläutern Sie das MVC-Muster." | Alle drei Schichten benennen + je eine klare Zuständigkeit |
| Vorteilsfrage | „Welche Vorteile bietet die Trennung nach MVC?" | Wartbarkeit, Testbarkeit, parallele Entwicklung |
| Abgrenzungsfrage | „Worin unterscheidet sich MVC von MVVM?" | ViewModel statt Controller, automatisches Data Binding nennen |
| Praxisbezug | „Wie würden Sie eine Anfrage in einer MVC-Anwendung beschreiben?" | Ablauf Controller → Model → Controller → View, mit Beispiel |
| Architekturkritik | „Was passiert, wenn Fachlogik im Controller liegt?" | Schlechte Testbarkeit, Wartungsprobleme, „Spaghetti-Code" benennen |

---

## Merksätze für die mündliche Prüfung

> Model kennt weder View noch Controller – die Abhängigkeit zeigt immer nur in eine Richtung.

> Der Controller ist der Vermittler, nicht der Ausführende – er delegiert, statt selbst zu rechnen.

> In Web-MVC ist das Model passiv: Es antwortet nur, wenn der Controller fragt.

> TypeScript macht die Schichtgrenzen von MVC verbindlich – Interfaces sind der Vertrag zwischen Model, View und Controller.

---

```yaml
titel: "MVC-Architektur in TypeScript"
typ: "Typ A - Kompakter Pruefungs-Wiki"
lernfeld: "Softwarearchitektur / Entwurfsmuster"
zielgruppe: "FIAE/FISI, 2. Lehrjahr"
pruefungsrelevanz: "AP2 schriftlich + Fachgespraech"
status: "final"
stand: "2026"
autorin_autor: "David"
```
