import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[tk.Button(root, text=' ', font=('normal', 20), width=5, height=2, command=lambda i=i, j=j: self.click(i, j), bd=5) for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, i, j):
        if self.board[i][j] == ' ':
            self.board[i][j] = self.current_player
            color = 'red' if self.current_player == 'X' else 'blue'
            self.buttons[i][j].config(text=self.current_player, fg=color, state=tk.DISABLED)
            if self.check_winner(i, j):
                messagebox.showinfo("Tic Tac Toe", f"Le joueur {self.current_player} a gagné!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "Match nul!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        # Vérification horizontale
        if all(self.board[row][j] == self.current_player for j in range(3)):
            return True
        # Vérification verticale
        if all(self.board[i][col] == self.current_player for i in range(3)):
            return True
        # Vérification diagonale principale
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        # Vérification diagonale secondaire
        if row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
