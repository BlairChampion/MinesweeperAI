# Allows a human player to see the available moves and choose one

from utils.framework import Player


class Human(Player):

    # Return the move this player wants to make
    def move(self, game):
        moves = game.moves()
        print("Possible moves:", moves)

        move = None
        while move not in moves:
            move = eval(input("Your choice: "))
        return move
