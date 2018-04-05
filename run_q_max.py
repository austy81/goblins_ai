import numpy as np
from random import randint
import time

from agents import agent_max_q as a1
from agents import agent_max_q as a2

from goblins import game


# https://github.com/DanielSlater/AlphaToe
def run():
    winner = [0, 0, 0]
    for episode in range(1, 1000001):
        done = False
        player_1 = 1
        player_2 = 2
        cur_player = 1
        board = game.new_game()
        while not done:
            moved = False
            if player_1 == cur_player:
                action = a1.act(board)
                old_board = board
                moved, board, done, winner, info = game.make_move(
                    action, cur_player, board)  # 2
                reward = _get_reward(moved, done, winner == cur_player)
                a1.learn(old_board, board, action, reward)
            else:
                # moved, board, done, winner, info = game.make_move(
                #     randint(1, 9), player_2, board)
                action = a2.act(board)
                old_board = board
                moved, board, done, winner, info = game.make_move(
                    action, cur_player, board)  # 2
                reward = _get_reward(moved, done, winner == cur_player)
                a2.learn(old_board, board, action, reward)
            #game.render(board)
            #time.sleep(0.1)
            if done and cur_player:
                winner[cur_player] = winner[cur_player] + 1
            if moved:
                cur_player = player_1 if cur_player == player_2 else player_2


        if episode % 1000 == 0:
            print('Episode {} player1 wins:{}'.format(episode, winner[0]))


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
