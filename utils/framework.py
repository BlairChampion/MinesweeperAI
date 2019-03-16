from time import time, sleep


# Superclass for all games
class Game(object):

    # Return whether this game is equivalent to the other
    def __eq__(self, other):
        raise NotImplementedError

    # Return a hash code for this game
    def __hash__(self):
        raise NotImplementedError

    # Return the utility of this game (if it's over)
    # If this game isn't over yet, return None
    def utility(self):
        raise NotImplementedError

    # Return a list of legal moves
    def moves(self):
        raise NotImplementedError

    # Return a new game created by a move
    def child(self, move):
        raise NotImplementedError

    # Print this game to the console
    def display(self):
        raise NotImplementedError

    # Conduct this game
    def play(self, player, interval=1):
        print("Playing game:")
        self.display()
        moves = 0
        seconds = 0

        game = self

        while game.utility() is None:

            start = time()
            move = player.move(game)
            seconds = time() - start

            game = game.child(move)
            game.display()
            moves += 1

            sleep(interval)

        print(game.utility(), "after", seconds, "seconds.")


# Superclass for all players
class Player(object):

    # Return the move this player wants to make
    def move(self, game):
        raise NotImplementedError