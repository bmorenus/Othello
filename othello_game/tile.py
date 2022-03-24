class Tile:
    """
    Purpose:
    The Tile class represents each tile placed on the game board, tracks
    the current state of each tile over the course of the game, and updates
    the state of the tile as events progress.

    Methods:
    display: displays the tile object

    Attributes:
    _x: int, the x-coordinate (px) of the center of the tile object
    _y: int, the y-coordinate (px) of the center of the tile object
    _color: str, the color of the tile object (white or black)
    _is_hint: bool, specifies whether the tile should be displayed as a game
        tile or as a tile hint
    """

    MIN_COLOR = 0
    MAX_COLOR = 255
    BLACK_FILL = 0
    WHITE_FILL = 1
    TILE_DIAMETER = 80
    TILE_STROKE_WEIGHT = 2

    def __init__(self, x, y, color, is_hint=False):
        self._x = x
        self._y = y
        self._color = color
        self._is_hint = is_hint

    @property
    def x(self):
        """getter method for self._x"""
        return self._x

    @property
    def y(self):
        """getter method for self._y"""
        return self._y

    @property
    def color(self):
        """getter method for self._color"""
        return self._color

    @color.setter
    def color(self, color):
        """setter method for self._color"""
        print("here")
        self._color = color

    @property
    def is_hint(self):
        """getter method for self._is_hint"""
        return self._is_hint

    def display(self):
        """
        Function -- display
            Draws the tile or tile hint
        Parameters:
            None
        Returns:
            None
        """
        if self.is_hint:
            stroke(self.MAX_COLOR, self.MAX_COLOR, self.MIN_COLOR)
            noFill()

        else:
            if self.color == "black":
                fill(self.BLACK_FILL)
            elif self.color == "white":
                fill(self.WHITE_FILL)
            stroke(self.BLACK_FILL)

        strokeWeight(self.TILE_STROKE_WEIGHT)
        circle(self.x, self.y, self.TILE_DIAMETER)
