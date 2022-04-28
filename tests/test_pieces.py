import pytest
from pieces import Pawn

class TestPiece:
    @pytest.fixture
    def pawn(self):
        Pawn.__abstractmethods__ = set()
        p = Pawn(0, 6, white=True)
        yield p

    @pytest.fixture
    def rook(self):
        r = Rook(0, 7, white=True)
        yield r

    @pytest.fixture
    def knight(self):
        p = Knight(1, 7, white=True)
        yield p

    @pytest.fixture
    def Bishop(self):
        p = bishop(2, 7, white=True)
        yield p

    @pytest.fixture
    def Queen(self):
        p = queen(3, 7, white=True)
        yield p

    @pytest.fixture
    def King(self):
        p = king(4, 7, white=True)
        yield p

    def test_the_pawn_has_correct_symbol_for_notation_and_wP_for_string(self, pawn):
        notation = pawn.notation
        assert notation == ""
        assert str(pawn) == "wP"

    def test_you_can_get_the_current_position_of_a_piece(self, pawn):
        assert pawn.get_position() == (0, 6)

    def test_a_piece_stores_all_possible_moves_from_current_position_ignoring_other_pieces(self, pawn):
        assert pawn.all_possible_moves() == [(0, 5), (0, 4)]

    def test_a_piece_shows_all_legal_moves_from_current_position(self, pawn):
        assert pawn.legal_moves() == [(0, 5), (0, 4)]
