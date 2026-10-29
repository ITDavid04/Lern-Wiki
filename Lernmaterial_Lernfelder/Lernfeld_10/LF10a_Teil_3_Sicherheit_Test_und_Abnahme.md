# LF10a Teil 3 – Sicherheit, Test & Abnahme

> **Zielgruppe:** Umschüler FIAE, 2. Lehrjahr (Aufbaustufe)
> **Prüfungsrelevanz:** Schwerpunkt AP2 im Prüfungsbereich "Planen eines Softwareproduktes" (schriftlich, 90 Minuten, 10% Gewichtung) – insbesondere "Maßnahmen zur Qualitätskontrolle planen und durchführen"; Datenschutzbezug auch für WiSo relevant. Projektbezogene Inhalte (Abnahme, Dokumentation) können außerdem im Fachgespräch relevant werden, sofern sie Teil der eigenen betrieblichen Projektarbeit sind.
> **Lernzeit:** Ca. 2,5–3 Stunden Lesen/Durcharbeiten, +1,5–2 Stunden für Teststrategie-/Abnahme-Übungen
> **Status:** Final
> **Stand:** 2026-09-14
>
>Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.
>
> **Hinweis zur Abgrenzung:** Letzter Teil der dreiteiligen LF10a-Serie (Teil 1: Konzeption & Struktur; Teil 2: Interaktion & Daten; Teil 3: Sicherheit, Test & Abnahme). Die WCAG-2.2-AA-Prüfwerttabelle in Abschnitt 2.3 ist inhaltsgleich mit der in Teil 1 (Abschnitt 4.4) eingeführten Tabelle – **Teil 1 ist die Pflegeautorität** für diese Werte, hier wird sie nur für die Testperspektive angewendet.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Wie unterscheiden sich Identity, Authentication, Authorization und Rolle, und warum ist Ausblenden keine Authorization? | [→ 1. Rollen, Datenschutz und sichere UI](#1-rollen-datenschutz-und-sichere-ui) |
| 2 | Wie wird eine risikoorientierte Teststrategie aufgebaut, und was leistet eine manuelle Accessibility-Prüfung gegenüber einem automatisierten Scan? | [→ 2. Funktions-, UX- und Accessibility-Tests](#2-funktions--ux--und-accessibility-tests) |
| 3 | Was macht einen Auslieferungsstand reproduzierbar, und welche Abnahmeentscheidungen gibt es? | [→ 3. Gesamtauftrag, Dokumentation und Abnahme](#3-gesamtauftrag-dokumentation-und-abnahme) |

---

## 1. Rollen, Datenschutz und sichere UI

> **Grundprinzip:** Ein Museumswärter, der am Eingang den Ausweis kontrolliert (Authentication), muss trotzdem an jeder Vitrine erneut prüfen, ob genau diese Person genau diesen Raum betreten darf (Authorization) – der Ausweis am Eingang beantwortet nur, wer da ist, nicht was diese Person darf.

### 1.1 Identity, Authentication, Authorization, Rolle

Für diesen Abschnitt werden bewusst die englischen Fachbegriffe verwendet – nicht aus Stilgründen, sondern weil das Deutsche hier zwei Wörter (Authentisierung/Authentifizierung) für denselben Vorgang kennt, deren Zuordnung in der Fachliteratur uneinheitlich gehandhabt wird. Im Englischen gibt es nur **ein** Wort, "authentication", das den gesamten Vorgang (Nachweis **und** Prüfung) abdeckt – und genau dieser englische Begriff ist auch der, mit dem in der Praxis tatsächlich gearbeitet wird: in Bibliotheken (`authenticate()`-Middleware), Protokollen (OAuth, OpenID Connect), HTTP-Status (401 Unauthorized) und Dokumentation. 🔴

| Begriff | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Identity** | Wer ein System nutzt | 🔴 |
| **Authentication** | Eine Identität wird behauptet und durch einen Nachweis (Passwort, Zertifikat, Token) belegt und geprüft – Nachweis und Prüfung werden hier bewusst nicht künstlich in zwei deutsche Einzelbegriffe zerlegt | 🔴 |
| **Authorization** | Entscheidet, welche Aktion diese Identität ausführen darf | 🔴 |
| **Rolle** | Bündelt fachliche Verantwortungen und Berechtigungen | 🟡 |

> **Hinweis:** Wird in einer Prüfungsaufgabe ausdrücklich nach "Authentisierung" oder "Authentifizierung" gefragt, bezieht sich das im Kern auf denselben Vorgang wie hier "Authentication" – die feinere deutsche Zweiteilung (Nachweis durch die Person vs. Prüfung durch das System) kann je nach Quelle unterschiedlich zugeordnet sein und muss deshalb nicht auswendig in einer bestimmten Richtung memoriert werden. Entscheidend ist das Verständnis des Ablaufs, nicht die exakte deutsche Wortwahl.

In einem echten System klärt die Anmeldung zuerst, ob jemand wirklich die Person ist, die er vorgibt zu sein. Danach merkt sich das System das über eine Sitzung mit Ablaufzeit oder ein **Zugangstoken**. Trotzdem prüft der Server bei jeder geschützten Anfrage erneut, ob diese Person das darf. Er verlässt sich weder darauf, dass die UI den Button versteckt hat, noch auf eine einmalige Prüfung beim Login. Wie das technisch gelöst ist, etwa über Sitzungsdaten, Claims im Token oder eine eigene Rechte-Engine, ist von System zu System verschieden. 🔴 Ein Zugangstoken gilt nur für begrenzte Zeit und für bestimmte Zwecke, und der Server prüft es bei jeder Verwendung. Es hat nichts zu suchen in der URL, in Fehlermeldungen, in Logs oder im Git-Repository. 🔴

### 1.2 Rollen-/Aktions-/Datenmatrix

Für jede Rolle hältst du fest: Was darf sie fachlich tun? Welche Daten braucht sie, und welche ausdrücklich **nicht**? Was zeigt ihr die UI? Welche Regel muss der Server durchsetzen?

> **Wichtig für die Prüfung:** Versteckte oder ausgegraute Buttons helfen bei der Orientierung, sind aber **keine Authorization**. Das ist dieselbe Warnung wie in Teil 1 bei der Navigation und in Teil 2 bei der Clientvalidierung. Wer die Adresse direkt aufruft oder eine Anfrage verändert, darf trotzdem nicht an geschützte Aktionen kommen, und das sicherstellen kann nur das Backend. Verschiedene Menüs je Rolle sind deshalb noch **kein Rollenmodell**: Solange nicht dasteht, welche Daten jede Rolle sieht und welche Regel der Server prüft, bleibt offen, was wirklich erlaubt ist.

### 1.3 Datenschutz systematisch prüfen

Bei jedem Feld mit personenbezogenen Daten fragst du: Wozu? Ist es wirklich nötig? Auf welcher Rechtsgrundlage? Wissen die Betroffenen davon? Wer sieht es? Wie lange wird es aufbewahrt? **Datenminimierung** (Art. 5 Abs. 1 lit. c DSGVO) heißt: nur so viele personenbezogene Daten wie für den Zweck nötig. Ob eine Verarbeitung insgesamt rechtmäßig ist, hängt von mehr ab, und ein Lernprojekt kann das **nicht nebenbei klären**. Unklare Punkte wie Rechtsgrundlage, Löschfristen oder Informationspflichten schreibst du deshalb offen als ungeklärt auf, statt so zu tun, als wären sie erledigt.

> **Wichtig für die Prüfung:** "Dann holen wir eben eine Einwilligung ein" ist keine Antwort für jedes Feld. Zuerst kommt die Frage, wofür das Feld da ist und ob es wirklich gebraucht wird, dann die passende Rechtsgrundlage. Wer reflexhaft auf Einwilligung setzt, überspringt diese Fragen und übersieht leicht, dass das Feld überflüssig ist. 🟡

### 1.4 Sichere Ein- und Ausgabegrenzen

Was Nutzer:innen eingeben, wird als **Text behandelt, nie als Code**. Für Inhalte zur Laufzeit nimmst du deshalb `textContent`. `innerHTML` wertet HTML-Tags aus und ist mit ungeprüften Eingaben eine offene Tür für Cross-Site-Scripting (XSS).

```js
output.textContent = userInput; // sicher: wird als Text dargestellt, nicht als Markup interpretiert
```

Außerdem gilt: Geheimnisse wie Tokens oder Passwörter tauchen weder in der URL noch in der Konsole noch in Fehlermeldungen auf. Der Server validiert immer selbst. Werte werden dort passend kodiert, wo sie eingesetzt werden, im Backend wie im Frontend. Eine Ablehnung ist verständlich, verrät aber keine internen Details. Und in Tests kommen keine echten Personen- oder Zugangsdaten vor.

> **IHK-Typfrage:** *"Eine Testeingabe `<strong>Admin</strong>` wird in einem Statusfeld über `output.innerHTML = userInput` ausgegeben. Bewerten Sie das Risiko und schlagen Sie eine sichere Alternative vor."*
> **Musterantwort:** `innerHTML` interpretiert den Eingabewert als HTML-Markup statt als reinen Text – die Zeichenkette `<strong>Admin</strong>` würde also tatsächlich fett dargestellt, statt wörtlich angezeigt zu werden. Bei ungeprüften Nutzereingaben entsteht dadurch eine HTML-Injection- und potenziell eine **Cross-Site-Scripting (XSS)**-Gefahr – nicht zwangsläufig, weil ein einfach eingefügtes `<script>`-Element automatisch ausgeführt würde, sondern weil andere aktive Konstrukte wie Event-Handler-Attribute (z. B. `onerror`) auf diesem Weg in die Seite gelangen können. Die sichere Alternative ist `output.textContent = userInput`: `textContent` interpretiert den Wert grundsätzlich als reinen Text, unabhängig vom Inhalt der Zeichenkette. Serverseitige Validierung bleibt zusätzlich erforderlich; Ausgaben müssen außerdem dort sicher behandelt werden, wo sie tatsächlich eingefügt werden (als HTML, Attribut, URL oder JavaScript-Wert) – Ausgabesicherheit ist kontextabhängig, nicht allein eine Backend-Aufgabe. 🔴

### 1.5 Missbrauchstests und die Grenze der Simulation

Beim Missbrauchstest benutzt du die Anwendung absichtlich falsch: Rolle wechseln, eine Seite direkt über die Adresse aufrufen, Eingaben verfälschen, mit abgelaufener Sitzung weitermachen, nach Daten suchen, die man nicht sehen dürfte. In einem reinen UI-Projekt prüfst du, **wie die Oberfläche reagiert**, und schreibst auf, was sich erst mit einem echten Backend beurteilen lässt. Getestet wird nur die eigene Anwendung mit erfundenen Daten, **fremde Systeme** werden weder gescannt noch angegriffen.

> **Wichtig für die Prüfung:** Ein Umschalter für Rollen im Frontend spielt nur verschiedene Ansichten durch. Er prüft niemandes Identität und schützt keine Daten. Wer ihn als Login ausgibt, verspricht eine **Sicherheit, die es nicht gibt**. Kurz gesagt: Die UI zeigt, was erlaubt ist, durchsetzen muss es das System dahinter.

---

## 2. Funktions-, UX- und Accessibility-Tests

> **Grundprinzip:** Wer beim TÜV nur Licht und Hupe prüft, obwohl gerade die Bremsen neu eingebaut wurden, hat zwar getestet, aber am falschen Ende. Eine Teststrategie fängt deshalb bei der Frage an, wo das Risiko liegt und wie gründlich es geprüft werden muss. Welche Werkzeuge dafür taugen, kommt danach.

### 2.1 Teststrategie, Rückverfolgbarkeit und Testarten

Die **Teststrategie** legt fest, was getestet wird, mit welcher Testart, wie wichtig es ist und warum. Ausgangspunkt sind die Anforderungen und Risiken, nicht ein Tool. **Rückverfolgbarkeit** heißt: Von jeder Anforderung führt ein Faden zu ihrem Risiko, zu den Testfällen und zu deren Ergebnissen. Wird ein Fehler behoben, hängen die Entscheidung dazu und der Nachtest am selben Faden.

| Testart | Prüft | IHK-Relevanz |
| --- | --- | --- |
| **Funktionstest** | Beobachtbares Sollverhalten | 🔴 |
| **Zustandstest** | Normal-, Leer-, Lade-, Fehler-, Erfolgszustände (vgl. Teil 1, Abschnitt 2.3) | 🔴 |
| **Tastaturtest** | Erreichbarkeit, Reihenfolge, Fokus | 🟡 |
| **Accessibility-Prüfung** | Ausgewählte WCAG-bezogene Kriterien, manuell und werkzeuggestützt | 🟡 |
| **UX-Test** | Wie Personen realistische Aufgaben bearbeiten | 🟡 |
| **Browser-Engine-Vergleich** | Technische Abweichungen zwischen Rendering-/JavaScript-Engines | 🟢 |

> **Wichtig für die Prüfung:** Automatische Tests sind stark bei Regeln, die immer gleich ablaufen und ein klares Ja oder Nein haben. Ob eine Beschriftung verständlich, eine Reihenfolge logisch oder eine Fehlermeldung hilfreich ist, können sie **nicht verlässlich** beurteilen. 🔴 GUI-Tests schauen auf zwei Seiten, die zusammengehören, aber getrennt geprüft werden: **Darstellung** (Anordnung, Kontrast, Verhalten bei verschiedenen Breiten) und **Funktion** (Navigation, Ereignisse, Zustandswechsel). Ein Button kann perfekt aussehen und das Falsche tun, oder richtig arbeiten, aber seine Rückmeldung geht unter oder er ist per Tastatur gar nicht erreichbar. 🟡

### 2.2 Gute Funktionsfälle

Zu einem vollständigen Testfall gehören: eine feste Test-ID mit Verweis auf die Anforderung, Vorbedingungen und Testdaten, Schritte, die jeder nachmachen kann, ein klares Soll-Ergebnis, das tatsächliche Ist-Ergebnis mit Beleg und der Status. Testen solltest du den Normalfall, falsche Eingaben, Grenzwerte, Abbrüche, verschiedene Rollen und Zustände. "Funktioniert" ist als Soll-Ergebnis **zu ungenau**.

### 2.3 Manuelle Accessibility-Prüfung

Für die Nachweise gelten die WCAG-2.2-AA-Werte aus Teil 1, Abschnitt 4.4. Geändert werden sie nur dort:

| Prüfgegenstand | Erfolgskriterium | Prüfwert |
| --- | --- | --- |
| Textkontrast | 1.4.3 | mind. 4,5:1 (mind. 3:1 bei großem Text) |
| Textvergrößerung | 1.4.4 | bis 200% ohne Inhalts-/Funktionsverlust |
| Reflow | 1.4.10 | bei vertikal scrollendem Inhalt bis 320 CSS-Pixel Breite grundsätzlich ohne Verlust und ohne zweidimensionales Scrollen (bei horizontaler Leserichtung entsprechend 256 CSS-Pixel Höhe); ausgenommen sind Inhaltsteile, deren Nutzung oder Bedeutung ein zweidimensionales Layout tatsächlich erfordert – "breit" allein ist keine Ausnahme |
| Nichttextkontrast | 1.4.11 | mind. 3:1 für wesentliche grafische Objekte/Bedienelemente, soweit für Verständnis/Bedienung erforderlich |
| Sichtbarer Fokus | 2.4.7 | jedes tastaturbedienbare Element hat sichtbaren Fokusindikator |
| Fokus nicht verdeckt (neu in WCAG 2.2) | 2.4.11 | Ein fokussiertes Element darf durch vom Autor erstellten Inhalt nicht vollständig verdeckt sein |
| Zielgröße | 2.5.8 | mind. 24×24 CSS-Pixel; kleinere Ziele nur über definierte Ausnahmen (u. a. messbare Abstandsausnahme, gleichwertige Alternative, Inline-Ziele, User-Agent-Steuerung, wesentliche Darstellung) |
| Statusmeldungen | 4.1.3 | programmatisch ermittelbar, ohne dafür Fokus zu erhalten |

Dazu kommen von Hand: Stimmt die Reihenfolge? Haben alle Bedienelemente einen auslesbaren Namen und eine sichtbare Beschriftung? Kommt man mit der Tastatur einmal komplett durch? Ein Prüftool **hilft** dabei, nimmt dir die Prüfung aber nicht ab. Notiere, welches Tool in welcher Version du genutzt hast und was es nicht erkennt. Diese Tabelle ist wie in Teil 1 **kein vollständiger WCAG-Konformitätsnachweis**, sondern eine ausgewählte, modulübergreifend wiederkehrende Referenz.

### 2.4 Moderierter UX-Test

UX-Tests verwenden realistische Zielaufgaben ohne Bedienhinweise. Drei Schritte werden getrennt gehalten: **Beobachtung** ("Person öffnet dreimal die Navigation"), **Interpretation** ("Der Einstieg wird möglicherweise nicht erkannt"), **Vorschlag** ("Primäraktion eindeutiger benennen und erneut testen").

> **Wichtig für die Prüfung:** Ein UX-Test beobachtet echte Nutzung und findet dabei auch Probleme, an die vorher niemand gedacht hat. Ein **Akzeptanztest** (siehe Teil 1, Abschnitt 2.5) hakt dagegen ab, was vorher vereinbart war. Ein UX-Befund kann zu einer neuen Anforderung oder Verbesserung führen. Ein durchgefallenes Akzeptanzkriterium ist er **deshalb noch nicht**, denn oft betrifft er etwas, das nie vereinbart war.

Welches Verfahren passt, hängt von der Frage ab, die du beantworten willst (Kontextanalyse, Fokusgruppe, Online-Umfrage, Expertenprüfung bzw. heuristische Evaluation, Labortest, Eye-Tracking, siehe Teil 1, Abschnitt 2.5). Fokusgruppe und Umfrage liefern, was Menschen **sagen**. Kontextanalyse und Labortest zeigen, was sie **tun**. Eye-Tracking verrät, wohin jemand schaut, aber nicht den Grund dafür.

### 2.5 Browser-Engine-Vergleich, Befunde und Regression

> **Typische Prüfungsfalle:** Chrome und Edge laufen beide auf Chromium. Wer nur diese zwei testet, hat **keine verschiedenen Engines** verglichen, denn technisch verhalten sie sich sehr ähnlich. Ein echter Vergleich nimmt etwa auch Firefox (Gecko) und Safari (WebKit) dazu und notiert jeweils Browser, Engine, Version, Betriebssystem, Fensterbreite und was nur simuliert war. Abweichungen sortierst du nach Darstellung, Fokus, Eingabe und Funktion.

Ein Befund beschreibt: welche Folgen er hat, wie man ihn nachstellt, wie dringend er ist, wer sich kümmert und was entschieden wurde. **Blockierend** ist ein Fehler nur, wenn man das Hauptziel nicht erreicht oder die Nutzung unsicher wird. Wer alles zur Top-Priorität erklärt, hat am Ende keine mehr. Nach einer Korrektur testest du nicht nur den einen Fall neu, sondern auch, was drumherum liegt (**Regressionstest**, siehe Teil 2, Abschnitt 1).

---

## 3. Gesamtauftrag, Dokumentation und Abnahme

> **Grundprinzip:** Ein Umzugsunternehmen, das am Zielort Kisten mit unklarer, teils widersprüchlicher Beschriftung abstellt, hat zwar "geliefert" – aber niemand kann ohne Rückfrage sagen, was fertig gepackt und was noch unvollständig ist. Konsolidierung schafft genau diese Eindeutigkeit vor der Übergabe.

### 3.1 Konsolidierung und Rückverfolgbarkeitsmatrix

Die **Rückverfolgbarkeitsmatrix** ist eine Tabelle mit einer Zeile je Muss-Anforderung. Die Spalten: wo sie in der UI umgesetzt ist, welcher Test dazu gehört und was er ergab, der Status (umgesetzt, teilweise, nicht umgesetzt, nicht prüfbar), was noch fehlt und was dazu entschieden wurde.

> **Wichtig für die Prüfung:** Was nicht umgesetzt ist, **bleibt in der Matrix stehen**, denn genau daran sieht man, was fehlt und welches Risiko bleibt. Streicht man es heraus, sieht das Projekt fertiger aus, als es ist, und bei der Abnahme fehlt die Grundlage für eine ehrliche Entscheidung. Mit alten Wireframes und doppelten Dateien ist es ähnlich: weder heimlich löschen noch unkommentiert liegen lassen, sondern klar markieren, welche Fassung gilt und was ins Archiv gehört.

### 3.2 Reproduzierbarer Auslieferungsstand

**Reproduzierbar** ist ein Stand, wenn jemand, der nicht im Projekt war, ihn allein mit der Dokumentation zum Laufen bringt, ohne nachfragen zu müssen. Dafür braucht es: Voraussetzungen/unterstützte Umgebung, Bezugs-/Installationsschritte, eindeutiger Startbefehl, freigegebene synthetische Testdatenquelle, dokumentierte Testkonten für eine nicht-produktive Umgebung (ohne echte Passwörter oder produktive Zugangsdaten), bekannte Einschränkungen, erwartetes Ergebnis eines **Smoke-Tests** (kurzer Durchlauf der wichtigsten Start-/Kernfunktionen – ersetzt keine vollständigen Funktions-, Accessibility- oder Regressionstests). "Bei uns läuft es" ist **kein Nachweis**.

### 3.3 Nutzer- und Entwicklungsdokumentation

| Zielgruppe | Inhalt |
| --- | --- |
| **Nutzerkurzanleitung** | Aufgabe/Einstieg, Kernabläufe in fachlicher Sprache, erkennbare Zustände/Korrekturwege, Hilfe-/Kontaktstelle – keine unnötigen internen Implementierungsdetails |
| **Entwicklungsdokumentation** | Aufbau und wichtige Entscheidungen, Designsystem und Datenvertrag, Rollen und Sicherheitsgrenzen, wie Tests laufen und was sie nicht abdecken, wo sich die Anwendung erweitern lässt, genutzte Bibliotheken mit Version, Herkunft, Lizenz und Grund für die Wahl |

> **Wichtig für die Prüfung:** Was im Backend noch fehlt, steht ehrlich als offen in der Doku. Eine nachgespielte UI wird **nicht** als fertiges Speichern, fertiger Login oder fertige Rechteprüfung verkauft (siehe Abschnitt 1.5). 🔴 Wird ein Framework eingesetzt, wird zusätzlich der vorgegebene Anwendungsrahmen mit seinen Folgen für Start, Build, Test und Wartung dokumentiert – Bibliothek und Framework bleiben dabei begrifflich getrennt (vgl. Teil 2, Abschnitt 1.3). 🟡

### 3.4 Soll-Ist-Abnahme

Bei der **Abnahme** wird der gelieferte Stand an den vereinbarten Kriterien gemessen, persönlicher Geschmack zählt nicht. Jedes Abnahmeszenario dokumentiert Ausgangslage, Soll, Durchführung, Beleg, Ist und Abweichung. Dieser Artikel arbeitet mit drei möglichen Entscheidungen. Das ist kein feststehender Rechtsbegriff, sondern ein praktisches Raster für Projekte wie dieses:

| Entscheidung | Bedeutung im Lernprojekt | IHK-Relevanz |
| --- | --- | --- |
| **Abnahmefähig** | Vereinbarte Muss-Kriterien sind erfüllt; dokumentierte geringfügige Restabweichungen verhindern den vorgesehenen Einsatz nicht | 🔴 |
| **Bedingt abnahmefähig** | Der vereinbarte Zweck ist nur unter konkret dokumentierten Bedingungen oder Einschränkungen erreichbar | 🔴 |
| **Nicht abnahmefähig** | Eine blockierende Abweichung verhindert den vereinbarten Zweck | 🔴 |

> **IHK-Typfrage:** *"Ein Projekt erhält die Abnahmeentscheidung 'bedingt abnahmefähig'. Was fehlt dieser Formulierung noch, um vollständig zu sein?"*
> **Musterantwort:** Nur "bedingt abnahmefähig" zu schreiben, reicht nicht. Solange Bedingung, zuständige Person und Termin oder Auslöser fehlen, weiß niemand, ab wann die Einschränkung erledigt ist. Die offene Entscheidung wird so nur vertagt. Vollständig wäre zum Beispiel: "Bedingt abnahmefähig: freigegeben zum Vorführen mit erfundenen Daten, nicht für den Echtbetrieb. Es fehlen Speicherung und Rechteprüfung auf dem Server. Bedingung: Das Backend-Team liefert beides bis [Termin], zuständig ist [Rolle/Person]."

### 3.5 Nutzen, Aufwand und Sensitivität

Eine einfache Wirtschaftlichkeitsrechnung hält belegte Zahlen und Schätzungen auseinander. Zum Beispiel: Vorgänge pro Monat × geschätzte Ersparnis in Minuten ÷ 60 ergibt die gesparten Stunden pro Monat; mal einem begründeten internen Stundensatz ergibt das den Wert in Euro. Bei der **Sensitivitätsanalyse** drehst du an einer unsicheren Annahme, halbierst etwa die Minutenersparnis, und schaust, ob die Entscheidung dann noch dieselbe wäre.

> **Wichtig für die Prüfung:** Ein ausgerechneter Schätzwert ist **kein Messergebnis**. Die Formel kann stimmen, das Ergebnis ist trotzdem nur so gut wie die Annahmen. Sind Fallzahl und Zeitersparnis nicht als Schätzung markiert und nie variiert worden, tut die Zahl genauer, als sie ist.

### 3.6 Präsentation und Übergabe

Ein roter Faden für die Präsentation: (1) Problem und Nutzergruppen, (2) die wichtigsten Anforderungen und wie du sie gestaltet hast, (3) Live-Demo der Kernabläufe, (4) Testergebnisse und Korrekturen, (5) Grenzen bei Barrierefreiheit, Datenschutz und Backend, (6) Nutzen, Aufwand und deine Empfehlung zur Abnahme. Für die Demo brauchst du einen Plan B, etwa einen lokalen Stand, der sicher startet, oder einen vorher aufgezeichneten Ablauf. Folien über das Produkt ersetzen nicht, es zu zeigen.

---

## 4. Zusammenspiel der Konzepte in LF10a Teil 3

Die drei Module schließen die LF10a-Serie ab, indem sie die in Teil 1 und Teil 2 entwickelte Oberfläche auf Vertrauenswürdigkeit prüfen und übergabefähig machen: **Rollen, Datenschutz und sichere UI** (Abschnitt 1) ziehen die Grenze zwischen dem, was die Oberfläche anzeigen darf, und dem, was nur ein Backend verbindlich durchsetzen kann – dieselbe Grenze, die in Teil 1 (Navigation) und Teil 2 (Clientvalidierung) bereits als "Ausblenden/Client-geprüft ist nicht geschützt" auftauchte. **Funktions-, UX- und Accessibility-Tests** (Abschnitt 2) wenden die in Teil 1 eingeführten UI-Zustände und die WCAG-Tabelle konkret auf die Testphase an. **Gesamtauftrag, Dokumentation und Abnahme** (Abschnitt 3) fasst alles zusammen: Eine Abnahme ist nur so belastbar wie die Rückverfolgbarkeit zwischen Anforderung (Teil 1), Umsetzung (Teil 1/2) und Testbeleg (Abschnitt 2) – und eine ehrliche Übergabe benennt offen, wo UI-Simulation endet und echte Backend-Absicherung erst beginnen müsste.

---

## 5. Typische Prüfungsfallen

| # | Falle | Richtigstellung | IHK-Relevanz |
| --- | --- | --- | --- |
| 1 | Nach erfolgreicher Anmeldung ist jede weitere Aktion automatisch autorisiert | Der Server setzt bei jeder geschützten Aktion die Authorization verbindlich durch – Authentication und Authorization sind getrennte, wiederkehrende Prüfungen | 🔴 |
| 2 | Je Rolle ein anderes Menü, fertig ist das Rollenmodell | Erst wenn für jede Rolle Aktionen, Daten und die Serverregel feststehen, ist klar, was wirklich erlaubt ist | 🔴 |
| 3 | Mit einer Einwilligung ist jedes Feld abgedeckt | Erst kommen Zweck und Notwendigkeit, dann die passende Rechtsgrundlage; der Griff zur Einwilligung lässt leicht übersehen, dass ein Feld überflüssig ist | 🟡 |
| 4 | Freitext kann man ruhig per `innerHTML` einsetzen | `innerHTML` führt HTML aus, das öffnet XSS die Tür; für Text gehört `textContent` her | 🔴 |
| 5 | Ein lokaler Rollenschalter beweist Authentication | Er simuliert nur einen UI-Zustand, prüft keine Identität und schützt keine Daten | 🔴 |
| 6 | Ist der Accessibility-Scan grün, ist die Seite barrierefrei | Ein Scan findet nur bestimmte technische Fehler; ob Texte verständlich sind, die Fokusreihenfolge Sinn ergibt und alles per Tastatur geht, muss ein Mensch prüfen | 🔴 |
| 7 | Zwei Browser mit derselben Engine sind ein vollständiger Engine-Vergleich | Sie teilen viele technische Eigenschaften – ein echter Vergleich dokumentiert tatsächlich unterschiedliche Engines | 🟡 |
| 8 | Ein UX-Befund ist automatisch ein fehlgeschlagenes Akzeptanzkriterium | UX-Test und Akzeptanztest beantworten unterschiedliche Fragen – ein UX-Befund kann eine neue Anforderung auslösen, ohne ein Kriterium zu verfehlen | 🟡 |
| 9 | Nicht umgesetzte Anforderungen gehören nicht in die Rückverfolgbarkeitsmatrix | Gerade sie zeigen Restumfang und Risiko – ihr Fehlen würde die Abdeckung besser erscheinen lassen, als sie ist | 🔴 |
| 10 | Eine überzeugende Demo ist bereits produktionsreif | Lokale Fixtures/Rollenschalter zeigen Abläufe, beweisen aber weder Persistenz noch Authentication/Authorization | 🔴 |

---

## 6. Vertiefung und Ausblick (freiwillig – für den ersten Durchgang nicht erforderlich)

- **OAuth/OpenID Connect im Detail**: Wie Authentication und Authorization in produktiven Systemen über etablierte Protokolle statt eigener Lösungen umgesetzt werden.
- **Content Security Policy (CSP)**: Wie eine zusätzliche Browser-Schutzschicht auch bei Fehlern in der Ausgabe-Kodierung greifen kann.
- **Automatisierte Accessibility-Testwerkzeuge im Detail**: Wie Tools wie axe-core oder Lighthouse technisch funktionieren und wo genau ihre Erkennungsgrenzen liegen.
- **A/B-Tests als UX-Verfahren**: Wie sich quantitative Vergleichsverfahren zu den in Abschnitt 2.4 genannten qualitativen Verfahren verhalten.
- **Explorative Testtechniken**: Strukturiertes, aber nicht vollständig vorab skriptgebundenes Testen als Ergänzung zu geplanten Testfällen.

---

## 7. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Was unterscheidet Authentication und Authorization? | Authentication prüft eine Identität; Authorization entscheidet über eine konkrete Aktion/einen Datenzugriff |
| 2 | Warum reicht Ausblenden einer UI-Funktion nicht als Zugriffsschutz? | Client-Code und Adressen lassen sich manipulieren – nur ein Backend kann eine Aktion verbindlich ablehnen |
| 3 | Was bedeutet Datenminimierung nach Art. 5 Abs. 1 lit. c DSGVO? | Nur so viele personenbezogene Daten verarbeiten, wie der Zweck tatsächlich erfordert |
| 4 | Warum ist `textContent` für Nutzereingaben sicherer als `innerHTML`? | `textContent` interpretiert den Wert immer als reinen Text, `innerHTML` interpretiert ihn als Markup |
| 5 | Was unterscheidet Darstellung und Funktionalität bei einem GUI-Test? | Darstellung: Anordnung/Kontrast/visuelle Konsistenz; Funktionalität: Navigation/Ereignisse/Zustandswechsel |
| 6 | Was unterscheidet UX-Test und Akzeptanztest? | UX-Test untersucht tatsächliche Nutzung; Akzeptanztest prüft vorab vereinbarte Kriterien |
| 7 | Was macht einen Auslieferungsstand reproduzierbar? | Die Doku zu Voraussetzungen, Startbefehl, Testdaten, bekannten Einschränkungen und Smoke-Test reicht, damit jemand Fremdes den Stand ohne Rückfragen startet |
| 8 | Nenne die drei Abnahmeentscheidungen dieses Lernprojekt-Modells. | Abnahmefähig, bedingt abnahmefähig, nicht abnahmefähig – ein operatives Modell für dieses Projekt, kein allgemeingültiger Rechtsbegriff |
| 9 | Warum ist ein berechneter Nutzen-Schätzwert kein gemessener Fakt? | Er bleibt von Annahmen (Fallzahl, Zeitersparnis) abhängig – eine Sensitivitätsbetrachtung prüft, ob die Empfehlung bei veränderten Annahmen stabil bleibt |

---

## 8. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Identity/Authentication/Authorization/Rolle** | Wer nutzt / Identität wird nachgewiesen+geprüft / Aktion wird erlaubt / bündelt Verantwortung |
| **Zugangstoken** | Zeitlich/im Umfang begrenztes Zugriffsmittel, vom Server validiert – nicht in URL/Fehlermeldung/Logausgabe/Repository |
| **Rollen-/Aktions-/Datenmatrix** | Aktion + benötigte/nicht benötigte Daten + UI-Darstellung + serverseitige Regel je Rolle |
| **Ausblenden ≠ Authorization** | Verbessert Orientierung, ersetzt keine serverseitige Prüfung |
| **Datenminimierung** | Art. 5 Abs. 1 lit. c DSGVO – Daten auf notwendiges Maß beschränken |
| **textContent vs. innerHTML** | Text sicher darstellen / Markup interpretieren (Risiko bei ungeprüften Eingaben) |
| **Teststrategie** | Was wird mit welcher Testart/Priorität/Begründung geprüft – beginnt bei Risiken, nicht beim Werkzeug |
| **Rückverfolgbarkeit** | Anforderung ↔ Risiko ↔ Testfall ↔ Ergebnis ↔ Korrektur/Nachtest |
| **Darstellung vs. Funktionalität** | Zwei getrennte, verbundene Prüfbereiche bei GUI-Tests |
| **Beobachtung/Interpretation/Vorschlag** | Drei zu trennende Schritte im UX-Test |
| **Smoke-Test** | Kurzer Durchlauf der Kernfunktionen – ersetzt keine vollständigen Tests |
| **Rückverfolgbarkeitsmatrix** | Muss-Anforderung ↔ UI-Bereich ↔ Test/Ergebnis ↔ Status ↔ Restabweichung |
| **Abnahmefähig/bedingt/nicht abnahmefähig** | Drei operative Abnahmeentscheidungen dieses Lernprojekt-Modells (kein universeller Rechtsbegriff) – "bedingt" braucht Bedingung + Verantwortlichkeit + Termin |
| **Sensitivitätsbetrachtung** | Prüft, ob eine Nutzen-/Aufwandsempfehlung bei veränderter Annahme stabil bleibt |

---

## 9. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die Prüfung hören will |
| --- | --- | --- |
| Rollenmodell bewerten | "Bewerten Sie dieses Rollenkonzept" | Konkret benennen, was serverseitig zusätzlich durchgesetzt werden muss |
| Datenschutzfrage einordnen | "Ist dieses Feld erforderlich?" | Zweck, Erforderlichkeit und Rechtsgrundlage getrennt benennen, nicht pauschal entscheiden |
| Sichere Ausgabe bewerten | "Bewerten Sie diese Codezeile" | Konkretes Risiko (Markup-Interpretation) benennen, sichere Alternative nennen |
| Teststrategie begründen | "Warum diese Testart für dieses Risiko?" | Auswirkung und Wahrscheinlichkeit des konkreten Fehlers als Begründung |
| Abnahmeentscheidung vervollständigen | "Ist diese Abnahme vollständig dokumentiert?" | Bedingung, Verantwortlichkeit, Termin/Auslöser einfordern |

---

## 10. Merksätze für das Fachgespräch

> Die Oberfläche zeigt, was erlaubt ist; ob es erlaubt ist, entscheidet der Server.

> Ausgeblendet ist nicht geschützt, simuliert ist nicht authentisiert.

> Ein guter Test klärt eine Frage zu einem echten Risiko und hinterlässt einen Beleg, den jeder nachprüfen kann.

> Ein grüner Scan ist ein Teilnachweis, kein Beweis vollständiger Barrierefreiheit.

> Abnahmefähig wird ein Projekt durch einen Stand, der überall startet, lückenlose Belege und ehrlich benannte Grenzen.

---

```yaml
dokument: LF10a-Teil3-wiki-artikel
lernfeld: "LF10a Teil 3 (Module 10a.8-10a.10)"
titel: "Sicherheit, Test & Abnahme"
typ: "Typ A – Kompakter Prüfungs-Wiki (FIAE-fokussiert)"
status: final
stand: 2026-09-14
quellen_intern:
  - "LF10a.8-10: Rollen/Datenschutz/sichere UI, Funktions-/UX-/Accessibility-Tests, Gesamtauftrag/Dokumentation/Abnahme"
  - "WCAG-2.2-AA-Tabelle in Abschnitt 2.3 bewusst inhaltsgleich mit der final korrigierten Tabelle aus LF10a Teil 1, Abschnitt 4.4 übernommen (dort explizit als Pflegeautorität gekennzeichnet, inkl. 2.4.11-Ergänzung aus Teil-1-Review) - Rohmaterial-Tabelle in LF10a.9 selbst war noch ohne 2.4.11, deshalb bewusst nicht wörtlich übernommen"
  - "Bewusste Rückbezüge zu Teil 1 (UI-Zustände, Ausblenden-ist-nicht-Authorization, Akzeptanztest-Abgrenzung) und Teil 2 (Clientvalidierung-ist-nicht-Sicherheit, Regressionstest, Bibliothek/Framework) statt Wiederholung"
quellen_fachlich:
  - titel: "Datenschutz-Grundverordnung (EU) 2016/679, Art. 5 Abs. 1 lit. c"
    herausgeber: "Europäische Union (EUR-Lex)"
    status: "Rohmaterial verlinkt Primärquelle; Artikelnummer und Grundsatz der Datenminimierung stabiles, etabliertes Recht, keine gesonderte Web-Verifikation nötig"
  - titel: "WCAG 2.2 (W3C)"
    herausgeber: "W3C"
    status: "Werte identisch zur bereits in LF10a Teil 1 web-verifizierten Tabelle übernommen, keine erneute Verifikation nötig"
  - titel: "Rollen-/Autorisierungsmodell, Teststrategie/Rückverfolgbarkeit, Abnahmekonzept"
    herausgeber: "Rohmaterial + etabliertes Software-Engineering-/Security-Standardwissen"
    status: "stabile Konzepte, keine Web-Verifikation nötig"
review_historie:
  - runde: 1
    datum: 2026-09-14
    ergebnis: "Erstdraft erstellt aus dem recherchierten Material. Als ein zusammenhängender Artikel (Teil 3 von 3, letzter Teil der LF10a-Serie) verfasst. WCAG-Tabelle bewusst aus der final korrigierten Teil-1-Fassung übernommen statt aus einer älteren Fassung (die noch kein 2.4.11 enthielt), um serienweite Konsistenz zu wahren. Zahlreiche bewusste Querverweise zu Teil 1 und Teil 2 eingebaut, um die 'Ausblenden/Client-geprüft ist nicht sicher'-Kernlinie über die gesamte Serie sichtbar zu halten. Von Anfang an gehedgte Formulierungen basierend auf den umfangreichen Lektionen aus Teil 1 und Teil 2 Review-Historien."
  - runde: 2
    datum: 2026-09-14
    ergebnis: "3 Reviews eingearbeitet. Wichtigster Fund (2 Reviews, gut begründet): innerHTML/XSS-Musterantwort war zu pauschal ('Skriptcode wird eingebracht') - technisch präzisiert (Event-Handler-Attribute statt automatischer Skriptausführung, XSS-Begriff explizit benannt), Ausgabe-Kodierung nicht mehr pauschal als reine Backend-Pflicht dargestellt. Authentisierung/Authentifizierung-Behauptung einer Review eigenständig recherchiert: Quellen widersprechen sich tatsächlich über die Zuordnungsrichtung (BSI-Quellen und andere Quellen nennen teils entgegengesetzte Zuordnungen) - keine einseitige 'Korrektur' vorgenommen, stattdessen Hinweis auf uneinheitlichen Sprachgebrauch ergänzt. Abnahmekategorien (2 Reviews) explizit als Lernprojekt-Modell statt universelle Rechtsterminologie gekennzeichnet. Weitere Korrekturen: Reflow um 256px-Detail bei horizontaler Leserichtung ergänzt, Zielgröße-Ausnahmen vollständiger aufgezählt (dadurch entsteht eine geringe zusätzliche Präzisionsdifferenz zur kompakteren Teil-1-Tabelle - bewusst in Kauf genommen, da Teil 3 die Testperspektive vertieft, ohne der Teil-1-Tabelle zu widersprechen); 'neue' Autorisierungsentscheidung leicht entschärft (Durchsetzung statt zwingend neuer Datenbankabfrage); Zugangstoken-Definition präzisiert (Logausgabe ergänzt); Testidentitäten-Formulierung geklärt (keine produktiven statt 'ohne jegliche' Geheimnisse); Datenschutz-Prüfliste um Rechtsgrundlage ergänzt; Farbmarkierungs-Ankündigung entfernt, da im gesamten LF10a-Fließtext (auch Teil 1/2) faktisch nicht angewendet - serienweites Muster, hier lokal korrigiert statt falsche Erwartung zu wecken. Eine vorgeschlagene Änderung (sichtbarer-Fokus-Formulierung) wurde geprüft, aber zugunsten exakter Konsistenz mit der Teil-1-Pflegeautorität nicht übernommen."
  - runde: 3
    datum: 2026-09-14
    ergebnis: "Auf ausdrücklichen Wunsch des Auftraggebers zwei gezielte Nacharbeiten: (1) Authentisierung/Authentifizierung-Terminologie in Abschnitt 1.1 auf englische Fachbegriffe (Identity/Authentication/Authorization) umgestellt, da Englisch im Programmierkontext ohnehin die gebräuchliche, eindeutige Terminologie ist (OAuth, HTTP 401, authenticate()-Middleware) - löst die uneinheitliche deutsche Zuordnung elegant, statt sie nur zu kommentieren. Alle weiteren 'Autorisierung'-Fundstellen im Artikel konsistent auf 'Authorization' umgestellt. (2) IHK-Relevanz-Markierungen (🔴/🟡/🟢) tatsächlich in den Fließtext eingebaut (Begriffstabelle 1.1, Testarten-Tabelle 2.1, Abnahme-Tabelle 3.4, mehrere Wichtig-Blöcke) statt nur die Ankündigung zu entfernen - Auftraggeber plant, Teil 1 und Teil 2 in einem separaten Durchgang ebenfalls entsprechend nachzuziehen. WCAG-Tabelle in 2.3 bewusst ohne Relevanz-Spalte belassen, da Teil-1-Pflegeautorität ebenfalls keine hat."
  - runde: 4
    datum: 2026-09-14
    ergebnis: "Eigene Abschlussprüfung nach externem Re-Review (drei weitere Reviews, überwiegend Bestätigung, einige reine Stil-/Formatierungshinweise auf Weisung des Auftraggebers ignoriert, da keine Fachfehler). Zwei echte Selbstkonsistenz-Reste gefunden und behoben: Selbsttest 8 und der Cheatsheet-Eintrag zu den Abnahmeentscheidungen nannten die drei Kategorien noch ohne den in 3.4 bewusst ergänzten Modellcharakter-Vorbehalt ('kein universeller Rechtsbegriff, sondern Lernprojekt-Modell') - angeglichen. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 4 Runden (3 externe Prüfrunden + 1 eigene Abschlussprüfung, 2026-09-14) – Freigabe durch Autor:in bestätigt. Serie LF10a (Teil 1-3) damit vollständig final."
```