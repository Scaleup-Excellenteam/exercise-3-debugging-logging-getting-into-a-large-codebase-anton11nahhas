import unittest
from unittest.mock import patch, Mock
from Piece import Knight
from chess_engine import game_state
import chess_engine
from enums import Player
import ai_engine

"""
3 unit tests of 3 different occasions of the knight positioning
"""
class TestKnight(unittest.TestCase):

    """
    this test is a unitest, and it checks if the function get valid peaceful moves returns the correct tuples
    the board has all the pieces however the knight is found in the position 3, 4 in the board
    the result of tuples must be the size of 6 since there are only 6 positions the knight can
    go from that position, the two other possible positions are not empty, there are white pawns
    in them so they wont be included in the result.

    """
    def test_get_valid_peaceful_moves(self):
        game_state_1 = chess_engine.game_state()
        knight = Knight('n', 3, 4, Player.PLAYER_1)
        result = knight.get_valid_peaceful_moves(game_state_1)
        self.assertEqual(result, [(2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3)])

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
        self.assertEqual(result, [(6, 3), (6, 7), (7, 6), (7, 4)])

    """
        this test is a uni test, where it clears the board and only adds a knight in the position 3,4 
        then it checks if the tuples return by both function checked above are correct, the first result
        must return a tuple of size 8 with all the possibilities since the board is empty. whereas the 
        second result must return an empty list since there are no rival pieces in the board, thus no
        valid takes.
    """
    def test_both(self):
        game_state_3 = chess_engine.game_state()
        game_state_3.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        knight = Knight('n', 3, 4, Player.PLAYER_1)
        result1 = knight.get_valid_peaceful_moves(game_state_3)
        result2 = knight.get_valid_piece_takes(game_state_3)
        self.assertEqual(result1, [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3)])
        self.assertEqual(result2, [])

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
        self.assertEqual(result, [(3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 6), (7, 4)])


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
        self.assertEqual(result, 0)

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
        self.assertEqual(result, 0)


