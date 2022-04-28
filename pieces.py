from piece import Piece
import constants as C
from collections import namedtuple

Coordinates = namedtuple("Coordinates", ["x", "y"])

def on_board(x: int, y: int) -> bool:
    return 0 <= x < 8 and 0 <= y < 8


class Pawn(Piece):
    def __init__(self, x: int, y: int, white: bool=True) -> None:
        self.position = Coordinates(x=x, y=y)
        self.notation = ""
        if white:
            self.colour = "white"
        else:
            self.colour = "black"
        self.moves = C.DIRECTIONS["pawn"]
        self.has_moved = False
        self.number_of_moves = 0
        self.can_capture = None
        self.en_passant = None

    def __str__(self) -> str:
        if self.colour == "white":
            return f"{C.WHITE_PIECES['pawn']}"
        return f"{C.BLACK_PIECES['pawn']}"

    def get_position(self) -> tuple[int, int]:
        """
        Returns the current position of the current piece.
        """
        return (self.position.x, self.position.y)

    def all_possible_moves(self) -> list[Coordinates[int, int]]:
        """
        Returns all possible moves of the current piece without considering
        other pieces on the board.
        """
        moves = []
        for x, y in self.moves:
            if self.colour == "white":
                if on_board(self.position.x - x, self.position.y - y):
                    moves.append(
                        Coordinates(x=self.position.x - x, y=self.position.y - y)
                    )
            else:
                if on_board(self.position.x + x, self.position.y + y):
                    moves.append(   
                        Coordinates(x=self.position.x + x, y=self.position.y + y)
                    )
        return moves
    
    def legal_moves(self) -> list[Coordinates[int, int]]:
        """
        Returns all the legal moves the current piece can make.
        """
        legal = []
        possible_moves = self.all_possible_moves()
        for x, y in possible_moves if not self.has_moved else possible_moves[:1]:
           if on_board(x, y):
                legal.append(
                    Coordinates(x=x, y=y)
                )

        if self.can_capture == "BOTH":
            for x, y in C.PAWN_CAPTURES["wBOTH"] if self.colour == "white" else C.PAWN_CAPTURES["bBOTH"]:
                if on_board(self.position.x + x, self.position.y + y):
                    legal.append(
                        Coordinates(x=self.position.x + x, y=self.position.y + y)
                    )
        elif self.can_capture == "LEFT" or self.en_passant == "LEFT":
            x, y = C.PAWN_CAPTURES["wLEFT"] if self.colour == "white" else C.PAWN_CAPTURES["bLEFT"]
            if on_board(self.position.x + x, self.position.y + y):
                legal.append(
                    Coordinates(x=self.position.x + x, y=self.position.y + y)
                )
        elif self.can_capture == "RIGHT" or self.en_passant == "RIGHT":
            x, y = C.PAWN_CAPTURES["wRIGHT"] if self.colour == "white" else C.PAWN_CAPTURES["bRIGHT"]
            if on_board(self.position.x + x, self.position.y + y):
                legal.append(
                    Coordinates(x=self.position.x + x, y=self.position.y + y)
                )
        return legal

    def draw(self) -> None:
        pass

    def draw_moves(self) -> None:
        pass