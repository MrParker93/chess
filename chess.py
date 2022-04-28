import constants as C
from board import Board
from pieces import Pawn


class Chess:
    def __init__(self) -> None:
        self.b = Board()
        self.board = self.b.board
        self.history = self.b.history
        self.white_pieces = []
        self.black_pieces = []
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
            self.black_pieces.append(Pawn(i, 1, white=False))
    
    def set_board(self) -> None:
        """
        Sets up the board with each piece in the correct position.
        """
        for pieces in self.white_pieces + self.black_pieces:
            self.b.add_piece(pieces, pieces.position, self.board)
