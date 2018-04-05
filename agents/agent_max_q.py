import numpy as np
from random import randint


Q = np.zeros([3 ** 10, 10])
alpha = 0.618


def act(board):
    state_number = _board_to_state(board)
    if all(item == 0 for item in Q[state_number]):
        return randint(1, 9)
    action = np.argmax(Q[state_number])
    return action


def learn(old_board, new_board, action, reward):
    old_state = _board_to_state(old_board)
    new_state = _board_to_state(new_board)
    Q[old_state, action] += alpha * \
        (reward + np.max(Q[new_state]) - Q[old_state, action])


def _board_to_state(board):
    state = 0
    for index in range(0, len(board)-1):
        state += board[index] * (3 ** index)
    return int(state)