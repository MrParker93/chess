import pyxel
from constants import GRIDSIZE, OFFSET_X, OFFSET_Y, RANKS, FILES
from piece import Piece


def coordinates_to_board(piece_x: int, piece_y: int) -> tuple[int, int]:
    board_x = piece_x * GRIDSIZE + OFFSET_X
    board_y = piece_y * GRIDSIZE + OFFSET_Y
    return (board_x, board_y)


def board_to_coordinates(board_x: int, board_y: int) -> tuple[int, int]:
    piece_x = (board_x - OFFSET_X) // GRIDSIZE
    piece_y = (board_y - OFFSET_Y) // GRIDSIZE
    return (abs(piece_x), abs(piece_y))


def mouse_position(pieces: list[Piece]) -> Piece | None:
    for piece in pieces:
        if board_to_coordinates(pyxel.mouse_x, pyxel.mouse_y) == board_to_coordinates(
            piece.x, piece.y
        ):
            return piece


def notation(
    piece: str,
    coords: tuple[int, int],
    captured: bool = False,
    en_passant: bool = False,
    castling: bool = False,
    promotion: bool = False,
    promoted_piece: str="",
    check: bool = False,
    checkmate: bool = False,
) -> str:
    if castling:
        if file_to_column((coords[0], coords[1])) == "a":
            return "O-O"
        else:
            return "O-O-O"
    
    if promotion:
        return file_to_column((coords[0], coords[1])) + rank_to_row(
        (coords[0], coords[1])) + "=" + promoted_piece
        
    notation = ""
    if piece:
        notation += piece
    if en_passant:
        notation += "e"
    if captured:
        notation += "x"

    notation += file_to_column((coords[0], coords[1])) + rank_to_row(
        (coords[0], coords[1])
    )

    if check:
        notation += "+"
    elif checkmate:
        notation += "++"
    
    return notation


def rank_to_row(coords: tuple[int, int]) -> str:
    rank = [k for k, v in RANKS.items() if v == coords[1]]
    return rank[0]


def file_to_column(coords: tuple[int, int]) -> str:
    file = [k for k, v in FILES.items() if v == coords[0]]
    return file[0]
