import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe (Human vs Computer)")
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
            # Human move
            self.make_move(r, c, 'X')
            
            if not self.check_winner() and not self.is_board_full():
                # Computer move
                self.computer_move()

    def make_move(self, r, c, player):
        self.board[r][c] = player
        self.buttons[r][c].config(text=player)
        
        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            self.window.destroy()
        elif self.is_board_full():
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            self.window.destroy()

    def computer_move(self):
        # Simple random move for computer
        empty_spots = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == '']
        if empty_spots:
            r, c = random.choice(empty_spots)
            self.make_move(r, c, 'O')

    def is_board_full(self):
        return all(self.board[i][j] != '' for i in range(3) for j in range(3))

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '': return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '': return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '': return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '': return self.board[0][2]
        return None

if __name__ == '__main__':
    TicTacToe()
