from utils.framework import Player
from random import choice


class Logic(Player):

    def __init__(self, grid, size, bombs):
        self.grid = grid
        self.size = size
        self.bombs = bombs

    def move(self, game):
        moves = game.moves()

        bombs = set()

        validmoves = set()

        topleft = None
        top = None
        topright = None
        left = None
        right = None
        bottomleft = None
        bottom = None
        bottomright = None
        topleftfirst = None
        topfirst = None
        toprightfirst = None
        leftfirst = None
        rightfirst = None
        bottomleftfirst = None
        bottomfirst = None
        bottomrightfirst = None
        topleftsecond = None
        topsecond = None
        toprightsecond = None
        leftsecond = None
        rightsecond = None
        bottomleftsecond = None
        bottomsecond = None
        bottomrightsecond = None
        centervalue = None
        topleftvalue = None
        topvalue = None
        toprightvalue = None
        leftvalue = None
        rightvalue = None
        bottomleftvalue = None
        bottomvalue = None
        bottomrightvalue = None

        for r in range(self.size):
            for c in range(self.size):
                center = self.grid[r][c]
                (centerfirst, centersecond) = center
                if centerfirst == 1:
                    centervalue = centersecond
                if r > 0 and c > 0:
                    topleft = self.grid[r - 1][c - 1]
                    (topleftfirst, topleftsecond) = topleft
                    if topleftfirst == 1:
                        topleftvalue = topleftsecond
                if r > 0:
                    top = self.grid[r - 1][c]
                    (topfirst, topsecond) = top
                    if topfirst == 1:
                        topvalue = topsecond
                if r > 0 and c < self.size - 1:
                    topright = self.grid[r - 1][c + 1]
                    (toprightfirst, toprightsecond) = topright
                    if toprightfirst == 1:
                        toprightvalue = toprightsecond
                if c > 0:
                    left = self.grid[r][c - 1]
                    (leftfirst, leftsecond) = left
                    if leftfirst == 1:
                        leftvalue = leftsecond
                if c < self.size - 1:
                    right = self.grid[r][c + 1]
                    (rightfirst, rightsecond) = right
                    if rightfirst == 1:
                        rightvalue = rightsecond
                if r < self.size - 1 and c > 0:
                    bottomleft = self.grid[r + 1][c - 1]
                    (bottomleftfirst, bottomleftsecond) = bottomleft
                    if bottomleftfirst == 1:
                        bottomleftvalue = bottomleftsecond
                if r < self.size - 1:
                    bottom = self.grid[r + 1][c]
                    (bottomfirst, bottomsecond) = bottom
                    if bottomfirst == 1:
                        bottomvalue = bottomsecond
                if r < self.size - 1 and c < self.size - 1:
                    bottomright = self.grid[r + 1][c + 1]
                    (bottomrightfirst, bottomrightsecond) = bottomright
                    if bottomrightfirst == 1:
                        bottomrightvalue = bottomrightsecond
                if centervalue == 0:
                    if topleft is not None:
                        validmoves.add((r - 1, c - 1))
                    if top is not None:
                        validmoves.add((r - 1, c))
                    if topright is not None:
                        validmoves.add((r - 1, c + 1))
                    if left is not None:
                        validmoves.add((r, c - 1))
                    if right is not None:
                        validmoves.add((r, c + 1))
                    if bottomleft is not None:
                        validmoves.add((r + 1, c - 1))
                    if bottom is not None:
                        validmoves.add((r + 1, c))
                    if bottomright is not None:
                        validmoves.add((r + 1, c + 1))

                topleft = None
                top = None
                topright = None
                left = None
                right = None
                bottomleft = None
                bottom = None
                bottomright = None
                topleftfirst = None
                topfirst = None
                toprightfirst = None
                leftfirst = None
                rightfirst = None
                bottomleftfirst = None
                bottomfirst = None
                bottomrightfirst = None
                topleftsecond = None
                topsecond = None
                toprightsecond = None
                leftsecond = None
                rightsecond = None
                bottomleftsecond = None
                bottomsecond = None
                bottomrightsecond = None
                topleftvalue = None
                topvalue = None
                toprightvalue = None
                leftvalue = None
                rightvalue = None
                bottomleftvalue = None
                bottomvalue = None
                bottomrightvalue = None
                centervalue = None

        for move in moves:
            if move in validmoves:
                return move

        for r in range(self.size):
            for c in range(self.size):
                center = self.grid[r][c]
                (centerfirst, centersecond) = center
                if centerfirst == 1:
                    centervalue = centersecond
                if r > 0 and c > 0:
                    topleft = self.grid[r - 1][c - 1]
                    (topleftfirst, topleftsecond) = topleft
                    if topleftfirst == 1:
                        topleftvalue = topleftsecond
                if r > 0:
                    top = self.grid[r - 1][c]
                    (topfirst, topsecond) = top
                    if topfirst == 1:
                        topvalue = topsecond
                if r > 0 and c < self.size - 1:
                    topright = self.grid[r - 1][c + 1]
                    (toprightfirst, toprightsecond) = topright
                    if toprightfirst == 1:
                        toprightvalue = toprightsecond
                if c > 0:
                    left = self.grid[r][c - 1]
                    (leftfirst, leftsecond) = left
                    if leftfirst == 1:
                        leftvalue = leftsecond
                if c < self.size - 1:
                    right = self.grid[r][c + 1]
                    (rightfirst, rightsecond) = right
                    if rightfirst == 1:
                        rightvalue = rightsecond
                if r < self.size - 1 and c > 0:
                    bottomleft = self.grid[r + 1][c - 1]
                    (bottomleftfirst, bottomleftsecond) = bottomleft
                    if bottomleftfirst == 1:
                        bottomleftvalue = bottomleftsecond
                if r < self.size - 1:
                    bottom = self.grid[r + 1][c]
                    (bottomfirst, bottomsecond) = bottom
                    if bottomfirst == 1:
                        bottomvalue = bottomsecond
                if r < self.size - 1 and c < self.size - 1:
                    bottomright = self.grid[r + 1][c + 1]
                    (bottomrightfirst, bottomrightsecond) = bottomright
                    if bottomrightfirst == 1:
                        bottomrightvalue = bottomrightsecond

                neighborcount = 0
                for i in range(8):
                    if centervalue == i + 1:
                        neighborcount = 0
                        if topleftvalue is None and topleft is not None:
                            neighborcount += 1
                        if topvalue is None and top is not None:
                            neighborcount += 1
                        if toprightvalue is None and topright is not None:
                            neighborcount += 1
                        if leftvalue is None and left is not None:
                            neighborcount += 1
                        if rightvalue is None and right is not None:
                            neighborcount += 1
                        if bottomleftvalue is None and bottomleft is not None:
                            neighborcount += 1
                        if bottomvalue is None and bottom is not None:
                            neighborcount += 1
                        if bottomrightvalue is None and bottomright is not None:
                            neighborcount += 1

                    if neighborcount == centervalue:
                        if topleftvalue is None and topleft is not None:
                            bombs.add((r - 1, c - 1))
                        if topvalue is None and top is not None:
                            bombs.add((r - 1, c))
                        if toprightvalue is None and topright is not None:
                            bombs.add((r - 1, c + 1))
                        if leftvalue is None and left is not None:
                            bombs.add((r, c - 1))
                        if rightvalue is None and right is not None:
                            bombs.add((r, c + 1))
                        if bottomleftvalue is None and bottomleft is not None:
                            bombs.add((r + 1, c - 1))
                        if bottomvalue is None and bottom is not None:
                            bombs.add((r + 1, c))
                        if bottomrightvalue is None and bottomright is not None:
                            bombs.add((r + 1, c + 1))

                topleft = None
                top = None
                topright = None
                left = None
                right = None
                bottomleft = None
                bottom = None
                bottomright = None
                topleftfirst = None
                topfirst = None
                toprightfirst = None
                leftfirst = None
                rightfirst = None
                bottomleftfirst = None
                bottomfirst = None
                bottomrightfirst = None
                topleftsecond = None
                topsecond = None
                toprightsecond = None
                leftsecond = None
                rightsecond = None
                bottomleftsecond = None
                bottomsecond = None
                bottomrightsecond = None
                topleftvalue = None
                topvalue = None
                toprightvalue = None
                leftvalue = None
                rightvalue = None
                bottomleftvalue = None
                bottomvalue = None
                bottomrightvalue = None
                centervalue = None

        for r in range(self.size):
            for c in range(self.size):
                center = self.grid[r][c]
                (centerfirst, centersecond) = center
                if centerfirst == 1:
                    centervalue = centersecond
                if r > 0 and c > 0:
                    topleft = self.grid[r - 1][c - 1]
                    (topleftfirst, topleftsecond) = topleft
                    if topleftfirst == 1:
                        topleftvalue = topleftsecond
                if r > 0:
                    top = self.grid[r - 1][c]
                    (topfirst, topsecond) = top
                    if topfirst == 1:
                        topvalue = topsecond
                if r > 0 and c < self.size - 1:
                    topright = self.grid[r - 1][c + 1]
                    (toprightfirst, toprightsecond) = topright
                    if toprightfirst == 1:
                        toprightvalue = toprightsecond
                if c > 0:
                    left = self.grid[r][c - 1]
                    (leftfirst, leftsecond) = left
                    if leftfirst == 1:
                        leftvalue = leftsecond
                if c < self.size - 1:
                    right = self.grid[r][c + 1]
                    (rightfirst, rightsecond) = right
                    if rightfirst == 1:
                        rightvalue = rightsecond
                if r < self.size - 1 and c > 0:
                    bottomleft = self.grid[r + 1][c - 1]
                    (bottomleftfirst, bottomleftsecond) = bottomleft
                    if bottomleftfirst == 1:
                        bottomleftvalue = bottomleftsecond
                if r < self.size - 1:
                    bottom = self.grid[r + 1][c]
                    (bottomfirst, bottomsecond) = bottom
                    if bottomfirst == 1:
                        bottomvalue = bottomsecond
                if r < self.size - 1 and c < self.size - 1:
                    bottomright = self.grid[r + 1][c + 1]
                    (bottomrightfirst, bottomrightsecond) = bottomright
                    if bottomrightfirst == 1:
                        bottomrightvalue = bottomrightsecond

                neighborcount = 0
                bombcount = 0
                for i in range(8):
                    if centervalue == i + 1:
                        neighborcount = 0
                        if topleftvalue is None and topleft is not None:
                            neighborcount += 1
                        if topvalue is None and top is not None:
                            neighborcount += 1
                        if toprightvalue is None and topright is not None:
                            neighborcount += 1
                        if leftvalue is None and left is not None:
                            neighborcount += 1
                        if rightvalue is None and right is not None:
                            neighborcount += 1
                        if bottomleftvalue is None and bottomleft is not None:
                            neighborcount += 1
                        if bottomvalue is None and bottom is not None:
                            neighborcount += 1
                        if bottomrightvalue is None and bottomright is not None:
                            neighborcount += 1

                        bombcount = 0
                        if (r - 1, c - 1) in bombs and topleft is not None:
                            bombcount += 1
                        if (r - 1, c) in bombs and top is not None:
                            bombcount += 1
                        if (r - 1, c + 1) in bombs and topright is not None:
                            bombcount += 1
                        if (r, c - 1) in bombs and left is not None:
                            bombcount += 1
                        if (r, c + 1) in bombs and right is not None:
                            bombcount += 1
                        if (r + 1, c - 1) in bombs and bottomleft is not None:
                            bombcount += 1
                        if (r + 1, c) in bombs and bottom is not None:
                            bombcount += 1
                        if (r + 1, c + 1) in bombs and bottomright is not None:
                            bombcount += 1

                    if centervalue == bombcount and neighborcount > centervalue:
                        if (r - 1, c - 1) not in bombs and topleft is not None and topleftfirst == 0:
                            validmoves.add((r - 1, c - 1))
                        if (r - 1, c) not in bombs and top is not None and topfirst == 0:
                            validmoves.add((r - 1, c))
                        if (r - 1, c + 1) not in bombs and topright is not None and toprightfirst == 0:
                            validmoves.add((r - 1, c + 1))
                        if (r, c - 1) not in bombs and left is not None and leftfirst == 0:
                            validmoves.add((r, c - 1))
                        if (r, c + 1) not in bombs and right is not None and rightfirst == 0:
                            validmoves.add((r, c + 1))
                        if (r + 1, c - 1) not in bombs and bottomleft is not None and bottomleftfirst == 0:
                            validmoves.add((r + 1, c - 1))
                        if (r + 1, c) not in bombs and bottom is not None and bottomfirst == 0:
                            validmoves.add((r + 1, c))
                        if (r + 1, c + 1) not in bombs and bottomright is not None and bottomrightfirst == 0:
                            validmoves.add((r + 1, c + 1))



                topleft = None
                top = None
                topright = None
                left = None
                right = None
                bottomleft = None
                bottom = None
                bottomright = None
                topleftfirst = None
                topfirst = None
                toprightfirst = None
                leftfirst = None
                rightfirst = None
                bottomleftfirst = None
                bottomfirst = None
                bottomrightfirst = None
                topleftsecond = None
                topsecond = None
                toprightsecond = None
                leftsecond = None
                rightsecond = None
                bottomleftsecond = None
                bottomsecond = None
                bottomrightsecond = None
                topleftvalue = None
                topvalue = None
                toprightvalue = None
                leftvalue = None
                rightvalue = None
                bottomleftvalue = None
                bottomvalue = None
                bottomrightvalue = None
                centervalue = None

        for move in moves:
            if move in validmoves:
                return move

        for move in moves:
            if move not in bombs and len(bombs) == self.bombs:
                return move


        randommove = choice(game.moves())
        while randommove in bombs:
            randommove = choice(game.moves())
        return randommove