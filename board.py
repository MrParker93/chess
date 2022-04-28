from collections import namedtuple

from numpy import isin
from piece import Piece

Coordinates = namedtuple("Coordinates", ["x", "y"])

History = namedtuple(
    "History",
    ["piece", "start_position", "destination", "captured_piece", "castling"],
    defaults=["", "", "", None, False],
)


class Board:
    def __init__(self) -> None:
        self.board = [["" for _ in range(8)] for _ in range(8)]
        self.history = []
        self.whites_move = True

    def setup(self) -> None:
        """
        Sets the pieces in their starting positions on the board.
        """
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

    def move(
        self, starting_position: tuple[int, int], destination: tuple[int, int], board: list[list]
    ) -> None:
        """
        Moves a piece from starting_position to destination on the board.
        Adds the move to history and changes the player turn to other player.
        """
        piece = board[starting_position[1]][starting_position[0]]
        if self.is_valid_move(piece, destination, board):
            self.remove_piece(starting_position, board)
            self.add_piece(piece, destination, board)
            self.history.append(
                History(
                    piece=piece,
                    start_position=starting_position,
                    destination=destination,
                )
            )
            self.whites_move = not self.whites_move

    def remove_piece(self, position: tuple[int, int], board: list[list]) -> None:
        """
        Removes the piece occupying the given position.
        """
        board[position[1]][position[0]] = ""

    def add_piece(self, piece: str, position: tuple[int, int], board: list[list]) -> None:
        """
        Adds the piece passed as a parameter to the given position on the board.
        """
        if self.is_empty(position, board):
            board[position[1]][position[0]] = str(piece)

    def is_empty(self, position: tuple[int, int], board: list[list]) -> bool:
        """
        Checks if the current position is empty.
        """
        return board[position[1]][position[0]] == ""

    def is_valid_move(self, piece: str, destination: tuple[int, int], board: list[list]) -> bool:
        """
        Ensure the attempted move is legal by checking if it puts the King in check
        and checking the destination is not occupied by ally pieces.
        """
        if self.is_empty(destination, board):
            return True
        elif piece[0] != board[destination[1]][destination[0]][0]:
            print("CAPTURE")
            self.remove_piece(destination, board)
            return True
        elif piece[0] == board[destination[1]][destination[0]][0]:
            print("ALLY PIECE")
            return False

    def check_diagonals(self, position: Coordinates[int, int], board: list[list]) -> str | None:
        """
        Checks the positions diagonally in front of the current selected Pawn piece
        and returns the direction the Pawn can capture in.
        """
        piece = board[position.y][position.x]
        # if isinstance(piece, Pawn):
        #     # TODO: Check for instance of Pawn class BEFORE calling this function in chess.py

        if piece.endswith("P") and self.whites_move:
            if board[position.y - 1][position.x - 1].startswith("b") and board[position.y - 1][position.x + 1].startswith("b"):
                return "BOTH"
            elif board[position.y - 1][position.x - 1].startswith("b"):
                return "LEFT"
            elif board[position.y - 1][position.x + 1].startswith("b"):
                return "RIGHT"
        elif piece.endswith("P") and not self.whites_move:
            if board[position.y + 1][position.x - 1].startswith("w") and board[position.y + 1][position.x + 1].startswith("w"):
                return "BOTH"
            elif board[position.y + 1][position.x - 1].startswith("w"):
                return "LEFT"
            elif board[position.y + 1][position.x + 1].startswith("w"):
                return "RIGHT"
        return None

    def check_en_passant(self, position: Coordinates[int, int], board: list[list], pieces: list[Piece]) -> str | None:
        """
        Checks the adjacent positions of the current selected Pawn piece and returns True if the
        square is occupied by an enemy Pawn and En Passant can be performed.
        """
        current_piece = board[position.y][position.x]
        # if isinstance(piece, Pawn):
            # TODO: Check for instance of Pawn class BEFORE calling this function in chess.py
        if current_piece.endswith("P") and self.whites_move:
            if board[position.y][position.x - 1] == "bP" and self.is_empty((position.x - 1, position.y - 1), board):
                for piece in pieces:
                    if (position.x - 1, position.y) == piece.get_position() and piece.position.y == 3 and piece.number_of_moves == 1:
                        return "LEFT"
            elif board[position.y][position.x + 1] == "bP" and self.is_empty((position.x + 1, position.y - 1), board):
                for piece in pieces:
                    if (position.x + 1, position.y) == piece.get_position() and piece.position.y == 3 and piece.number_of_moves == 1:
                        return "RIGHT"
        
        elif current_piece.endswith("P") and not self.whites_move:
            if board[position.y][position.x - 1] == "wP" and self.is_empty((position.x - 1, position.y + 1), board):
                for piece in pieces:
                    if (position.x - 1, position.y) == piece.get_position() and piece.position.y == 4 and piece.number_of_moves == 1:
                        return "LEFT"
            elif board[position.y][position.x + 1] == "wP" and self.is_empty((position.x + 1, position.y + 1), board):
                for piece in pieces:
                    if (position.x + 1, position.y) == piece.get_position() and piece.position.y == 4 and piece.number_of_moves == 1:
                        return "RIGHT"
        return None



    def undo(self, board: list[list]) -> None:
        """
        Undo the previous move made by the player.
        """
        if len(self.history) == 0:
            return
        last_move = self.history.pop()
        self.move(last_move.destination, last_move.start_position, board)