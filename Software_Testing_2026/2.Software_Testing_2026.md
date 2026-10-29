# Software Testing 2026: Qualitätssicherung in Praxis und Ausbildung

> Ein Leitfaden für Umschüler – prüfungsrelevant, praxisnah, verständlich.

---

## Aktuelles Vorgehen 2026 – Best Practice im IT-Umfeld

Im IT-Umfeld des Jahres 2026 ist das Testen von Software keine reine Endkontrolle mehr. Es hat sich zu einem kontinuierlichen Prozess entwickelt, der das gesamte Team einbindet. Man spricht heute von **Quality Engineering (QE)** – der systematischen Qualitätsgestaltung von der ersten Idee bis zum fertigen Produkt.

### Zwei fundamentale Ansätze prägen die moderne Praxis

- **Shift-Left**  
  Testen verschiebt sich im Zeitstrahl nach links (also nach vorne). Das Team prüft Konzepte und Anforderungen schon, bevor überhaupt eine Zeile Code geschrieben wird. Das spart hohe Kosten, da logische Denkfehler sofort korrigiert werden können.

- **Shift-Right**  
  Das Testen wird nach dem Release auf der rechten Seite des Zeitstrahls fortgesetzt. Mithilfe von *Telemetrie* (automatisches Messen und Übertragen von Systemdaten wie Fehlermeldungen und Antwortzeiten direkt aus der Live-Anwendung) überwacht das Team die Qualität im echten Betrieb.

Ergänzt werden diese Methoden durch das **Shift-Smart-Testing**. Hier geht es nicht darum, möglichst viele Tests blind auszuführen. Stattdessen analysieren Testexperten gemeinsam mit dem Produktmanagement, welche Bereiche der Software das größte Risiko für das Unternehmen darstellen (*risikobasiertes Testen*) und prüfen diese besonders intensiv.

### Best-Practice-Konzepte

| Konzept | Einfache Erklärung | Praxis-Beispiel |
|---------|-------------------|-----------------|
| Shift-Left | So früh wie möglich testen. | Ein Entwickler bespricht die Kriterien für eine erfolgreiche Bestellung mit dem Fachbereich, noch bevor die Datenbank erstellt wird. |
| Shift-Right | Im Live-Betrieb weiter überwachen. | Ein Onlineshop misst automatisch, wie viele Nutzer den Kaufprozess aufgrund von Ladezeit-Verzögerungen abbrechen. |
| Shift-Smart | Nur das testen, was wirklich wichtig ist. | Bei einer Banking-App wird die Überweisungsfunktion extrem tief getestet, das Ändern des Profilbildes nur oberflächlich. |
| DevSecOps | Sicherheitstests fest einbauen. | Jedes Mal, wenn ein Entwickler Code speichert, sucht ein automatisches Tool im Hintergrund nach bekannten Sicherheitslücken. |

> 💡 **Was bedeutet das für deine Ausbildung & Prüfung?**  
> Sowohl für FIAE als auch für FISI ist das Verständnis dieser Lebenszyklen (SDLC) Pflicht. In deiner betrieblichen Projektarbeit (GAP2) musst du eine eigene Testphase dokumentieren. Der Prüfungsausschuss erwartet, dass du begründen kannst, warum du bestimmte Testfälle ausgewählt hast (risikobasiert) und wie du die Qualität deines Projekts abgesichert hast.

---

## Was wird aktuell genutzt?

In modernen IT-Projekten werden Testabläufe so weit wie möglich automatisiert, um Entwicklungszyklen zu beschleunigen. Folgende Technologien haben sich etabliert:

- **Selbstheilende Tests (Self-Healing)**  
  Klassische automatisierte Tests brechen oft ab, wenn ein Button auf einer Webseite verschoben oder umbenannt wird (sog. *Flaky Tests*). Selbstheilende Frameworks erkennen solche Änderungen mithilfe von KI eigenständig und passen den Suchpfad für das Element im laufenden Testbetrieb an.

- **Synthetische Testdaten**  
  Um echte Kundendaten gemäß DSGVO zu schützen, erzeugt man künstliche Daten. KI-Systeme generieren realistische Datensätze, die *referenzielle Integrität* wahren – alle logischen Beziehungen zwischen Tabellen bleiben korrekt (z. B. gehört jeder künstliche Auftrag zu einem existierenden künstlichen Kunden).

- **API-First-Testing**  
  Statt langwieriger Klick-Tests auf der Benutzeroberfläche werden die technischen Schnittstellen (APIs) sofort nach Bereitstellung isoliert auf Einhaltung ihrer Verträge geprüft.

### Wichtige Metriken (für die Prüfung)

**Anweisungsüberdeckung (C₀)**

$$
C_0 = \frac{A_{ex}}{A_{tot}} \times 100\%
$$

Misst den Prozentsatz der ausgeführten Programmzeilen.

**Zweigüberdeckung (C₁)**

$$
C_1 = \frac{Z_{ex}}{Z_{tot}} \times 100\%
$$

Prüft, wie viele der logischen Entscheidungswege (z. B. Ja/Nein einer `if`-Abfrage) abgedeckt wurden.

> 💡 **Was bedeutet das für deine Ausbildung & Prüfung?**  
> Die Berechnung von C₀ und C₁ an einem kurzen Programmbeispiel ist eine Standard-Rechenaufgabe in der schriftlichen IHK-Prüfung für FIAEs. Du musst exakt bestimmen können, wie viele Testfälle für eine vollständige Abdeckung nötig sind.

---

## Welche Programme sind aktuell gefragt?

Wir unterscheiden zwischen **lernrelevanten Tools** (Prüfung & Ausbildung) und **Nice-to-know Enterprise-Tools** (Berufspraxis in großen Unternehmen).

### Lernrelevante Tools (Fokus Ausbildung)

| Tool | Einsatzgebiet | Warum wichtig? |
|------|---------------|----------------|
| **JUnit / NUnit** | Unit-Tests (Modultests) | Einzelne Funktionen testen. Standard in der Prüfung für FIAE. |
| **Postman** | API-Testing | Schnittstellen prüfen, z. B. Statuscode `200 OK`. Wichtig für FIAE & FISI. |
| **Wireshark** | Netzwerkanalyse | Protokollanalyse und Fehlersuche. Absolut prüfungsrelevant für FISI. |

### Nice-to-know Enterprise-Tools

- **Sauce Labs** – Cloud-Testing auf über 9.000 echten Geräten und Browsern.
- **Virtuoso QA** – KI-gestützte Testerstellung in natürlicher Sprache, automatische Reparatur bei UI-Änderungen.
- **Rainforest QA** – No-Code-Plattform für visuelle Testautomatisierung.
- **Tricentis Tosca** – Modellbasiertes Testen, besonders in komplexen SAP-/ERP-Landschaften.

> 💡 **Was bedeutet das für deine Ausbildung & Prüfung?**  
> Konzentriere dich zuerst auf JUnit/NUnit (als FIAE) bzw. Wireshark und Netzwerkbefehle (als FISI). In Prüfungen musst du oft die Syntax einfacher Test-Zusicherungen (z. B. `assertEquals` in JUnit) interpretieren können.

---

## Welche Bedeutung spielt KI aktuell?

KI verändert die Softwareentwicklung rasant, bringt jedoch neue Herausforderungen. Man spricht vom **AI Software Quality Gap** (Qualitätslücke durch KI-Code): Da 93 % der Entwickler KI-Tools wie GitHub Copilot nutzen, wird extrem viel Code in kurzer Zeit erzeugt. Die traditionelle Qualitätssicherung kommt oft nicht hinterher – die Folge können fehlerhafte Releases sein.

> **Wichtig:** KI-generierter Code darf niemals ungeprüft in Produktion gehen. Modelle neigen zu subtilen Logikfehlern oder versagen unter realer Last.

### Praxis-Tipp: KI als Lernbegleiter nutzen

Du kannst ChatGPT oder Claude hervorragend nutzen, um das Schreiben von Tests zu üben.  
Beispiel für einen guten Prompt:

> *„Ich lerne gerade das Schreiben von JUnit-Tests in Java. Hier ist meine Methode zur Berechnung von Versandkosten. Bitte erstelle mir ein strukturiertes JUnit-Test-Gerüst dafür. Berücksichtige Grenzwerte (z. B. exakt 100 € Bestellwert für kostenlosen Versand) und ungültige Eingaben wie negative Beträge.“*

So lernst du schnell, wie saubere Tests aufgebaut sein müssen – ohne monotone Tipparbeit.

### Begriffe auf einen Blick

| Begriff | Einfache Erklärung | Relevanz |
|---------|-------------------|----------|
| Agentic AI | KI-Systeme, die eigenständig handeln, Pläne schmieden und Tests ausführen. | Zukunftstrend; verringert manuellen Testaufwand. |
| Prompt Engineering | Die Kunst, einer KI präzise Anweisungen zu geben. | Kernkompetenz im Umgang mit modernen Entwickler-Tools. |
| Scheinkorrelation | Wenn eine KI fälschlich Zusammenhänge vermutet, die nicht existieren. | Risiko bei automatischer Fehleranalyse durch KI. |

> 💡 **Was bedeutet das für deine Ausbildung & Prüfung?**  
> In der IHK-Prüfung Teil 1 (GAP1) wird der Umgang mit KI in Geschäftsprozessen bereits abgefragt (oft rund 18 % der Gesamtpunkte). Du musst erklären können, wo KI-Unterstützung sinnvoll ist und wo rechtliche oder qualitative Risiken liegen.

---

## Was ist wichtig für Umschüler?

### Fachinformatiker Anwendungsentwicklung (FIAE)

Als FIAE musst du Code von Anfang an testbar entwerfen. Erfolgskritisch sind:

- **Äquivalenzklassenbildung**  
  Teile Eingabewerte in Gruppen mit gleichem Systemverhalten.  
  *Beispiel:* Rabatt ab 100 € – Klassen: ungültig (<0), kein Rabatt (0–99,99 €), Rabatt (≥100 €). Ein Wert pro Klasse reicht zum Testen.

- **Grenzwertanalyse**  
  Fehler entstehen oft an Bereichsgrenzen. Teste genau die Übergänge.  
  *Beispiel:* -0,01 € | 0,00 € | 99,99 € | 100,00 €.

- **Schreibtischtests (Trace Tables)**  
  Manuelle Code-Analyse auf Papier: Zeile für Zeile im Kopf durchgehen und jede Variablenänderung in eine Tabelle eintragen.

### Fachinformatiker Systemintegration (FISI)

Als FISI testest du die Stabilität und Sicherheit ganzer Infrastrukturen. Entscheidend sind:

- **Systematisches Troubleshooting**  
  Fehlermeldungen in Logfiles und Netzwerk-Traces deuten können.  
  *Klassiker:* IP-Adresse `169.254.x.x` → DHCP-Server nicht erreichbar.

- **Diagnose-Befehle aus dem Effeff**  
  - `ping` – Erreichbarkeit prüfen  
  - `tracert` / `traceroute` – Weg der Datenpakete verfolgen  
  - `nslookup` – DNS-Auflösung testen

- **Datensicherungs-Konzepte**  
  Backup-Strategien nach dem Generationen-Prinzip (Großvater-Vater-Sohn), Kennzahlen RTO (*Recovery Time Objective*) und RPO (*Recovery Point Objective*) berechnen können.

> 💡 **Was bedeutet das für deine Ausbildung & Prüfung?**  
> Die IHK trennt in der AP2 strikt: FIAEs erhalten komplexe Code- und Datenbank-Testaufgaben, FISIs analysieren Netzwerkdiagramme, berechnen IP-Subnetze und entwerfen Backup-Strategien.

---

## Prüfungsrelevanz (IHK)

Das Thema Qualitätssicherung ist in allen Teilen der gestreckten Abschlussprüfung (GAP) ein Kernbestandteil.

- **GAP1 (20 % der Gesamtnote)** – für alle Fachrichtungen identisch  
  Ergonomie, Datenschutz (Anonymisierung vs. Pseudonymisierung), IT-Sicherheit, einfache Ablaufanalysen.

- **GAP2 (80 % der Gesamtnote)** – fachspezifisch  
  - *FIAE:* Testing ist elementarer Block im Fach „Entwicklung und Umsetzung von Algorithmen“ (10 %). Die 80-stündige Projektarbeit erfordert lückenlose Testdokumentation.  
  - *FISI:* Fokus auf Verifizierung von System-/Netzwerkkonfigurationen und Abnahmeprotokollen im 40-stündigen Abschlussprojekt.

---

## Testen Sie sich selbst! (Typische Prüfungsfragen)

### Übung 1: Netzwerkdiagnose (alle Fachrichtungen)

**Frage:** Ein Benutzer meldet keinen Zugriff auf das Firmen-Intranet. Der Netzwerkadapter zeigt die IP-Adresse `169.254.12.8`. Was ist die Ursache?

**Antwort / Lösung:**  
APIPA-Adresse (Automatic Private IP Addressing). Der Client ist auf automatischen IP-Bezug konfiguriert, konnte aber den DHCP-Server nicht erreichen.

---

### Übung 2: Zweigüberdeckung berechnen (Fokus FIAE)

Gegeben ist folgende Java-Methode:

```java
public static int pruefeZutritt(int alter) {
    int erlaubt = 0;
    if (alter >= 18) {
        erlaubt = 1;
    }
    return erlaubt;
}


Fragen:

    Wie viele Testfälle benötigst du für 100 % Anweisungsüberdeckung (C₀)?

    Wie viele Testfälle benötigst du für 100 % Zweigüberdeckung (C₁)?

Antwort / Lösung:

    Ein Testfall (z. B. alter = 20) reicht für C₀ – alle Zeilen werden ausgeführt.

    Zwei Testfälle (alter = 20 und alter = 15) sind nötig, um beide logischen Pfade (if-Zweig und impliziter else-Zweig) zu durchlaufen.

    💡 Was bedeutet das für deine Ausbildung & Prüfung?
    Mut zur Lücke ist beim Thema Testing gefährlich. Ein fehlender oder fehlerhafter Testbericht in deiner Projektdokumentation führt zu massivem Punktabzug und kann zum Nichtbestehen führen.

Lernmaterialien – gut lesbar, praxisnah
Einstiegs-Level (1. Ausbildungsjahr)

    Video-Reihe „Thomas Grosser“ (YouTube)
    Erklärt Black-Box-/White-Box-Verfahren anschaulich mit Skizzen.

    IT-Berufe-Podcast von Stefan Macke
    Perfekt für unterwegs: Schreibtischtests, Tipps zur Projektdokumentation, IHK-Prüfer-Perspektive.

Fortgeschrittenen- & IHK-Prüfungs-Level (2.–3. Jahr)

    „Softwaretesten nach ISTQB CTFL 4.0 für Dummies“ (Wiley-VCH)
    Lockere, verständliche Einführung in den internationalen Test-Standard.

    Prüfungsvorbereitungsbücher (Europa-Lehrmittel Verlag)
    Originalnahe Testprüfungen für GAP1 und GAP2, getrennt für FIAE und FISI.

Experten-Level (nach der Umschulung)

    „Basiswissen Softwaretest“ – Spillner & Linz (dpunkt.verlag)
    Standardwerk für die ISTQB-Zertifizierung. Theoretisch, aber der Karriere-Turbo im Quality Engineering.

Dein empfohlener Lern-Fahrplan
text

       │
       ▼
[Monat 01 - 12] ──► YouTube (Thomas Grosser) & IT-Berufe-Podcast
       │
       ▼
[Monat 13 - 24] ──► "ISTQB für Dummies" & Europa-Lehrmittel Übungsbücher
       │
       ▼
[Vor der Prüfung] ──► Alte IHK-Originalprüfungen unter Zeitdruck lösen

    Viel Erfolg für deine Umschulung und die IHK-Prüfung!




# Quellenverzeichnis nach Kategorien

> Sortierte Linkliste für das Wiki – passend zu den Kapiteln der Ausarbeitung.

---

## 1. Allgemeine Trends & Best Practices 2026

Artikel und Analysen zu den aktuellen Entwicklungen der Qualitätssicherung, strategischen Ansätzen und Branchenprognosen.

| Titel / Beschreibung | URL |
|----------------------|-----|
| Software QA Testing in 2026: Best Practices, Tools & Strategies | https://ambalait.com/blogs/software-qa-testing-in-2026-best-practices-tools-strategies-for-web-and-mobile-apps |
| Top Software Testing & QA Trends for 2026 | https://tsg-training.co.uk/blog/top-software-testing-qa-trends-for-2026/ |
| Software Testing Trends (Testomat) | https://testomat.io/blog/software-testing-trends/ |
| Top 5 Software Testing Trends 2026 (Xray) | https://www.getxray.app/blog/top-5-software-testing-trends-2026 |
| Software Testing Best Practices (BugBug) | https://bugbug.io/blog/test-automation/software-testing-best-practices/ |

---

## 2. Künstliche Intelligenz im Testing

Quellen zu KI-gestütztem Testen, dem AI Software Quality Gap und den Auswirkungen generativer KI auf die Qualitätssicherung.

| Titel / Beschreibung | URL |
|----------------------|-----|
| How AI is Redefining Software Testing Practices in 2026 | https://www.evozon.com/how-ai-is-redefining-software-testing-practices-in-2026/ |
| AI in Software Testing (Autify) | https://autify.com/blog/ai-in-software-testing |
| SmartBear AI Software Quality Gap Report | https://smartbear.com/ai-software-quality-gap-report/ |
| AI-Augmented Software Testing Tools (Gartner) | https://www.gartner.com/reviews/market/ai-augmented-software-testing-tools |

---

## 3. Testautomatisierung & Tools

Vergleiche, Bewertungen und Fachartikel zu konkreten Testwerkzeugen und Automatisierungstrends (inkl. Enterprise-Tools und Open-Source).

| Titel / Beschreibung | URL |
|----------------------|-----|
| Test Automation Trends 2026 | https://www.testdevlab.com/blog/test-automation-trends-2026 |
| Best AI Testing Tools (Virtuoso QA) | https://www.virtuosoqa.com/post/best-ai-testing-tools |
| Comparing the Best AI Automation Testing Tools in 2026 (Sauce Labs) | https://saucelabs.com/resources/blog/comparing-the-best-ai-automation-testing-tools-in-2026 |
| Automated Testing (Rainforest QA) | https://www.rainforestqa.com/blog/automated-testing |
| Reddit: I tested 50 AI tools so you don't have to – here's my tier list | https://www.reddit.com/r/automation/comments/1tr496j/i_tested_50_ai_tools_so_you_dont_have_to_heres/ |

---

## 4. IHK-Prüfungen & Ausbildungsrahmen

Offizielle Dokumente der IHK, Prüfungsleitfäden, Umsetzungsempfehlungen und Prüfungsvorbereitung speziell für Fachinformatiker.

| Titel / Beschreibung | URL |
|----------------------|-----|
| Leitfaden Systemintegration (IHK) | https://www.ihk.de/blueprint/servlet/resource/blob/6595910/9922dea3d1a2402026b5f361442799f5/leitfaden-systemintegration-data.pdf |
| Merkblatt IHK Niederbayern | https://www.ihk-niederbayern.de/pdfs/merkblatt.pdf |
| Umsetzungsempfehlungen für die AP (IHK) | https://www.ihk.de/blueprint/servlet/resource/blob/5797456/b90eac6a81b93de6ab68925bf10c5c79/it-berufe-umsetzungsempfehlungen-fuer-die-durchfuehrung-der-ap-data.pdf |
| Prüfungsvorbereitung Fachinformatiker (ausbildung-in-der-it.de) | https://ausbildung-in-der-it.de/pruefungsvorbereitung-fachinformatiker |
| Mögliche Themen GAP Teil 2 – FIAE (IT-Berufe-Podcast) | https://it-berufe-podcast.de/vorbereitung-auf-die-ihk-abschlusspruefung-der-it-berufe/moegliche-themen-von-teil-2-der-gestreckten-abschlusspruefung-gap-fuer-fachinformatiker-anwendungsentwicklung/ |
| Mögliche Themen GAP Teil 1 (IT-Berufe-Podcast) | https://it-berufe-podcast.de/vorbereitung-auf-die-ihk-abschlusspruefung-der-it-berufe/moegliche-themen-von-teil-1-der-gestreckten-abschlusspruefung-gap-in-den-it-berufen/ |
| AP Teil 2 Prüfungsguide für Fachinformatiker (PDF) | https://ausbildung-in-der-it.de/assets/pdfs/AP_Teil_2_Pruefungsguide_fuer_Fachinformatiker.pdf |

---

## 5. Lernmaterialien, Bücher & Verlage

Empfohlene Fachliteratur, Verlagsseiten und Weiterbildungsanbieter für Softwaretesting und ISTQB-Zertifizierung.

| Titel / Beschreibung | URL |
|----------------------|-----|
| Prüfungsvorbereitung Europa-Lehrmittel Verlag | https://www.europa-lehrmittel.de/Ausbildung/IT-Berufe/Pruefungsvorbereitung/ |
| Basiswissen Softwaretest (dpunkt.verlag) | https://dpunkt.de/produkt/basiswissen-softwaretest-2/ |
| Empfohlene Literatur (German Testing Board) | https://www.gtb.de/service/empfohlene-literatur/ |
| Weiterbildung Softwaretester (WBSTraining) | https://www.wbstraining.de/kurse/weiterbildung/softwaretester-1/ |

---

## 6. Podcasts & Videos

Audiovisuelle Lernressourcen – perfekt für den Einstieg oder die mobile Prüfungsvorbereitung.

| Titel / Beschreibung | URL |
|----------------------|-----|
| IT-Berufe-Podcast – Neuer Prüfungskatalog AP1 ab 2025 (Episode 190) | https://www.podcast.de/episode/654873373/neuer-pruefungskatalog-fuer-die-ap1-der-it-berufe-ab-2025-it-berufe-podcast-190 |
| YouTube: Grundlagen Softwaretesting (Video) | https://www.youtube.com/watch?v=iV8EF5aUrjU |
| YouTube: ISTQB Foundation Level – Testmethoden (Video) | https://www.youtube.com/watch?v=v7dhi8ajza4 |

---

> **Hinweis:** Die Quellen sind thematisch nach den Kapiteln der Ausarbeitung sortiert. So findet jeder Leser auf einen Blick, welche Links zu welchem Thema gehören.
```

