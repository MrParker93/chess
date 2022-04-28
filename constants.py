WHITE_PIECES = {
    "pawn": "wP",
    "rook": "wR",
    "knight": "wN",
    "bishop": "wB",
    "queen": "wQ",
    "king": "wK",
}

BLACK_PIECES = {
    "pawn": "bP",
    "rook": "bR",
    "knight": "bN",
    "bishop": "bB",
    "queen": "bQ",
    "king": "bK",
}

DIRECTIONS = {
    "cardinal": [(1, 0), (-1, 0), (0, 1), (0, -1)],
    "diagonal": [(1, 1), (-1, 1), (1, -1), (-1, -1)],
    "knight": [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)],
    "pawn": [(0, 1), (0, 2)],
}

PAWN_CAPTURES = {
    "wRIGHT": (1, -1),
    "wLEFT": (-1, -1),
    "wBOTH": [(1, -1), (-1, -1)],
    "bRIGHT": (1, 1),
    "bLEFT": (-1, 1),
    "bBOTH": [(1, 1), (-1, 1)]
}
RANKS = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
FILES = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}