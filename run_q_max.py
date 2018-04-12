import numpy as np
from random import randint
import time

from agents import agent_max_q
from agents import agent_me
from agents import agent_random

from goblins import game


# https://github.com/DanielSlater/AlphaToe
def run():
    a1 = agent_max_q.AgentMaxQ()
    a2 = agent_max_q.AgentMaxQ()
    no_wins = [0, 0, 0]

    for episode in range(1, 20001):
        done = False
        player_1 = 1
        player_2 = 2
        cur_player = 1
        cur_agent = a1
        board = game.new_game()
        while not done:
            initial_board = list(board)
            action = cur_agent.act(board)
            moved, board, done, winner, info = game.make_move(
                action, cur_player, board)
            reward = _get_reward(moved, done, winner == cur_player)
            cur_agent.learn(initial_board, action, reward)

            if done and winner:
                no_wins[cur_player] += 1
                other_player = player_1 if cur_player == player_2 else player_2
                if other_player == 1:
                    a1.learn(list(board), 0, -20)
                else:
                    a2.learn(list(board), 0, -20)

                a1.new_game()
                a2.new_game()
            if done and not winner:
                no_wins[0] += 1
            if moved:
                cur_agent = a1 if cur_player == player_2 else a2
                cur_player = player_1 if cur_player == player_2 else player_2

        if episode % 1000 == 0:
            # a1 = agent_me()
            game.render(board)
            print('Episode {} WINS {}: {} {}: {} DRAWS: {}'.format(episode, a1.__class__.__name__, no_wins[1], a2.__class__.__name__, no_wins[2], no_wins[0]))
            # time.sleep(1)
            no_wins = [0, 0, 0]


def _get_reward(moved, done, winner):
    if not moved:
        return -100
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
