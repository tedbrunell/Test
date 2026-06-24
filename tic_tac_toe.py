import random

def print_board(board):
    print("\n")
    for row in board:
        print("|" + "|".join(row) + "|")
        print("-------")
    print("\n")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    print("Welcome to Tic-Tac-Toe against the Computer!")
    
    while True:
        print_board(board)
        
        if player == "X":
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if board[row][col] != " ":
                    print("Cell occupied!")
                    continue
            except (ValueError, IndexError):
                print("Invalid input!")
                continue
        else:
            print("Computer is thinking...")
            row, col = get_computer_move(board)
            
        board[row][col] = player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
            
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play()
