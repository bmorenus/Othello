import pytest

from banner import Banner
from player import Player
from game_board import GameBoard


@pytest.mark.skip(reason="Processing fonts must be imported to create Banner")
def test_constructor():
    gb: GameBoard = GameBoard(board_size=400)
    p: Player = Player(gb, "Player", "black")
    b: Banner = Banner(p, 18, 20)
    assert isinstance(b, Banner)
    assert isinstance(b.p, Player)
    assert b.winner == p
    assert b.player_1_score == 18
    assert b.player_2_score == 20
