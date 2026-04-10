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
                self.buttons[i][j] = tk.Button(self.window, text="", width=10, height=3,
                                               command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.turn
            self.buttons[row][col].config(text=self.turn)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.turn} wins!")
                self.window.destroy()
            elif all(all(cell != '' for cell in row) for row in self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
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

    def run(self):
        # self.window.mainloop() # Cannot run GUI mainloop in this environment
        pass

if __name__ == "__main__":
    game = TicTacToe()
    # game.run() 
