from goblins import game


class AgentMe:

    def __init__(self):
        pass

    def act(self, board):
        game.render(board)
        return input("insert your move [0-8]:")

    def new_game(self):
        pass

    def learn(self, board, action, reward):
        pass
