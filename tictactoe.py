def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ": return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ": return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ": return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ": return board[0][2]
    return None

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    turn = "X"
    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {turn}, enter row (0-2): "))
        col = int(input(f"Player {turn}, enter col (0-2): "))
        if board[row][col] != " ":
            print("Invalid move!")
            continue
        board[row][col] = turn
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {turn} wins!")
            return
        turn = "O" if turn == "X" else "X"
    print("It's a tie!")

if __name__ == "__main__":
    play()
