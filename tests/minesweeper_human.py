from games.minesweeper import Minesweeper
from players.human import Human

human = Human()

game = Minesweeper()
game.play(human)