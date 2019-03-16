from games.minesweeper import Minesweeper
from players.logic import Logic

logic = Logic(Minesweeper().grid, Minesweeper().size, Minesweeper().bombs)

game = Minesweeper()
game.play(logic)