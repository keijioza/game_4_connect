import random

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")

def initialize_board():
    return [["_" for _ in range(7)] for _ in range(6)]

def is_valid_move(board, column):
    return board[0][column] == "_"

def make_move(board, column, player):
    for row in range(5, -1, -1):
        if board[row][column] == "_":
            board[row][column] = player
            return

def check_win(board, player):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertical
    for col in range(7):
        for row in range(3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonals
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
            if all(board[row + i][col + 3 - i] == player for i in range(4)):
                return True

    return False

def computer_move(board):
    for col in range(7):
        if is_valid_move(board, col):
            # Try to win
            board_copy = [row[:] for row in board]
            make_move(board_copy, col, "X")
            if check_win(board_copy, "X"):
                return col

    for col in range(7):
        if is_valid_move(board, col):
            # Block the human
            board_copy = [row[:] for row in board]
            make_move(board_copy, col, "O")
            if check_win(board_copy, "O"):
                return col

    # Play a random valid move
    valid_moves = [col for col in range(7) if is_valid_move(board, col)]
    return random.choice(valid_moves)

def play_connect4():
    board = initialize_board()
    human = "O"
    computer = "X"

    while True:
        print_board(board)

        # Human's turn
        while True:
            try:
                column = int(input("Enter your move (0-6): "))
                if 0 <= column <= 6 and is_valid_move(board, column):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        make_move(board, column, human)

        if check_win(board, human):
            print_board(board)
            print("You win!")
            break

        # Computer's turn
        column = computer_move(board)
        make_move(board, column, computer)

        if check_win(board, computer):
            print_board(board)
            print("Computer wins!")
            break

if __name__ == "__main__":
    play_connect4()
