from scoreboard import Scoreboard
from game_controller import GameController


def test_constructor():
    gc: GameController = GameController(800, 800, 100, "Brian", "y", "h", {})
    assert isinstance(gc.sb, Scoreboard)
    assert gc.sb.width == 800
    assert gc.sb.height == 100
    assert gc.sb.color == "#808080"
