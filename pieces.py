import pyxel
import constants as C
from piece import Piece
from collections import namedtuple

Coordinates = namedtuple("Coordinates", ["x", "y"])


def on_board(x: int, y: int) -> bool:
    return 0 <= x < 8 and 0 <= y < 8

class Pawn(Piece):
    def __init__(self, x: int, y: int, white: bool = True) -> None:
        self.position = Coordinates(x=x, y=y)
        self.u = 0
        if white:
            self.colour = "white"
            self.v = 0
        else:
            self.colour = "black"
            self.v = 16
        self.letter = ""
        self.moves = C.DIRECTIONS["pawn"]
        self.has_moved = False
        self.number_of_moves = 0
        self.can_capture = None
        self.en_passant = None
        self.promote = False
        self.highlighted = False

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
                legal.append(Coordinates(x=x, y=y))

        if self.can_capture == "BOTH":
            for x, y in (
                C.PAWN_CAPTURES["wBOTH"]
                if self.colour == "white"
                else C.PAWN_CAPTURES["bBOTH"]
            ):
                if on_board(self.position.x + x, self.position.y + y):
                    legal.append(
                        Coordinates(x=self.position.x + x, y=self.position.y + y)
                    )
        elif self.can_capture == "LEFT" or self.en_passant == "LEFT":
            x, y = (
                C.PAWN_CAPTURES["wLEFT"]
                if self.colour == "white"
                else C.PAWN_CAPTURES["bLEFT"]
            )
            if on_board(self.position.x + x, self.position.y + y):
                legal.append(Coordinates(x=self.position.x + x, y=self.position.y + y))
        elif self.can_capture == "RIGHT" or self.en_passant == "RIGHT":
            x, y = (
                C.PAWN_CAPTURES["wRIGHT"]
                if self.colour == "white"
                else C.PAWN_CAPTURES["bRIGHT"]
            )
            if on_board(self.position.x + x, self.position.y + y):
                legal.append(Coordinates(x=self.position.x + x, y=self.position.y + y))
        return legal

    def can_promote(self) -> bool:
        """
        Checks if the Pawn has reached the opposite end of the board.
        """
        return self.position.y == 0 if self.colour == "white" else self.position == 7

    def draw(self) -> None:
        """
        Draws the piece to screen.
        """
        if self.highlighted:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y - 3 * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        """
        Draws all legal moves to screen.
        """
        pass


class Rook(Piece):
    def __init__(self, x: int, y: int, white: bool = True) -> None:
        self.position = Coordinates(x=x, y=y)
        self.u = 8
        if white:
            self.colour = "white"
            self.v = 0
        else:
            self.colour = "black"
            self.v = 16
        self.letter = "R"
        self.moves = C.DIRECTIONS["cardinal"]
        self.has_moved = False
        self.castling = None
        self.highlighted = False

    def __str__(self) -> str:
        if self.colour == "white":
            return f"{C.WHITE_PIECES['rook']}"
        return f"{C.BLACK_PIECES['rook']}"

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
            for i in range(1, 8):
                if on_board(self.position.x + x * i, self.position.y + y * i):
                    moves.append(
                        Coordinates(
                            x=self.position.x + x * i, y=self.position.y + y * i
                        )
                    )
        return moves

    def legal_moves(self) -> list[Coordinates[int, int]]:
        """
        Returns all the legal moves the current piece can make.
        """
        legal = []
        possible_moves = self.all_possible_moves()
        for x, y in possible_moves:
            if on_board(x, y):
                legal.append(Coordinates(x=x, y=y))

        if self.castling == "KINGSIDE":
            x, y = C.CASTLING["KINGSIDE"][1]
            if on_board(self.position.x + x, self.position.y + y):
                legal.append(Coordinates(x=self.position.x + x, y=self.position.y + y))
        elif self.castling == "QUEENSIDE":
            x, y = C.CASTLING["QUEENSIDE"][1]
            if on_board(self.position.x + x, self.position.y + y):
                legal.append(Coordinates(x=self.position.x + x, y=self.position.y + y))
        return legal

    def can_castle(self) -> bool:
        """
        Checks if the conditions are met for castling to occur.
        """
        return (
            self.position.y == 7 and not self.has_moved
            if self.colour == "white"
            else self.position.y == 0 and not self.has_moved
        )

    def draw(self) -> None:
        """
        Draws the piece to screen.
        """
        if self.highlighted:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y - 3 * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        """
        Draws all legal moves to screen.
        """
        pass


class Knight(Piece):
    def __init__(self, x: int, y: int, white: bool=True) -> None:
        self.position = Coordinates(x=x, y=y)
        self.u = 32
        if white:
            self.colour = "white"
            self.v = 0
        else:
            self.colour = "black"
            self.v = 16
        self.letter = "N"
        self.moves = C.DIRECTIONS["knight"]
        self.can_jump = True
        self.highlighted = False
        
    def __str__(self) -> str:
        if self.colour == "white":
            return f"{C.WHITE_PIECES['knight']}"
        return f"{C.BLACK_PIECES['knight']}"

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
            if on_board(self.position.x + x, self.position.y + y):
                moves.append(
                    Coordinates(x=self.position.x + x, y=self.position.y + y)
                )
        return moves

    def legal_moves(self) -> list[Coordinates[int, int]]:
        """
        Returns all the legal moves the current piece can make.
        """
        return self.all_possible_moves()

    def draw(self) -> None:
        """
        Draws the piece to screen.
        """
        if self.highlighted:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y - 3 * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        """
        Draws all legal moves to screen.
        """
        pass


class Bishop(Piece):
    def __init__(self, x: int, y: int, white: bool=True) -> None:
        self.position = Coordinates(x=x, y=y)
        self.u = 40
        if white:
            self.colour = "white"
            self.v = 0
        else:
            self.colour = "black"
            self.v = 16
        self.letter = "B"
        self.moves = C.DIRECTIONS["diagonal"]
        self.highlighted = False

    def __str__(self) -> str:
        if self.colour == "white":
            return f"{C.WHITE_PIECES['bishop']}"
        return f"{C.BLACK_PIECES['bishop']}"

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
        for x,y in self.moves:
            for i in range(1, 8):
                if on_board(self.position.x + x * i, self.position.y + y * i):
                    moves.append(
                        Coordinates(x=self.position.x + x * i, y=self.position.y + y * i)
                    )
        return moves

    def legal_moves(self) -> list[Coordinates[int, int]]:
        """
        Returns all the legal moves the current piece can make.
        """
        return self.all_possible_moves()

    def draw(self) -> None:
        """
        Draws the piece to screen.
        """
        if self.highlighted:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y - 3 * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        """
        Draws all legal moves to screen.
        """
        pass


class Queen(Piece):
    def __init__(self, x: int, y: int, white: bool=True) -> None:
        self.position = Coordinates(x=x, y=y)
        self.u = 16
        if white:
            self.colour = "white"
            self.v = 0
        else:
            self.colour = "black"
            self.v = 16
        self.letter = "Q"
        self.moves = C.DIRECTIONS["cardinal"] + C.DIRECTIONS["diagonal"]
        self.highlighted = False

    def __str__(self) -> str:
        if self.colour == "white":
            return f"{C.WHITE_PIECES['queen']}"
        return f"{C.BLACK_PIECES['queen']}"

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
            for i in range(1, 8):
                if on_board(self.position.x + x * i, self.position.y + y * i):
                    moves.append(
                        Coordinates(x=self.position.x + x * i, y=self.position.y + y * i)
                    )
        return moves

    def legal_moves(self) -> list[Coordinates[int, int]]:
        """
        Returns all the legal moves the current piece can make.
        """
        return self.all_possible_moves()

    def draw(self) -> None:
        """
        Draws the piece to screen.
        """
        if self.highlighted:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y - 3 * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        """
        Draws all legal moves to screen.
        """
        pass


class King(Piece):
    def __init__(self, x: int, y: int, white: bool=True) -> None:
        self.position = Coordinates(x=x, y=y)
        self.u = 24
        if white:
            self.colour = "white"
            self.v = 0
        else:
            self.colour = "black"
            self.v = 16
        self.letter = "K"
        self.moves = C.DIRECTIONS["cardinal"] + C.DIRECTIONS["diagonal"]
        self.has_moved = False
        self.castling = None
        self.in_check = False
        self.highlighted = False

    def __str__(self) -> str:
        if self.colour == "white":
            return f"{C.WHITE_PIECES['king']}"
        return f"{C.BLACK_PIECES['king']}"

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
        for x, y in possible_moves:
            if on_board(x, y):
                legal.append(Coordinates(x=x, y=y))

        if self.castling == "KINGSIDE":
            x, y = C.CASTLING["KINGSIDE"][0]
            if on_board(self.position.x + x, self.position.y + y):
                legal.append(Coordinates(x=self.position.x + x, y=self.position.y + y))
        elif self.castling == "QUEENSIDE":
            x, y = C.CASTLING["QUEENSIDE"][0]
            if on_board(self.position.x + x, self.position.y + y):
                legal.append(Coordinates(x=self.position.x + x, y=self.position.y + y))
        return legal

    def can_castle(self) -> bool:
        """
        Checks if the conditions are met for castling to occur.
        """
        return (
            self.position == (4, 7) and not self.has_moved
            if self.colour == "white"
            else self.position == (4, 0) and not self.has_moved
        )

    def draw(self) -> None:
        """
        Draws the piece to screen.
        """
        if self.highlighted:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y - 3 * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )
        else:
            pyxel.blt(
                x=self.position.x * C.SQUARESIZE + 12,
                y=self.position.y * C.SQUARESIZE + 10,
                img=0,
                u=self.u,
                v=self.v,
                w=8,
                h=12,
                colkey=pyxel.COLOR_DARK_BLUE,
            )

    def draw_moves(self) -> None:
        """
        Draws all legal moves to screen.
        """
        pass
