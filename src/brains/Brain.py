'''
Created on 29 jun. 2012

Template brain

@author: Jeroen Kools
'''

from random import shuffle, choice


# noinspection PyPep8Naming
class Brain:
    def __init__(self, game, army, boardWidth=None):
        self.army = army
        self.game = game

        global BOARD_WIDTH
        if boardWidth:
            BOARD_WIDTH = boardWidth

    def placeArmy(self, armyHeight):

        positions = []

        if self.army.color == "Blue":
            rows = range(armyHeight)
        else:
            rows = range(BOARD_WIDTH - armyHeight, BOARD_WIDTH)

        for row in rows:
            for column in range(BOARD_WIDTH):
                if self.army.getUnit(column, row) is None:
                    positions += [(column, row)]

        shuffle(positions)

        for unit in self.army.army:
            if unit.isOffBoard():
                unit.position = positions.pop()

    def findMove(self, gamestate):
        # Find a move given the current board situation
        # Returns (oldPosition, newPosition)
        pass
