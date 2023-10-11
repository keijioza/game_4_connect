import unittest
from game_connect4 import (
    initialize_board,
    is_valid_move,
    make_move,
    check_win,
)

class TestConnect4Functions(unittest.TestCase):

    def test_initialize_board(self):
        board = initialize_board()
        self.assertEqual(len(board), 6)
        self.assertEqual(len(board[0]), 7)
        self.assertTrue(all(cell == "_" for row in board for cell in row))

    def test_is_valid_move(self):
        board = initialize_board()
        column = 3 
        result = is_valid_move(board, column)
        self.assertTrue(result) 

    def test_make_move_o(self):
        board = initialize_board()
        make_move(board, 0, "O")
        self.assertEqual(board[5][0], "O")

    def test_make_move_x(self):
        board = initialize_board()
        make_move(board, 0, "X")
        self.assertEqual(board[5][0], "X")

    def test_check_win(self):
        board = initialize_board()
        board[2][0] = "O"
        board[2][1] = "O"
        board[2][2] = "O"
        board[2][3] = "O"
        self.assertTrue(check_win(board, "O"))

        board[2][0] = "X"
        board[2][1] = "X"
        board[2][2] = "X"
        board[2][3] = "X"
        self.assertTrue(check_win(board, "X"))


if __name__ == "__main__":
    unittest.main()
