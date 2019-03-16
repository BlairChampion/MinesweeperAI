from utils.framework import Game

SIZE = 9

BOMBS = 10

# Tuple[0] = revealed? Tuple[1] = number, bomb = B
GRID = [[(0, "B"),  (0, 2),     (0, 1),     (1, 0),     (1, 0),     (1, 0),     (1, 0),     (1, 0),   (1, 0)],
        [(0, 2),    (0, "B"),   (0, 1),     (1, 0),     (1, 0),     (1, 0),     (1, 0),     (1, 0),   (1, 0)],
        [(0, 1),    (0, 1),     (0, 1),     (1, 0),     (1, 0),     (1, 0),     (1, 0),     (1, 0),   (1, 0)],
        [(1, 0),    (1, 0),     (1, 0),     (1, 0),     (1, 0),     (0, 1),     (0, 1),     (0, 1),   (1, 0)],
        [(1, 0),    (0, 1),     (0, 1),     (0, 2),     (0, 1),     (0, 3),     (0, "B"),   (0, 2),   (1, 0)],
        [(1, 0),    (0, 2),     (0, "B"),   (0, 3),     (0, "B"),   (0, 4),     (0, "B"),   (0, 2),   (1, 0)],
        [(1, 0),    (0, 2),     (0, "B"),   (0, 4),     (0, 4),     (0, "B"),   (0, 3),     (0, 1),   (1, 0)],
        [(1, 0),    (0, 1),     (0, 1),     (0, 2),     (0, "B"),   (0, "B"),   (0, 2),     (1, 0),   (1, 0)],
        [(1, 0),    (1, 0),     (1, 0),     (0, 1),     (0, 2),     (0, 2),     (0, 1),     (1, 0),   (1, 0)]]

#GRID = [[(0, "B"), (0, 1), (1, 0)],
#        [(0, 1), (0, 1), (1, 0)],
#        [(1, 0), (1, 0), (1, 0)]]


class Minesweeper(Game):

    def __init__(self, grid=GRID, size=SIZE, bombs=BOMBS):
        self.grid = grid
        self.size = size
        self.bombs = bombs

    # Return whether this game is equivalent to the other
    def __eq__(self, other):
        self.grid = other.grid
        self.size = other.size
        self.bombs = other.bombs

    # Return a hash code for this game
    def __hash__(self):
        return hash((str(self.grid), self.size, self.bombs))

    # Return the utility of this game (if it's over)
    # If this game isn't over yet, return None
    def utility(self):
        count = 0
        win_count = 0

        for r in range(self.size):
            for c in range(self.size):
                (first, second) = self.grid[r][c]
                if second != "B":
                    win_count += 1

        for r in range(self.size):
            for c in range(self.size):
                (first, second) = self.grid[r][c]
                if first == 1 and second == "B":
                    return "You lose :("
                if first == 1:
                    count += 1

        if count == win_count:
            return "You win!"

    # Return a list of legal moves
    def moves(self):
        moves = list()
        for r in range(self.size):
            for c in range(self.size):
                (first, second) = self.grid[r][c]
                if first == 0:
                    moves.append((r, c))
        return moves

    # Return a new game created by a move
    def child(self, move):
        if move is None:
            print("Not sure about next move.")
        (r, c) = move
        (first, second) = self.grid[r][c]
        self.grid[r][c] = (1, second)
        return Minesweeper(self.grid)

    # Print this game to the console
    def display(self):
        for r in range(self.size):
            for c in range(self.size):
                (first, second) = self.grid[r][c]
                if first == 0:
                    print("*", end='')
                else:
                    print(second, end='')
            print()
        print()