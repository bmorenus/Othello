from board_square import BoardSquare
from legal_move import LegalMove
from game_board import GameBoard
from board_corner import BoardCorner


def test_constructor():
    gb: GameBoard = GameBoard(board_size=800)
    lm: LegalMove = LegalMove(
        gb.board[5][4], set(), 1, gb.BOARD_CORNERS[0], False, False
    )

    assert isinstance(lm, LegalMove)
    assert isinstance(lm.player_square, BoardSquare)
    assert isinstance(lm.flippable_squares, set)
    assert isinstance(lm.board_corner, BoardCorner)

    assert lm.total_flips == 1
    assert lm.is_corner_move is False
    assert lm.is_edge_move is False
    assert lm.move_value == 0
    assert lm.max_tiles == 0


def test_move_value_comparison():
    gb: GameBoard = GameBoard(board_size=800)
    lm_1: LegalMove = LegalMove(gb.board[5][4], set(), 0, None, False, False)

    lm_2: LegalMove = LegalMove(gb.board[2][3], set(), 0, None, False, False)

    assert lm_1 == lm_2
    lm_1.move_value = 1.0
    assert lm_1 > lm_2
    assert lm_2 < lm_1
