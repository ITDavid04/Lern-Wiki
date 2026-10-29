#!/usr/bin/env python3
"""Release-Wächter: prüft das Repo, bevor Inhalte in der Wiki-APP landen.

Die Wiki-APP lädt die Artikel direkt von main. Dieses Skript läuft im Workflow
bei jedem Pull Request und jedem Push auf main. Schlägt eine Pflichtprüfung
fehl, wird der Pull Request rot und sollte nicht gemergt werden.

Pflichtprüfungen (Fehler):
  * Rechtsdateien vorhanden (Lizenz, Impressum, Datenschutz, Nutzungshinweise)
  * keine offenen Platzhalter wie [PLZ] in Impressum und Datenschutz
  * keine gesperrten Begriffe (Liste NICHT im Repo, siehe unten)
  * keine übrig gebliebenen Chat-Sätze am Artikelanfang ("Gerne, hier ...")
  * keine Datei über 10 MB

Hinweise (blockieren nicht):
  * Bilder ohne aussagekräftigen Alternativtext

Gesperrte Begriffe (z. B. Namen von Bildungsträgern, Kursszenarien, Personen)
stehen bewusst nicht im öffentlichen Repo, sondern
  * lokal in der Datei .release-terms (eine Zeile pro Begriff, ist in .gitignore)
  * auf GitHub in der Repository-Variable RELEASE_FORBIDDEN_TERMS
    (Settings > Secrets and variables > Actions > Variables, Begriffe durch
    Komma getrennt)

Aufruf: python3 tools/release_check.py
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "_build", "site", "node_modules"}

REQUIRED = ["LICENSE", "LICENSE-CODE", "IMPRESSUM.md", "DATENSCHUTZ.md", "NUTZUNGSHINWEISE.md", "README.md"]
PLACEHOLDER_FILES = ["IMPRESSUM.md", "DATENSCHUTZ.md"]
PLACEHOLDER = re.compile(r"\[(Straße|PLZ|Ort|E-Mail|Datum|zuständige)[^\]]*\]")
CHAT_REMNANT = re.compile(
    r"^(Gerne\b|Klar[,!]|Hier kommt\b|Hier ist (die|der|das|dein|deine) gewünscht|"
    r"Hier (die|der|das) gewünscht|Natürlich[,!]|Selbstverständlich[,!])",
    re.IGNORECASE,
)
WEAK_ALT = re.compile(r"^(|alt text|image|bild|screenshot)$", re.IGNORECASE)
MAX_BYTES = 10 * 1024 * 1024


def files(pattern: str):
    for p in ROOT.rglob(pattern):
        if not (set(p.relative_to(ROOT).parts) & SKIP_DIRS) and p.is_file():
            yield p


def forbidden_terms() -> list[str]:
    terms: list[str] = []
    env = os.environ.get("RELEASE_FORBIDDEN_TERMS", "")
    terms += [t.strip() for t in env.split(",") if t.strip()]
    local = ROOT / ".release-terms"
    if local.exists():
        terms += [l.strip() for l in local.read_text(encoding="utf-8").splitlines()
                  if l.strip() and not l.startswith("#")]
    return sorted(set(terms), key=str.lower)


def main() -> int:
    errors: list[str] = []
    hints: list[str] = []

    for name in REQUIRED:
        if not (ROOT / name).exists():
            errors.append(f"Pflichtdatei fehlt: {name}")

    for name in PLACEHOLDER_FILES:
        path = ROOT / name
        if path.exists():
            for m in PLACEHOLDER.finditer(path.read_text(encoding="utf-8")):
                errors.append(f"{name}: Platzhalter noch nicht ausgefüllt: {m.group(0)}")

    terms = forbidden_terms()
    if not terms:
        msg = "Keine gesperrten Begriffe hinterlegt (.release-terms oder RELEASE_FORBIDDEN_TERMS)."
        # Auf GitHub ist die Liste Pflicht, lokal reicht ein Hinweis
        (errors if os.environ.get("GITHUB_ACTIONS") == "true" else hints).append(msg)
    # Ganze Wörter: ein gesperrter Begriff schlägt nicht an, wenn er nur Teil eines längeren Wortes ist
    term_rx = (re.compile(r"(?<!\w)(?:" + "|".join(re.escape(t) for t in terms) + r")(?!\w)", re.IGNORECASE)
               if terms else None)

    for md in files("*.md"):
        rel = md.relative_to(ROOT)
        text = md.read_text(encoding="utf-8")
        lines = text.splitlines()
        if term_rx:
            for i, line in enumerate(lines, 1):
                for m in term_rx.finditer(line):
                    errors.append(f"{rel}:{i}: gesperrter Begriff „{m.group(0)}“")
        for i, line in enumerate(lines[:5], 1):
            if CHAT_REMNANT.search(line.strip()):
                errors.append(f"{rel}:{i}: sieht nach übrig gebliebenem Chat-Satz aus: {line.strip()[:60]}")
        for alt, src in re.findall(r"!\[([^\]]*)\]\(([^)]*)\)", text):
            if WEAK_ALT.match(alt.strip()) or alt.strip() == Path(src).stem:
                hints.append(f"{rel}: Bild ohne aussagekräftigen Alternativtext: {src}")

    for f in files("*"):
        if f.stat().st_size > MAX_BYTES:
            errors.append(f"{f.relative_to(ROOT)}: größer als 10 MB")

    if hints:
        print(f"Hinweise ({len(hints)}, blockieren nicht):")
        for h in hints[:15]:
            print("  -", h)
        if len(hints) > 15:
            print(f"  … und {len(hints) - 15} weitere")
    if errors:
        print(f"\nRelease gestoppt, {len(errors)} Fehler:")
        for e in errors:
            print("  ✗", e)
        return 1
    print("\nRelease-Wächter: alles in Ordnung.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
