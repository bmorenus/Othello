class LegalMove:
    """
    Purpose:
    The LegalMove class creates a legal move for a given turn and supplies all
    necessary information concerning that move for the player move hint system
    and the computer's hard AI algorithm

    Methods: None

    Attributes:
    _player_square: BoardSquare, the board square on which a player must place
        the tile to execute this move
    _flippable_squares: list[Board], list of BoardSquare objects whose tiles
        can be flipped on this move
    _total_flips: int, the total number of flips this move will accomplish
    _board_corner: BoardCorner, a 4-tile corner of the board the move is
        associated with, if applicable
    _is_corner_move: bool, True if the move places a tile in a corner square,
        False if it does not
    _is_edge_move: bool, True if the move places a tile in an edge square,
        False if it does not
    _move_value: float, the float value of the move specifying its favorability
        for the computer's hard AI decision-making tree.
    _max_tiles: int, the max number of tiles making this move can achieve
        under the conditions determined by the hard AI algorithm
    """

    def __init__(
        self,
        player_square,
        flippable_squares,
        total_flips,
        board_corner,
        is_corner_move,
        is_edge_move,
    ):
        self._player_square = player_square
        self._flippable_squares = flippable_squares
        self._total_flips = total_flips
        self._board_corner = board_corner
        self._is_corner_move = is_corner_move
        self._is_edge_move = is_edge_move
        self._move_value = 0
        self._max_tiles = 0

    def __eq__(self, other):
        """Return a boolean representing equality of the move's move value"""
        return self.move_value == other.move_value

    def __lt__(self, other):
        """Return a boolean for the less than relationship"""
        return self.move_value < other.move_value

    def __gt__(self, other):
        """Return a boolean for the greater than relationship"""
        return self.move_value > other.move_value

    @property
    def player_square(self):
        """getter method for self._player_square"""
        return self._player_square

    @property
    def flippable_squares(self):
        """getter method for self._flippable_squares"""
        return self._flippable_squares

    @property
    def total_flips(self):
        """getter method for self._total_flips"""
        return self._total_flips

    @property
    def board_corner(self):
        """getter method for self._board_corner"""
        return self._board_corner

    @property
    def is_corner_move(self):
        """getter method for self._is_corner_move"""
        return self._is_corner_move

    @property
    def is_edge_move(self):
        """getter method for self._is_edge_move"""
        return self._is_edge_move

    @property
    def move_value(self):
        """getter method for self._move_value"""
        return self._move_value

    @move_value.setter
    def move_value(self, move_value):
        """setter method for self._move_value"""
        self._move_value = move_value

    @property
    def max_tiles(self):
        """getter method for self._max_tiles"""
        return self._max_tiles

    @max_tiles.setter
    def max_tiles(self, max_tiles):
        """setter method for self._max_tiles"""
        self._max_tiles = max_tiles
