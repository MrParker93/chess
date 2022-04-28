import pytest
from board import Board


class TestBoard:
    @pytest.fixture
    def board(self):
        b = Board()
        yield b

    def test_board_is_8_by_8(self, board):
        b = board.board
        assert len(b) == 8
        assert len(b[0]) == 8

    def test_board_setup(self, board):
        board.setup()
        assert board.board == [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                               ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                               ["", "", "", "", "", "", "", ""],
                               ["", "", "", "", "", "", "", ""],
                               ["", "", "", "", "", "", "", ""],
                               ["", "", "", "", "", "", "", ""],
                               ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                               ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

    def test_board_changes_turn_after_move(self, board):
        assert board.whites_move == True
        board.move((0, 0), (0, 0))
        assert board.whites_move == False

    def test_board_moves_piece_after_move(self, board):
        board.setup()
        assert board.board[6][0] == "wP"
        board.move((0, 6), (0, 5))
        assert board.board[6][0] == ""
        assert board.board[5][0] == "wP"

    def test_board_moves_piece_only_if_space_is_empty(self, board):
        board.setup()
        board.board[5][0] = "wP"
        board.move((0, 6), (0, 5))
        assert board.board[6][0] == "wP"
        assert board.board[5][0] == "wP"
        board.move((0, 6), (0, 4))
        assert board.board[6][0] == ""
        assert board.board[4][0] == "wP"


    def test_board_moves_pieces_to_capture_enemy_pieces(self, board):
        board.setup()
        board.board[5][0] = "wP"
        board.move((1, 6), (0, 5))
        assert board.board[6][1] == "wP"
        assert board.board[5][0] == "wP"
        board.board[5][0] = "bP"
        board.move((1, 6), (0, 5))
        assert board.board[6][1] == ""
        assert board.board[5][0] == "wP"

    def test_each_move_is_logged(self, board):
        board.setup()
        board.move((1, 6), (1, 5))
        assert board.board[6][1] == ""
        assert board.board[5][1] == "wP"
        assert len(board.history) == 1
        assert board.history[0].start_position == (1, 6)
        assert board.history[0].destination == (1, 5)

    def test_a_move_can_be_undone_with_undo_move(self, board):
        board.setup()
        board.move((1, 6), (1, 5))
        assert board.board[6][1] == ""
        board.undo()
        assert board.board[6][1] == "wP"