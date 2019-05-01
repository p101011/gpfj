# Copyright Byron Ambright, Peter Day, 2019 ##

import Brain

class ExpectiMinimaxBrain(Brain.Brain):
    def __init__(self, game, army, boardwidth=None, max_depth=5):
        Brain.__init__(self, game, army, boardwidth)
        self.depth = max_depth

    def findMove(self, gamestate):
        best_move = None
        best_move_val = -float('inf')
        for child in gamestate.children:
            if self.evaluate_state(child, self.depth) > best_move_val:
                best_move = child
        return best_move.action

    def placeArmy(self, armyHeight):
        Brain.placeArmy(armyHeight)

    def evaluate_state(self, state, depth):
        if state.is_terminal or depth == 0:
            return self.value(state)
        a = 0
        if state.to_play is self:
            a = -float('inf')
            for child_state in state.expand_children():
                a = max(a, self.evaluate_state(child_state, depth - 1))
        elif state.to_play == "chance":  # we hit this case whenever an unknown piece is attacked
            for outcome in state.expand_children():
                a += outcome.probability * self.evaluate_state(outcome, depth - 1)
        else:
            a = float('inf')
            for child_state in state.expand_children():
                a = min(a, self.evaluate_state(child_state, depth - 1))
        return a

    def value(self, state):
        return 1 if state.is_terminal and state.to_play is not self else 0
