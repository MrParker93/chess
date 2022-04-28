import pytest
from chess import Chess

class TestChess:
    @pytest.fixture
    def chess(self):
        c = Chess()
        yield c

    def test_board_is_set_up_correctly(self, chess):
        assert chess.board == [
            ["", "", "", "", "", "", "", ""],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["", "", "", "", "", "", "", ""],
        ]