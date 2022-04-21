import pyxel
import chess
from constants import GRIDSIZE
from pieces import Pawn
from helpers import board_to_coordinates, coordinates_to_board

pyxel.init(width=144, height=144, title="Retro Chess")
pyxel.load("assets/chess.pyxres")
pyxel.mouse(True)
c = chess.Chess()

def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
        
    c.update()

def draw():
    # c.draw()
    pyxel.bltm(x=0, y=0, tm=0, u=0, v=0, w=pyxel.width, h=pyxel.height)
    Pawn(*coordinates_to_board(0, 7), white=True).draw()
    Pawn(*coordinates_to_board(0, 7), white=True).draw_moves()

pyxel.run(update, draw)
