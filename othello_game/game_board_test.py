from game_board import GameBoard
from board_square import BoardSquare
from player import Player
from tile import Tile


def test_constructor():
    gb: GameBoard = GameBoard(board_size=800)
    assert isinstance(gb, GameBoard)

    # Confirm constant assignments
    assert gb.NUM_STARTING_TILES == 2
    assert gb.PIXEL_DISPLACEMENT == 50
    assert gb.SPACING == 100

    assert gb.board == [
        [gb.board[0][0], gb.board[0][1], gb.board[0][2], gb.board[0][3],
         gb.board[0][4], gb.board[0][5], gb.board[0][6], gb.board[0][7]],

        [gb.board[1][0], gb.board[1][1], gb.board[1][2], gb.board[1][3],
         gb.board[1][4], gb.board[1][5], gb.board[1][6], gb.board[1][7]],

        [gb.board[2][0], gb.board[2][1], gb.board[2][2], gb.board[2][3],
         gb.board[2][4], gb.board[2][5], gb.board[2][6], gb.board[2][7]],

        [gb.board[3][0], gb.board[3][1], gb.board[3][2], gb.board[3][3],
         gb.board[3][4], gb.board[3][5], gb.board[3][6], gb.board[3][7]],

        [gb.board[4][0], gb.board[4][1], gb.board[4][2], gb.board[4][3],
         gb.board[4][4], gb.board[4][5], gb.board[4][6], gb.board[4][7]],

        [gb.board[5][0], gb.board[5][1], gb.board[5][2], gb.board[5][3],
         gb.board[5][4], gb.board[5][5], gb.board[5][6], gb.board[5][7]],

        [gb.board[6][0], gb.board[6][1], gb.board[6][2], gb.board[6][3],
         gb.board[6][4], gb.board[6][5], gb.board[6][6], gb.board[6][7]],

        [gb.board[7][0], gb.board[7][1], gb.board[7][2], gb.board[7][3],
         gb.board[7][4], gb.board[7][5], gb.board[7][6], gb.board[7][7]]]

    assert gb.board_size == 800
    assert gb.board_start_x == 0
    assert gb.board_start_y == 100
    assert gb.MAX_INDEX == 7
    assert gb.empty_tiles == 60
    assert gb.white_tiles == 2
    assert gb.black_tiles == 2
    assert gb.legal_moves == []


def test__generate_game_board():
    gb: GameBoard = GameBoard(board_size=400)
    assert len(gb.board) == 4
    assert len(gb.board[0]) == 4
    assert len(gb.board[1]) == 4
    assert len(gb.board[2]) == 4
    assert len(gb.board[3]) == 4

    gb: GameBoard = GameBoard(board_size=800)
    assert len(gb.board) == 8
    assert len(gb.board[0]) == 8
    assert len(gb.board[1]) == 8
    assert len(gb.board[2]) == 8
    assert len(gb.board[3]) == 8
    assert len(gb.board[4]) == 8
    assert len(gb.board[5]) == 8
    assert len(gb.board[6]) == 8
    assert len(gb.board[7]) == 8


def test__get_board_start():
    # Scoreboard space removed for any board size != 400
    gb: GameBoard = GameBoard(board_size=400)
    gb.board_start_x == 0
    gb.board_start_y == 0

    gb: GameBoard = GameBoard(board_size=800)
    gb.board_start_x == 0
    gb.board_start_y == 100


def test__generate_game_board():
    gb: GameBoard = GameBoard(board_size=0)
    assert gb.board == []

    gb: GameBoard = GameBoard(board_size=400)
    assert gb.board == [[gb.board[0][0], gb.board[0][1],
                         gb.board[0][2], gb.board[0][3]],
                        [gb.board[1][0], gb.board[1][1],
                         gb.board[1][2], gb.board[1][3]],
                        [gb.board[2][0], gb.board[2][1],
                         gb.board[2][2], gb.board[2][3]],
                        [gb.board[3][0], gb.board[3][1],
                         gb.board[3][2], gb.board[3][3]]]

    # Board size of 800 tested in constructor test, see above


def test__set_starting_tiles():
    gb: GameBoard = GameBoard(board_size=0)
    # Confirm no starting tiles produced
    assert gb.board == []

    gb: GameBoard = GameBoard(board_size=400)
    # Ensure the scoreboard is not displayed on any board size != 800
    assert gb.board[1][1].x == 100
    assert gb.board[1][1].y == 100
    assert gb.board[1][1].tile.color == "white"
    assert gb.board[1][2].x == 200
    assert gb.board[1][2].y == 100
    assert gb.board[1][2].tile.color == "black"
    assert gb.board[2][1].x == 100
    assert gb.board[2][1].y == 200
    assert gb.board[2][1].tile.color == "black"
    assert gb.board[2][2].x == 200
    assert gb.board[2][2].y == 200
    assert gb.board[2][2].tile.color == "white"

    gb: GameBoard = GameBoard(board_size=800)
    assert gb.board[3][3].x == 300
    assert gb.board[3][3].y == 400
    assert gb.board[3][3].tile.color == "white"
    assert gb.board[3][4].x == 400
    assert gb.board[3][4].y == 400
    assert gb.board[3][4].tile.color == "black"
    assert gb.board[4][3].x == 300
    assert gb.board[4][3].y == 500
    assert gb.board[4][3].tile.color == "black"
    assert gb.board[4][4].x == 400
    assert gb.board[4][4].y == 500
    assert gb.board[4][4].tile.color == "white"


def test__generate_board_corners():
    # Board Corners are testing in BoardCorner testing suite
    pass


def test__generate_board_diagonals():
    gb: GameBoard = GameBoard(board_size=400)

    # Descending Diagonals
    assert (0, 0) in gb.BOARD_DIAGONALS
    assert (1, 1) in gb.BOARD_DIAGONALS
    assert (2, 2) in gb.BOARD_DIAGONALS
    assert (3, 3) in gb.BOARD_DIAGONALS

    # Ascending Diagonals
    assert (0, 3) in gb.BOARD_DIAGONALS
    assert (1, 2) in gb.BOARD_DIAGONALS
    assert (2, 1) in gb.BOARD_DIAGONALS
    assert (3, 0) in gb.BOARD_DIAGONALS

    gb: GameBoard = GameBoard(board_size=800)

    # Descending Diagonals
    assert (0, 0) in gb.BOARD_DIAGONALS
    assert (1, 1) in gb.BOARD_DIAGONALS
    assert (2, 2) in gb.BOARD_DIAGONALS
    assert (3, 3) in gb.BOARD_DIAGONALS
    assert (4, 4) in gb.BOARD_DIAGONALS
    assert (5, 5) in gb.BOARD_DIAGONALS
    assert (6, 6) in gb.BOARD_DIAGONALS
    assert (7, 7) in gb.BOARD_DIAGONALS

    # Ascending Diagonals
    assert (0, 7) in gb.BOARD_DIAGONALS
    assert (1, 6) in gb.BOARD_DIAGONALS
    assert (2, 5) in gb.BOARD_DIAGONALS
    assert (3, 4) in gb.BOARD_DIAGONALS
    assert (4, 3) in gb.BOARD_DIAGONALS
    assert (5, 2) in gb.BOARD_DIAGONALS
    assert (6, 1) in gb.BOARD_DIAGONALS
    assert (7, 0) in gb.BOARD_DIAGONALS


def test_calculate_legal_moves():
    gb: GameBoard = GameBoard(board_size=800)


def test__calculate_tile_flips():
    # Generate standard tile start positions on 8x8 gameboard
    gb: GameBoard = GameBoard(board_size=800)
    p: Player = Player(gb, "Player", "black")

    # Conduct test on legal move assessment for tile start positions

    legal_move_list = [(3, 2), (2, 3), (4, 5), (5, 4)]
    gb._calculate_tile_flips(p)

    for legal_move in gb.legal_moves:
        assert (legal_move.player_square.x_index,
                legal_move.player_square.y_index) in legal_move_list


def test__get_flippable_squares():
    # Generate standard tile start positions on 8x8 gameboard
    gb: GameBoard = GameBoard(board_size=800)
    # Add a white tile to the board at (x=4, y=5)
    gb.board[5][4].tile = Tile(450, 650, "white")
    # Add a white tile to the board at (x=5 ,y=6)
    gb.board[6][5].tile = Tile(550, 750, "white")
    # Add a black tile to the board at (x=6, y=6)
    gb.board[6][6].tile = Tile(650, 750, "black")
    # The placement of a black tile at (x=4, y=6) should flip the white tiles
    # at (x=4, y=4), (x=4, y=5), and (x=6, y=6) by meeting the black partner
    # tiles at (x=4, y=3) and (x=6, y=6).
    start_square = gb.board[6][4]
    flip_squares = set()
    # Call to x_dir = 0, y_dir = -1 adds squares (4, 4) and (4, 5) to set
    flip_squares.update(gb._get_flippable_squares("black",
                                                  start_square,
                                                  0,
                                                  -1,
                                                  flip_squares))
    # Call to x_dir = 1, y_dir = 0 adds squares (5, 6) to set
    flip_squares.update(gb._get_flippable_squares("black",
                                                  start_square,
                                                  1,
                                                  0,
                                                  flip_squares))
    assert gb.board[4][4] in flip_squares
    assert gb.board[5][4] in flip_squares
    assert gb.board[6][5] in flip_squares


def test__format_legal_move():
    # TEST NUMBER 1: CHECK FOR PROPER INPUTS IN MIDDLE OF BOARD

    # Generate standard tile start positions on 8x8 gameboard
    gb: GameBoard = GameBoard(board_size=800)
    assert gb.legal_moves == []

    # Add a white tile to the board at (x=4, y=5)
    gb.board[5][4].tile = Tile(450, 650, "white")
    # Add a white tile to the board at (x=5 ,y=6)
    gb.board[6][5].tile = Tile(550, 750, "white")
    # Add a black tile to the board at (x=6, y=6)
    gb.board[6][6].tile = Tile(650, 750, "black")

    start_square = gb.board[6][4]
    flip_squares = set()
    # Call to x_dir = 0, y_dir = -1 adds squares (4, 4) and (4, 5) to set
    flip_squares.update(gb._get_flippable_squares("black",
                                                  start_square,
                                                  0,
                                                  -1,
                                                  flip_squares))
    # Call to x_dir = 1, y_dir = 0 adds squares (5, 6) to set
    flip_squares.update(gb._get_flippable_squares("black",
                                                  start_square,
                                                  1,
                                                  0,
                                                  flip_squares))

    gb._format_legal_move(start_square, flip_squares, gb.legal_moves)

    # Confirm start square is transferred as player square to LegalMove object
    assert gb.legal_moves[0].player_square == start_square

    # Confirm all flippable squares are tracked in the legal move
    assert gb.board[4][4] in gb.legal_moves[0].flippable_squares
    assert gb.board[5][4] in gb.legal_moves[0].flippable_squares
    assert gb.board[6][5] in gb.legal_moves[0].flippable_squares

    # Confirm the total flips is accurate
    assert gb.legal_moves[0].total_flips == 3

    # Player square did not occupy a board corner
    assert gb.legal_moves[0].board_corner is None

    # Player square is not in a corner square
    assert gb.legal_moves[0].is_corner_move is False

    assert gb.legal_moves[0].is_edge_move is False

    # TEST NUMBER 2: CHECK FOR PROPER INPUTS IN A CORNER SQUARE

    # Generate standard tile start positions on 8x8 gameboard
    gb: GameBoard = GameBoard(board_size=800)
    assert gb.legal_moves == []

    # Add a white tile to the board at (x=7, y=6)
    gb.board[6][7].tile = Tile(450, 650, "white")
    # Add a white tile to the board at (x=7 ,y=5)
    gb.board[5][7].tile = Tile(550, 750, "white")
    # Add a black tile to the board at (x=7, y=4)
    gb.board[4][7].tile = Tile(650, 750, "black")

    # Start square is now a corner square
    start_square = gb.board[7][7]
    flip_squares = set()
    # Call to x_dir = 0, y_dir = -1 adds squares (7, 5) and (7, 6) to set
    flip_squares.update(gb._get_flippable_squares("black",
                                                  start_square,
                                                  0,
                                                  -1,
                                                  flip_squares))

    gb._format_legal_move(start_square, flip_squares, gb.legal_moves)

    # Confirm start square is transferred as player square to LegalMove object
    assert gb.legal_moves[0].player_square == start_square

    # Confirm all flippable squares are tracked in the legal move
    assert gb.board[6][7] in gb.legal_moves[0].flippable_squares
    assert gb.board[5][7] in gb.legal_moves[0].flippable_squares

    # Confirm the total flips is accurate
    assert gb.legal_moves[0].total_flips == 2

    # Player square occupied the bottom right board corner
    assert gb.legal_moves[0].board_corner is None

    # Player square is in a corner square
    assert gb.legal_moves[0].is_corner_move is True

    # Player square is on an edge
    assert gb.legal_moves[0].is_edge_move is True

    # TEST NUMBER 3: CHECK FOR PROPER INPUTS IN AN X-SQUARE

    # Generate standard tile start positions on 8x8 gameboard
    gb: GameBoard = GameBoard(board_size=800)
    assert gb.legal_moves == []

    # Add a white tile to the board at (x=7 ,y=5)
    gb.board[5][7].tile = Tile(550, 750, "white")
    # Add a black tile to the board at (x=7, y=4)
    gb.board[4][7].tile = Tile(650, 750, "black")

    # Start square is now a corner square
    start_square = gb.board[6][7]
    flip_squares = set()
    # Call to x_dir = 0, y_dir = -1 adds squares (7, 5) to set
    flip_squares.update(gb._get_flippable_squares("black",
                                                  start_square,
                                                  0,
                                                  -1,
                                                  flip_squares))

    gb._format_legal_move(start_square, flip_squares, gb.legal_moves)

    # Confirm start square is transferred as player square to LegalMove object
    assert gb.legal_moves[0].player_square == start_square

    # Confirm all flippable squares are tracked in the legal move
    assert gb.board[5][7] in gb.legal_moves[0].flippable_squares

    # Confirm the total flips is accurate
    assert gb.legal_moves[0].total_flips == 1

    # Player square occupied the bottom right board corner
    assert gb.legal_moves[0].board_corner is gb.BOARD_CORNERS[3]

    # Player square is in a corner square
    assert gb.legal_moves[0].is_corner_move is False

    # Player square is on an edge
    assert gb.legal_moves[0].is_edge_move is True


def test_yield_board_squares():
    gb: GameBoard = GameBoard(board_size=800)
    # Ensure yield_board_squares function returns a generator that produces
    # GameSquare type values
    for board_square in gb.yield_board_squares():
        isinstance(board_square, BoardSquare)
    accumulator = 0
    # Ensure yield_board_squares function yields all boards squares on board
    for board_square in gb.yield_board_squares():
        accumulator += 1
    assert accumulator == 64
