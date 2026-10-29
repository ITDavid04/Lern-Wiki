
# 🔄 Git-Workflow in der Praxis – Vom Ändern bis zum Synchronisieren

Diese Anleitung verbindet die drei Zustände einer Datei in Git mit den zentralen Befehlen und der Synchronisation mit einem Remote-Server.

---

## 📊 Die drei Zustände einer Datei (Modified, Staged, Committed)

Jede Datei in einem Git-Repository durchläuft genau diese drei Zustände:

| Zustand      | Bedeutung |
|--------------|-----------|
| **Modified** | Datei wurde verändert, aber noch nicht für den nächsten Commit vorgemerkt. |
| **Staged**   | Datei wurde mit `git add` in die Staging-Area aufgenommen. Sie ist für den nächsten Commit vorgemerkt. |
| **Committed**| Die Änderung ist als unveränderlicher Snapshot in der lokalen Git-Historie gespeichert. |

```

[Working Directory]    →    [Staging Area]    →    [Lokales Repository]
     modified                 staged                 committed
```

- `git add`     → verschiebt Änderungen von *modified* nach *staged*
- `git commit`  → speichert alles aus *staged* als neuen, dauerhaften Commit

---

## 🧭 Vollständiger Arbeitsablauf mit `add`, `commit`, `push`, `pull`

### 1. Änderungen vornehmen und Status prüfen

```bash

git status ```

Git zeigt z. B.:```

Changes not staged for commit:

modified:   index.html

```

→ Die Datei ist **modified**.

### 2. Änderungen vormerken (`add`)

```bash

git add index.html

```

Jetzt ist die Datei **staged**. `git status` zeigt: ```

Changes to be committed:

  modified:   index.html

```

### 3. Snapshot lokal speichern (`commit`)

```bash

git commit -m "Header-Layout korrigiert"

```

Die Änderung ist nun **committed** und hat einen eindeutigen Hash (z.B. `a1b2c3d`).

### 4. Lokale Commits auf den Remote-Server hochladen (`push`)

```bash

git push origin main

```

- `origin` = Standard-Name des Remote-Servers  
- `main`  = der aktuelle Branch  

Der Commit liegt jetzt auch auf dem Server, alle Teammitglieder können ihn sehen.

### 5. Änderungen anderer herunterladen und integrieren (`pull`)

```bash

git pull

```

Dieser Befehl vereint zwei Schritte:

1. `git fetch` – Holt alle neuen Commits vom Remote, ohne die eigenen Dateien zu ändern.  
2. `git merge` – Führt die neuen Commits mit dem lokalen Branch zusammen.

> **⚠️ Merge-Konflikt:**  
> Wenn zwei Personen die gleiche Zeile unterschiedlich ändern, kann Git nicht automatisch mergen.  
> Git markiert die Konfliktstelle in der Datei → manuell korrigieren → `git add` → `git commit` (ohne Message, Git generiert sie).

---

## 📋 Befehlsübersicht (Spickzettel)

| Befehl                    | Wirkung |
|---------------------------|---------|
| `git status`              | Zeigt den Zustand aller Dateien an (modified, staged, committed) |
| `git add <datei>`         | Datei in die Staging-Area aufnehmen (modified → staged) |
| `git commit -m "Text"`    | Snapshot der Staging-Area erstellen (staged → committed) |
| `git push origin main`    | Lokale Commits auf den Remote-Server hochladen |
| `git pull`                | Neue Commits vom Remote holen und integrieren |
| `git log --oneline`       | Zeigt die Commit-Historie kompakt an |

---

## ✅ Selbsttest – Erreiche ich die drei Lernziele?

**K1 – Die drei Zustände definieren:**

- [ ] Ich kann erklären, was *modified* bedeutet und welcher Befehl zu *staged* führt.
- [ ] Ich weiß, dass ein Commit nur Dinge aus der Staging-Area speichert.
- [ ] Ich kann den Unterschied zwischen *staged* und *committed* in eigenen Worten beschreiben.

**K3 – add und commit ausführen:**

- [ ] Ich kann mit `git add` eine geänderte Datei vormerken.
- [ ] Ich kann mit `git commit -m "Nachricht"` einen Snapshot erstellen.
- [ ] Ich verstehe, dass ein Commit immer eine logische Einheit sein sollte.

**K3 – push und pull nutzen:**

- [ ] Ich kann lokale Commits mit `git push` auf einen Remote-Server übertragen.
- [ ] Ich kann mit `git pull` Änderungen anderer abrufen und integrieren.
- [ ] Ich weiß, dass `git pull` aus `fetch` + `merge` besteht und was bei einem Konflikt zu tun ist.

---

## 💡 Pro-Tipp für die Prüfung

Behalte das Zusammenspiel im Kopf:  

`modified` → `git add` → `staged` → `git commit` → `committed` → `git push` → Remote  
Remote → `git pull` → lokaler Branch (Arbeitsverzeichnis)  

Zeichne dir diesen Ablauf auf einen Zettel – viele IHK-Aufgaben verlangen genau diese Reihenfolge. 

```