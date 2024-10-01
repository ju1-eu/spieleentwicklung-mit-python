---
title: "Beschreibung-main"
author: "Jan Unger"
date: "2024-10-01"
---

# Zusammenfassung Tic-Tac-Toe

Das vorliegende Tic-Tac-Toe-Spiel ist eine Python-Anwendung, die mithilfe der Tkinter-Bibliothek eine grafische Benutzeroberfläche implementiert. Die Hauptklasse TicTacToeApp orchestriert das gesamte Spielgeschehen.

Beim Start präsentiert das Programm ein Startmenü mit den Optionen "Neues Spiel starten" und "Beenden". Wählt der Benutzer ein neues Spiel, wird ein 3x3-Spielfeld aus Buttons generiert. Spieler X beginnt, gefolgt von Spieler O, die abwechselnd ihre Züge machen.

Die Spiellogik überprüft nach jedem Zug, ob ein Spieler gewonnen hat oder ob ein Unentschieden vorliegt. Dazu werden Reihen, Spalten und Diagonalen des Spielfelds analysiert. Bei einem Sieg oder Unentschieden wird eine Benachrichtigung angezeigt, und das Spiel kehrt zum Startmenü zurück.

Die Anwendung nutzt objektorientierte Programmierung, um den Code strukturiert und wartbar zu halten. Methoden wie create_start_menu(), create_game_board(), make_move(), check_winner() und is_board_full() kapseln verschiedene Aspekte des Spiels.

Besonderes Augenmerk wurde auf die Benutzerfreundlichkeit gelegt, mit klaren Anweisungen und einer intuitiven Oberfläche. Die Möglichkeit, jederzeit zum Hauptmenü zurückzukehren, erhöht die Flexibilität für den Benutzer.

## Struktogramm (Flussdiagramm)

```
┌─ Programm Start
│
├─ TicTacToeApp Klasse initialisieren
│  │
│  ├─ Hauptfenster erstellen
│  │
│  └─ create_start_menu() aufrufen
│     │
│     ├─ Startmenü anzeigen
│     │  │
│     │  ├─ "Neues Spiel starten" Button
│     │  │   └─ Bei Klick: start_game() aufrufen
│     │  │
│     │  └─ "Beenden" Button
│     │      └─ Bei Klick: Programm beenden
│     │
│     └─ Warten auf Benutzeraktion
│
├─ start_game()
│  │
│  └─ create_game_board() aufrufen
│     │
│     ├─ Spielbrett erstellen
│     │
│     └─ Auf Spielerzüge warten
│        │
│        └─ Bei Klick auf Feld: make_move() aufrufen
│           │
│           ├─ Zug ausführen
│           │
│           ├─ Gewinner überprüfen (check_winner())
│           │  │
│           │  └─ Falls Gewinner: Spiel beenden und zum Startmenü zurückkehren
│           │
│           ├─ Unentschieden überprüfen (is_board_full())
│           │  │
│           │  └─ Falls unentschieden: Spiel beenden und zum Startmenü zurückkehren
│           │
│           └─ Spieler wechseln
│
└─ Programm Ende (wenn Benutzer "Beenden" wählt)
```

## MindMap

```
Tic-Tac-Toe Spiel
│
├─ TicTacToeApp Klasse
│  │
│  ├─ Attribute
│  │  ├─ root (Hauptfenster)
│  │  ├─ current_player
│  │  ├─ board (Spielfeld)
│  │  └─ buttons (GUI-Elemente)
│  │
│  └─ Methoden
│     ├─ __init__
│     ├─ create_start_menu
│     ├─ start_game
│     ├─ create_game_board
│     ├─ make_move
│     ├─ check_winner
│     └─ is_board_full
│
├─ Benutzeroberfläche
│  │
│  ├─ Startmenü
│  │  ├─ Titel
│  │  ├─ "Neues Spiel starten" Button
│  │  └─ "Beenden" Button
│  │
│  └─ Spielbrett
│     ├─ 3x3 Button-Grid
│     └─ "Zurück zum Hauptmenü" Button
│
└─ Spiellogik
   │
   ├─ Spielerzüge verarbeiten
   ├─ Gewinnbedingungen prüfen
   ├─ Unentschieden erkennen
   └─ Spielerwechsel durchführen
```

## Commit-Nachricht im Conventional Commits-Format

```
feat: Grundlegende Struktur und Startmenü für Tic-Tac-Toe-Spiel

- Konfigurierte Python-Umgebung und installierte Abhängigkeiten
- Erstellte Hauptfenster der Anwendung mit Tkinter
- Implementierte TicTacToeApp-Klasse mit Initialisierungsmethode
- Fügte Startmenü mit 'Neues Spiel' und 'Beenden' Optionen hinzu
```

## Visualisierung des Commit-Prozesses:

```
1. Änderungen vorbereiten (Staging)
   ┌────────────────────────────────────┐
   │ $ git add main.py                  │
   └────────────────────────────────────┘

2. Commit erstellen
   ┌────────────────────────────────────┐
   │ $ git commit -m "feat: Grundlegen- │
   │   de Struktur und Startmenü für    │
   │   Tic-Tac-Toe-Spiel                │
   │                                    │
   │   - Konfigurierte Python-Umgebung  │
   │     und installierte Abhängigkeiten│
   │   - Erstellte Hauptfenster der     │
   │     Anwendung mit Tkinter          │
   │   - Implementierte TicTacToeApp-   │
   │     Klasse mit Initialisierungs-   │
   │     methode                        │
   │   - Fügte Startmenü mit 'Neues     │
   │     Spiel' und 'Beenden' Optionen  │
   │     hinzu"                         │
   └────────────────────────────────────┘

3. Überprüfen des Commits
   ┌────────────────────────────────────┐
   │ $ git log -1                       │
   └────────────────────────────────────┘

4. Push zum Remote-Repository (optional)
   ┌────────────────────────────────────┐
   │ $ git push origin main             │
   └────────────────────────────────────┘
```

Erklärung der Commit-Nachricht:

- `feat:` zeigt an, dass es sich um ein neues Feature handelt.
- Die erste Zeile ist eine kurze Zusammenfassung der Änderungen.
- Die folgenden Punkte geben detaillierte Informationen über die vorgenommenen Änderungen.
