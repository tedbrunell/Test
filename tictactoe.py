import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.turn = 'X'
        self.board = [''] * 9
        self.buttons = []
        
        for i in range(9):
            btn = tk.Button(root, text='', font=('normal', 20), width=5, height=2,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)
            
    def on_click(self, index):
        if self.board[index] == '' and self.turn == 'X':
            self.board[index] = 'X'
            self.buttons[index].config(text='X')
            if self.check_winner('X'):
                messagebox.showinfo("Tic-Tac-Toe", "You win!")
                self.reset()
            elif '' not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset()
            else:
                self.turn = 'O'
                self.computer_move()
                
    def computer_move(self):
        # Very simple AI: picks first available spot
        for i in range(9):
            if self.board[i] == '':
                self.board[i] = 'O'
                self.buttons[i].config(text='O')
                break
        if self.check_winner('O'):
            messagebox.showinfo("Tic-Tac-Toe", "Computer wins!")
            self.reset()
        elif '' not in self.board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            self.reset()
        else:
            self.turn = 'X'
            
    def check_winner(self, player):
        win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] == player:
                return True
        return False
        
    def reset(self):
        self.board = [''] * 9
        self.turn = 'X'
        for btn in self.buttons:
            btn.config(text='')

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
