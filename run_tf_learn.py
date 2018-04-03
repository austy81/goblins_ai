import numpy as np
import math
from random import randint
import time


from goblins import game


def run():
    Q = np.zeros([3 ** 10, 10])
    G = 0
    alpha = 0.618
    for episode in range(1, 1000001):
        done = False
        G, reward = 0, 0
        ai_player = 1
        random_player = 2
        cur_player = 1
        state = game.new_game()
        while not done:
            moved = False
            if ai_player == cur_player:
                state_number = _board_to_state(state)
                action = np.argmax(Q[state_number])  # 1
                moved, board, done, winner, info = game.make_move(
                    action, ai_player, state)  # 2
                state2 = board
                state2_number = _board_to_state(state2)

                reward = _get_reward(moved, done, winner == ai_player)
                #print(reward, G)
                #input()
                Q[state_number, action] += alpha * (reward + np.max(Q[state2_number]) - Q[state_number, action])  # 3
                G += reward
                state = state2
            else:
                moved, board, done, winner, info = game.make_move(
                    randint(1, 9), random_player, state)
            #game.render(state)
            #time.sleep(0.1) 
            if moved:
                cur_player = ai_player if cur_player == random_player else random_player

        if episode % 1000 == 0:
            print('Episode {} Total Reward: {}'.format(episode, G))


def _get_reward(moved, done, winner):
    if not moved:
        return -10
    if done and winner:
        return +10
    if done and not winner:
        return -5
    return 1


def _board_to_state(board):
    state = 0
    for index in range(0, len(board)-1):
        state += board[index] * (3 ** index)
    return int(state)


run()
