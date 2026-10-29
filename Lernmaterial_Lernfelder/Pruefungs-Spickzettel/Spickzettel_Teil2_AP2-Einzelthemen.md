# Prüfungs-Spickzettel Teil 3 – AP2-Einzelthemen

> **Zielgruppe:** Umschüler FIAE/FISI
> **Prüfungsrelevanz:** Teil 2 der gestreckten Abschlussprüfung (AP2) – die vier Themen liegen inhaltlich vor allem im Prüfungsbereich "Konzeption und Administration von IT-Systemen" (FISI); für FIAE als fachrichtungsübergreifendes IT-Sicherheits-Querschnittswissen relevant.
> **Lernzeit:** 30–45 Minuten (Wiederholungskarten, kein Erstlernen)
> **Status:** Final
> **Stand:** 2026-09-22
>
> **Hinweis zum Format:** Kompakte Wiederholungskarten für Themen, die in keinem bestehenden Lernfeld-Artikel ausführlich behandelt werden, aber in echten AP2-Prüfungen oder dem aktuellen Prüfungskatalog nachweisbar relevant sind. Themen wie Netzplantechnik, Nutzwertanalyse, RAID, Backup-Strategien, Rechtsformen und Vertragsarten stehen bereits in Teil 1/2 dieser Serie bzw. in den Lernfeld-Artikeln und werden hier nicht dupliziert.
>
> **Umfang:** Dieser Teil ist bewusst kürzer als Teil 1 und 2, da die übrigen AP2-Standardthemen bereits in den Lernfeld-Artikeln und vorhandenen Spickzetteln behandelt werden – hier stehen nur die vier Themen, die im Gesamtaudit als konkrete, bisher unabgedeckte Lücken identifiziert wurden.

**Legende:** 🔴 hohe Prüfungsrelevanz · 🟡 mittlere Prüfungsrelevanz · 🟢 ergänzende Prüfungsrelevanz

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Wie unterscheiden sich Virus, Wurm, Trojaner und Ransomware? | [→ 1](#1-malware-taxonomie) |
| 2 | Was unterscheidet einen Hypervisor Typ 1 von einem Typ 2? | [→ 2](#2-hypervisor-typ-1-vs-typ-2) |
| 3 | Was bedeuten Security by Design und Security by Default? | [→ 3](#3-security-by-design-und-security-by-default) |
| 4 | Was unterscheidet White-Hat- von Black-Hat-Hackern? | [→ 4](#4-white-hat-vs-black-hat-hacker) |

---

## 1. Malware-Taxonomie

> **Grundprinzip:** Die Begriffe werden in Prüfungsaufgaben häufig als Zuordnungstabelle abgefragt. Virus und Wurm unterscheiden sich vor allem durch ihre Replikation und die Bindung an einen Wirt, der Trojaner durch seine Tarnung und Ransomware durch ihre Erpressungsfunktion.

| Typ | Verbreitung | Braucht Wirtsprogramm? | Charakteristik |
|---|---|---|---|
| **Virus** | Verbreitet sich, indem er sich an andere Programme/Dateien/ausführbare Wirtsbereiche anhängt | Ja | Wird erst durch Ausführung des infizierten Wirts aktiv |
| **Wurm** | Verbreitet sich selbstständig, häufig über Netzwerke, aber auch z. B. über Wechseldatenträger | Nein | Repliziert sich eigenständig und befällt weitere Systeme |
| **Trojaner** | Wird als legitime bzw. nützliche Datei/Anwendung getarnt verbreitet | Nein (ist selbst das Programm) | Täuscht eine erwünschte Funktion vor, führt aber verdeckt Schadfunktionen aus |
| **Ransomware** | Häufig über Phishing, Trojaner oder Sicherheitslücken eingeschleust | Kein definierendes Merkmal (kommt in verschiedenen Formen vor) | Sperrt den Zugriff auf Systeme oder verschlüsselt Daten und fordert Lösegeld; oft zusätzlich Drohung mit Veröffentlichung gestohlener Daten |

🔴 **Stolperstein:** Der Unterschied Virus/Wurm wird am häufigsten falsch beantwortet – die entscheidende Frage ist nicht "verbreitet er sich über das Netz" (ein Wurm kann sich z. B. auch per USB-Stick verbreiten), sondern **"braucht er ein Wirtsprogramm, um überhaupt aktiv zu werden"**. Ein Wurm braucht keines, ein Virus schon.

🟡 **Taxonomie-Hinweis:** Virus, Wurm und Trojaner beschreiben vor allem Verbreitungs- bzw. Tarnmechanismen. Ransomware ist dagegen nach ihrer Schadfunktion – der digitalen Erpressung – benannt. Eine Schadsoftware kann deshalb mehreren Kategorien gleichzeitig angehören (z. B. ein Wurm, der Ransomware nachlädt).

🟡 **Kontextwissen:** Weitere verwandte Begriffe: Spyware (spioniert Daten aus), Adware (blendet unerwünschte Werbung ein), Keylogger (zeichnet Tastatureingaben auf) – diese lassen sich mit Viren/Würmern/Trojanern kombinieren, sind aber nach ihrer Funktion, nicht nach ihrer Verbreitungsart benannt.

---

## 2. Hypervisor Typ 1 vs. Typ 2

> **Grundprinzip:** Ein Hypervisor ist die Software-Schicht, die virtuelle Maschinen verwaltet. Der entscheidende Unterschied zwischen den beiden Typen ist, worauf der Hypervisor direkt aufsetzt.

| Merkmal | Typ 1 (nativ / bare-metal) | Typ 2 (gehostet) |
|---|---|---|
| Läuft auf | Direkt auf der Hardware | Auf einem bereits installierten Betriebssystem |
| Zugriff auf Ressourcen | Unmittelbar bzw. über privilegierte Verwaltungsbereiche, dadurch effizienter | Über das Host-Betriebssystem, dadurch mehr Overhead |
| Typischer Einsatz | Serverbetrieb, produktive Bereitstellung von VMs | Arbeitsplätze, Entwicklung und Test von Software |
| Marktgängige Produkte | Microsoft Hyper-V, VMware ESXi, KVM | VMware Workstation, Oracle VirtualBox, Parallels Desktop |

🔴 **Stolperstein:** Typ 1 wird oft fälschlich als "der neuere/bessere" Typ dargestellt – tatsächlich ist die Wahl eine Frage des Einsatzzwecks: Für Serverbetrieb ist Typ 1 wegen des effizienteren Hardwarezugriffs die übliche Wahl, für Arbeitsplatzrechner mit gelegentlichem Testbedarf reicht Typ 2 oft aus und ist einfacher einzurichten.

---

## 3. Security by Design und Security by Default

> **Grundprinzip:** Beide Prinzipien verlagern IT-Sicherheit von einer nachträglichen Ergänzung hin zu einem von Anfang an mitgedachten Bestandteil der Entwicklung.

| Prinzip | Bedeutung |
|---|---|
| **Security by Design** | Sicherheitsaspekte werden von Beginn der Entwicklung an in die Architektur eingeplant, nicht erst nachträglich ergänzt |
| **Security by Default** | Das System wird mit sicheren, möglichst restriktiven Voreinstellungen ausgeliefert – zusätzliche Funktionen oder Berechtigungen müssen bewusst aktiviert werden, nicht umgekehrt |

> **Mögliche Prüfungsfrage** (plausible Ableitung aus dem Katalog, nicht aus einer eingesehenen Prüfung belegt): *"Nennen Sie ein Beispiel für Security by Default bei der Auslieferung eines neuen IT-Systems."*
> **Musterantwort:** Unnötige Dienste und Ports sind standardmäßig deaktiviert, es wird kein einheitliches Standard- oder Werkpasswort verwendet (individuelle Vergabe bei der Ersteinrichtung sollte erzwungen werden), unnötige Standardkonten sind deaktiviert.

🟡 **Kontextwissen:** Beide Prinzipien werden häufig zusammen mit dem Least-Privilege-Prinzip und Zero Trust genannt (siehe LF4.3A). Die Prinzipien ergänzen sich, statt sich scharf zu trennen: Security by Design/Default verankert Sicherheit bereits in Entwicklung, Architektur und Voreinstellungen. Least Privilege begrenzt Berechtigungen auf das erforderliche Minimum. Zero Trust verlangt fortlaufende Prüfung von Zugriffen statt Vertrauen aufgrund des Netzwerkstandorts – auch das muss bereits beim Systemdesign mitgedacht werden, nicht erst im laufenden Betrieb.

---

## 4. White-Hat vs. Black-Hat-Hacker

> **Grundprinzip:** Die Unterscheidung liegt nicht in der technischen Fähigkeit, sondern darin, ob eine ausdrückliche Autorisierung durch eine dazu berechtigte Stelle vorliegt und der vereinbarte Prüfungsumfang (Scope) eingehalten wird.

| Merkmal | White-Hat-Hacker | Black-Hat-Hacker |
|---|---|---|
| Autorisierung | Handelt mit ausdrücklicher Erlaubnis einer berechtigten Stelle und innerhalb des vereinbarten Scopes (z. B. Penetrationstest) | Handelt ohne erforderliche Erlaubnis oder überschreitet bewusst den vereinbarten Scope |
| Ziel | Schwachstellen finden, um die IT-Sicherheit zu verbessern | Schwachstellen ausnutzen für persönliche, finanzielle oder sonstige Vorteile |
| Umgang mit Funden | Ergebnisse werden über vereinbarte Wege dokumentiert und gemeldet | Werden ausgenutzt, verkauft oder veröffentlicht |

🟢 **Kontextwissen:** Als "Grey-Hat" werden uneinheitlich Personen bezeichnet, deren Vorgehen zwischen White Hat und Black Hat eingeordnet wird – typisch ist eine Schwachstellensuche ohne vorherige Autorisierung, teilweise mit anschließender Meldung statt Ausnutzung. Eine gute Absicht ersetzt aber keine erforderliche Erlaubnis; je nach konkretem Vorgehen kann das rechtlich unzulässig bzw. strafbar sein.

---

## Typische Prüfungsfallen

| # | Falle | Richtigstellung |
|---|---|---|
| 1 | Virus und Wurm anhand der Verbreitung über das Netzwerk unterscheiden | Entscheidend ist, ob ein Wirtsprogramm nötig ist (Virus: ja, Wurm: nein) |
| 2 | Hypervisor Typ 1 sei grundsätzlich "besser" als Typ 2 | Die Wahl richtet sich nach dem Einsatzzweck (Server vs. Arbeitsplatz/Test) |
| 3 | Security by Design/Default mit Zero Trust/Least Privilege gleichsetzen | Verwandte, sich ergänzende Prinzipien – Security by Design/Default betrifft primär Entwicklung/Voreinstellungen, Least Privilege/Zero Trust primär Zugriffssteuerung; beide gehören bereits ins Systemdesign |
| 4 | White-Hat-Hacking mit "erlaubtem Hacking allgemein" gleichsetzen | Entscheidend sind Autorisierung durch eine berechtigte Stelle und die Einhaltung des vereinbarten Scopes, nicht nur die gute Absicht |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Virus | Braucht Wirtsprogramm, wird durch dessen Ausführung aktiv |
| Wurm | Repliziert und verbreitet sich selbstständig (z. B. über Netzwerke/Wechseldatenträger), ohne Wirtsprogramm |
| Trojaner | Als legitime Software/Datei getarnte Malware mit verdeckter Schadfunktion |
| Ransomware | Sperrt Systeme oder verschlüsselt Daten, um Lösegeld zu erpressen |
| Hypervisor Typ 1 | Läuft direkt auf der Hardware (bare-metal), typisch für Server |
| Hypervisor Typ 2 | Läuft auf einem Host-Betriebssystem, typisch für Arbeitsplatz/Test |
| Security by Design | Sicherheit von Beginn der Entwicklung an mitgeplant |
| Security by Default | Sichere, restriktive Voreinstellungen als Auslieferungszustand |
| White-Hat-Hacker | Handelt autorisiert und innerhalb des vereinbarten Scopes |
| Black-Hat-Hacker | Handelt ohne Autorisierung, zum eigenen Vorteil oder in sonstiger schädlicher Absicht (z. B. Sabotage, Spionage) |

---

## Merksätze für die Prüfung

> Ein Virus infiziert einen Wirt, ein Wurm repliziert sich selbstständig.

> Security by Default: sicher ab Werk, nicht sicher erst nach dem Nachrüsten.

> White Hat hat Autorisierung und Scope, Black Hat nicht.

---

```yaml
dokument: Pruefungs-Spickzettel-Teil3-AP2
lernfeld: "Querschnittsthema, kein einzelnes Lernfeld (analog zu Mathe_Was_Notwendig_ist)"
titel: "Prüfungs-Spickzettel Teil 3 – AP2-Einzelthemen"
typ: "Typ A – Kompakte Wiederholungskarten"
status: final
stand: 2026-09-22
quellen_intern:
  - "Teil 3 einer dreiteiligen Serie (AP1 / WiSo-Multiple-Choice / AP2), analog zur Mathe_Was_Notwendig_ist-Serie als eigener Querschnitts-Ordner angelegt"
  - "Themenauswahl basiert auf einem Gesamtaudit des Wiki-Repos gegen echtes IHK-Prüfungsmaterial in vorheriger Session; bewusst auf Themen begrenzt, die weder in bestehenden Lernfeld-Artikeln noch im bereits vorhandenen Standardthemen-Spickzettel (Netzplantechnik, Nutzwertanalyse, RAID, Rechtsformen, Vertragsarten u. a.) abgedeckt sind"
quellen_fachlich:
  - titel: "AP2 Sommer 2024 FISI (echte Prüfung mit Lösungen)"
    herausgeber: "ZPA Nord-West"
    status: "Direkt eingesehen - bestätigt Malware-Taxonomie (Virus/Wurm/Trojaner/Ransomware als 4-Punkte-Zuordnungstabelle) sowie White-Hat-/Black-Hat-Hacker-Unterscheidung"
  - titel: "AP2 Sommer 2025 FISI, Teil 1 (echte Prüfung mit Lösungen)"
    herausgeber: "ZPA Nord-West"
    status: "Direkt eingesehen - bestätigt Hypervisor Typ 1/Typ 2 als 8-Punkte-Vergleichsaufgabe mit Praxisbeispielen"
  - titel: "Fachinformatiker_Prüfungskatalog_2025 (Änderungsvergleich 2020→2025)"
    herausgeber: "U-Form Verlag / ZPA Nord-West"
    status: "Web-verifiziert, bestätigt 'Härtung Betriebssystem (Schwachstellen schließen)' als neu aufgenommenes Thema. WICHTIG: Anders als die drei anderen Themen dieser Datei (direkt in echten Prüfungen belegt) stützt sich Security by Design/Default nur auf diesen Katalogbezug, nicht auf eine konkret eingesehene Prüfungsaufgabe - Musterfrage/-antwort in Abschnitt 3 daher als plausible Ableitung zu kennzeichnen, nicht als Zitat einer realen Prüfungsaufgabe"
review_historie:
  - runde: 1
    datum: 2026-09-22
    ergebnis: "Erstdraft erstellt. Themenauswahl bewusst schmal gehalten (4 Themen statt der 10 in Part 1) - AP2 ist durch den bereits vorhandenen Standardthemen-Spickzettel und die ausführlichen Lernfeld-Artikel (v. a. LF4.3A für Security-Grundlagen) schon deutlich besser abgedeckt als AP1 es vor Teil 1 war. Nur Themen aufgenommen, die im Gesamtaudit als konkrete Lücke mit Beleg aus echten Prüfungen identifiziert wurden. Security by Design/Default bewusst von Zero Trust/Least Privilege abgegrenzt, um keine Redundanz zu LF4.3A zu erzeugen."
  - runde: 2
    datum: 2026-09-22
    ergebnis: "3 Reviews eingearbeitet. Wichtigster, dreifach bestätigter Fund: Die Ransomware-Zeile war unscharf ('Unterschiedlich' bei Wirtsprogramm, Charakteristik nur auf Verschlüsselung begrenzt) - korrigiert auf 'Nein (eigenständig)' konsistent zur Trojaner-Zeile, Charakteristik um Systemsperre/Double-Extortion erweitert (BSI-konform), zusätzlicher Taxonomie-Hinweis ergänzt, dass Ransomware nach Schadfunktion statt Verbreitungsmechanismus benannt ist und sich Kategorien überschneiden können. Ebenfalls mehrfach bestätigt: Virus/Wurm-Merksatz 'braucht nur ein Netzwerk' war zu eng (Würmer verbreiten sich auch z. B. per USB) - auf 'repliziert sich selbstständig' als eigentliches Kriterium umgestellt; White-Hat-Grundprinzip und Tabelle von 'Auftrag des Systeminhabers' auf 'Autorisierung durch eine berechtigte Stelle + vereinbarter Scope' erweitert (wichtig bei Cloud/Hosting mit mehreren Beteiligten), Merksatz und Prüfungsfalle entsprechend nachgezogen; leere Tabellen-Header-Zellen bei Hypervisor und White-/Black-Hat gefüllt ('Merkmal'); Hypervisor 'Standardwahl' zu 'übliche Wahl' entschärft, vSphere durch ESXi ersetzt (vSphere ist die Produktsuite, ESXi der Hypervisor); Security by Default 'sicherste Konfiguration' präzisiert (theoretisch sicherste Konfiguration wäre ein abgeschaltetes System) auf 'sichere, restriktive Voreinstellungen', Zero-Trust-Abgrenzung von strikt zeitlich getrennt auf 'sich ergänzende Prinzipien' korrigiert. Kleinere Präzisierungen: Trojaner-Formulierung (Tarnung statt Installation als Kernmerkmal), Grey-Hat neutraler (nicht jeder meldet Funde), Musterantwort sprachlich geglättet. Ein behaupteter Formatfehler (IHK-Kernfragen-Tabellenkopf angeblich kaputt) wurde gegen die tatsächliche Datei geprüft und als falsch verworfen - die Tabelle war korrekt aufgebaut. Zwei strukturelle Ergänzungen: FIAE/FISI-Prüfungsbereichs-Zuordnung präzisiert (die vier Themen liegen inhaltlich näher an FISI, für FIAE als Querschnittswissen gekennzeichnet); Belegstärke in der YAML ehrlich differenziert (Security by Design/Default stützt sich nur auf Katalogbezug, nicht auf eine konkret eingesehene Prüfung, im Unterschied zu den anderen drei Themen). Fachlich freigabefähig; Finalisierung obliegt David."
  - runde: 3
    datum: 2026-09-22
    ergebnis: "3 Re-Reviews eingearbeitet. Der wichtigste Punkt war eine echte Wiederholung: Zwei Reviews meldeten unabhängig zurück, dass meine Runde-2-Korrektur der Ransomware-Zeile ('Nein (eigenständig)') immer noch nicht stimmig war - sie widersprach dem eigenen, direkt darunter stehenden Taxonomie-Hinweis (Ransomware ist nach Schadfunktion benannt, nicht nach Verbreitungsmechanismus, daher ist 'Wirtsprogramm nötig?' für Ransomware gar kein sinnvolles Ja/Nein-Merkmal). Jetzt konsequent auf 'Kein definierendes Merkmal' geändert, Grundprinzip des Abschnitts entsprechend umformuliert (passt jetzt auf alle vier Begriffe: Virus/Wurm über Replikation, Trojaner über Tarnung, Ransomware über Schadfunktion). Dabei auch 'Dropper' als unerklärtes Fachwort entfernt. Zweiter mehrfach bestätigter Fund: Cheatsheet-Eintrag für Wurm war bei der Runde-2-Korrektur der Haupttabelle nicht mitgezogen worden und stand noch mit der alten, zu engen 'nur Netzwerk'-Formulierung da - nachgezogen. Dreifach bestätigt: 'IHK-Typfrage' bei Security by Default war irreführend, da die YAML bereits zugab, dass diese Frage nicht aus einer eingesehenen Prüfung stammt, sondern eine plausible Ableitung ist - im sichtbaren Text jetzt auch so gekennzeichnet ('Mögliche Prüfungsfrage', mit Klammerzusatz), Einleitungssatz entsprechend von 'wiederkehrend Punkte bringen' auf 'nachweisbar relevant' (Prüfung ODER Katalog als Beleg) abgeschwächt. Kleinere Präzisierungen: Passwort-Musterantwort entschärft ('kein einheitliches Standardpasswort' statt absolutem 'vorgeschrieben'), langer Satz mit problematischem Doppelpunkt in besser lesbare Sätze aufgeteilt, Black-Hat-Cheatsheet um Sabotage/Spionage erweitert (nicht nur 'eigener Vorteil'), Grey-Hat-Rechtsaussage vorsichtiger formuliert (hängt vom konkreten Vorgehen ab statt pauschal 'außerhalb legaler Beauftragung'), Parallels auf 'Parallels Desktop' präzisiert. Ein Vorschlag (KVM aus der Hypervisor-Typ-1-Liste entfernen) erneut nicht übernommen - in der vorherigen Runde hatten zwei unabhängige Reviews die KVM-Einordnung als Typ 1 explizit als für IHK-Zwecke üblich und korrekt bestätigt; eine einzelne erneute Gegenstimme in dieser Runde reicht nicht, um von diesem bereits gut abgewogenen Konsens abzuweichen. Fachlich freigabefähig; von David final freigegeben."
naechste_review: "Bei Änderung des Prüfungskatalogs oder nach Auswertung neuer AP2-Prüfungen"
```