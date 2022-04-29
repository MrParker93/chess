import pyxel
import constants as C
from board import Board
from pieces import Pawn, Rook, Knight, Bishop, Queen, King


class Chess:
    def __init__(self) -> None:
        self.b = Board()
        self.board = self.b.board
        self.history = self.b.history
        self.white_pieces = []
        self.black_pieces = []
        self.white_captures = []
        self.black_captures = []
        self.board_setup = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        self.whites_move = True
        self.add_pieces()
        self.set_board()

        self.current_piece = None

    def add_pieces(self) -> None:
        """
        Adds all the starting pieces for each player.
        """
        for i in range(8):
            self.white_pieces.append(Pawn(i, 6, white=True))
            self.white_pieces.append(self.board_setup[i](i, 7, white=True))
            self.black_pieces.append(Pawn(i, 1, white=False))
            self.black_pieces.append(self.board_setup[i](i, 0, white=False))

    def set_board(self) -> None:
        """
        Sets up the board with each piece in the correct position.
        """
        for pieces in self.white_pieces + self.black_pieces:
            self.b.add_piece(pieces, pieces.position, self.board)

    def update(self) -> None:
        """
        Handles the chess logic.
        """
        pass

    def draw(self) -> None:
        """
        Draws the game to screen.
        """
        pyxel.cls(0)
        pyxel.bltm(x=0, y=0, tm=0, u=0, v=0, w=pyxel.width, h=pyxel.height)
        peach = True
        for i in range(8):
            for j in range(8):
                colour = pyxel.COLOR_PEACH if peach else pyxel.COLOR_BROWN
                peach = not peach
                pyxel.rect(
                    x=C.OFFSET + (i * C.SQUARESIZE),
                    y=C.OFFSET + (j * C.SQUARESIZE),
                    w=C.SQUARESIZE,
                    h=C.SQUARESIZE,
                    col=colour,
                )
            peach = not peach

        for piece in self.white_pieces + self.black_pieces:
            piece.draw()