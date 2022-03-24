from board_corner import BoardCorner
from board_square import BoardSquare
from legal_move import LegalMove
from tile import Tile


class GameBoard:
    """
    Purpose:
    The GameBoard class creates the game board, monitors its state, and serves
    as an interface by which players and the game controller can interact with
    it

    Methods:
    _generate_game_board: creates the nested lists of BoardSquares on the board
    _set_starting_tiles: places the black and white starting tiles on the board
    _generate_board_corners: creates four BoardCorner instances that represent
        each corner of the board and the 3 tiles that surround it.
    _generate_board_diagonals: create a list of all BoardSquare instances that
        are diagonal to the game board's 4 corners
    calculate_legal_moves: interface by which objects can identify legal moves
    _calculate_tile_flips: creates a list of all moves that flip opposing tiles
    _get_flippable_squares: gets list of all flippable squares with tiles
    _format_legal_move: formats each legal move and creates LegalMove instance
    yield_board_squares: generator function that yields all board squares
    display: displays all board squares that comprise the game board
    display_on_turn: displays all game board components relevant to player turn

    Attributes:
    board: list[list[BoardSquare]], a list representation of the Othello board
        BoardSquare objects
    _board_size: int, the size of the width/height of the game board (px)
    _board_start_x: int, the top-left, x pixel coordinate of the board
        relative to the game screen
    _board_start_y: int, the top-left, y pixel coordinate of the board
        relative to the game screen
    _MAX_INDEX: int, the maximum accessible index for the board list
    _BOARD_CORNERS: list[BoardCorner], the 4 squares in each corner of the
        board
    _empty_tiles: int, the number of empty board squares remaining on the board
    _BOARD_DIAGONALS: list[tuple[int, int]], list of x,y coor pairs diagonal to
        the board's corners
    _white_tiles: int, the number of white tiles on the board
    _black_tiles: int, the number of black tiles on the board
    _legal_moves: list[LegalMove], list of legal move objects for reference
    """

    NUM_STARTING_TILES = 2
    NUM_PLAYERS = 2
    PIXEL_DISPLACEMENT = 50  # ensures (x,y) is not on px border of a square
    SPACING = 100
    SCOREBOARD_DISPLACEMENT = 100
    STD_BOARD_SIZE = 800

    def __init__(self, board_size=800):
        self._board_size = board_size
        self._board_start_x = 0
        self._board_start_y = (self.SCOREBOARD_DISPLACEMENT
                               if board_size == self.STD_BOARD_SIZE else 0)
        self._MAX_INDEX = int((self.board_size / self.SPACING) - 1)
        self._generate_game_board()
        self._set_starting_tiles()
        self._BOARD_CORNERS = self._generate_board_corners()
        self._empty_tiles = ((board_size / self.SPACING) ** 2) - (
            self.NUM_PLAYERS * self.NUM_STARTING_TILES
        )
        self._BOARD_DIAGONALS = self._generate_board_diagonals()
        self._white_tiles = self.NUM_STARTING_TILES
        self._black_tiles = self.NUM_STARTING_TILES
        self._legal_moves = []

    @property
    def board_size(self):
        """getter method for self._board_size"""
        return self._board_size

    @property
    def board_start_x(self):
        """getter method for self._board_start_x"""
        return self._board_start_x

    @property
    def board_start_y(self):
        """getter method for self._board_start_y"""
        return self._board_start_y

    @property
    def MAX_INDEX(self):
        """getter method for self._MAX_INDEX"""
        return self._MAX_INDEX

    @property
    def BOARD_CORNERS(self):
        """getter method for self._BOARD_CORNERS"""
        return self._BOARD_CORNERS

    @property
    def BOARD_DIAGONALS(self):
        """getter method for self._BOARD_DIAGONALS"""
        return self._BOARD_DIAGONALS

    @property
    def empty_tiles(self):
        """getter method for self._empty_tiles"""
        return self._empty_tiles

    @empty_tiles.setter
    def empty_tiles(self, number):
        """setter method for self._empty_tiles"""
        self._empty_tiles = number

    @property
    def white_tiles(self):
        """getter method for self._white_tiles"""
        return self._white_tiles

    @white_tiles.setter
    def white_tiles(self, number):
        """setter method for self._white_tiles"""
        self._white_tiles = number

    @property
    def black_tiles(self):
        """getter method for self._black_tiles"""
        return self._black_tiles

    @black_tiles.setter
    def black_tiles(self, number):
        """setter method for self._black_tiles"""
        self._black_tiles = number

    @property
    def legal_moves(self):
        """getter method for self._legal_moves"""
        return self._legal_moves

    @legal_moves.setter
    def legal_moves(self, legal_moves):
        """setter method for self._legal_moves"""
        if legal_moves == []:
            # Ensure hint tiles are cleared along with legal moves list
            for move in self._legal_moves:
                move.player_square.tile_hint = None
        self._legal_moves = legal_moves

    def _get_board_start(self):
        if self.board_size == self.STD_BOARD_SIZE:
            return 0, self.SCOREBOARD_DISPLACEMENT
        else:
            return 0, 0

    def _generate_game_board(self):
        """
        Function -- _generate_game_board
            Creates the game board by producing nested lists of BoardSquare
            objects with a length of (self.board_size / 100). For a board size
            of 800 pixels, this will result in a width and a height of 8 board
            squares.
        Parameters:
            None
        Returns:
            None
        """
        self.board = [
            [
                BoardSquare(
                    self,
                    column,
                    row,
                    (int(column / self.SPACING)),
                    (int((row - self.board_start_y) / self.SPACING)),
                    tile=None,
                )
                for column in range(self.board_start_x,
                                    self.board_size,
                                    self.SPACING)
            ]
            for row in range(
                self.board_start_y,
                self.board_start_y + self.board_size,
                self.SPACING
            )
        ]

    def _set_starting_tiles(self):
        """
        Function -- _generate_game_board
            Creates the game board by producing nested lists of BoardSquare
            objects with a length of (self.board_size / 100). For a board size
            of 800 pixels, this will result in a width and a height of 8 board
            squares.
        Parameters:
            None
        Returns:
            None
        """
        # Prevent start tiles on boards with zero of odd number of squares
        if self.board_size % 2 == 0 and self.board_size != 0:

            # For 800px, MIDDLE_OF_BOARD = 4
            MIDDLE_OF_BOARD = int((len(self.board) / 2))

            top_row = MIDDLE_OF_BOARD - 1
            bottom_row = MIDDLE_OF_BOARD
            left_col = MIDDLE_OF_BOARD - 1
            right_col = MIDDLE_OF_BOARD

            # top left starting tile
            square = self.board[top_row][left_col]
            square.tile = Tile(
                square.x + self.PIXEL_DISPLACEMENT,
                square.y + self.PIXEL_DISPLACEMENT,
                "white",
            )

            # top right starting tile
            square = self.board[top_row][right_col]
            square.tile = Tile(
                square.x + self.PIXEL_DISPLACEMENT,
                square.y + self.PIXEL_DISPLACEMENT,
                "black",
            )

            # bottom left starting tile
            square = self.board[bottom_row][left_col]
            square.tile = Tile(
                square.x + self.PIXEL_DISPLACEMENT,
                square.y + self.PIXEL_DISPLACEMENT,
                "black",
            )

            # bottom right starting tile
            square = self.board[bottom_row][right_col]
            square.tile = Tile(
                square.x + self.PIXEL_DISPLACEMENT,
                square.y + self.PIXEL_DISPLACEMENT,
                "white",
            )

    def _generate_board_corners(self):
        """
        Function -- _generate_board_corners
            Creates four BoardCorner instances that represent each corner of
            theboard and the 3 tiles that surround it. A BoardCorner instance
            is associated with a LegalMove if it is found that the legal move
            places a tile in one of the three squares surrounding the corner
            square. These moves are to be avoided in particular by the AI and
            the information found in associated BoardCorner instance allows the
            AI to make decisions concerning corner play.
        Parameters:
            None
        Returns:
            board_corners: list[BoardCorners], a list of all 4 BoardCorner
                instances
        """
        if self.board_size % 2 == 0 and self.board_size != 0:
            board_corners = [
                BoardCorner(self.board[0][0], ((1, 0), (1, 1), (0, 1))),
                BoardCorner(
                    self.board[0][self.MAX_INDEX],
                    (
                        (self.MAX_INDEX - 1, 0),
                        (self.MAX_INDEX - 1, 1),
                        (self.MAX_INDEX, 1),
                    ),
                ),
                BoardCorner(
                    self.board[self.MAX_INDEX][0],
                    (
                        (0, self.MAX_INDEX - 1),
                        (1, self.MAX_INDEX - 1),
                        (1, self.MAX_INDEX),
                    ),
                ),
                BoardCorner(
                    self.board[self.MAX_INDEX][self.MAX_INDEX],
                    (
                        (self.MAX_INDEX - 1, self.MAX_INDEX),
                        (self.MAX_INDEX - 1, self.MAX_INDEX - 1),
                        (self.MAX_INDEX, self.MAX_INDEX - 1),
                    ),
                ),
            ]

            return board_corners

    def _generate_board_diagonals(self):
        """
        Function -- _generate_board_diagonals
            Generates a list of all x,y coordinate pairs that are diagonal to
            the board corners for use in computer AI decision-making.
        Parameters:
            None
        Returns:
            board_diagonals: list[tuple[int, int]], list of diagonal coor pairs
        """
        board_diagonals = []

        for coordinate in range(0, self.MAX_INDEX + 1):
            x = coordinate
            y = coordinate
            board_diagonals.append((x, y))

        for x, y in enumerate(list(range(self.MAX_INDEX, -1, -1))):
            board_diagonals.append((x, y))

        return board_diagonals

    def calculate_legal_moves(self, player):
        """
        Function -- calculate_legal_moves
            Serves as the interface by which the game controller and players
            can access a list of all legal moves for a given turn to prevent
            an illegal move from occuring and to assist in computer AI
            implementations
        Parameters:
            player: Player, a player object for calculations needing tile color
        Returns:
            None
        """
        self.legal_moves = self._calculate_tile_flips(player)

    def _calculate_tile_flips(self, player):
        """
        Function -- _calculate_tile_flips
            Runs the logic for determining all board squares that will yield
            one or more tile flips for the current player
        Parameters:
            player: Player, a player object for calculations needing tile color
        Returns:
            None
        """
        NEG_DIR_INDEX = -1
        POS_DIR_INDEX = 2

        legal_moves = []
        for player_square in self.yield_board_squares():

            if player_square.is_empty:
                flippable_squares = set()

                for y_dir in range(NEG_DIR_INDEX, POS_DIR_INDEX):
                    for x_dir in range(NEG_DIR_INDEX, POS_DIR_INDEX):
                        flip_squares = self._get_flippable_squares(
                            player.color, player_square, x_dir, y_dir, set()
                        )

                        flippable_squares.update(flip_squares)

                if flippable_squares:

                    self._format_legal_move(
                        player_square, flippable_squares, legal_moves
                    )

        return legal_moves

    def _get_flippable_squares(
        self, player_color, start_square, x_dir, y_dir, flip_squares
    ):
        """
        Function -- _get_flippable_squares
            Uses recursion to identify all flippable tiles emanating from
            the given start square. Function recursively calls itself as long
            as the start_square is bordered by tiles opposite the player's
            color. If a player's "partner" tile is found at the end of the
            recursive call, all intermediate, opposing tiles are returned as
            flippable. Otherwise, no tiles are returned.
        Parameters:
            player_color: String, the color of the current turn player
            start_square: BoardSquare, the board square from which the
                flippable squares are identified
            x_dir: int, the x-direction in which the recursive call will move
            y_dir: int, the y-direction in which the recursive call will move
            flip_squares: set, a set of all flippable tiles in the x_dir, y_dir
                direction
        Returns:
            flip_squares: set, either empty set or set of flippable squares
        """
        next_square = None

        # Confirm a square exists in the direction of (x_dir, y_dir)
        if (0 <= start_square.x_index + x_dir <= self._MAX_INDEX) and (
            0 <= start_square.y_index + y_dir <= self._MAX_INDEX
        ):

            next_square = self.board[start_square.y_index + y_dir][
                start_square.x_index + x_dir
            ]

        # If no square exists, no tiles are flippable in this (x_dir, y_dir)
        # Therefore, make flip_squares an empty set and return it
        if next_square is None or next_square.tile is None:
            flip_squares = set()

        # If next square holds a tile of the opposing player, it is flippable
        # Therefore, add the tile to flip squares and continue to search for
        # a partner tile to complete the flip
        elif next_square.tile.color != player_color:
            flip_squares.add(next_square)
            flip_squares = self._get_flippable_squares(
                player_color, next_square, x_dir, y_dir, flip_squares
            )

        # If neither of the above two conditions are met, a partner tile has
        # been found and the current flip_squares set contains flippable tiles
        return flip_squares

    def _format_legal_move(self,
                           player_square,
                           flippable_squares,
                           legal_moves):
        """
        Function -- _format_legal_move
            Creates a LegalMove instance with all information required to
            support Player hint functionality and Computer AI decision-making.
            Associates a BoardCorner instance with the LegalMove if applicable
            and also determines whether the move is a corner move or not. Once
            the LegalMove instance is created, it is appended onto the list of
            all legal moves for the given turn.
        Parameters:
            player_square: BoardSquare, the board square of the legal move
            flippable_squares: list[BoardSquare], all squares that will be
                flipped if the legal move is made
            legal_moves: list[LegalMove], list of all LegalMove instances
                created and appended for the turn so far
        Returns:
            None
        """
        tracked_board_corner = None
        is_corner_move = False
        is_edge_move = False

        x_index = player_square.x_index
        y_index = player_square.y_index

        # Determines if the move is in an X square (borders a corner square)
        for board_corner in self.BOARD_CORNERS:
            if (x_index, y_index) in board_corner.x_squares:
                tracked_board_corner = board_corner

        # Determines if the move occupies a corner square
        if (
            (x_index, y_index) == (0, 0) or
            (x_index, y_index) == (0, self.MAX_INDEX) or
            (x_index, y_index) == (self.MAX_INDEX, 0) or
            (x_index, y_index) == (self.MAX_INDEX, self.MAX_INDEX)
        ):
            is_corner_move = True

        # Determines if the move occupies a square on the edge of the board
        if (
            (player_square.x_index == 0)
            or (player_square.y_index == 0)
            or (player_square.x_index == self.MAX_INDEX)
            or (player_square.y_index == self.MAX_INDEX)
        ):

            is_edge_move = True

        legal_move = LegalMove(
            player_square,
            flippable_squares,
            len(flippable_squares),
            tracked_board_corner,
            is_corner_move,
            is_edge_move,
        )

        legal_moves.append(legal_move)

    def yield_board_squares(self):
        """
        Function -- yield_board_squares
            Generator function that yields all board squares on the game board
            in an iterator
        Parameters:
            None
        Yields:
            board_square: BoardSquare, a BoardSquare object on the board
        """
        for row in self.board:
            for board_square in row:
                yield board_square

    def display(self):
        """
        Function -- display
            Displays all components of the game board
        Parameters:
            None
        Returns:
            None
        """
        for row in self.board:
            for square in row:
                square.display()

    def display_on_turn(self, player):
        """
        Function -- display_on_turn
            Displays components of the game board that are only relevant for
            a given player's turn:

            1. For all legal moves, this function generates a tile_hint Tile
                that represents a potential board square for the player to
                place their tile on.
        Parameters:
            player: the player whose turn it is
        Returns:
            None
        """
        for legal_move in self.legal_moves:
            player_square = legal_move.player_square

            if not player_square.tile_hint:
                player_square.tile_hint = Tile(
                    player_square.x + self.PIXEL_DISPLACEMENT,
                    player_square.y + self.PIXEL_DISPLACEMENT,
                    player.color,
                    is_hint=True,
                )

            player_square.display_on_turn()
