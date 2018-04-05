import numpy as np
import math
from random import randint
import time

from agents import agent_max_q
from goblins import game


# https://www.oreilly.com/ideas/reinforcement-learning-with-tensorflow
def run():

    won_games = 0
    for episode in range(1, 1000001):
        done = False
        player_1 = 1
        player_2 = 2
        cur_player = 1
        board = game.new_game()
        while not done:
            moved = False
            if player_1 == cur_player:
                action = agent_max_q.act(board)
                moved, board, done, winner, info = game.make_move(
                    action, player_1, board)  # 2
                state2 = board
                state2_number = _board_to_state(state2)
                won_games += 1 if done and winner == player_1 else 0
                reward = _get_reward(moved, done, winner == player_1)
                #print(reward, G)
                #input()
                if np.max(Q[state2_number]) > 0:
                    pass
                Q[state_number, action] += alpha * (reward + np.max(Q[state2_number]) - Q[state_number, action])  # 3
                G += reward
                board = state2
            else:
                moved, board, done, winner, info = game.make_move(
                    randint(1, 9), player_2, board)
            #game.render(state)
            #time.sleep(0.2)
            if moved:
                cur_player = player_1 if cur_player == player_2 else player_2

        if episode % 10 == 0:
            print('Episode {} Total Reward: {}. Won games {}'.format(episode, G, won_games))
            won_games = 0





def _get_reward(moved, done, winner):
    if not moved:
        return -10
    if done and winner:
        return +10
    if done and not winner:
        return -5
    return 1





run()
