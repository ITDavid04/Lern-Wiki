🚀 Wissensdatenbank: Git & GitHub für den Arbeitsalltag

Diese Schnellreferenz hilft dir, die häufigsten Git-Situationen im Ausbildungsalltag sicher zu meistern.
1. Identität konfigurieren (Initialisierung)

Bevor du loslegst, muss Git wissen, wer du bist. Nur so können deine Commits in VS Code und auf GitHub korrekt zugeordnet werden.

bash
# Deinen Namen einstellen

git config --global user.name "Vorname Nachname"

# Deine E-Mail einstellen (verwende die gleiche wie bei GitHub!)

git config --global user.email "deine.email@beispiel.de"

    Hinweis: Die E-Mail muss nicht zwingend mit deiner GitHub-Adresse übereinstimmen, aber nur dann werden deine Commits auf GitHub mit deinem Profilbild verknüpft.

2. Der „Divergent Branches“-Fehler

Wenn du git pull ausführst und diese Meldung siehst:
text

hint: You have divergent branches and need to specify how to reconcile them.

Dann haben sich deine lokalen Commits und die auf dem Server unterschiedlich entwickelt – Git weiß nicht, ob es die Änderungen zusammenführen (merge) oder neu anordnen (rebase) soll.

Die empfohlene Lösung für den Einstieg:

bash

git config --global pull.rebase false

Warum?

Damit legst du fest, dass Git bei pull immer einen Merge-Commit erzeugt. Das ist die einfachste und nachvollziehbarste Strategie, weil der Verlauf nicht umgeschrieben wird – ideal für Einsteiger und Teams, die Klarheit schätzen.

    Alternativ (für Neugierige): Mit git config --global pull.rebase true würdest du ein rebase erzwingen, was eine linearere Historie schafft, aber komplexer sein kann. Für den Start bleib bei false.

3. Änderungen zwischenspeichern mit git stash

Manchmal hast du lokal schon angefangen zu arbeiten, möchtest aber erst die aktuellste Version vom Server holen, ohne deine unfertigen Änderungen committen zu müssen. Genau dafür ist git stash da.
Der sichere Workflow Schritt für Schritt

Befehl	Was passiert?

git stash	Packt alle deine aktuellen Änderungen sicher „in den Schrank“.

git pull	Holt die neuesten Daten vom Server (jetzt völlig sauber).

git stash pop	Holt deine Änderungen aus dem Schrank zurück und wendet sie an.

Achtung: Nach git stash pop kann es zu Merge-Konflikten kommen, wenn die gleichen Dateien sowohl auf dem Server als auch lokal geändert wurden. Git markiert die Konfliktstellen dann in den betroffenen Dateien – löse sie wie gewohnt und führe anschließend git add und git commit aus.

    💡 Profi-Tipp: Mit git stash list siehst du alle zwischengespeicherten Änderungen. git stash drop löscht einen alten Stash, falls du ihn nicht mehr brauchst.

4. SSH-Authentifizierung einrichten

Mit SSH musst du nicht bei jedem Push/Pull dein Passwort eingeben – die Verbindung ist verschlüsselt und im Arbeitsalltag der Standard.
A) Schlüsselpaar erzeugen
bash

ssh-keygen -t ed25519 -C "deine.email@beispiel.de"

    -t ed25519 wählt den sicheren und schnellen Algorithmus.

    -C setzt ein Label (z. B. deine E-Mail zur Wiedererkennung).

    Alle Abfragen einfach mit Enter bestätigen (kein Passwort vergeben, sonst musst du es bei jedem Git-Befehl neu eingeben).

B) SSH-Agent starten und Schlüssel laden

Dieser Schritt fehlt oft und ist die Hauptursache für Permission denied-Fehler.
bash

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

C) Public Key kopieren
bash

cat ~/.ssh/id_ed25519.pub

Kopiere die gesamte Ausgabe (eine lange Zeile, die mit ssh-ed25519 beginnt).
D) Bei GitHub hinterlegen

    Gehe zu GitHub.com → Settings → SSH and GPG keys.

    Klicke auf New SSH key.

    Title: Gib einen sprechenden Namen ein (z. B. Arbeitsrechner-2026).

    Key: Füge den kopierten Public Key ein.

    Speichere mit Add SSH key.

    📖 Eine noch ausführlichere Anleitung mit Fehlerbehebung findest du im separaten Leitfaden: „SSH-Zugriff für GitHub einrichten“.

5. Quick-Check: Ist alles bereit?

Teste die gesamte Konfiguration mit einem einzigen Befehl:
bash

ssh -T git@github.com

Erscheint die Meldung
Hi [DeinName]! You've successfully authenticated...
dann hast du alles perfekt vorbereitet und kannst durchstarten!
💡 Tipp speziell für Umschüler

Git ist wie ein Sicherheitsnetz – es bewahrt dich davor, dass Code verloren geht. Hab keine Angst, Dinge auszuprobieren! Wenn du mal das Gefühl hast, dich „festgefahren“ zu haben, gib einfach ein:
bash

git status

Dieser Befehl zeigt dir jederzeit, in welchem Zustand sich dein Repository befindet und was Git als Nächstes von dir erwartet. Er ist dein bester Freund im Arbeitsalltag.