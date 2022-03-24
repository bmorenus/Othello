from board_square import BoardSquare
from game_board import GameBoard
from tile import Tile


def test_constructor():
    gb: GameBoard = GameBoard(board_size=800)
    bs: BoardSquare = BoardSquare(gb, x=0, y=0, x_index=0, y_index=0)
    assert isinstance(bs, BoardSquare)
    assert bs.x == 0
    assert bs.y == 0
    assert bs.x_index == 0
    assert bs.y_index == 0
    assert bs.tile is None
    assert bs.tile_hint is None

    bs.tile = Tile(50, 50, "black")
    assert bs.tile is not None
    assert bs.tile.x == 50
    assert bs.tile.y == 50
    assert bs.tile.color == "black"

    bs: BoardSquare = BoardSquare(
        gb, x=0, y=0, x_index=0, y_index=0, tile=Tile(50, 50, "black"))
    assert bs.tile is not None
    assert bs.tile.x == 50
    assert bs.tile.y == 50
    assert bs.tile.color == "black"


def test_is_empty():
    gb: GameBoard = GameBoard(board_size=800)
    bs: BoardSquare = BoardSquare(gb, x=0, y=0, x_index=0, y_index=0)
    assert bs.is_empty is True
    bs.tile = Tile(50, 50, "black")
    assert bs.is_empty is False
