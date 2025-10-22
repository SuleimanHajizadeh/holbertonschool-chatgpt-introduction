#!/usr/bin/python3
def print_board(board):
    """Print the current Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check all win conditions (rows, columns, diagonals)."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_full(board):
    """Check if the board is full (draw)."""
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """Main game function."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Get valid input
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 2.")
            continue

        # Check range
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Row and column must be 0, 1, or 2.")
            continue

        # Check if spot is empty
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the move
        board[row][col] = player

        # Check winner
        if check_winner(board):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            break

        # Check draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()

