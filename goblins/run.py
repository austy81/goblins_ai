import game
from random import randint
import time


def main():
    start = time.time()
    for i in range(1, 100):
        player = 1
        board = game.new_game()
        done = False
        steps = 0
        while not done:
            game.draw_board(board)
            # to = input('Player {} --- Your move [1-9]:'.format(player))
            to = randint(1, 9)
            moved, board, done, winner = game.make_move(to, player, board)
            if moved and not done:
                steps = steps + 1
                player = 1 if player == 2 else 2
        game.draw_board(board)
        print('Game finished, player {} won in {} steps. Run time: {}'.format(winner, steps, (time.time() - start)))


if __name__ == '__main__':
    main()