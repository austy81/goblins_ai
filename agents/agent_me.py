from goblins import game


class AgentMe:

    def __init__(self):
        pass

    def act(self, board):
        game.render(board)
        return int(input("insert your move [1-9]:")) - 1

    def new_game(self):
        pass

    def learn(self, board, action, reward):
        pass
