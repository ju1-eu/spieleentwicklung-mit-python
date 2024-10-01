---
title: "Implementierung-Logik-Tic-Tac-Toe"
author: "Jan Unger"
date: "2024-10-01"
---

# Implementierung der Programmlogik und Testung

bearbeitet am 29. September 2024

- [Implementierung der Programmlogik und Testung](#implementierung-der-programmlogik-und-testung)
  - [Schritt 1: Einrichtung der Entwicklungsumgebung](#schritt-1-einrichtung-der-entwicklungsumgebung)
  - [Schritt 2: Implementierung des Grundgerüsts in main.py](#schritt-2-implementierung-des-grundgerüsts-in-mainpy)
  - [Schritt 3: Entwicklung des Startmenüs](#schritt-3-entwicklung-des-startmenüs)
  - [Schritt 4: Erstellung des Spielfelds](#schritt-4-erstellung-des-spielfelds)
  - [Schritt 5: Implementierung der Spielmechanik](#schritt-5-implementierung-der-spielmechanik)
  - [Schritt 6: Schreiben von Unit-Tests](#schritt-6-schreiben-von-unit-tests)
  - [Schritt 7: Erweiterung der Benutzeroberfläche](#schritt-7-erweiterung-der-benutzeroberfläche)
  - [Schritt 8: Implementierung der Fehlerbehandlung](#schritt-8-implementierung-der-fehlerbehandlung)
  - [Schritt 9: Dokumentation ergänzen](#schritt-9-dokumentation-ergänzen)
  - [Schritt 10: Implementierung des KI-Gegners](#schritt-10-implementierung-des-ki-gegners)
  - [Schritt 11: Abschließende Tests und Qualitätssicherung](#schritt-11-abschließende-tests-und-qualitätssicherung)
  - [Abschluss](#abschluss)
    - [Weiterführende Schritte](#weiterführende-schritte)

## Schritt 1: Einrichtung der Entwicklungsumgebung

**Ziele**

- Sicherstellen, dass die Python-Umgebung korrekt eingerichtet ist.
- Installation aller erforderlichen Bibliotheken und Abhängigkeiten.

---

**Aktionen**

1. **Überprüfen der Python-Installation**

   Zunächst ist zu prüfen, ob Python in der Version 3.x auf dem System installiert ist.

   ```bash
   python --version
   ```

   Sollte Python nicht installiert sein oder eine ältere Version anzeigen, kann die aktuelle Version von der offiziellen [Python-Website](https://www.python.org/downloads/) heruntergeladen und installiert werden.

2. **Einrichtung einer Conda-Umgebung**

   Es wird empfohlen, eine virtuelle Umgebung mit Conda zu erstellen, um Abhängigkeiten sauber zu verwalten.

   - **Conda installieren**: Falls noch nicht vorhanden, kann Anaconda oder Miniconda von der [Anaconda-Website](https://www.anaconda.com/products/individual) heruntergeladen werden.

   - **Conda-Kanäle konfigurieren**

     ```bash
     conda config --add channels conda-forge
     conda config --set channel_priority strict
     ```

   - **Erstellen oder Aktualisieren der Umgebung**

     ```bash
     # Erstmalige Erstellung
     conda env create -f environment.yml

     # Aktualisierung der Umgebung
     conda env update --file environment.yml --prune
     ```

     *Hinweis:* Die Datei `environment.yml` sollte sich im Hauptverzeichnis des Projekts befinden und alle erforderlichen Pakete auflisten.

   - **Aktivieren der Umgebung**

     ```bash
     conda activate meinenv
     ```

     *Hinweis:* Ersetzen Sie `meinenv` durch den tatsächlichen Namen der Umgebung, wie er in `environment.yml` definiert ist.

3. **Überprüfung der Abhängigkeiten**

   - **Inhalt der `environment.yml` überprüfen**

     Stellen Sie sicher, dass alle benötigten Bibliotheken wie `tkinter`, `unittest`, `pygame` usw. in der `environment.yml` aufgeführt sind. Ein Beispielinhalt könnte wie folgt aussehen:

     ```yaml
     name: meinenv
     channels:
       - defaults
       - conda-forge
     dependencies:
       - python=3.x
       - tkinter
       - pytest
       - pygame
       - jupyterlab
       - pip
       - pip:
         - some_additional_package
     ```

   - **Installieren der Pakete mit `pip` (falls erforderlich)**

     Falls bestimmte Pakete nicht über Conda verfügbar sind, können diese mit `pip` installiert werden:

     ```bash
     pip install -r requirements.txt
     ```

     *Hinweis:* Die Datei `requirements.txt` sollte alle zusätzlichen Python-Pakete enthalten, die nicht in `environment.yml` aufgelistet sind.

4. **Überprüfung der Installation von `pygame`**

   ```bash
   pip show pygame
   ```

   Falls `pygame` nicht installiert ist, kann es mit folgendem Befehl installiert werden:

   ```bash
   pip install pygame
   ```

5. **Überprüfung der Installation von `pytorch` (falls erforderlich)**

   ```bash
   conda list pytorch
   ```

   Wenn das Projekt `pytorch` verwendet, sollte es in der Liste erscheinen. Ansonsten kann es wie folgt installiert werden:

   ```bash
   conda install pytorch torchvision torchaudio -c pytorch
   ```

6. **Starten von Jupyter Lab oder Ausführen eines Python-Skripts**

   - **Starten von Jupyter Lab**

     ```bash
     jupyter lab
     ```

     Dies öffnet Jupyter Lab im Browser, wo Notebooks erstellt und bearbeitet werden können.

   - **Ausführen eines Python-Skripts**

     ```bash
     python ./src/test_installation.py
     ```

     *Hinweis:* Das Skript `test_installation.py` sollte ein einfaches Programm sein, das die erfolgreiche Installation der Pakete testet.

7. **Konvertieren von Jupyter Notebooks in Python-Skripte**

   Falls die Installation mit einem Jupyter Notebook getestet wurde, kann dieses in ein Python-Skript konvertiert werden:

   ```bash
   jupyter nbconvert --to python src/test_installation.ipynb
   ```

8. **Deaktivieren der Conda-Umgebung**

   Nach Abschluss der Arbeiten kann die Umgebung wie folgt deaktiviert werden:

   ```bash
   conda deactivate
   ```

---

**Tests**

- **Ausführen eines einfachen Python-Skripts**

  Erstellen Sie ein einfaches Python-Skript, um die Installation zu überprüfen:

  ```python
  # src/test_installation.py
  import sys
  import tkinter
  import pygame

  print("Python-Version:", sys.version)
  print("tkinter-Version:", tkinter.TkVersion)
  print("pygame-Version:", pygame.ver)

  root = tkinter.Tk()
  root.title("Testfenster")
  root.mainloop()
  ```

  Führen Sie das Skript aus:

  ```bash
  python ./src/test_installation.py
  ```

  **Erwartetes Ergebnis:**

  - Ausgabe der Versionen von Python, tkinter und pygame in der Konsole.
  - Öffnen eines einfachen Fensters mit dem Titel "Testfenster".

**Erstellung des Git-Repositories und erster Commit**

1. **Erstellen der `README.md`-Datei**

   ```bash
   echo "# Spieleentwicklung mit Python" > README.md
   ```

2. **Initialisieren des Git-Repositories**

   ```bash
   git init
   ```

3. **Hinzufügen der Dateien zum Repository**

   ```bash
   git add README.md
   git add .gitignore
   git add environment.yml
   git add requirements.txt
   ```

   *Hinweis:* Fügen Sie weitere relevante Dateien hinzu.

4. **Durchführen des ersten Commits**

   ```bash
   git commit -m "Initialer Commit: Einrichtung der Projektstruktur und Entwicklungsumgebung"
   ```

---

**Verbindung mit GitHub und Push zum Remote-Repository**

1. **Umbenennen des Hauptbranches (optional, falls noch nicht geschehen)**

   ```bash
   git branch -M main
   ```

2. **Hinzufügen des Remote-Repositorys**

   ```bash
   git remote add origin git@github.com:ju1-eu/spieleentwicklung-mit-python.git
   ```

   *Hinweis:* Stellen Sie sicher, dass die SSH-Schlüssel korrekt eingerichtet sind, um eine Verbindung zu GitHub herzustellen.

3. **Push zum Remote-Repository**

   ```bash
   git push -u origin main
   ```

---

**Versionierung mit Git-Tags**

1. **Erstellen eines Tags für Version 1.0**

   ```bash
   git tag -a v1.0 -m "Version 1.0: Initiale Veröffentlichung"
   ```

2. **Push des Tags zum Remote-Repository**

   ```bash
   git push origin v1.0
   ```

---

**Nutzung von Git und GitHub für die Zusammenarbeit**

**a) Branching-Strategie**

1. **Erstellen eines neuen Feature-Branches**

   ```bash
   git checkout -b feature/neues-feature
   ```

2. **Arbeiten am neuen Feature**

   - Änderungen vornehmen und Dateien bearbeiten.

3. **Änderungen zum Commit hinzufügen**

   ```bash
   git add .
   ```

4. **Commit der Änderungen**

   ```bash
   git commit -m "Implementierung des neuen Features"
   ```

5. **Push des Feature-Branches zum Remote-Repository**

   ```bash
   git push -u origin feature/neues-feature
   ```

**b) Erstellen eines Pull Requests auf GitHub**

1. Gehen Sie zum Repository auf GitHub.

2. Klicken Sie auf den Button **"Compare & pull request"** für den neuen Branch.

3. Fügen Sie eine aussagekräftige Beschreibung hinzu und klicken Sie auf **"Create pull request"**.

4. Nach der Überprüfung kann der Pull Request in den `main`-Branch gemerged werden.

---

**Zusätzliche Hinweise**

- **.gitignore-Datei verwenden**

  Erstellen Sie eine `.gitignore`-Datei, um unnötige oder sensible Dateien vom Tracking auszuschließen. Beispielinhalt:

  ```
  __pycache__/
  *.pyc
  .vscode/
  .idea/
  env/
  ```

- **Regelmäßige Commits**

  Führen Sie häufig Commits durch, um den Fortschritt festzuhalten und die Nachverfolgbarkeit zu gewährleisten.

- **Dokumentation aktualisieren**

  Halten Sie die `README.md` und weitere Dokumentationsdateien aktuell, um den Projektstatus und wichtige Informationen festzuhalten.


## Schritt 2: Implementierung des Grundgerüsts in main.py

**Ziele:**

- Erstellung des Hauptfensters der Anwendung.
- Initialisierung der Hauptklasse.

**Aktionen:**

- Navigieren zu `./src/Anfänger/Tic-Tac-Toe/`.
- Öffnen der Datei `main.py`.
- Importieren der notwendigen Module:

  ```python
  import tkinter as tk
  from tkinter import messagebox
  ```

- Definieren der Hauptklasse `TicTacToeApp`:

  ```python
  class TicTacToeApp:
      def __init__(self, root):
          self.root = root
          self.root.title("Tic-Tac-Toe")
          self.root.geometry("400x400")
          self.current_player = "X"
          self.board = [["" for _ in range(3)] for _ in range(3)]
          self.create_start_menu()
  ```

- Implementieren der Methode `create_start_menu()` (Platzhalter für den Moment).

- Starten der Anwendung:

  ```python
  if __name__ == "__main__":
      root = tk.Tk()
      app = TicTacToeApp(root)
      root.mainloop()
  ```

**Tests:**

- Ausführen von `main.py` und Überprüfen, ob ein Fenster mit dem Titel "Tic-Tac-Toe" erscheint.

## Schritt 3: Entwicklung des Startmenüs

**Ziele:**

- Anzeige eines Startmenüs mit Optionen.

**Aktionen:**

- Implementieren der Methode `create_start_menu()`:

  ```python
  def create_start_menu(self):
      # Löschen aller Widgets
      for widget in self.root.winfo_children():
          widget.destroy()
      # Titel hinzufügen
      title = tk.Label(self.root, text="Tic-Tac-Toe", font=("Helvetica", 24))
      title.pack(pady=20)
      # Buttons hinzufügen
      start_button = tk.Button(self.root, text="Neues Spiel starten", command=self.start_game)
      start_button.pack(pady=10)
      exit_button = tk.Button(self.root, text="Beenden", command=self.root.quit)
      exit_button.pack(pady=10)
  ```

- Implementieren der Methode `start_game()` als Platzhalter:

  ```python
  def start_game(self):
      self.create_game_board()
  ```

**Tests:**

- Ausführen der Anwendung und Klicken auf "Neues Spiel starten", um sicherzustellen, dass keine Fehler auftreten.

## Schritt 4: Erstellung des Spielfelds

**Ziele:**

- Darstellung des 3x3-Spielfelds.
- Vorbereitung für die Spielerinteraktionen.

**Aktionen:**

- Implementieren der Methode `create_game_board()`:

  ```python
  def create_game_board(self):
      # Löschen aller Widgets
      for widget in self.root.winfo_children():
          widget.destroy()
      # Spielfeld erstellen
      self.buttons = []
      for row in range(3):
          button_row = []
          for col in range(3):
              button = tk.Button(self.root, text="", font=("Helvetica", 32), width=5, height=2,
                                 command=lambda r=row, c=col: self.make_move(r, c))
              button.grid(row=row, column=col)
              button_row.append(button)
          self.buttons.append(button_row)
  ```

- Implementieren der Methode `make_move()` als Platzhalter:

  ```python
  def make_move(self, row, col):
      pass
  ```

**Tests:**

- Starten des Spiels und Überprüfen, ob das Spielfeld korrekt angezeigt wird.
- Klicken auf verschiedene Felder, um sicherzustellen, dass keine Fehler auftreten.

## Schritt 5: Implementierung der Spielmechanik

**Ziele:**

- Verarbeitung der Spielerzüge.
- Aktualisierung des Spielfelds.
- Überprüfung der Siegbedingungen.

**Aktionen:**

- Aktualisieren der Methode `make_move()`:

  ```python
  def make_move(self, row, col):
      if self.board[row][col] == "":
          self.board[row][col] = self.current_player
          self.buttons[row][col].config(text=self.current_player)
          if self.check_winner(self.current_player):
              messagebox.showinfo("Spiel beendet", f"Spieler {self.current_player} hat gewonnen!")
              self.reset_game()
          elif self.is_draw():
              messagebox.showinfo("Spiel beendet", "Unentschieden!")
              self.reset_game()
          else:
              self.switch_player()
  ```

- Implementieren der Methode `switch_player()`:

  ```python
  def switch_player(self):
      self.current_player = "O" if self.current_player == "X" else "X"
  ```

- Implementieren der Methode `check_winner(player)`:

  ```python
  def check_winner(self, player):
      # Reihen prüfen
      for row in self.board:
          if all(cell == player for cell in row):
              return True
      # Spalten prüfen
      for col in range(3):
          if all(self.board[row][col] == player for row in range(3)):
              return True
      # Diagonalen prüfen
      if all(self.board[i][i] == player for i in range(3)):
          return True
      if all(self.board[i][2 - i] == player for i in range(3)):
              return True
      return False
  ```

- Implementieren der Methode `is_draw()`:

  ```python
  def is_draw(self):
      return all(self.board[row][col] != "" for row in range(3) for col in range(3))
  ```

- Implementieren der Methode `reset_game()`:

  ```python
  def reset_game(self):
      self.current_player = "X"
      self.board = [["" for _ in range(3)] for _ in range(3)]
      self.create_game_board()
  ```

**Tests:**

- Spielen eines vollständigen Spiels und Überprüfen, ob Sieg- und Unentschieden-Bedingungen korrekt erkannt werden.
- Testen aller möglichen Siegkombinationen (horizontal, vertikal, diagonal).

## Schritt 6: Schreiben von Unit-Tests

**Ziele:**

- Sicherstellung der korrekten Funktion der Methoden.
- Automatisierte Tests für zukünftige Änderungen.

**Aktionen:**

- Erstellen der Testdatei `test_tictactoe.py` im Verzeichnis `./src/Anfänger/Tic-Tac-Toe/tests/`.
- Importieren des Moduls `unittest` und der Hauptklasse:

  ```python
  import unittest
  from main import TicTacToeApp
  import tkinter as tk
  ```

- Schreiben von Testfällen:

  ```python
  class TestTicTacToe(unittest.TestCase):
      def setUp(self):
          self.root = tk.Tk()
          self.game = TicTacToeApp(self.root)
          self.game.board = [
              ["X", "X", "X"],
              ["", "", ""],
              ["", "", ""]
          ]

      def test_check_winner(self):
          self.assertTrue(self.game.check_winner("X"))

      def test_no_winner(self):
          self.game.board = [
              ["X", "O", "X"],
              ["O", "O", "X"],
              ["X", "X", "O"]
          ]
          self.assertFalse(self.game.check_winner("X"))

      def tearDown(self):
          self.root.destroy()

  if __name__ == '__main__':
      unittest.main()
  ```

**Tests:**

- Ausführen der Tests:

  ```bash
  python test_tictactoe.py
  ```

- Sicherstellen, dass alle Tests erfolgreich sind.

## Schritt 7: Erweiterung der Benutzeroberfläche

**Ziele:**

- Verbesserung der Benutzererfahrung.
- Hinzufügen von Farben und Schriftarten.

**Aktionen:**

- Anpassen der Buttons in `create_game_board()`:

  ```python
  def create_game_board(self):
      # ... vorheriger Code ...
      for row in range(3):
          button_row = []
          for col in range(3):
              button = tk.Button(self.root, text="", font=("Helvetica", 32), width=5, height=2,
                                 command=lambda r=row, c=col: self.make_move(r, c),
                                 bg="lightblue")
              button.grid(row=row, column=col)
              button_row.append(button)
      # ... restlicher Code ...
  ```

- Ändern der Farbe der Buttons nach jedem Zug:

  ```python
  def make_move(self, row, col):
      # ... vorheriger Code ...
      self.buttons[row][col].config(text=self.current_player, state="disabled",
                                    disabledforeground="black")
      # ... restlicher Code ...
  ```

**Tests:**

- Visuelle Überprüfung der GUI.
- Sicherstellen, dass die Buttons korrekt aktualisiert werden.

## Schritt 8: Implementierung der Fehlerbehandlung

**Ziele:**

- Verbesserung der Robustheit des Programms.
- Verhindern von unerwarteten Abstürzen.

**Aktionen:**

- Anpassen der Methode `make_move()`:

  ```python
  def make_move(self, row, col):
      try:
          if self.board[row][col] == "":
              # ... vorheriger Code ...
          else:
              messagebox.showwarning("Ungültiger Zug", "Dieses Feld ist bereits belegt.")
      except Exception as e:
          messagebox.showerror("Fehler", f"Ein unerwarteter Fehler ist aufgetreten: {e}")
  ```

**Tests:**

- Versuchen, auf bereits belegte Felder zu klicken.
- Überprüfen, ob entsprechende Warnungen angezeigt werden.

## Schritt 9: Dokumentation ergänzen

**Ziele:**

- Verbesserung der Verständlichkeit des Codes.
- Bereitstellung von Hilfestellungen für zukünftige Entwickler.

**Aktionen:**

- Hinzufügen von Docstrings zu allen Methoden.
- Beispiel:

  ```python
  def check_winner(self, player):
      """
      Überprüft, ob der angegebene Spieler gewonnen hat.

      Parameter:
      player (str): Der Spieler, "X" oder "O".

      Rückgabewert:
      bool: True, wenn der Spieler gewonnen hat, sonst False.
      """
      # ... restlicher Code ...
  ```

- Aktualisieren der README-Datei in `./README.md` mit Anweisungen zur Ausführung des Spiels.

**Tests:**

- Durchlesen des Codes und Sicherstellen, dass die Kommentare und Docstrings verständlich sind.

## Schritt 10: Implementierung des KI-Gegners

**Ziele:**

- Einführung eines KI-Gegners.
- Anwendung von Algorithmen zur Entscheidungsfindung.

**Aktionen:**

- Hinzufügen einer Auswahlmöglichkeit für den Spielmodus im Startmenü:

  ```python
  def create_start_menu(self):
      # ... vorheriger Code ...
      mode_label = tk.Label(self.root, text="Spielmodus auswählen:")
      mode_label.pack()
      single_player_button = tk.Button(self.root, text="Einzelspieler", command=lambda: self.start_game(ai=True))
      single_player_button.pack()
      multi_player_button = tk.Button(self.root, text="Mehrspieler", command=lambda: self.start_game(ai=False))
      multi_player_button.pack()
      # ... restlicher Code ...
  ```

- Anpassen der Methode `start_game()`:

  ```python
  def start_game(self, ai=False):
      self.ai = ai
      self.create_game_board()
  ```

- Implementieren der Methode `computer_move()`:

  ```python
  import random

  def computer_move(self):
      empty_cells = [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == ""]
      if empty_cells:
          row, col = random.choice(empty_cells)
          self.board[row][col] = self.current_player
          self.buttons[row][col].config(text=self.current_player, state="disabled",
                                        disabledforeground="black")
          if self.check_winner(self.current_player):
              messagebox.showinfo("Spiel beendet", f"Spieler {self.current_player} hat gewonnen!")
              self.reset_game()
          elif self.is_draw():
              messagebox.showinfo("Spiel beendet", "Unentschieden!")
              self.reset_game()
          else:
              self.switch_player()
  ```

- Anpassen der Methode `make_move()`:

  ```python
  def make_move(self, row, col):
      # ... vorheriger Code ...
      else:
          self.switch_player()
          if self.ai and self.current_player == "O":
              self.computer_move()
  ```

**Tests:**

- Spielen gegen den KI-Gegner und Überprüfen, ob die Züge korrekt verarbeitet werden.
- Sicherstellen, dass das Spiel bei Sieg oder Unentschieden korrekt endet.

## Schritt 11: Abschließende Tests und Qualitätssicherung

**Ziele:**

- Sicherstellen, dass alle Funktionen wie erwartet arbeiten.
- Identifizieren und Beheben von verbleibenden Fehlern.

**Aktionen:**

- Durchführen umfangreicher Tests für beide Spielmodi.
- Überprüfen der Tests in `test_tictactoe.py` und Hinzufügen weiterer Testfälle für die KI.

**Tests:**

- Manuelles Testen aller Spielabläufe.
- Ausführen aller Unit-Tests und Sicherstellen, dass sie erfolgreich sind.

## Abschluss

Durch die schrittweise Implementierung und gründliche Testung jeder Komponente haben Sie ein funktionales und robustes Tic-Tac-Toe-Spiel entwickelt. Die Verwendung der vorhandenen Projektstruktur erleichtert die Organisation des Codes und ermöglicht eine einfache Erweiterung des Projekts in der Zukunft.

### Weiterführende Schritte

- **Erweiterung des KI-Gegners**: Implementierung des Minimax-Algorithmus für einen stärkeren Gegner.
- **Grafische Verbesserungen**: Hinzufügen von Bildern und Sounds aus dem `assets`-Ordner.
- **Highscore-System**: Speicherung der Spielergebnisse in einer Datei oder Datenbank.
- **Dokumentation**: Ergänzung der Entwicklerdokumentation in `./docs/Entwicklerdokumentation`.

**Hinweis**: Denken Sie daran, bei jeder Erweiterung gründlich zu testen und die Dokumentation entsprechend zu aktualisieren.
