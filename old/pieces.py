import pyxel
from piece import Piece
from helpers import board_to_coordinates, coordinates_to_board
from constants import (
    GRIDSIZE,
    MOVE_SQUARE_OFFSET_X,
    MOVE_SQUARE_OFFSET_Y,
    PIECE_HEIGHT,
    WHITE_PIECES,
    BLACK_PIECES,
    DIRECTIONS,
)


def legal_move(x: int, y: int) -> bool:
    return 0 <= x < 8 * GRIDSIZE and 0 <= y < 8 * GRIDSIZE

def moves_to_coordinates(legal_moves: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [board_to_coordinates(x, y) for x, y in legal_moves]
    
class Pawn(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 0
        self.v = 0 if white else 16
        self.symbol = ""
        self.moves = DIRECTIONS["pawn"]
        self.highlighted = False
        self.can_jump = False
        self.moved = False
        self.promote = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                _x = self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X
                _y = self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y
                if legal_move(_x, _y):
                    move_coordinates.append((_x, _y))
            else:
                _x = self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X
                _y = self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y
                if legal_move(_x, _y):
                    move_coordinates.append((_x, _y))
        return move_coordinates 

    def get_coordinates(self) -> tuple[int, int]:
        return coordinates_to_board(self.x, self.y)

    def has_moved(self) -> bool:
        return self.moved

    def draw(self) -> None:
        if self.highlighted:
            pyxel.blt(
                x=self.x,
                y=self.y - 3,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.x,
                y=self.y,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        possible_moves = self.possible_moves()
        for x, y in possible_moves if not self.moved else possible_moves[:1]:
            if self.v == 0:
                if self.y > PIECE_HEIGHT:
                    # if pyxel.pget(x, y) == pyxel.COLOR_BROWN or pyxel.pget(x, y) == pyxel.COLOR_PEACH:
                    pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)
                else:
                    return None
            else:
                if self.y <= 7 * GRIDSIZE:
                    # if pyxel.pget(x, y) == pyxel.COLOR_BROWN or pyxel.pget(x, y) == pyxel.COLOR_PEACH:
                    pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)
                else:
                    return None

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["pawn"]}: {self.get_coordinates()}'
        return f'{BLACK_PIECES["pawn"]}: {self.get_coordinates()}'


class Rook(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 8
        self.v = 0 if white else 16
        self.symbol = "R"
        self.moves = DIRECTIONS["cardinal"]
        self.highlighted = False
        self.can_jump = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            for i in range(1, 8):
                if self.v == 0:
                    _x = self.x - (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X
                    _y = self.y - (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y
                    if legal_move(_x, _y):
                        move_coordinates.append((_x, _y))
                else:
                    _x = self.x + (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X
                    _y = self.y + (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y
                    if legal_move(_x, _y):
                        move_coordinates.append((_x, _y))
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return coordinates_to_board(self.x, self.y)

    def draw(self) -> None:
        if self.highlighted:
            pyxel.blt(
                x=self.x,
                y=self.y - 3,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.x,
                y=self.y,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        possible_moves = self.possible_moves()
        for x, y in possible_moves:
            # if pyxel.pget(x, y) == pyxel.COLOR_BROWN or pyxel.pget(x, y) == pyxel.COLOR_PEACH:
            pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["rook"]}: {self.get_coordinates()}'
        return f'{BLACK_PIECES["rook"]}: {self.get_coordinates()}'


class Queen(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 16
        self.v = 0 if white else 16
        self.symbol = "Q"
        self.moves = DIRECTIONS["cardinal"] + DIRECTIONS["diagonal"]
        self.highlighted = False
        self.can_jump = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            for i in range(1, 8):
                if self.v == 0:
                    _x = self.x - (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X
                    _y = self.y - (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y
                    if legal_move(_x, _y):
                        move_coordinates.append((_x, _y))
                else:
                    _x = self.x + (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X
                    _y = self.y + (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y
                    if legal_move(_x, _y):
                        move_coordinates.append((_x, _y))
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return coordinates_to_board(self.x, self.y)

    def draw(self) -> None:
        if self.highlighted:
            pyxel.blt(
                x=self.x,
                y=self.y - 3,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.x,
                y=self.y,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        possible_moves = self.possible_moves()
        for x, y in possible_moves:
            # if pyxel.pget(x, y) == pyxel.COLOR_BROWN or pyxel.pget(x, y) == pyxel.COLOR_PEACH:
            pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)
    
    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["queen"]}: {self.get_coordinates()}'
        return f'{BLACK_PIECES["queen"]}: {self.get_coordinates()}'


class King(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 24
        self.v = 0 if white else 16
        self.symbol = "K"
        self.moves = DIRECTIONS["cardinal"] + DIRECTIONS["diagonal"]
        self.highlighted = False
        self.can_jump = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                _x = self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X
                _y = self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y
                if legal_move(_x, _y):
                    move_coordinates.append((_x, _y))
            else:
                _x = self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X
                _y = self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y
                if legal_move(_x, _y):
                    move_coordinates.append((_x, _y))
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return coordinates_to_board(self.x, self.y)

    def draw(self) -> None:
        if self.highlighted:
            pyxel.blt(
                x=self.x,
                y=self.y - 3,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.x,
                y=self.y,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        possible_moves = self.possible_moves()
        for x, y in possible_moves:
            # if pyxel.pget(x, y) == pyxel.COLOR_BROWN or pyxel.pget(x, y) == pyxel.COLOR_PEACH:
            pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["king"]}: {self.get_coordinates()}'
        return f'{BLACK_PIECES["king"]}: {self.get_coordinates()}'


class Knight(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 32
        self.v = 0 if white else 16
        self.symbol = "N"
        self.moves = DIRECTIONS["knight"]
        self.highlighted = False
        self.can_jump = True

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                _x = self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X
                _y = self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y
                if legal_move(_x, _y):
                    move_coordinates.append((_x, _y))
            else:
                _x = self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X
                _y = self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y
                if legal_move(_x, _y):
                    move_coordinates.append((_x, _y))
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return coordinates_to_board(self.x, self.y)

    def draw(self) -> None:
        if self.highlighted:
            pyxel.blt(
                x=self.x,
                y=self.y - 3,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.x,
                y=self.y,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        possible_moves = self.possible_moves()
        for x, y in possible_moves:
            # if pyxel.pget(x, y) == pyxel.COLOR_BROWN or pyxel.pget(x, y) == pyxel.COLOR_PEACH:
            pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["knight"]}: {self.get_coordinates()}'
        return f'{BLACK_PIECES["knight"]}: {self.get_coordinates()}'


class Bishop(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 40
        self.v = 0 if white else 16
        self.symbol = "B"
        self.moves = DIRECTIONS["diagonal"]
        self.highlighted = False
        self.can_jump = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            for i in range(1, 8):
                if self.v == 0:
                    _x = self.x - (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X
                    _y = self.y - (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y
                    if legal_move(_x, _y):
                        move_coordinates.append((_x, _y))
                else:
                    _x = self.x + (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X
                    _y = self.y + (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y
                    if legal_move(_x, _y):
                        move_coordinates.append((_x, _y))
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return coordinates_to_board(self.x, self.y)

    def draw(self) -> None:
        if self.highlighted:
            pyxel.blt(
                x=self.x,
                y=self.y - 3,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.x,
                y=self.y,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        possible_moves = self.possible_moves()
        for x, y in possible_moves:
            # if pyxel.pget(x, y) == pyxel.COLOR_BROWN or pyxel.pget(x, y) == pyxel.COLOR_PEACH:
            pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["bishop"]}: {self.get_coordinates()}'
        return f'{BLACK_PIECES["bishop"]}: {self.get_coordinates()}'
