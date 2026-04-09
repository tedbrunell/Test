import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.turn = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 20), width=5, height=2,
                                              command=lambda r=i, c=j: self.on_click(r, c))
                self.buttons[i][j].grid(row=i, column=j)

        self.window.mainloop()

    def on_click(self, r, c):
        if self.board[r][c] == '' and not self.check_winner():
            self.board[r][c] = self.turn
            self.buttons[r][c].config(text=self.turn)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.turn} wins!")
                self.window.destroy()
            elif all(self.board[i][j] != '' for i in range(3) for j in range(3)):
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.window.destroy()
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '': return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '': return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '': return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '': return True
        return False

if __name__ == '__main__':
    TicTacToe()
