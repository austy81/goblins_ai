from goblins import game
from random import randint
import time


def main():
    # start = time.time()
    for i in range(1, 100):
        player = 1
        board = game.new_game()
        done = False
        while not done:
            print('')
            game.render(board)
            if player == 1:
                to = input('Player {} --- Your move [1-9]:'.format(player))
            else:
                to = randint(1, 9)
            moved, board, done, winner, info = game.make_move(
                to, player, board)
            print(info)
            if moved and not done:
                player = 1 if player == 2 else 2
        game.render(board)
        print('RESULTS above, board below.')

        # print('Game finished, player {} won. Run time: {}'.format(
        #     winner, (time.time() - start)))


if __name__ == '__main__':
    main()
