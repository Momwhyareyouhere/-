# tic_tac_toe.py

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    total_moves = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while total_moves < 9:
        row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
            total_moves += 1
            print_board(board)

            if check_win(board, current_player):
                print(f"Player {current_player} wins!")
                return

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
