import numpy
from colorama import init
from colorama import Fore, Back, Style
import logging

init()


def render(b):
    # print(numpy.reshape(b, (3, 3)))
    for row in range(0, 3):
        print(Style.RESET_ALL+'-------')
        print_row = '|'
        for column in range(0, 3):
            print_row += _colorize(b[column + (3*row)]) + '|'
        print(print_row)
    print(Style.RESET_ALL+'-------')


def _colorize(player):
    if(player == 1):
        return Fore.RED + 'X' + Style.RESET_ALL
    if(player == 2):
        return Fore.GREEN + 'O' + Style.RESET_ALL
    if(player == 0):
        return ' '


def _move(to, player, board):
    try:
        to = int(to) - 1
    except:
        return False, board, 'Wrong input [{}]'.format(to)

    if to > 8 or to < 0:
        return False, board, 'Input must be between 1 - 9. Entered: {}'.format(to)

    if not isinstance(player, int) or player < 1 or player > 2:
        return False, board, 'Player must be number 1 or 2'

    if board[to] > 0:
        return False, board, 'Field is already taken.'

    board[to] = player
    return True, board, 'OK'


def is_done(board):
    # Any player has copleted row?
    win_configs = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]]
    for player in range(1, 2):
        for win_config in win_configs:
            done = True
            for index in win_config:
                if board[index-1] != player:
                    done = False
                    next
            if done:
                return True, player, "Player {} completed row.".format(player)

    # All fields are filled?
    for cell in board:
        if cell == 0:
            return False, None, "No"
    return True, None, "Board is full."


def new_game():
    return numpy.zeros((9))


def make_move(to, player, board):
    moved, board, move_info = _move(to, player, board)
    done, winner, done_info = is_done(board)
    return moved, board, done, winner, 'Is Done:{} Move info:{}'.format(done_info, move_info)
