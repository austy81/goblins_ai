import numpy as np
from random import randint
import time

from agents.agent_max_q import Agent

from goblins import game

# FIX when player one wins
# https://github.com/DanielSlater/AlphaToe
def run():
    a1 = Agent()
    a2 = Agent()
    no_wins = [0, 0, 0]

    for episode in range(1, 100001):
        done = False
        player_1 = 1
        player_2 = 2
        cur_player = 1
        board = game.new_game()
        while not done:
            moved = False
            if player_1 == cur_player:
                initial_board = list(board)
                action = a1.act(board)
                moved, board, done, winner, info = game.make_move(
                    action, cur_player, board)
                
                reward = _get_reward(moved, done, winner == cur_player)
                a1.learn(initial_board, action, reward)
            else:
                initial_board = list(board)
                action = a2.act(board)
                moved, board, done, winner, info = game.make_move(
                    action, cur_player, board)
                reward = _get_reward(moved, done, winner == cur_player)
                a2.learn(initial_board, action, reward)
            if done:
                no_wins[cur_player] = no_wins[cur_player] + 1
                other_player = player_1 if cur_player == player_2 else player_2
                if other_player == 1:
                    a1.learn(list(board), 0, -20)
                else:
                    a2.learn(list(board), 0, -20)

                a1.new_game()
                a2.new_game()
            if moved:
                cur_player = player_1 if cur_player == player_2 else player_2

        if episode % 10 == 0:
            game.render(board)
            time.sleep(1)
            print('Episode {} player1 wins:{}'.format(episode, no_wins[2]))


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
