import pyxel
import chess

pyxel.init(width=144, height=144, title="Retro Chess")
pyxel.load("assets/chess.pyxres")
pyxel.mouse(True)
c = chess.Chess()


def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()

    c.update()


def draw():
    c.draw()

pyxel.run(update, draw)
