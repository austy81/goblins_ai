import numpy


def draw_board(b):
    print('-------')
    print('|{:01.0f}|{:01.0f}|{:01.0f}|'.format(b[0], b[1], b[2]))
    print('-------')
    print('|{:01.0f}|{:01.0f}|{:01.0f}|'.format(b[3], b[4], b[5]))
    print('-------')
    print('|{:01.0f}|{:01.0f}|{:01.0f}|'.format(b[6], b[7], b[8]))
    print('-------')


def move(to, player, board):
    try:
        to = int(to) - 1
    except:
        print('Wrong input [{}]'.format(to))
        return False, board

    if to > 8 or to < 0:
        print('Input must be between 1 - 9. Entered: {}'.format(to))
        return False, board

    if not isinstance(player, int) or player < 1 or player > 2:
        print('Player must be number 1 or 2')
        return False, board

    if board[to] > 0:
        print('Field is already taken.') 
        return False, board

    board[to] = player
    return True, board


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
                return True, player
    
    # All fields are filled?
    for cell in board:
        if cell == 0:
            return False, None
    print("FULL")
    return True, None


def new_game():
    return numpy.zeros((9))


def make_move(to, player, board):
    moved, board = move(to, player, board)
    done, winner = is_done(board)
    return moved, board, done, winner
