---
title: "Benutzerhandbuch"
author: "Jan Unger"
date: "2024-10-01"
---

# Entwicklerdokumentation und Benutzerhandbuch: Tic-Tac-Toe

bearbeitet am 01. Oktober 2024

- [Entwicklerdokumentation und Benutzerhandbuch: Tic-Tac-Toe](#entwicklerdokumentation-und-benutzerhandbuch-tic-tac-toe)
  - [Einleitung](#einleitung)
  - [Projektübersicht](#projektübersicht)
  - [Systemanforderungen](#systemanforderungen)
  - [Projektstruktur](#projektstruktur)
  - [Hauptkomponenten](#hauptkomponenten)
    - [TicTacToeApp Klasse](#tictactoeapp-klasse)
  - [Erweiterungsmöglichkeiten](#erweiterungsmöglichkeiten)
  - [Bekannte Probleme und Einschränkungen](#bekannte-probleme-und-einschränkungen)
  - [Testanweisungen](#testanweisungen)
  - [Benutzerhandbuch](#benutzerhandbuch)
    - [Einführung](#einführung)
    - [Installation](#installation)
    - [Spielstart](#spielstart)
    - [Spielablauf](#spielablauf)
    - [Gewinnbedingungen](#gewinnbedingungen)
    - [Unentschieden](#unentschieden)
    - [Neues Spiel starten](#neues-spiel-starten)
    - [Spiel beenden](#spiel-beenden)
  - [Code-Review](#code-review)

## Einleitung

Diese Dokumentation dient als umfassende Quelle für Entwickler und Benutzer des Tic-Tac-Toe-Spiels. Sie bietet technische Details zur Implementierung sowie eine Anleitung zur Nutzung der Anwendung. Die Dokumentation richtet sich an Personen mit Grundkenntnissen in der Softwareentwicklung, insbesondere im Bereich der objektorientierten Programmierung mit Python.

## Projektübersicht

Dieses Projekt implementiert ein einfaches Tic-Tac-Toe-Spiel mit einer grafischen Benutzeroberfläche. Es nutzt Python als Programmiersprache und Tkinter (Python-Standardbibliothek für grafische Benutzeroberflächen) für die Darstellung.

## Systemanforderungen

- Python 3.x
- Tkinter (in den meisten Python-Standardinstallationen enthalten)

## Projektstruktur

```
tic-tac-toe/
│
├── main.py
├── docs/
│   ├── Entwicklerdokumentation.md
│   └── Benutzerhandbuch.md
└── README.md
```

## Hauptkomponenten

### TicTacToeApp Klasse

Die `TicTacToeApp` Klasse bildet das Herzstück der Anwendung. Sie verwaltet den Spielzustand und die Benutzeroberfläche.

Wichtige Methoden:
- `__init__(self, root)`: Initialisiert die Anwendung
  ```python
  def __init__(self, root):
      self.root = root
      self.root.title("Tic-Tac-Toe")
      self.root.geometry("400x400")
      self.current_player = "X"
      self.board = [["" for _ in range(3)] for _ in range(3)]
      self.create_start_menu()
  ```
- `create_start_menu(self)`: Erstellt das Startmenü
- `create_game_board(self)`: Erstellt das Spielbrett
- `make_move(self, row, col)`: Führt einen Spielzug aus
- `check_winner(self, player)`: Überprüft, ob ein Spieler gewonnen hat
- `is_board_full(self)`: Überprüft, ob das Spielfeld voll ist

Die Klasse nutzt eine 3x3-Matrix (`self.board`) zur Repräsentation des Spielfelds und verwaltet den aktuellen Spieler (`self.current_player`).

## Erweiterungsmöglichkeiten

1. Implementierung eines KI-Gegners
   - Mögliche Umsetzung: Implementierung des Minimax-Algorithmus für optimale Züge
2. Hinzufügen von Spielstatistiken
   - Technischer Ansatz: Erweiterung der `TicTacToeApp`-Klasse um Methoden zur Datenpersistenz
3. Möglichkeit, die Spielfeldgröße zu ändern
   - Implementierungsidee: Parametrisierung der Spielfeldgröße im Konstruktor
4. Implementierung verschiedener Schwierigkeitsgrade
   - Konzept: Erstellung einer `AIPlayer`-Klasse mit verschiedenen Strategien

## Bekannte Probleme und Einschränkungen

- Lokales Spiel: Das Spiel unterstützt derzeit nur lokales Spielen für zwei Spieler. Eine Netzwerkfunktionalität würde eine Client-Server-Architektur erfordern.
- Keine Speicherfunktion: Es gibt keine Möglichkeit, ein laufendes Spiel zu speichern oder zu laden. Dies könnte durch Serialisierung des Spielzustands implementiert werden.

## Testanweisungen

Derzeit sind keine automatisierten Tests implementiert. Manuelle Tests sollten Folgendes abdecken:

1. Starten eines neuen Spiels
   ```python
   app = TicTacToeApp(root)
   app.start_game()
   ```
2. Durchführen gültiger und ungültiger Züge
   ```python
   app.make_move(0, 0)  # Gültiger Zug
   app.make_move(0, 0)  # Ungültiger Zug (Feld bereits besetzt)
   ```
3. Überprüfen von Gewinnbedingungen in allen Richtungen
4. Testen von Unentschieden-Szenarien
5. Überprüfen der Funktionalität des "Zurück zum Hauptmenü" Buttons

## Benutzerhandbuch

### Einführung

Tic-Tac-Toe ist ein klassisches Strategiespiel für zwei Spieler. Es wird auf einem 3x3-Spielfeld gespielt und erfordert logisches Denken und vorausschauendes Planen.

### Installation

1. Sicherstellen der Python 3.x Installation auf dem System
2. Herunterladen der Spieldateien
3. Öffnen eines Terminals/einer Kommandozeile im Spielverzeichnis
4. Ausführen von `python main.py` zum Starten des Spiels

### Spielstart

Nach dem Programmstart erscheint das Hauptmenü mit zwei Optionen:
- "Neues Spiel starten"
- "Beenden"

Ein Klick auf "Neues Spiel starten" beginnt eine neue Partie.

### Spielablauf

1. Das Spiel findet auf einem 3x3 Gitter statt.
2. Spieler X beginnt immer.
3. Spielzüge erfolgen durch Klicken auf ein leeres Feld.
4. Die Spieler wechseln sich ab, bis ein Spieler gewinnt oder ein Unentschieden eintritt.

### Gewinnbedingungen

Ein Spieler gewinnt, wenn er drei seiner Symbole (X oder O) in einer Reihe, Spalte oder Diagonale platziert hat.

### Unentschieden

Ein Unentschieden tritt ein, wenn alle Felder gefüllt sind und kein Spieler gewonnen hat.

### Neues Spiel starten

Nach Spielende kehrt man automatisch zum Hauptmenü zurück. Hier kann ein neues Spiel gestartet oder das Programm beendet werden.

### Spiel beenden

Das Spiel kann jederzeit durch Klicken auf "Beenden" im Hauptmenü oder Schließen des Spielfensters beendet werden.

## Code-Review

Der vorliegende Python-Code implementiert ein Tic-Tac-Toe-Spiel mit grafischer Benutzeroberfläche unter Verwendung der Tkinter-Bibliothek.

Positive Aspekte:

1. Klare Strukturierung: Der Code ist in einer Klasse `TicTacToeApp` organisiert, was eine gute Kapselung der Funktionalität ermöglicht.
2. Dokumentation: Jede Methode ist mit einem Docstring versehen, der die Funktionalität erklärt.
3. Logische Aufteilung: Die Funktionalität ist in separate Methoden unterteilt, was die Lesbarkeit und Wartbarkeit erhöht.
4. Korrekte Implementierung: Die Spiellogik scheint korrekt implementiert zu sein, einschließlich der Überprüfung auf Gewinner und Unentschieden.

Verbesserungsvorschläge:

1. Typhinweise: Es könnten Typhinweise (type hints) hinzugefügt werden, um die Codequalität zu erhöhen und potenzielle Fehler frühzeitig zu erkennen.
2. Konstanten: Wiederholte Werte wie die Spielfeldgröße (3x3) könnten als Klassenkonstanten definiert werden.
3. Fehlerbehandlung: Es fehlt eine explizite Fehlerbehandlung, z.B. für den Fall, dass ein ungültiger Spieler übergeben wird.
4. Testbarkeit: Die Methoden `check_winner` und `is_board_full` könnten statisch sein, um die Testbarkeit zu verbessern.

Beispiele für Verbesserungen:

```python
from typing import List, Optional

class TicTacToeApp:
    BOARD_SIZE = 3
    PLAYERS = ('X', 'O')

    def __init__(self, root: tk.Tk) -> None:
        # ...

    def make_move(self, row: int, col: int) -> None:
        if self.board[row][col] == "" and self.current_player in self.PLAYERS:
            # ...

    @staticmethod
    def check_winner(board: List[List[str]], player: str) -> bool:
        # ...

    @staticmethod
    def is_board_full(board: List[List[str]]) -> bool:
        # ...
```

Insgesamt ist der Code gut strukturiert und implementiert die Grundfunktionalität eines Tic-Tac-Toe-Spiels effektiv.