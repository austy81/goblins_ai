import unittest
import numpy

import goblins.game


class GameTest(unittest.TestCase):
    def test_new_game(self):
        board = goblins.game.new_game()
        expected_board = self._get_board()

        self.assertEqual(len(board), len(expected_board))
        numpy.testing.assert_array_equal(board, expected_board)

    def test_is_not_done(self):
        board = self._get_board()
        done, winner, message = goblins.game.is_done(board)

        self.assertFalse(done)
        self.assertIsNone(winner)

    def test_is_done_win(self):
        board = self._get_board()

        for player in range(1, 2):
            board[0:3] = player
            done, winner, message = goblins.game.is_done(board)

            self.assertTrue(done)
            self.assertEqual(winner, player)

    def test_is_done_full(self):
        board = self._get_board()

        for player in range(1, 2):
            board[0] = player
            board[3] = player
            board[4] = player
            board[5] = player
            done, winner, message = goblins.game.is_done(board)

            self.assertTrue(done)
            self.assertEqual(winner, player)

    def _get_board(self):
        return numpy.zeros((9))
