# Uses the logic agent to try to solve the minesweeper game

from games.minesweeper import Minesweeper
from players.logic import Logic

logic = Logic(Minesweeper().grid, Minesweeper().size, Minesweeper().bombs)

game = Minesweeper()
game.play(logic)