# Broadcast Domain

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 20–25 Minuten
> **Status:** Final
> **Stand:** 2026

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Was ist eine Broadcast Domain? | [1. Definition](#1-definition) |
| 2 | Auf welcher OSI-Schicht liegt das Konzept? | [2. OSI-Einordnung](#2-osi-einordnung) |
| 3 | Was unterscheidet Broadcast Domain und Collision Domain? | [3. Broadcast vs. Collision Domain](#3-broadcast-vs-collision-domain) |
| 4 | Welche Geräte begrenzen eine Broadcast Domain? | [4. Akteure & Aufbau](#4-akteure--aufbau) |
| 5 | Warum wird ein Netz in mehrere Broadcast Domains segmentiert? | [5. Betrieblicher Nutzen](#5-betrieblicher-nutzen) |

---

## 1. Definition

> Eine Broadcast Domain ist der logische Bereich eines Netzwerks, in dem ein Layer-2-Broadcast eines Geräts alle anderen Geräte in diesem Bereich erreicht.

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Grundprinzip | Ein Frame an die Zieladresse `FF:FF:FF:FF:FF:FF` wird an alle Geräte im selben Bereich gesendet | 🔴 |
| Grenze | Logische, nicht zwingend physische Grenze (Subnetz, VLAN, Router-Interface) | 🔴 |
| Typisches Beispiel | ARP-Anfrage eines PCs erreicht alle Geräte hinter demselben Switch – bis zum nächsten Router | 🔴 |
| Ende der Domain | An der Router-Schnittstelle, da Router Layer-2-Broadcasts nicht weiterleiten | 🔴 |

> **IHK-Typfrage:** „Was ist eine Broadcast Domain?“
> **Musterantwort:** Der logische Netzwerkbereich, in dem alle Geräte einen Layer-2-Broadcast (Ziel-MAC FF:FF:FF:FF:FF:FF) empfangen. Switches leiten diesen Broadcast an alle Ports weiter, Router grenzen die Domain ab.

---

## 2. OSI-Einordnung

| Schicht | Bezug zur Broadcast Domain | IHK-Relevanz |
|---|---|---|
| Layer 1 (Physical) | Hubs vergrößern die Domain physisch, definitorisch bleibt das Konzept aber auf Layer 2 | 🟢 |
| Layer 2 (Data Link) | Primäre Ebene: MAC-Adressen, Ethernet-Frames, Switches/Bridges realisieren Broadcasts | 🔴 |
| Layer 3 (Network) | IP-Subnetze liegen meist auf den Grenzen der Broadcast Domain; Router trennen Domains | 🔴 |

**Merksatz:** Broadcast Domain = Layer-2-Konzept, aber die Grenze wird typischerweise von einem Layer-3-Gerät (Router) gezogen.

---

## 3. Broadcast vs. Collision Domain

```
┌─────────────── Broadcast Domain (1 Router-Interface / 1 VLAN) ───────────────┐
│                                                                              │
│   ┌── Collision Domain 1 ──┐   ┌── Collision Domain 2  ──┐   ┌── CD 3 ──┐    │
│   │  PC1 ── Switch-Port 1  │   │  PC2 ── Switch-Port 2   │   │  PC3     │    │
│   └────────────────────────┘   └─────────────────────────┘   └──────────┘    │
│                          alle über denselben Switch                          │
└──────────────────────────────────────────────────────────────────────────────┘
```

| Aspekt | Broadcast Domain | Collision Domain | IHK-Relevanz |
|---|---|---|---|
| Was passiert | Broadcast-Frame erreicht alle Teilnehmer | Physische Paketkollisionen möglich | 🔴 |
| Wer trennt | Router / Layer-3-Switch | Switch (pro Port eine eigene Domain) | 🔴 |
| Typische Größe im modernen Switch-Netz | Größer (ein VLAN/Subnetz) | Sehr klein (pro Switchport) | 🟡 |

---

## 4. Akteure & Aufbau

| Akteur | Rolle | IHK-Relevanz |
|---|---|---|
| Endgerät (PC, Server, Drucker) | Sendet und empfängt Broadcasts (z. B. ARP), muss jeden Broadcast der eigenen Domain prüfen | 🟡 |
| Switch / Bridge | Flutet Broadcast-Frames an alle Ports der Domain; trennt Collision-, nicht Broadcast-Domains (außer bei VLANs) | 🔴 |
| Router / Layer-3-Switch | Leitet Layer-2-Broadcasts nicht weiter → bildet Grenze zwischen Broadcast Domains | 🔴 |
| VLAN | Logisches Konstrukt, das Ports mehrerer Switches zu einer gemeinsamen Broadcast Domain zusammenfasst | 🔴 |
| Netzwerkadministrator | Plant Größe/Struktur der Domains, überwacht Broadcast-Traffic (z. B. Storm Control) | 🟡 |

**Faustregel:** Ein VLAN = eine Broadcast Domain = in der Regel ein IP-Subnetz.

---

## 5. Betrieblicher Nutzen

| Grund für Segmentierung | Beschreibung | IHK-Relevanz |
|---|---|---|
| Performance | Weniger Geräte pro Domain = weniger unnötige Broadcast-Last auf jedem Endgerät | 🔴 |
| Sicherheit | Trennung sensibler Bereiche (Server-Netz, Produktion, Gäste-WLAN) über eigene VLANs | 🔴 |
| Fehlerbegrenzung | Broadcast Storms bleiben innerhalb einer Domain, betreffen nicht das gesamte Netz | 🔴 |
| Skalierbarkeit | Kleinere, klar abgegrenzte Domains sind bei vielen Clients besser wartbar | 🟡 |

> **IHK-Typfrage:** „Warum segmentiert man ein Netz in mehrere Broadcast Domains?“
> **Musterantwort:** Um Broadcast-Last zu begrenzen, Sicherheitszonen zu trennen und die Auswirkungen von Fehlkonfigurationen (Broadcast Storms) auf einen kleineren Bereich zu beschränken.

---

## Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Ziel-MAC eines Broadcasts? | `FF:FF:FF:FF:FF:FF` |
| 2 | Welches Gerät trennt Broadcast Domains? | Router / Layer-3-Switch |
| 3 | Trennt ein normaler Switch Broadcast Domains? | Nein, nur mit VLAN-Konfiguration |
| 4 | Was ist eine Broadcast Storm? | Massenhafte, unkontrollierte Broadcasts, z. B. durch Loop ohne Spanning Tree |
| 5 | Entspricht ein VLAN typischerweise einer Broadcast Domain? | Ja |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Broadcast Domain | Logischer Bereich, in dem Layer-2-Broadcasts alle Geräte erreichen |
| Collision Domain | Bereich, in dem physische Paketkollisionen möglich sind |
| VLAN | Logisches Segment, das eine eigene Broadcast Domain bildet |
| Subnetz | IP-Adressbereich, der meist mit einer Broadcast Domain übereinstimmt |
| Broadcast-MAC | `FF:FF:FF:FF:FF:FF` |
| Broadcast Storm | Unkontrollierte Broadcast-Flut, z. B. durch Netzwerk-Loop |
| Storm Control | Switch-Feature zur Begrenzung von Broadcast-Traffic |
| Spanning Tree (STP) | Verhindert Loops, die Broadcast Storms verursachen können |
| Flooding | Weiterleitung eines Frames an alle Ports einer Domain durch den Switch |
| Layer-3-Switch | Gerät, das VLANs routet und damit Broadcast Domains trennt |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
|---|---|---|
| Begriffsdefinition | „Definieren Sie Broadcast Domain“ | Logischer L2-Bereich + Beispiel (ARP) + Abgrenzung durch Router |
| Vergleichsfrage | „Unterschied Broadcast vs. Collision Domain“ | Klare Trennung: Verteilung vs. Kollision, unterschiedliche trennende Geräte |
| Netzskizze | „Zeichnen/markieren Sie die Broadcast Domains“ | Jede Router-Schnittstelle = eigene Domain, VLANs korrekt eingezeichnet |
| Anwendungsfrage | „Warum mehrere Broadcast Domains sinnvoll?“ | Performance + Sicherheit + Fehlerbegrenzung nennen |

---

## Merk-Sätze (Fachgespräch)

> Eine Broadcast Domain endet an jeder Router-Schnittstelle.

> Switches fluten Broadcasts, Router blockieren sie.

> Ein VLAN ist in der Praxis meist gleichbedeutend mit einer Broadcast Domain.

> Kleinere Broadcast Domains bedeuten weniger Last und bessere Fehlerisolation.

---

```yaml
titel: Broadcast Domain
lernfeld: Netzwerktechnik-Grundlagen
typ: A
ihk_relevanz: hoch
letzte_pruefung: 2026
verwandte_artikel:
  - VLAN
  - Subnetting
  - OSI-Modell
  - Spanning Tree Protocol
```