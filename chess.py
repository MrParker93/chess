import pyxel
import numpy as np
from constants import GRIDSIZE
from piece import Piece
from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from helpers import board_to_coordinates, coordinates_to_board, mouse_position, notation


class Chess:
    def __init__(self) -> None:
        self.board = self.board = np.full(shape=[8, 8], fill_value="", dtype="U256")
        self.move_log = []
        self.white_pieces = []
        self.black_pieces = []
        self.white_captures = []
        self.black_captures = []
        self.setup = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        self.add_pieces()
        self.set_board()
        
        self.current_piece = None
        self.selected_piece = ()
        self.from_to_coordinates = []
        
    def add_pieces(self) -> None:
        for i in range(8):
            self.white_pieces.append(Pawn(*coordinates_to_board(i, 6), white=True))
            self.white_pieces.append(self.setup[i](*coordinates_to_board(i, 7), white=True))
            self.black_pieces.append(Pawn(*coordinates_to_board(i, 1), white=False))
            self.black_pieces.append(self.setup[i](*coordinates_to_board(i, 0), white=False))
    
    def set_board(self) -> None:
        for piece in self.white_pieces + self.black_pieces:
            self.add_piece(piece, board_to_coordinates(piece.x, piece.y))
            
    def print(self) -> None:
        print(*self.board, sep="\n")

    def add_piece(self, piece: str, coords: tuple[int, int]) -> None:
        if self.is_empty((coords[0], coords[1])):
            self.board[coords[1]][coords[0]] = piece
        return

    def remove_piece(self, coords: tuple[int, int]) -> None:
        self.board[coords[1]][coords[0]] = ""

    def get_piece(self, coords: tuple[int, int]) -> str:
        return self.board[coords[1]][coords[0]]

    def is_empty(self, coords: tuple[int, int]) -> bool:
        return self.board[coords[1]][coords[0]] == ""

    def at_opposite_edge(self, coords: tuple[int, int], white: bool=True) -> bool:
        if white:
            return coords[1] == 7
        return coords[1] == 0
    
    def update(self) -> None:
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            selected_piece = mouse_position(self.white_pieces + self.black_pieces)
            if isinstance(selected_piece, Piece):
                self.current_piece = selected_piece
                if self.selected_piece == board_to_coordinates(self.current_piece.x, self.current_piece.y):
                    self.selected_piece = ()
                    self.from_to_coordinates = []
                else:
                    self.selected_piece = board_to_coordinates(self.current_piece.x, self.current_piece.y)
                    self.from_to_coordinates.append(self.selected_piece)
            else:
                if len(self.from_to_coordinates) != 0:
                    self.from_to_coordinates.append(board_to_coordinates(pyxel.mouse_x, pyxel.mouse_y))
                    
            if len(self.from_to_coordinates) == 2:
                self.remove_piece(board_to_coordinates(self.current_piece.x, self.current_piece.y))
                self.current_piece.x, self.current_piece.y = coordinates_to_board(self.from_to_coordinates[1][0], self.from_to_coordinates[1][1])  
                self.add_piece(self.current_piece, board_to_coordinates(self.current_piece.x, self.current_piece.y))
                print(notation(self.current_piece.symbol, board_to_coordinates(self.current_piece.x, self.current_piece.y)))
                self.move_log.append(notation(self.current_piece.symbol, board_to_coordinates(self.current_piece.x, self.current_piece.y)))
                self.selected_piece = ()
                self.from_to_coordinates = []

    def draw(self) -> None:
        pyxel.cls(0)
        pyxel.bltm(x=0, y=0, tm=0, u=0, v=0, w=pyxel.width, h=pyxel.height)
        for pieces in self.white_pieces + self.black_pieces:
            pieces.draw()
        pieces.draw_moves()