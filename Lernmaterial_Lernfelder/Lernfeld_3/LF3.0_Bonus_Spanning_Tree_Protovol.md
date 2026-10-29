# LF3.3 Bonus – Spanning Tree Protocol (STP)

> **Zielgruppe:** Umschüler:innen FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 25–30 Minuten
> **Status:** Draft
> **Stand:** 2026

**Einordnung:** Dieser Artikel ergänzt LF3.3 (Strukturierte Verkabelung & Netzwerktopologien) um das Thema Schleifenvermeidung bei redundanter Verkabelung. Baut auf dem Grundverständnis von Switches/Bridges und Broadcast-Domänen auf.

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Warum braucht man STP, wenn Redundanz doch gut ist? | [1](#1-das-problem-redundanz-vs-loop) |
| 2 | Wie wird die Root Bridge bestimmt? | [2](#2-die-root-bridge-wahl) |
| 3 | Was ist der Unterschied zwischen Portrolle und Portzustand? | [3](#3-portrollen-und-portzustände) |
| 4 | Was passiert beim Ausfall des aktiven Weges? | [4](#4-warum-blockiert-stp-überhaupt) |
| 5 | Was ist der Unterschied zwischen STP und RSTP? | [5](#6-rstp-und-die-weiterentwicklungen) |

---

## 1. Das Problem: Redundanz vs. Loop

> Ein Netzwerk ohne Redundanz ist bei einem Kabelbruch tot. Ein Netzwerk mit Redundanz ohne Schleifenschutz ist bei einem Broadcast tot.

Switches leiten Broadcast-Frames grundsätzlich über alle passenden Ports weiter. Bei einer redundanten Verkabelung zwischen zwei oder mehr Switches entsteht ein physischer Kreis (Loop). Ein Broadcast-Frame wird dabei immer weiter vervielfältigt und zirkuliert dauerhaft im Netz – es entsteht ein **Broadcast Storm**.

Ethernet-Frames besitzen kein mit der IP-TTL vergleichbares Hop-Limit. Deshalb kann ein Layer-2-Loop nicht automatisch durch Ablauf eines solchen Zählers beendet werden.

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Auslöser | Redundante Verkabelung zwischen zwei oder mehr Switches | 🔴 |
| Folge | Broadcast Storm – starke Vervielfältigung und Zirkulation von Broadcasts, CPU/Bandbreite überlastet | 🔴 |
| Ursache technisch | Kein TTL-Mechanismus auf Layer 2 | 🟡 |
| Lösung | Spanning Tree Protocol, entwickelt von Radia Perlman (1985), standardisiert als IEEE 802.1D | 🔴 |

---

## 2. Die Root Bridge-Wahl

> Der Switch mit der niedrigsten Bridge-ID wird zum "Chef" des Baums – alle anderen richten sich an ihm aus.

Alle Switches tauschen **BPDUs** (Bridge Protocol Data Units) aus. Eine BPDU enthält unter anderem: Root-Bridge-ID, Root Path Cost, Sender-Bridge-ID, Port-ID und Timer. Für die Root-Wahl entscheidend ist die **Bridge-ID**: vereinfacht Priorität + MAC-Adresse. Der Switch mit dem niedrigsten Wert gewinnt.

> ⚠️ **Prüfungsfalle:** Bei STP gewinnt die **niedrigere** numerische Priorität – nicht die höhere.

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Bridge-ID (vereinfacht) | Priorität + MAC-Adresse; niedrigster Wert gewinnt | 🔴 |
| Bridge-ID (VLAN-Praxis) | Bei VLAN-basierten Implementierungen kommt eine Extended System ID (meist VLAN-ID) hinzu | 🟡 |
| Standardpriorität | 32768; wird in der Praxis oft in festen Schritten (z. B. 4096) gesenkt, um bewusst zu steuern, welcher Switch Root wird | 🟡 |
| Tie-Breaker bei gleicher Priorität | Niedrigste MAC-Adresse gewinnt | 🟡 |

> **Beispiel:** Switch A hat Priorität 32768 (Standard), Switch B wurde manuell auf 4096 gesetzt. Switch B gewinnt die Root-Wahl, weil 4096 kleiner ist – unabhängig von der MAC-Adresse.

> **IHK-Typfrage:** "Wie entscheidet STP, welcher Switch die Root Bridge wird?"
> **Musterantwort:** Alle Switches tauschen BPDUs mit ihrer Bridge-ID aus (Priorität + MAC-Adresse, ggf. Extended System ID). Der Switch mit der niedrigsten Bridge-ID wird zur Root Bridge gewählt.

---

## 3. Portrollen und Portzustände

> Portrolle und Portzustand sind zwei verschiedene Dinge – ein Port hat immer beides gleichzeitig.

Ein häufiger Anfängerfehler ist, "Blocking" als eigene Portrolle neben "Root Port" und "Designated Port" zu behandeln. Fachlich korrekt ist die Trennung:

**Portrollen** (wofür ein Port zuständig ist):

| Portrolle | Funktion | IHK-Relevanz |
|---|---|---|
| Root Port | Der Port eines Nicht-Root-Switches, über den der kostengünstigste Gesamtpfad (Root Path Cost) zur Root Bridge führt – genau einer pro Nicht-Root-Switch | 🔴 |
| Designated Port | Pro Netzwerksegment der Port mit dem günstigsten Pfad zur Root Bridge; er darf für dieses Segment Daten weiterleiten. Auf der Root Bridge selbst sind alle Ports Designated Ports | 🔴 |
| Nicht weiterleitender Port | Redundanter Pfad, der zur Schleifenvermeidung blockiert wird (bei RSTP genauer: Alternate Port / Backup Port) | 🟡 |

Bei gleicher Root Path Cost entscheiden weitere Kriterien: niedrigere Bridge-ID des Nachbarswitches, dann niedrigere Port-ID.

**Portzustände** (was ein Port gerade tut) – siehe Abschnitt zu den Zuständen unten.

> **Merke:** Ein Port kann z. B. die Rolle "Nicht weiterleitend" haben und sich im Zustand "Blocking" befinden. Rolle und Zustand hängen zusammen, sind aber nicht dasselbe.

---

## 4. Warum blockiert STP überhaupt?

> Physisch redundant, logisch schleifenfrei.

STP entfernt die Redundanz **nicht physisch**. Ein redundanter Link bleibt eingesteckt, wird aber logisch nicht gleichzeitig für die normale Datenweiterleitung genutzt.

Fällt der aktive Weg aus (z. B. Kabelbruch), bemerkt STP das durch ausbleibende BPDUs, berechnet die Topologie neu und aktiviert den bisher blockierten Ersatzweg. Das Netzwerk "heilt" sich also selbst – bei klassischem STP dauert das allerdings, siehe unten.

```text
        +----------+
        | Switch A |   Root Bridge
        +--+----+--+
           |    |
    aktiv  |    |  blockiert (redundant)
           |    |
        +--+----+--+
        | Switch B |
        +----------+
```

Ein Link ist aktiv, der zweite wird von STP blockiert. Fällt der aktive Link aus, übernimmt der bisher blockierte Link.

---

## 5. Port-Zustände (klassisches STP)

> Die eigentliche Konvergenz durchläuft vier Zustände: Blocking → Listening → Learning → Forwarding. "Disabled" gehört nicht zu dieser Abfolge.

| Zustand | Bedeutung | IHK-Relevanz |
|---|---|---|
| Blocking | Keine Weiterleitung normaler Datenframes, kein MAC-Learning; BPDUs werden weiterhin verarbeitet. Kann im stabilen Netz dauerhaft bestehen | 🔴 |
| Listening (~15 Sek.) | STP bestimmt die aktive Topologie, noch keine Nutzdatenweiterleitung | 🟡 |
| Learning (~15 Sek.) | MAC-Adressen werden gelernt, noch keine Nutzdatenweiterleitung | 🟡 |
| Forwarding | Normale Nutzdatenweiterleitung | 🔴 |
| Disabled | Port administrativ/physikalisch nicht aktiv – **kein** normaler Übergangszustand der STP-Konvergenz | 🟢 |

**Konvergenzzeit:** Die beiden Forward-Delay-Phasen (Listening + Learning) dauern standardmäßig je 15 Sekunden, zusammen also ca. 30 Sekunden. Kommt zusätzlich die Max-Age-Zeit (Standard 20 Sekunden) zum Tragen, ergibt sich die bekannte Faustregel:

Konvergenzzeit ≈ 2 × Forward Delay + Max Age = 2 × 15 s + 20 s = **50 Sekunden**

Deshalb liest man je nach Fehlerfall Werte zwischen ca. 30 und 50 Sekunden.

---

## 6. RSTP und die Weiterentwicklungen

> Klassisches STP war für damalige Netze konzipiert; in modernen Netzen kann die klassische Konvergenzzeit problematisch sein.

**RSTP (IEEE 802.1w)** überarbeitet das Protokollverfahren und führt zusätzliche Portrollen ein (Alternate Port, Backup Port) sowie den Zustand "Discarding" anstelle von Blocking/Listening. Bei geeigneter Topologie und korrekt konfigurierten Punkt-zu-Punkt- bzw. Edge-Ports erreicht RSTP oft eine Konvergenz im Bereich von Millisekunden bis wenigen Sekunden – garantiert ist das aber nicht, etwa wenn ältere STP-Geräte beteiligt sind.

**MSTP (IEEE 802.1s, heute in IEEE 802.1Q integriert)** gruppiert VLANs nicht in einen Baum pro VLAN, sondern in **MST-Instanzen** – mehrere VLANs teilen sich eine Spanning-Tree-Berechnung. Das spart Ressourcen gegenüber PVST+.

| Protokoll | Standard | Kernvorteil | IHK-Relevanz |
|---|---|---|---|
| STP | IEEE 802.1D | Ursprungsprotokoll, Konvergenz ca. 30–50 Sek. | 🔴 |
| RSTP | IEEE 802.1w | Deutlich schnellere Konvergenz (Millisekunden bis wenige Sekunden) | 🔴 |
| MSTP | IEEE 802.1s (→ 802.1Q) | VLANs werden zu MST-Instanzen gruppiert statt ein Baum pro VLAN | 🟡 |
| PVST+ / RPVST+ | Cisco-proprietär | 🟢 Cisco-Spezialwissen: eigene STP-Instanz pro VLAN | 🟢 |

---

## Kulturelle Randnotiz: "Algorhyme"

Radia Perlman beschrieb den Spanning-Tree-Algorithmus unter anderem in ihrem bekannten Gedicht **"Algorhyme"**. Die ungewöhnliche Darstellung kann als Merkhilfe dienen, ist für die Prüfung aber nicht relevant.

---

## Selbsttest

| Frage | Kurzantwort |
|---|---|
| Was verhindert STP konkret? | Broadcast Storms durch Layer-2-Loops |
| Wonach wird die Root Bridge gewählt? | Niedrigste Bridge-ID (Priorität, ggf. Extended System ID, MAC) |
| Was ist der Unterschied zwischen Portrolle und Portzustand? | Rolle = wofür der Port zuständig ist (z. B. Root Port); Zustand = was er gerade tut (z. B. Blocking) |
| Was passiert beim Ausfall des aktiven Weges? | STP erkennt das über ausbleibende BPDUs, berechnet neu und aktiviert den blockierten Ersatzweg |
| Was verbessert RSTP gegenüber STP? | Deutlich schnellere Konvergenz durch überarbeitetes Verfahren und zusätzliche Portrollen |

---

## IHK-Cheatsheet

1. **STP** – Spanning Tree Protocol, IEEE 802.1D, verhindert Layer-2-Loops
2. **BPDU** – Bridge Protocol Data Unit; enthält u. a. Root-Bridge-ID, Root Path Cost, Sender-Bridge-ID, Port-ID
3. **Bridge-ID** – Priorität, ggf. Extended System ID, MAC-Adresse; niedrigster Wert gewinnt
4. **Root Bridge** – Switch mit niedrigster Bridge-ID, Bezugspunkt des Baums
5. **Root Port** – Port mit dem kostengünstigsten Gesamtpfad zur Root Bridge
6. **Designated Port** – Port eines Segments mit dem günstigsten Pfad zur Root Bridge
7. **Blocking** – Zustand: keine Nutzdatenweiterleitung, kein MAC-Learning, BPDUs werden verarbeitet
8. **Path Cost** – STP-Kosten eines Pfads, hängen typischerweise von der Linkgeschwindigkeit ab
9. **RSTP** – Rapid STP, IEEE 802.1w, schnellere Konvergenz, zusätzliche Portrollen
10. **Broadcast Storm** – starke Vervielfältigung und Zirkulation von Broadcasts durch einen Layer-2-Loop

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
|---|---|---|
| Erklärfrage | "Warum wird bei redundanter Verkabelung STP benötigt?" | Broadcast Storm als konkrete Folge nennen, nicht nur "Schleifen sind schlecht" |
| Vergleichsfrage | "Was unterscheidet STP von RSTP?" | Konvergenzzeit und zusätzliche Portrollen als zentrale Unterschiede benennen |
| Praxisfrage | "Ein Port ist im Blocking-Zustand – was bedeutet das?" | Physisch verbunden, leitet keine Nutzdaten weiter; BPDUs werden weiterhin verarbeitet |

---

## Merk-Sätze

> STP verhindert Broadcast Storms, indem es aus einem physisch vermaschten Netz logisch einen schleifenfreien Baum macht.

> Die Root Bridge wird über die niedrigste Bridge-ID gewählt – niedrigere Priorität gewinnt.

> Portrolle und Portzustand sind nicht dasselbe: ein Port kann z. B. "Nicht weiterleitend" sein und sich im Zustand "Blocking" befinden.

> Physisch redundant, logisch schleifenfrei – fällt der aktive Weg aus, aktiviert STP den Ersatzweg.

> RSTP löst das Hauptproblem von STP: die lange Konvergenzzeit von 30–50 Sekunden.

---

```yaml
lernfeld: LF3.3
typ: Bonus-Artikel (Typ A)
thema: Spanning Tree Protocol
status: Draft
stand: 2026
bezug: Ergänzung zu LF3.3 Strukturierte Verkabelung & Netzwerktopologien
```