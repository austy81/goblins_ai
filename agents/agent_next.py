

class AgentNext:

    def __init__(self):
        self.next = 0

    def act(self, board):
        return self.next

    def new_game(self):
        self.next = 0

    def learn(self, board, action, reward):
        if reward < 0: 
            self.next += 1
        if self.next > 8:
            self.next = 0
