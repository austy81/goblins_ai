import numpy as np
from random import randint


class AgentMaxQ:

    def __init__(self):
        self.Q = np.zeros([3 ** 9, 9])
        self.history = []
        self.alpha = 0.618

    def act(self, board):
        state_number = self._board_to_state(board)
        if all(item == 0 for item in self.Q[state_number]):
            return randint(0, 8)
        action = np.argmax(self.Q[state_number])
        return action

    def new_game(self):
        self.history = []

    def learn(self, board, action, reward):
        state = self._board_to_state(board)
        if reward == -100:
            self.Q[state, action] += -100
            return
        self.history.append(
            {'state': state, 'action': action, 'reward': reward})
        self._propagate_reward(reward)

    def _propagate_reward(self, reward):
        max_history = len(self.history)
        for i in range(0, max_history):
            exponent = max_history - i
            reward_lowered = reward * (self.alpha ** exponent)
            self.Q[self.history[i]['state'], self.history[i]['action']] += reward_lowered

            # alpha * (reward + np.max(Q[new_state]) - Q[old_state, action])

    def _board_to_state(self, board):
        state = 0
        for index in range(0, len(board)-1):
            state += board[index] * (3 ** index)
        return int(state)
