"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = game_agent.MinimaxPlayer()
        self.game = isolation.Board(self.player1, self.player2)
        print(self.game.to_string())
        self.game.apply_move((3, 3))
        print(self.game.to_string())
        self.game.apply_move((4, 4))
        print(self.game.to_string())
        self.game.apply_move((5, 4))
        print(self.game.to_string())
        self.game.apply_move((6, 5))
        print(self.game.to_string())
        self.game.apply_move((4, 6))
        print(self.game.to_string())


    def test_legal_moves_quantity(self):
        self.assertEqual(self.game.active_player, self.player2)
        self.assertEqual(len(self.game.get_legal_moves()), 1)

    def test_just_play(self):
        self.game.play()

if __name__ == '__main__':
    unittest.main()
