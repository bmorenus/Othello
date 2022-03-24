class BoardCorner:
    """
    Purpose:
    The BoardCorner class represents the 4 tiles in each corner of the board
    as a general grouping. As a result, the GameBoard object has 4 BoardCorner
    objects. The corner_square attribute of BoardCorner is the board square
    object that occupies the corner of the game board for that specific
    GameBoard object. The x_squares attribute contains a list of all three
    game board squares that surround the corner square. The information found
    in the four BoardCorner objects associated with the GameBoard are used in
    the decision-making tree of the computer's hard difficult AI.

    Methods:
    None

    Attributes:
    corner_square: BoardSquare, a BoardSquare object in the board's corner
    x_squares: list[BoardSquare], a list of BoardSquare objects that surround
        the corner_square instance
    """
    def __init__(self, corner_square, x_squares):
        self._corner_square = corner_square
        self._x_squares = x_squares

    @property
    def corner_square(self):
        """getter method for self._corner_square"""
        return self._corner_square

    @property
    def x_squares(self):
        """getter method for self._x_squares"""
        return self._x_squares
