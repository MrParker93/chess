import pyxel
from piece import Piece
from helpers import board_to_coordinates, coordinates_to_board
from constants import GRIDSIZE, MOVE_SQUARE_OFFSET_X, MOVE_SQUARE_OFFSET_Y, WHITE_PIECES, BLACK_PIECES, DIRECTIONS


class Pawn(Piece):
    def __init__(self, x, y, white=True) -> None:
        self.x = x
        self.y = y
        self.u = 0
        self.v = 0 if white else 16
        self.symbol = ""
        self.moves = DIRECTIONS["pawn"]
        self.moved = False
        self.promote = False

    def move(self) -> None:
        pass
    
    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                move_coordinates.append(
                    (self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
                )
            else:
                move_coordinates.append(
                    (self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
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
        for x, y in possible_moves:
            pyxel.
    
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

    def move(self) -> None:
        pass
    
    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                move_coordinates.append(
                    (self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
                )
            else:
                move_coordinates.append(
                    (self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
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

    def move(self) -> None:
        pass
    
    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                move_coordinates.append(
                    (self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
                )
            else:
                move_coordinates.append(
                    (self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
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

    def move(self) -> None:
        pass
    
    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                move_coordinates.append(
                    (self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
                )
            else:
                move_coordinates.append(
                    (self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
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

    def move(self) -> None:
        pass
    
    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                move_coordinates.append(
                    (self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
                )
            else:
                move_coordinates.append(
                    (self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
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

    def move(self) -> None:
        pass
    
    def possible_moves(self) -> list[tuple[int, int]]:
        move_coordinates = []
        for x, y in self.moves:
            if self.v == 0:
                move_coordinates.append(
                    (self.x - (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y - (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
                )
            else:
                move_coordinates.append(
                    (self.x + (x * GRIDSIZE) + MOVE_SQUARE_OFFSET_X,
                     self.y + (y * GRIDSIZE) + MOVE_SQUARE_OFFSET_Y)
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
        
    def __str__(self) -> str:
        if self.v == 0:
            return f'{WHITE_PIECES["bishop"]}'
        return f'{BLACK_PIECES["bishop"]}'
