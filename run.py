import time

from agents import agent_max_q
from agents import agent_me
from agents import agent_random
from agents import agent_next
from agents import agent_keras

from goblins import game


reward_win = 1
reward_lost = 0
reward_draw = 0
reward_illegal_move = -10

# https://github.com/DanielSlater/AlphaToe
def run():
    a1 = agent_random.AgentRandom()
    a2 = agent_random.AgentRandom()
    a1_learn = agent_keras.AgentKeras()
    a2_learn = agent_keras.AgentKeras()
    no_wins = [0, 0, 0]
    player_1 = 1
    player_2 = 2

    for episode in range(1, 10001):
        done = False
        cur_player = player_1
        cur_agent = a1
        cur_learn_agent = a1_learn
        board = game.new_game()
        while not done:
            initial_board = list(board)
            action = cur_agent.act(board)
            moved, board, done, winner, info = game.make_move(
                action, cur_player, board)
            reward = _get_reward(moved, done, winner, cur_player)
            cur_learn_agent.learn(initial_board, action, reward)

            if done:
                if winner:
                    no_wins[cur_player] += 1
                    if cur_player == player_2:
                        a1_learn.learn(list(board), 0, reward_lost)
                    else:
                        a2_learn.learn(list(board), 0, reward_lost)
                else:  # draw game
                    no_wins[0] += 1
                a1.new_game()
                a2.new_game()
                a1_learn.new_game()
                a2_learn.new_game()

            if moved:
                cur_agent = a1 if cur_player == player_2 else a2
                cur_player = player_1 if cur_player == player_2 else player_2
                cur_learn_agent = a1_learn if cur_learn_agent == a2_learn else a2_learn

        if episode % 100 == 0:
            game.render(board)
            print('Episode {} WINS {}: {} {}: {} DRAWS: {}'.format(
                episode, a1.__class__.__name__, no_wins[1], a2.__class__.__name__, no_wins[2], no_wins[0]))
            no_wins = [0, 0, 0]
        
        if episode == 500:
            a1 = a1_learn
            a1_learn = agent_random.AgentRandom()
            a2_learn = agent_random.AgentRandom()


def _get_reward(moved, done, winner, cur_player):
    if not moved:
        return reward_illegal_move
    if done and not winner:  # DRAW
        return reward_draw
    if done and winner == cur_player:  # WIN
        return reward_win
    if done and winner != cur_player:  # LOST
        return reward_lost
    return 0


def _board_to_state(board):
    state = 0
    for index in range(0, len(board)-1):
        state += board[index] * (3 ** index)
    return int(state)


run()
