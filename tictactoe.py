import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [" " for _ in range(9)]
        self.human = "X"
        self.computer = "O"
        self.buttons = []
        for i in range(9):
            btn = tk.Button(root, text=" ", font=('Arial', 20), width=5, height=2,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def on_click(self, index):
        if self.board[index] == " " and not self.check_winner():
            self.board[index] = self.human
            self.buttons[index].config(text=self.human)
            if not self.check_winner() and " " in self.board:
                self.computer_move()
                self.check_winner()

    def _check_win(self, board, player):
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in wins:
            if board[a] == board[b] == board[c] == player:
                return True
        return False

    def computer_move(self):
        # 1. Try to win
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.computer
                if self._check_win(self.board, self.computer):
                    self.buttons[i].config(text=self.computer)
                    return
                self.board[i] = " "

        # 2. Block human
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.human
                if self._check_win(self.board, self.human):
                    self.board[i] = self.computer
                    self.buttons[i].config(text=self.computer)
                    return
                self.board[i] = " "

        # 3. Take center
        if self.board[4] == " ":
            self.board[4] = self.computer
            self.buttons[4].config(text=self.computer)
            return

        # 4. Take random
        available = [i for i, x in enumerate(self.board) if x == " "]
        if available:
            move = random.choice(available)
            self.board[move] = self.computer
            self.buttons[move].config(text=self.computer)

    def check_winner(self):
        if self._check_win(self.board, self.human):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            self.reset_game()
            return True
        if self._check_win(self.board, self.computer):
            messagebox.showinfo("Tic-Tac-Toe", "Computer wins!")
            self.reset_game()
            return True
        if " " not in self.board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            self.reset_game()
            return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for btn in self.buttons:
            btn.config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()