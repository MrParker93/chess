from collections import namedtuple

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
        self, starting_position: tuple[int, int], destination: tuple[int, int]
    ) -> None:
        """
        Moves a piece from starting_position to destination on the board.
        Adds the move to history and changes the player turn to other player.
        """
        piece = self.board[starting_position[1]][starting_position[0]]
        if self.is_valid_move(piece, destination):
            self.remove_piece(starting_position)
            self.add_piece(piece, destination)
            self.history.append(
                History(
                    piece=piece,
                    start_position=starting_position,
                    destination=destination,
                )
            )
            self.whites_move = not self.whites_move

    def remove_piece(self, position: tuple[int, int]) -> None:
        """
        Removes the piece occupying the given position.
        """
        self.board[position[1]][position[0]] = ""

    def add_piece(self, piece: str, position: tuple[int, int]) -> None:
        """
        Adds the piece passed as a parameter to the given position on the board.
        """
        self.board[position[1]][position[0]] = piece

    def is_empty(self, position: tuple[int, int]) -> bool:
        """
        Checks if the current position is empty.
        """
        return self.board[position[1]][position[0]] == ""

    def is_valid_move(self, piece: str, destination: tuple[int, int]) -> bool:
        """
        Ensure the attempted move is legal by checking if it puts the King in check
        and checking the destination is not occupied by ally pieces.
        """
        if self.is_empty(destination):
            return True
        elif piece[0] != self.board[destination[1]][destination[0]][0]:
            print("CAPTURE")
            return True
        elif piece[0] == self.board[destination[1]][destination[0]][0]:
            print("ALLY PIECE")
            return False

    def undo(self) -> None:
        """
        Undo the previous move made by the player.
        """
        if len(self.history) == 0:
            return
        last_move = self.history.pop()
        self.move(last_move.destination, last_move.start_position)