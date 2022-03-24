from legal_move import LegalMove
from player import Player
from game_board import GameBoard


def test_constructor():
    gb: GameBoard = GameBoard(board_size=400)
    p: Player = Player(gb, "Player", "black")
    assert p.gb == gb
    assert p.name == "Player"
    assert p.color == "black"

    p: Player = Player(gb, "Computer", "white")
    assert p.gb == gb
    assert p.name == "Computer"
    assert p.color == "white"


def test_take_turn():
    gb: GameBoard = GameBoard(board_size=800)
    board_square = gb.board[5][4]
    lm: LegalMove = LegalMove(gb.board[2][3],
                              set(),
                              1,
                              None,
                              False,
                              False)
    gb.legal_moves = [lm]
    p: Player = Player(gb, "Player", "black")

    # Confirm after player takes their turn, turn_complete changes to True and
    # a tile is placed in the box they clicked on
    assert p.turn_complete is False
    assert gb.board[2][3].is_empty is True
    p.take_turn(350, 350)
    assert p.turn_complete is True
    assert gb.board[2][3].is_empty is False

    # Confirm when a player cannot place a tile in a box that already has one
    gb: GameBoard = GameBoard(board_size=800)
    p: Player = Player(gb, "Player", "white")
    assert gb.board[3][4].is_empty is False
    assert gb.board[3][4].tile.color == "black"
    # Coordinate (450, 450) is located in board[3][4] BoardSquare
    p.take_turn(450, 450)
    assert gb.board[3][4].is_empty is False
    assert gb.board[3][4].tile.color == "black"

    # Confirm a player cannot place a tile once they have placed one that turn
    gb: GameBoard = GameBoard(board_size=800)
    lm: LegalMove = LegalMove(gb.board[2][3],
                              set(),
                              1,
                              None,
                              False,
                              False)
    gb.legal_moves = [lm]
    p: Player = Player(gb, "Player", "black")

    # Confirm after player takes their turn, turn_complete changes to True and
    # a tile is placed in the box they clicked on
    assert p.turn_complete is False
    assert gb.board[2][3].is_empty is True
    p.take_turn(350, 350)
    assert p.turn_complete is True
    assert gb.board[2][3].is_empty is False
    # Player attempts to place a second tile in the same turn
    # Coordinate (150, 50) is located in board[0][1] BoardSquare
    p.take_turn(150, 150)
    assert gb.board[0][1].is_empty is True


def test__place_tile():
    gb: GameBoard = GameBoard(board_size=800)
    lm: LegalMove = LegalMove(gb.board[2][3],
                              [gb.board[3][3]],
                              1,
                              None,
                              False,
                              False)
    gb.legal_moves = [lm]
    p: Player = Player(gb, "Player", "black")
    # Player will place tile in top left board square
    assert lm.player_square.is_empty is True
    assert gb.empty_tiles == 60
    assert gb.black_tiles == 2
    assert gb.white_tiles == 2
    p._place_tile(gb.legal_moves[0])
    assert lm.player_square.is_empty is False
    assert gb.empty_tiles == 59
    assert gb.black_tiles == 4
    assert gb.white_tiles == 1

    gb: GameBoard = GameBoard(board_size=800)
    lm: LegalMove = LegalMove(gb.board[2][4],
                              [gb.board[3][4]],
                              1,
                              None,
                              False,
                              False)
    gb.legal_moves = [lm]
    p: Player = Player(gb, "Player", "white")
    # Player will place tile in top left board square
    assert lm.player_square.is_empty is True
    assert gb.empty_tiles == 60
    assert gb.black_tiles == 2
    assert gb.white_tiles == 2
    p._place_tile(gb.legal_moves[0])
    assert lm.player_square.is_empty is False
    assert gb.empty_tiles == 59
    assert gb.black_tiles == 1
    assert gb.white_tiles == 4
