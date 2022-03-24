from board_corner import BoardCorner
from game_board import GameBoard


def test_constructor():
    gb: GameBoard = GameBoard(board_size=800)
    # All 4 board corners exist
    assert isinstance(gb.BOARD_CORNERS[0], BoardCorner)
    assert isinstance(gb.BOARD_CORNERS[1], BoardCorner)
    assert isinstance(gb.BOARD_CORNERS[2], BoardCorner)
    assert isinstance(gb.BOARD_CORNERS[3], BoardCorner)

    # All 4 board corner object have the proper corner square
    assert gb.BOARD_CORNERS[0].corner_square.x_index == 0
    assert gb.BOARD_CORNERS[0].corner_square.y_index == 0
    assert gb.BOARD_CORNERS[1].corner_square.x_index == 7
    assert gb.BOARD_CORNERS[1].corner_square.y_index == 0
    assert gb.BOARD_CORNERS[2].corner_square.x_index == 0
    assert gb.BOARD_CORNERS[2].corner_square.y_index == 7
    assert gb.BOARD_CORNERS[3].corner_square.x_index == 7
    assert gb.BOARD_CORNERS[3].corner_square.y_index == 7

    # All 4 board corner object have the correctly associated x-squares
    assert (1, 0) in gb.BOARD_CORNERS[0].x_squares
    assert (1, 1) in gb.BOARD_CORNERS[0].x_squares
    assert (0, 1) in gb.BOARD_CORNERS[0].x_squares

    assert (6, 0) in gb.BOARD_CORNERS[1].x_squares
    assert (6, 1) in gb.BOARD_CORNERS[1].x_squares
    assert (7, 1) in gb.BOARD_CORNERS[1].x_squares

    assert (0, 6) in gb.BOARD_CORNERS[2].x_squares
    assert (1, 6) in gb.BOARD_CORNERS[2].x_squares
    assert (1, 7) in gb.BOARD_CORNERS[2].x_squares

    assert (6, 6) in gb.BOARD_CORNERS[3].x_squares
    assert (6, 7) in gb.BOARD_CORNERS[3].x_squares
    assert (7, 6) in gb.BOARD_CORNERS[3].x_squares
