import pyxel
import numpy as np
from constants import GRID_OFFSET, GRIDSIZE
from piece import Piece
from pieces import Pawn, Rook, Knight, Bishop, Queen, King, moves_to_coordinates
from helpers import board_to_coordinates, coordinates_to_board, mouse_position, notation


class Chess:
    def __init__(self) -> None:
        self.board = self.board = np.full(shape=[8, 8], fill_value="", dtype="U256")
        self.move_log = []
        self.white_pieces = []
        self.black_pieces = []
        self.captures = []
        self.setup = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        self.add_pieces()
        self.set_board()

        self.current_piece = None
        self.selected_piece = ()
        self.from_to_coordinates = []

    def add_pieces(self) -> None:
        for i in range(8):
            self.white_pieces.append(Pawn(*board_to_coordinates(i, 6), white=True))
            self.white_pieces.append(
                self.setup[i](*board_to_coordinates(i, 7), white=True)
            )
            self.black_pieces.append(Pawn(*board_to_coordinates(i, 1), white=False))
            self.black_pieces.append(
                self.setup[i](*board_to_coordinates(i, 0), white=False)
            )

    def set_board(self) -> None:
        for piece in self.white_pieces + self.black_pieces:
            self.add_piece(piece, coordinates_to_board(piece.x, piece.y))

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

    def within_board(self, coords: tuple[int, int]) -> bool:
        return 0 <= coords[0] < 8 and 0 <= coords[1] < 8

    def update(self) -> None:
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 8 < pyxel.mouse_x < 136 and 8 < pyxel.mouse_y < 136:
                selection = mouse_position(self.white_pieces + self.black_pieces)
                capture = None
                
                if isinstance(selection, Piece) and self.current_piece is None:
                    self.current_piece = selection
                    self.current_piece.highlighted = True

                    if self.selected_piece == coordinates_to_board(self.current_piece.x, self.current_piece.y):
                        self.selected_piece = ()
                        self.from_to_coordinates = []
                        self.current_piece.highlighted = False
                    else: 
                        self.selected_piece = coordinates_to_board(self.current_piece.x, self.current_piece.y)
                        self.from_to_coordinates.append(self.selected_piece)
                
                elif isinstance(selection, Piece) and self.current_piece is not None:
                    if len(self.from_to_coordinates) != 0:
                        capture = mouse_position(self.white_pieces + self.black_pieces)
                        self.from_to_coordinates.append(coordinates_to_board(pyxel.mouse_x, pyxel.mouse_y))
                
                else:
                    if len(self.from_to_coordinates) != 0:
                        self.from_to_coordinates.append(coordinates_to_board(pyxel.mouse_x, pyxel.mouse_y))
                
                if len(self.from_to_coordinates) == 2:
                    pass
                        
                self.current_piece = None
                print(self.from_to_coordinates)
                    

    def draw(self) -> None:
        pyxel.cls(0)
        pyxel.bltm(x=0, y=0, tm=0, u=0, v=0, w=pyxel.width, h=pyxel.height)
        change_colour = True
        for i in range(8):
            for j in range(8):
                colour = pyxel.COLOR_PEACH if change_colour else pyxel.COLOR_BROWN
                change_colour = not change_colour
                pyxel.rect(
                    x=GRID_OFFSET + (i * GRIDSIZE),
                    y=GRID_OFFSET + (j * GRIDSIZE),
                    w=GRIDSIZE,
                    h=GRIDSIZE,
                    col=colour,
                )
            change_colour = not change_colour
            
        for pieces in self.white_pieces + self.black_pieces:
            pieces.draw()

        if self.current_piece:
            if self.current_piece.highlighted:
                for x, y in self.current_piece.possible_moves():
                    if self.is_empty(coordinates_to_board(x, y)):
                        self.current_piece.draw_moves()
