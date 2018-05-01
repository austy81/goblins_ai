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
        if reward < -1:
            self.Q[state, action] += reward
            return
        self.history.append(
            {'state': state, 'action': action, 'reward': reward})
        self._propagate_reward(reward)

    def _propagate_reward(self, reward):
        alfa = 0.68
        reward_coeficient = alfa ** 9
        for history_entry in self.history:
            state = history_entry['state']
            action = history_entry['action']     
            self.Q[state, action] += reward * reward_coeficient
            reward_coeficient = reward_coeficient / alfa

            # alpha * (reward + np.max(Q[new_state]) - Q[old_state, action])

    def _board_to_state(self, board):
        state = 0
        for index in range(0, len(board)-1):
            state += board[index] * (3 ** index)
        return int(state)
