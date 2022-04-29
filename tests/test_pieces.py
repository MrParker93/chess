import pytest
from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from board import Board


class TestPiece:
    @pytest.fixture
    def pawn(self):
        p = Pawn(0, 6, white=True)
        yield p

    @pytest.fixture
    def pawn_two(self):
        p = Pawn(1, 6, white=True)
        yield p

    @pytest.fixture
    def pawn_three(self):
        p = Pawn(0, 3, white=True)
        p.has_moved = True
        yield p

    @pytest.fixture
    def rook(self):
        r = Rook(0, 7, white=True)
        yield r

    @pytest.fixture
    def rook_two(self):
        r = Rook(7, 7, white=True)
        yield r

    @pytest.fixture
    def knight(self):
        p = Knight(1, 7, white=True)
        yield p

    @pytest.fixture
    def bishop(self):
        p = Bishop(2, 7, white=True)
        yield p

    @pytest.fixture
    def queen(self):
        p = Queen(3, 7, white=True)
        yield p

    @pytest.fixture
    def king(self):
        p = King(4, 7, white=True)
        yield p

    @pytest.fixture
    def board(self):
        b = Board()
        yield b

    def test_the_pawn_has_correct_symbol_for_notation_and_wP_for_string(self, pawn):
        notation = pawn.notation
        assert notation == ""
        assert str(pawn) == "wP"

    def test_you_can_get_the_current_position_of_pawn(self, pawn):
        assert pawn.get_position() == (0, 6)

    def test_pawn_stores_all_possible_moves_from_current_position_ignoring_other_pieces(
        self, pawn
    ):
        assert pawn.all_possible_moves() == [(0, 5), (0, 4)]

    def test_pawn_shows_all_legal_moves_from_current_position_if_pawn_has_not_moved_yet(
        self, pawn
    ):
        assert pawn.legal_moves() == [(0, 5), (0, 4)]

    def test_pawn_shows_all_legal_moves_from_current_position_if_pawn_has_moved_before(
        self, pawn
    ):
        pawn.has_moved = True
        assert pawn.legal_moves() == [(0, 5)]

    def test_pawn_shows_diagonal_capture_as_legal_move_if_pawn_can_capture_a_piece_from_current_position(
        self, pawn, board
    ):
        board.setup()
        board.board[5][1] = "bP"
        assert board.check_diagonals(pawn.position, board.board) == "RIGHT"
        pawn.can_capture = board.check_diagonals(pawn.position, board.board)
        assert pawn.legal_moves() == [(0, 5), (0, 4), (1, 5)]

    def test_pawn_does_not_show_diagonal_capture_as_legal_move_if_pawn_cannot_capture_a_piece_from_current_position(
        self, pawn, board
    ):
        board.setup()
        board.board[5][1] = "wP"
        assert board.check_diagonals(pawn.position, board.board) == None
        pawn.can_capture = board.check_diagonals(pawn.position, board.board)
        assert pawn.legal_moves() == [(0, 5), (0, 4)]

    def test_pawn_shows_both_diagonal_captures_as_legal_move_if_pawn_can_capture_two_pieces_from_current_position(
        self, pawn_two, board
    ):
        board.setup()
        board.board[5][2] = "bP"
        board.board[5][0] = "bP"
        assert board.check_diagonals(pawn_two.position, board.board) == "BOTH"
        pawn_two.can_capture = board.check_diagonals(pawn_two.position, board.board)
        assert pawn_two.legal_moves() == [(1, 5), (1, 4), (2, 5), (0, 5)]

    def test_pawn_can_execute_en_passant_when_conditions_are_met(
        self, pawn_three, board
    ):
        board.setup()
        en_passant_piece = Pawn(1, 1, white=False)
        board.move(
            en_passant_piece.position, en_passant_piece.legal_moves()[1], board.board
        )
        en_passant_piece.position = en_passant_piece.legal_moves()[1]
        en_passant_piece.has_moved = True
        en_passant_piece.number_of_moves += 1
        board.whites_move = not board.whites_move
        assert board.board[3][1] == str(en_passant_piece)
        assert en_passant_piece.position == (1, 3)
        board.board[3][0] = str(pawn_three)
        assert (
            board.check_en_passant(pawn_three.position, board.board, [en_passant_piece])
            == "RIGHT"
        )
        pawn_three.en_passant = board.check_en_passant(
            pawn_three.position, board.board, [en_passant_piece]
        )
        assert pawn_three.legal_moves() == [(0, 2), (1, 2)]

    def test_rook_can_perfom_castling_when_conditions_are_met(self, rook, king, board):
        board.setup()
        board.remove_piece((1, 7), board.board)
        board.remove_piece((2, 7), board.board)
        board.remove_piece((3, 7), board.board)
        assert board.board[7][1] == ""
        assert board.board[7][2] == ""
        assert board.board[7][3] == ""
        assert (
            board.check_castling(rook.position, board.board, [rook, king])
            == "QUEENSIDE"
        )
        assert (
            board.check_castling(king.position, board.board, [rook, king])
            == "QUEENSIDE"
        )
        rook.castling = board.check_castling(rook.position, board.board, [rook, king])
        king.castling = board.check_castling(king.position, board.board, [rook, king])
        assert rook.legal_moves() == [
            (1, 7),
            (2, 7),
            (3, 7),
            (4, 7),
            (5, 7),
            (6, 7),
            (7, 7),
            (0, 6),
            (0, 5),
            (0, 4),
            (0, 3),
            (0, 2),
            (0, 1),
            (0, 0),
            (3, 7),
        ]
        assert king.legal_moves() == [(5, 7), (3, 7), (4, 6), (5, 6), (3, 6), (2, 7)]

    def test_every_piece_moves_correctly(self, pawn, rook, knight, bishop, queen, king):
        assert pawn.legal_moves() == [(0, 5), (0, 4)]
        assert rook.legal_moves() == [
            (1, 7),
            (2, 7),
            (3, 7),
            (4, 7),
            (5, 7),
            (6, 7),
            (7, 7),
            (0, 6),
            (0, 5),
            (0, 4),
            (0, 3),
            (0, 2),
            (0, 1),
            (0, 0),
        ]
        assert knight.legal_moves() == [(2, 5), (3, 6), (0, 5)]
        assert bishop.legal_moves() == [
            (3, 6),
            (4, 5),
            (5, 4),
            (6, 3),
            (7, 2),
            (1, 6),
            (0, 5),
        ]
        assert queen.legal_moves() == [
            (4, 7),
            (5, 7),
            (6, 7),
            (7, 7),
            (2, 7),
            (1, 7),
            (0, 7),
            (3, 6),
            (3, 5),
            (3, 4),
            (3, 3),
            (3, 2),
            (3, 1),
            (3, 0),
            (4, 6),
            (5, 5),
            (6, 4),
            (7, 3),
            (2, 6),
            (1, 5),
            (0, 4),
        ]
        assert king.legal_moves() == [(5, 7), (3, 7), (4, 6), (5, 6), (3, 6)]
