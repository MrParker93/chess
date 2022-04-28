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

    def __str__(self) -> str:
        if self.colour == "white":
            return f"{C.WHITE_PIECES['pawn']}"
        return f"{C.BLACK_PIECES['pawn']}"

    def get_position(self) -> tuple[int, int]:
        return (self.position.x, self.position.y)

    def all_possible_moves(self) -> list[Coordinates[int, int]]:
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
        pass