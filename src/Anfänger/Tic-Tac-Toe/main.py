import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    """
    Eine Klasse, die ein Tic-Tac-Toe-Spiel mit grafischer Benutzeroberfläche implementiert.
    """

    def __init__(self, root):
        """
        Initialisiert die TicTacToeApp.

        :param root: Das Hauptfenster der Anwendung (Tkinter root)
        """
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x400")
        self.current_player = "X"  # Startspieler ist X
        self.board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 leeres Spielfeld
        self.create_start_menu()

    def create_start_menu(self):
        """Erstellt und zeigt das Startmenü an."""
        # Löschen aller vorhandenen Widgets
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

    def start_game(self):
        """Startet ein neues Spiel."""
        self.create_game_board()

    def create_game_board(self):
        """Erstellt das Spielbrett."""
        # Löschen aller vorhandenen Widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Erstellen des 3x3 Spielbretts
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Helvetica", 20), width=5, height=2,
                                   command=lambda r=i, c=j: self.make_move(r, c))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
        # Button zum Zurückkehren zum Hauptmenü
        back_button = tk.Button(self.root, text="Zurück zum Hauptmenü", command=self.create_start_menu)
        back_button.grid(row=3, column=0, columnspan=3, pady=10)

    def make_move(self, row, col):
        """
        Führt einen Spielzug aus.

        :param row: Zeilenindex des geklickten Feldes
        :param col: Spaltenindex des geklickten Feldes
        """
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Spiel beendet", f"Spieler {self.current_player} hat gewonnen!")
                self.create_start_menu()
            elif self.is_board_full():
                messagebox.showinfo("Spiel beendet", "Unentschieden!")
                self.create_start_menu()
            else:
                # Spielerwechsel
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        """
        Überprüft, ob der aktuelle Spieler gewonnen hat.

        :param player: Der zu überprüfende Spieler ('X' oder 'O')
        :return: True, wenn der Spieler gewonnen hat, sonst False
        """
        # Überprüfen der Reihen und Spalten
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        # Überprüfen der Diagonalen
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        """
        Überprüft, ob das Spielfeld voll ist (Unentschieden).

        :return: True, wenn das Spielfeld voll ist, sonst False
        """
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()