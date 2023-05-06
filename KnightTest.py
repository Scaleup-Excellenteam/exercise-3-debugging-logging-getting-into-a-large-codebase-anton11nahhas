import unittest
from unittest.mock import patch, Mock

import pytest as pytest

from Piece import Knight
from chess_engine import game_state
import chess_engine
from enums import Player
import ai_engine

"""
3 unit tests of 3 different occasions of the knight positioning
"""
class TestKnight(unittest.TestCase):

    def empty_board(self):
        game_board = game_state()
        game_board.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        return game_board

    """
    this test is a unitest, and it checks if the function get valid peaceful moves returns the correct tuples
    the board is clear and has no pieces, the knight is in the position 3,4 and the tuples needed are found
    in expected results after calling the peaceful_moves method.

    """

    def test_get_valid_peaceful_moves(self):
        empty_board = self.empty_board()
        knight = Knight('n', 3, 4, Player.PLAYER_1)
        with patch.object(empty_board, 'get_piece', return_value=Player.EMPTY):
            result = knight.get_valid_peaceful_moves(empty_board)
            expected_result = [(5, 5), (1, 5), (4, 6), (4, 2), (2, 6), (2, 2), (5, 3), (1, 3)]
            self.assertEqual(set(result), set(expected_result))

    """
    this testis a unitest, and it checks if the function get valid piece takes returns the correct tuples.
    again the board has all the pieces in their starting positions, so when a knight is in
    the position 5,5 the valid piece takes, or the positions there are the rival's pieces, are
    the ones being tested.
    """
    def test_get_valid_piece_takes(self):
        game_state_2 = chess_engine.game_state()
        knight = Knight('n', 5,5, Player.PLAYER_1)
        result = knight.get_valid_piece_takes(game_state_2)
        expected_result = [(6, 3), (6, 7), (7, 6), (7, 4)]
        self.assertEqual(result, expected_result)

    """
        this test is a uni test, where it clears the board and only adds a knight in the position 3,4 
        then it checks if the tuples return by both function checked above are correct, the first result
        must return a tuple of size 8 with all the possibilities since the board is empty. whereas the 
        second result must return an empty list since there are no rival pieces in the board, thus no
        valid takes.
    """
    def test_both(self):
        empty_board = self.empty_board()
        knight = Knight('n', 3, 4, Player.PLAYER_1)
        with patch.object(empty_board, 'get_piece', return_value=Player.EMPTY):
            result1 = knight.get_valid_peaceful_moves(empty_board)
            result2 = knight.get_valid_piece_takes(empty_board)
            expected_result1 = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3)]
            expected_result2 = []
            self.assertEqual(result1, expected_result1)
            self.assertEqual(result2, expected_result2)



    """
    this test is an integration test, since it calls a function that calls another 2 functions.
    the test checks if the function get_valid_piece_moves returns the correct tuple of positions.
    the function must return all the peacful positions and the valid takes positions. in this case
    the number of positions are 8.  
    """
    def test_get_valid_piece_moves(self):
        game_state_4 = chess_engine.game_state()
        knight = Knight('n', 5, 5, Player.PLAYER_1)
        result = knight.get_valid_piece_moves(game_state_4)
        expected_result = [(3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 6), (7, 4)]
        self.assertEqual(result, expected_result)


    """
    this test is an integration test, since it is testing multiple functionalities in the code, this is
    done by calling a function that calls other functions. In our case, we create a game_state object and 
    an ai object, then we call the evaluate function which computes the evalutation score for the white player
    meaning how much do the rival pieces cost. in this case, a board full of pieces. the evaluation must be 0.
    """
    def test_evaluate_board(self):
        game_state_5 = chess_engine.game_state()
        ai = ai_engine.chess_ai()
        result = ai.evaluate_board(game_state_5, Player.PLAYER_1)
        expected_result = 0
        self.assertEqual(result, expected_result)

    """
    this is a systemic test, where it tests a full game of chess, the test performs the fools
    mate, which is the fastest game of reaching a checkmate, in this case the white looses, so
    after we perform our movements we call the checkmate function which must return 0 if white lost. 
    """
    def test_fools_mate(self):
        game_state_6 = chess_engine.game_state()
        game_state_6.move_piece((1, 2), (2, 2), False)
        game_state_6.move_piece((6, 3), (5, 3), False)
        game_state_6.move_piece((1, 1), (3, 1), False)
        game_state_6.move_piece((7, 4), (3, 0), False)
        result = game_state_6.checkmate_stalemate_checker()
        expected_result = 0
        self.assertEqual(result, expected_result)


