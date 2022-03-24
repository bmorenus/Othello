from tile import Tile


def test_constructor():
    t: Tile = Tile(50, 50, "black")
    assert isinstance(t, Tile)
    assert t.x == 50
    assert t.y == 50
    assert t.color == "black"
