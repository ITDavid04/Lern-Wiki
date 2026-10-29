

## 1. Voraussetzungen & Ziel

- **sqlite3** ist in Python eingebaut.
- Wir speichern eure Spieldaten (ein `dict`) als **JSON‑Text** in einer SQLite‑Tabelle.
- Wir arbeiten mit **sicheren Transaktionen**, dem **WAL‑Modus** und **parameterisierten Abfragen**.

---

## 2. Tabellenstruktur (festlegen)

Eine einfache, aber erweiterbare Tabelle:

| Spalte       | Typ     | Bedeutung                                      |
|--------------|---------|-------------------------------------------------|
| `id`         | INTEGER | Eindeutige ID (automatisch)                     |
| `save_name`  | TEXT    | Name des Spielstands (eindeutig)                |
| `created_at` | TEXT    | Zeitstempel der Speicherung (wird automatisch gesetzt) |
| `data_json`  | TEXT    | Die kompletten Spieldaten als JSON‑String        |

**Warum `UNIQUE` bei `save_name`?** Ihr könnt so einen Spielstand einfach überschreiben, ohne vorher prüfen zu müssen, ob er schon existiert.

---

## 3. Datenbank und Tabelle einmalig anlegen

Am einfachsten direkt in Python – so müsst ihr nie von Hand eine DB‑Datei vorbereiten.

```python
import sqlite3

def init_db(db_path="dice_game.db"):
    """Stellt sicher, dass die Datenbank und die Tabelle existieren."""
    conn = sqlite3.connect(db_path)
    # WAL-Modus aktivieren (bleibt dauerhaft in der DB gespeichert)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS game_states (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            save_name TEXT NOT NULL UNIQUE,
            created_at TEXT DEFAULT (datetime('now','localtime')),
            data_json TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
```

`init_db()` könnt ihr einmal beim Programmstart aufrufen – die Tabelle wird nur erzeugt, falls sie noch fehlt.

---

## 4. Verbindung herstellen (ohne doppelte PRAGMA)
Da der WAL‑Modus schon in der Datenbank gespeichert ist, muss er nicht bei jedem Verbinden neu gesetzt werden. Die Funktion `connect()` genügt, wir kümmern uns aber um **explizites Schließen** der Verbindung, damit nichts offen bleibt.

```python
def get_connection(db_path="dice_game.db"):
    """Gibt eine neue Datenbankverbindung zurück (WAL ist bereits aktiv)."""
    return sqlite3.connect(db_path)
```

---

## 5. Spielstand speichern (sicher und überschreibend)

Wir nutzen `INSERT OR REPLACE` – das löscht bei Namenskonflikt die alte Zeile und fügt eine neue ein. **Wichtig:** Dadurch ändert sich die `id` und der Zeitstempel wird aktualisiert. Für ein einfaches Spiel völlig in Ordnung. (Eine Alternative, die die `id` behält, zeige ich nachher.)

```python
import json

def save_game(save_name, game_data, db_path="dice_game.db"):
    # Spieldaten als JSON-Text aufbereiten (UTF-8, daher Umlaute okay)
    json_text = json.dumps(game_data, ensure_ascii=False)

    conn = get_connection(db_path)
    try:
        with conn:  # Transaktion: commit oder rollback
            conn.execute(
                "INSERT OR REPLACE INTO game_states (save_name, data_json) VALUES (?, ?)",
                (save_name, json_text)
            )
    finally:
        conn.close()   # Verbindung in jedem Fall schließen
```

**Erklärung:**

- `with conn:` startet eine Transaktion. Wenn der `INSERT`-Befehl fehlerfrei durchläuft, wird automatisch ein `commit` ausgeführt; bei einem Fehler ein `rollback`.
- `finally: conn.close()` sorgt dafür, dass die Verbindung **immer** geschlossen wird, auch wenn vorher eine Exception aufgetreten ist.

---

## 6. Spielstand laden

```python
def load_game(save_name, db_path="dice_game.db"):
    conn = get_connection(db_path)
    try:
        row = conn.execute(
            "SELECT data_json FROM game_states WHERE save_name = ?",
            (save_name,)
        ).fetchone()
    finally:
        conn.close()

    if row is None:
        raise FileNotFoundError(f"Kein Spielstand mit Name '{save_name}' gefunden.")

    return json.loads(row[0])   # zurück in ein dict
```

Auch hier `finally` für das Schließen – schützt vor offenen Verbindungen, wenn beim `fetchone()` ein Fehler passiert.

---

## 7. Alle Spielstände anzeigen oder löschen (optional)

```python
def list_saves(db_path="dice_game.db"):
    conn = get_connection(db_path)
    try:
        return conn.execute(
            "SELECT save_name, created_at FROM game_states ORDER BY created_at DESC"
        ).fetchall()
    finally:
        conn.close()

def delete_save(save_name, db_path="dice_game.db"):
    conn = get_connection(db_path)
    try:
        with conn:
            conn.execute(
                "DELETE FROM game_states WHERE save_name = ?",
                (save_name,)
            )
    finally:
        conn.close()
```

---

## 8. Einfacher Wrapper – ersetzt euren bisherigen Speicher‑Agenten

```python
class SQLiteStorage:
    def __init__(self, db_path="dice_game.db"):
        self.db_path = db_path
        init_db(db_path)      # Tabelle ggf. anlegen, WAL aktivieren

    def save(self, name, data):
        save_game(name, data, self.db_path)

    def load(self, name):
        return load_game(name, self.db_path)

    def list_saves(self):
        return list_saves(self.db_path)

    def delete(self, name):
        delete_save(name, self.db_path)
```

In eurem Spielcode tauscht ihr dann einfach die bisherige Storage‑Klasse aus:

```python
# Vorher: storage = JsonFileStorage("./spielstaende/")
# Jetzt:
storage = SQLiteStorage("dice_game.db")
```

---

## 9. Warum das sicherer ist als reines JSON/YAML

- **Transaktionen:** Absturzsicher – entweder wird der Spielstand ganz geschrieben oder gar nicht (keine halben Dateien).
- **WAL‑Modus:** Erlaubt parallele Lese‑ und Schreibzugriffe und schützt vor Datenverlust bei plötzlichem Programmende.
- **Keine manuelle Dateisperre:** SQLite kümmert sich selbst um die Koordination.

---

## 10. Backup (freiwillig, aber einfach)

Da die DB eine einzelne Datei ist, könnt ihr sie einfach kopieren oder die eingebaute Backup‑Funktion nutzen:

```python
def backup_db(source="dice_game.db", dest="backup.db"):
    src = sqlite3.connect(source)
    dst = sqlite3.connect(dest)
    src.backup(dst)
    dst.close()
    src.close()
```

Nach jedem `save_game()` ausgeführt, habt ihr immer eine Sicherheitskopie.

---

## 🔧 Optionale Alternative: `INSERT ... ON CONFLICT` (behält die `id`)

Falls ihr später einmal die `id` eines Spielstands behalten müsst (z. B. weil sie in einer Highscore‑Tabelle referenziert wird), könnt ihr statt `REPLACE` auch `UPSERT` verwenden. So bleibt die Zeile erhalten und nur `data_json` und Zeitstempel werden aktualisiert:

```python
conn.execute("""
    INSERT INTO game_states (save_name, data_json, created_at)
    VALUES (?, ?, datetime('now','localtime'))
    ON CONFLICT(save_name) DO UPDATE SET
        data_json = excluded.data_json,
        created_at = datetime('now','localtime')
""", (save_name, json_text))
```

Für den Einstieg ist `INSERT OR REPLACE` aber vollkommen ausreichend und einfacher zu verstehen.

---

## 💡 Zusammenfassung eurer verbesserten Schritte

1. `init_db()` einmal beim Programmstart aufrufen.
2. `get_connection()` nur noch für das reine Verbinden nutzen (WAL ist schon aktiv).
3. In allen DB‑Funktionen `conn.close()` per `try...finally` sicherstellen.
4. `save_game()`/`load_game()` verwenden JSON und parameterisierte Queries.
5. Die neue `SQLiteStorage`‑Klasse einbinden und testen.

end