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


class Pawn(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 0
        self.v = 0 if white else 16
        self.symbol = ""
        self.moves = DIRECTIONS["pawn"]
        self.highlighted = False
        self.moved = False
        self.promote = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                move_coordinates.append(
                    (
                        self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                        self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y,
                    )
                )
            else:
                move_coordinates.append(
                    (
                        self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                        self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y,
                    )
                )
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return board_to_coordinates(self.x, self.y)

    def has_moved(self) -> bool:
        return self.moved

    def draw(self) -> None:
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
                    pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)
                else:
                    return None
            else:
                if self.y <= 7 * GRIDSIZE:
                    pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)
                else:
                    return None

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["pawn"]}'
        return f'{BLACK_PIECES["pawn"]}'


class Rook(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 8
        self.v = 0 if white else 16
        self.symbol = "R"
        self.moves = DIRECTIONS["cardinal"]
        self.highlighted = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            for i in range(1, 8):
                if self.v == 0:
                    move_coordinates.append(
                        (
                            self.x - (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X,
                            self.y - (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y,
                        )
                    )
                else:
                    move_coordinates.append(
                        (
                            self.x + (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X,
                            self.y + (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y,
                        )
                    )
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return board_to_coordinates(self.x, self.y)

    def draw(self) -> None:
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
            pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["rook"]}'
        return f'{BLACK_PIECES["rook"]}'


class Queen(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 16
        self.v = 0 if white else 16
        self.symbol = "Q"
        self.moves = DIRECTIONS["cardinal"] + DIRECTIONS["diagonal"]
        self.hightlighted = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            for i in range(1, 8):
                if self.v == 0:
                    move_coordinates.append(
                        (
                            self.x - (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X,
                            self.y - (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y,
                        )
                    )
                else:
                    move_coordinates.append(
                        (
                            self.x + (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X,
                            self.y + (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y,
                        )
                    )
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return board_to_coordinates(self.x, self.y)

    def draw(self) -> None:
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
            pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["queen"]}'
        return f'{BLACK_PIECES["queen"]}'


class King(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 24
        self.v = 0 if white else 16
        self.symbol = "K"
        self.moves = DIRECTIONS["cardinal"] + DIRECTIONS["diagonal"]
        self.highlighted = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                move_coordinates.append(
                    (
                        self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                        self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y,
                    )
                )
            else:
                move_coordinates.append(
                    (
                        self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                        self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y,
                    )
                )
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return board_to_coordinates(self.x, self.y)

    def draw(self) -> None:
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
            pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["king"]}'
        return f'{BLACK_PIECES["king"]}'


class Knight(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 32
        self.v = 0 if white else 16
        self.symbol = "N"
        self.moves = DIRECTIONS["knight"]
        self.highlighted = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                move_coordinates.append(
                    (
                        self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                        self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y,
                    )
                )
            else:
                move_coordinates.append(
                    (
                        self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                        self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y,
                    )
                )
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return board_to_coordinates(self.x, self.y)

    def draw(self) -> None:
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
            pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["knight"]}'
        return f'{BLACK_PIECES["knight"]}'


class Bishop(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 40
        self.v = 0 if white else 16
        self.symbol = "B"
        self.moves = DIRECTIONS["diagonal"]
        self.highlighted = False

    def move(self) -> None:
        pass

    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            for i in range(1, 8):
                if self.v == 0:
                    move_coordinates.append(
                        (
                            self.x - (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X,
                            self.y - (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y,
                        )
                    )
                else:
                    move_coordinates.append(
                        (
                            self.x + (x * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_X,
                            self.y + (y * GRIDSIZE * i) + MOVE_SQUARE_OFFSET_Y,
                        )
                    )
        return move_coordinates

    def get_coordinates(self) -> tuple[int, int]:
        return board_to_coordinates(self.x, self.y)

    def draw(self) -> None:
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
            pyxel.rect(x=x, y=y, w=6, h=6, col=pyxel.COLOR_RED)

    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["bishop"]}'
        return f'{BLACK_PIECES["bishop"]}'
