from random import randint


class AgentRandom:

    def __init__(self):
        pass

    def act(self, board):
        return randint(0, 8)

    def new_game(self):
        pass

    def learn(self, board, action, reward):
        pass
