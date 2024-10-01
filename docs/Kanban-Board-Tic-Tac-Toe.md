---
title: "Kanban-Board-Tic-Tac-Toe"
author: "Jan Unger"
date: "2024-09-29"
---

# Kanban-Board und To-Do-Listen - Tic-Tac-Toe

bearbeitet am 1. Oktober 2024

- [Kanban-Board und To-Do-Listen - Tic-Tac-Toe](#kanban-board-und-to-do-listen---tic-tac-toe)
  - [Einrichtung des Kanban-Boards](#einrichtung-des-kanban-boards)
  - [Visualisierung des Kanban-Boards](#visualisierung-des-kanban-boards)
    - [**Kanban-Board Struktur:**](#kanban-board-struktur)
    - [**Priorisierung und WIP-Limits:**](#priorisierung-und-wip-limits)
  - [To-Do-Listen für jedes Modul](#to-do-listen-für-jedes-modul)
    - [**1. Grundlegende Module**](#1-grundlegende-module)
      - [**Modul 1: Startmenü**](#modul-1-startmenü)
      - [**Modul 2: Spielfeldverwaltung**](#modul-2-spielfeldverwaltung)
      - [**Modul 3: Spielmechanik**](#modul-3-spielmechanik)
    - [**2. Erweiterte Module**](#2-erweiterte-module)
      - [**Modul 4: Highscore-System**](#modul-4-highscore-system)
      - [**Modul 5: Dokumentation und Hilfe**](#modul-5-dokumentation-und-hilfe)
    - [**3. Fortgeschrittene Module**](#3-fortgeschrittene-module)
      - [**Modul 6: KI-Gegner**](#modul-6-ki-gegner)
  - [Tabelle für das Kanban-Board](#tabelle-für-das-kanban-board)
  - [Priorisierung von Aufgaben nach Wichtigkeit und Dringlichkeit](#priorisierung-von-aufgaben-nach-wichtigkeit-und-dringlichkeit)
  - [Begrenzung der gleichzeitigen Aufgaben (WIP-Limit)](#begrenzung-der-gleichzeitigen-aufgaben-wip-limit)
    - [**Implementierung des WIP-Limits:**](#implementierung-des-wip-limits)
  - [Einrichtung des Kanban-Boards in Trello (Beispiel)](#einrichtung-des-kanban-boards-in-trello-beispiel)
  - [Karte in Trello](#karte-in-trello)
  - [Zusammenfassung](#zusammenfassung)

## Einrichtung des Kanban-Boards

**Schritte zur Einrichtung:**

1. **Wählen Sie ein Kanban-Tool:**
   - **Trello:** Einfach zu bedienen, ideal für Anfänger.
   - **GitHub Projects:** Integriert in GitHub, gut für Entwicklerteams.
   - **Jira:** Leistungsstark und flexibel, geeignet für komplexere Projekte.
   - **KanbanFlow:** Bietet Echtzeit-Tracking und Zeitmanagement-Funktionen.

2. **Erstellen Sie die Hauptspalten:**
   - **Backlog:** Alle geplanten Aufgaben, die noch nicht begonnen wurden.
   - **To Do:** Aufgaben, die als nächstes bearbeitet werden sollen.
   - **In Bearbeitung:** Aufgaben, an denen aktuell gearbeitet wird (begrenzte Anzahl durch WIP-Limits).
   - **Review:** Aufgaben, die überprüft oder getestet werden müssen.
   - **Fertig:** Abgeschlossene Aufgaben.

3. **Definieren Sie Prioritäten:**
   - **Hoch (H):** Kritische Aufgaben, die sofortige Aufmerksamkeit erfordern.
   - **Mittel (M):** Wichtige Aufgaben, die nach den hohen Aufgaben bearbeitet werden.
   - **Niedrig (L):** Aufgaben, die weniger dringend sind und nach den mittleren Aufgaben erledigt werden können.

4. **Setzen Sie WIP-Limits:**
   - Begrenzen Sie die Anzahl der gleichzeitig bearbeiteten Aufgaben in der Spalte **"In Bearbeitung"** auf 1-3 Aufgaben, um Überlastung zu vermeiden und den Fokus zu behalten.

## Visualisierung des Kanban-Boards

Hier ist eine beispielhafte Darstellung eines Kanban-Boards für das **Tic-Tac-Toe**-Projekt:

### **Kanban-Board Struktur:**

| **Backlog**                          | **To Do**                                            | **In Bearbeitung**                         | **Review**                         | **Fertig**                        |
| ------------------------------------ | ---------------------------------------------------- | ------------------------------------------ | ---------------------------------- | --------------------------------- |
| **Grundlegende Module:**             | **Startmenü:** implementieren (H)                    | **Spielfeldverwaltung:** erstellen (H)     | **Spielmechanik:** Überprüfung (M) | **Startmenü:** erstellt           |
| - Benutzeroberfläche (GUI) entwerfen | **Eingabeverwaltung:** Funktionen implementieren (M) | **Spielfeldverwaltung:** aktualisieren (M) | **Spielmechanik:** Testen (M)      | **Spielfeldverwaltung:** erstellt |
| - Event-Handling implementieren      | **Spielmechanik:** Grundlogik entwickeln (H)         | **Spielmechanik:** Spielerwechsel (H)      | **Dokumentation:** überprüfen (L)  | **Spielmechanik:** implementiert  |
| **Erweiterte Module:**               | **Highscore-System:** entwickeln (M)                 |                                            |                                    | **Dokumentation:** aktualisiert   |
| - Highscore-System planen            | **Dokumentation:** erweitern (L)                     |                                            |                                    |                                   |
| **Fortgeschrittene Module:**         | **KI-Gegner:** implementieren (L)                    |                                            |                                    |                                   |
| - KI-Algorithmen erforschen          |                                                      |                                            |                                    |                                   |

### **Priorisierung und WIP-Limits:**

- **Hoch (H):** Startmenü implementieren, Spielfeldverwaltung erstellen, Spielmechanik Grundlogik entwickeln, Spielerwechsel implementieren.
- **Mittel (M):** Eingabeverwaltung Funktionen implementieren, Spielfeldverwaltung aktualisieren, Spielmechanik Überprüfung, Highscore-System entwickeln, Dokumentation erweitern.
- **Niedrig (L):** Dokumentation überprüfen, KI-Gegner implementieren.

- **WIP-Limit:** Maximal 2 Aufgaben gleichzeitig in der Spalte **"In Bearbeitung"**.

## To-Do-Listen für jedes Modul

### **1. Grundlegende Module**

#### **Modul 1: Startmenü**

| **Aufgabe**                                                    | **Priorität** | **Status**     |
| -------------------------------------------------------------- | ------------- | -------------- |
| GUI-Design des Startmenüs                                      | H             | To Do          |
| Buttons für „Neues Spiel“, „Anleitung“, „Beenden“ hinzufügen   | H             | To Do          |
| Event-Handling für Buttons implementieren                      | H             | In Bearbeitung |
| Spielmodus-Auswahl (Einzelspieler, Mehrspieler) implementieren | H             | To Do          |
| Testen des Startmenüs                                          | M             | Review         |

#### **Modul 2: Spielfeldverwaltung**

| **Aufgabe**                                  | **Priorität** | **Status**     |
| -------------------------------------------- | ------------- | -------------- |
| 3x3-Gitter mit Tkinter erstellen             | H             | To Do          |
| Funktionen zur Aktualisierung des Spielfelds | M             | In Bearbeitung |
| Anzeige der Spielerzüge                      | M             | To Do          |
| Testen der Spielfeldverwaltung               | M             | Review         |

#### **Modul 3: Spielmechanik**

| **Aufgabe**                         | **Priorität** | **Status**     |
| ----------------------------------- | ------------- | -------------- |
| Grundlogik der Spielzüge entwickeln | H             | To Do          |
| Überprüfung der Siegbedingungen     | H             | In Bearbeitung |
| Spielerwechsel implementieren       | H             | In Bearbeitung |
| Testen der Spielmechanik            | M             | Review         |

### **2. Erweiterte Module**

#### **Modul 4: Highscore-System**

| **Aufgabe**                               | **Priorität** | **Status** |
| ----------------------------------------- | ------------- | ---------- |
| Highscore-System planen                   | M             | Backlog    |
| Speicherung der Highscores implementieren | M             | To Do      |
| Anzeige der Highscores                    | M             | To Do      |
| Eingabe von Spielernamen bei Highscore    | M             | To Do      |
| Testen des Highscore-Systems              | M             | Review     |

#### **Modul 5: Dokumentation und Hilfe**

| **Aufgabe**                   | **Priorität** | **Status** |
| ----------------------------- | ------------- | ---------- |
| Spielanleitung erstellen      | L             | To Do      |
| Bedienungsanleitung erweitern | L             | To Do      |
| Dokumentation überprüfen      | L             | Review     |

### **3. Fortgeschrittene Module**

#### **Modul 6: KI-Gegner**

| **Aufgabe**                                 | **Priorität** | **Status** |
| ------------------------------------------- | ------------- | ---------- |
| Entscheidungsalgorithmen erforschen         | L             | Backlog    |
| KI-Zugberechnung implementieren             | L             | To Do      |
| Verschiedene Schwierigkeitsgrade hinzufügen | L             | To Do      |
| Testen der KI-Gegner                        | L             | Review     |

## Tabelle für das Kanban-Board

Hier ist eine vollständige Tabelle, die das Kanban-Board mit den oben genannten Aufgaben und Prioritäten visualisiert:

| **Backlog**                    | **To Do**                                            | **In Bearbeitung**                         | **Review**                         | **Fertig**                        |
| ------------------------------ | ---------------------------------------------------- | ------------------------------------------ | ---------------------------------- | --------------------------------- |
| **Grundlegende Module:**       | **Startmenü:** implementieren (H)                    | **Spielfeldverwaltung:** aktualisieren (M) | **Spielmechanik:** Überprüfung (M) | **Startmenü:** erstellt           |
| - KI-Gegner implementieren (L) | - GUI-Design des Startmenüs (H)                      | - Spielfeld aktualisieren (M)              | - Spielmechanik testen (M)         | **Spielfeldverwaltung:** erstellt |
| **Erweiterte Module:**         | **Eingabeverwaltung:** Funktionen implementieren (M) | **Spielmechanik:** Spielerwechsel (H)      | **Highscore-System:** testen (M)   | **Spielmechanik:** implementiert  |
| - Highscore-System planen      | **Spielmechanik:** Grundlogik entwickeln (H)         |                                            |                                    | **Dokumentation:** aktualisiert   |
| **Fortgeschrittene Module:**   | **Highscore-System:** speichern (M)                  |                                            |                                    |                                   |
|                                | **Highscore-System:** anzeigen (M)                   |                                            |                                    |                                   |
|                                | **Dokumentation:** Spielanleitung erstellen (L)      |                                            |                                    |                                   |
|                                | **Dokumentation:** Bedienungsanleitung erweitern (L) |                                            |                                    |                                   |

## Priorisierung von Aufgaben nach Wichtigkeit und Dringlichkeit

Um sicherzustellen, dass die wichtigsten und dringendsten Aufgaben zuerst erledigt werden, nutzen wir die **Eisenhower-Matrix**:

| **Priorität**   | **Beschreibung**                               | **Beispielaufgaben**                                                                                                                                  |
| --------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hoch (H)**    | Wichtig und dringend                           | Startmenü implementieren, Spielfeldverwaltung aktualisieren, Spielmechanik Grundlogik entwickeln, Spielerwechsel implementieren                       |
| **Mittel (M)**  | Wichtig, aber nicht dringend                   | Eingabeverwaltung Funktionen implementieren, Spielfeld aktualisieren, Spielmechanik Überprüfung, Highscore-System entwickeln, Dokumentation erweitern |
| **Niedrig (L)** | Nicht wichtig, aber interessant oder umgekehrt | Dokumentation erstellen, KI-Gegner implementieren                                                                                                     |

## Begrenzung der gleichzeitigen Aufgaben (WIP-Limit)

Um die Effizienz zu steigern und Überlastung zu vermeiden, begrenzen wir die Anzahl der Aufgaben in der **"In Bearbeitung"**-Spalte auf maximal **2 Aufgaben**.

### **Implementierung des WIP-Limits:**

- **WIP-Limit:** 2 Aufgaben gleichzeitig in **"In Bearbeitung"**
  
  | **Spalte**         | **WIP-Limit** |
  | ------------------ | ------------- |
  | Backlog            | Unbegrenzt    |
  | To Do              | Unbegrenzt    |
  | **In Bearbeitung** | **2**         |
  | Review             | Unbegrenzt    |
  | Fertig             | Unbegrenzt    |

- **Regel:** Bevor eine neue Aufgabe in die **"In Bearbeitung"**-Spalte verschoben wird, stellen Sie sicher, dass das WIP-Limit nicht überschritten wird. Falls das Limit erreicht ist, schließen Sie eine bestehende Aufgabe ab, bevor Sie eine neue starten.

## Einrichtung des Kanban-Boards in Trello (Beispiel)

**Schritte:**

1. **Erstellen Sie ein neues Board:**
   - Loggen Sie sich in [Trello](https://trello.com/) ein.
   - Klicken Sie auf **„Create new board“** und benennen Sie es z.B. **„Tic-Tac-Toe Projekt“**.

2. **Fügen Sie die Spalten hinzu:**
   - **Backlog**
   - **To Do**
   - **In Bearbeitung**
   - **Review**
   - **Fertig**

3. **Erstellen Sie Karten für jede Aufgabe:**
   - Klicken Sie auf **„Add a card“** unter der entsprechenden Spalte.
   - Benennen Sie die Karten entsprechend den Aufgaben, z.B. **„Startmenü: GUI-Design implementieren (H)“**.

4. **Markieren Sie die Prioritäten:**
   - Verwenden Sie **Labels** in Trello, um die Prioritäten **H (Rot)**, **M (Gelb)** und **L (Grün)** zu kennzeichnen.

5. **Setzen Sie WIP-Limits:**
   - Trello unterstützt keine nativen WIP-Limits, aber Sie können eine **Power-Up** wie **Kanban WIP Limit** hinzufügen oder die Anzahl der Karten in der **"In Bearbeitung"**-Spalte manuell kontrollieren.

6. **Verwenden Sie Checklisten und Fälligkeitsdaten:**
   - Fügen Sie Checklisten zu den Karten hinzu, um Teilaufgaben zu verfolgen.
   - Setzen Sie Fälligkeitsdaten, um den Zeitrahmen für die Aufgaben zu verwalten.

## Karte in Trello

**Karte:**

- **Titel:** `feat(start-menu): implementiere Startmenü mit Tkinter`
- **Label:** `H` (Rot)
- **Beschreibung:**
  ```
  - Erstelle Startmenü mit Optionen für neues Spiel, Anleitung und Beenden
  - Implementiere Spielmodus-Auswahl (Einzelspieler, Mehrspieler)
  - Füge Event-Handling für Buttons hinzu
  ```
- **Checkliste:**
  - [ ] GUI-Design des Startmenüs
  - [ ] Buttons hinzufügen
  - [ ] Event-Handling implementieren
  - [ ] Spielmodus-Auswahl implementieren
  - [ ] Testen des Startmenüs

## Zusammenfassung

Ein gut strukturiertes **Kanban-Board** unterstützt Sie dabei, den Überblick über die verschiedenen Aufgaben in Ihrem **Tic-Tac-Toe**-Projekt zu behalten und den Fortschritt effizient zu verfolgen. Durch die Priorisierung von Aufgaben nach Wichtigkeit und Dringlichkeit sowie die Implementierung von WIP-Limits stellen Sie sicher, dass Sie fokussiert und produktiv arbeiten. Nutzen Sie Tools wie **Trello** oder andere Kanban-Tools, um Ihre Aufgaben visuell zu organisieren und den Entwicklungsprozess zu optimieren.
