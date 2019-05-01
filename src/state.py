class State:
    def __init__(self, to_play, red_player, blue_player, probability=1.0, risk=None):
        self.to_play = to_play
        self.red = red_player
        self.blue = blue_player
        self.is_terminal = self.has_move()
        self.risk = risk
        self.probability = probability


    def expand_children(self):
        output = []
        if self.to_play == 'chance':
            return self.expand_chance_node()
        for piece in self.to_play.army:
            if piece.alive and piece.isMovable():
                (col, row) = piece.getPosition()

                if piece.walkFar:
                    dist = range(1, self.to_play.board_width)
                else:
                    dist = [1]

                moves = []

                for d in dist:
                    north = (col, row - d)
                    south = (col, row + d)
                    west = (col - d, row)
                    east = (col + d, row)

                    moves += [direction for direction in [north, south, west, east] if
                              0 <= direction[0] < self.to_play.board_width and
                              0 <= direction[1] < self.to_play.board_width and
                              not self.to_play.army.getUnit(direction[0], direction[1]) and
                              self.to_play.game.legalMove(piece, direction[0], direction[1])]

                for move in moves:
                    attack_move = self.to_play.game.getUnit(move[0], move[1])
                    piece.setPosition(move)
                    if attack_move:
                        output.append(State('chance', self.red, self.blue, 1.0, piece))
                    elif self.to_play == 'Red':
                        output.append(State('Blue', self.red, self.blue))
                    else:
                        output.append(State('Red', self.red, self.blue))
        return output

    def expand_chance_node(self):
        output = []
        if self.risk is None:
            return output
        possible_opponent_ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99]
        for outcome in possible_opponent_ranks:
            pass
            # this is garbage
            # attacker.isKnown = True
            # defender.isKnown = True
            #
            # if defender.name == "Flag":
            #     attacker.position = defender.position
            #     defender.die()
            #     self.victory(attacker.color)
            #
            # elif attacker.canDefuseBomb and defender.name == "Bomb":
            #     attacker.position = defender.position
            #     defender.die()
            #     defenderArmy.nrOfLiving -= 1
            #     defenderArmy.nrOfKnownUnmovable -= 1
            #     attacker.justAttacked = True
            #     if (abs(attacker.position[0] - self.blueArmy.army[0].position[0]) + abs(attacker.position[1] - self.blueArmy.army[0].position[1]) == 1):
            #         self.blueArmy.flagIsBombProtected = False
            #     if (abs(attacker.position[0] - self.redArmy.army[0].position[0]) + abs(attacker.position[1] - self.redArmy.army[0].position[1]) == 1):
            #         self.redArmy.flagIsBombProtected = False
            #
            # elif defender.name == "Bomb":
            #     x, y = defender.getPosition()
            #     x = (x + .5) * self.tilePix
            #     y = (y + .5) * self.tilePix
            #
            #     attackerTag = "u" + str(id(attacker))
            #     attacker.die()
            #     # print 'attacker:', attackerTag, self.map.find_withtag(attackerTag)
            #
            #     self.root.after(200, lambda: self.map.delete(attackerTag))
            #     explosion.kaboom(x, y, 5, self.map, self.root)
            #
            #     attackerArmy.nrOfLiving -= 1
            #     attackerArmy.nrOfKnownMovable -= 1
            #
            # elif attacker.canKillMarshal and defender.name == "Marshal":
            #     attacker.position = defender.position
            #     defenderArmy.nrOfLiving -= 1
            #     defenderArmy.nrOfMoved -= 1
            #     defender.die()
            #     attacker.justAttacked = True
            #
            # elif attacker.rank > defender.rank:
            #     attacker.position = defender.position
            #     defenderArmy.nrOfLiving -= 1
            #     defenderArmy.nrOfMoved -= 1
            #     defender.die()
            #     attacker.justAttacked = True
            #
            # elif attacker.rank == defender.rank:
            #     defenderArmy.nrOfLiving -= 1
            #     defenderArmy.nrOfMoved -= 1
            #     attackerArmy.nrOfLiving -= 1
            #     attackerArmy.nrOfMoved -= 1
            #     attacker.die()
            #     defender.die()
            #
            # else:
            #     attackerArmy.nrOfLiving -= 1
            #     attackerArmy.nrOfMoved -= 1
            #     attacker.die()


    def has_move(self):
        return True