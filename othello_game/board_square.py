class BoardSquare:
    """
    Purpose:
    The BoardSquare class sets the attributes and methods for each square on
    the game board. It tracks the board square location (pixel and index),
    monitors the state of the tile that occupies it, if any, and offers a
    place for tile placement hints if desired by the user.

    Methods:
    display: displays the board square representation

    Attributes:
    _gb: GameBoard, the Othello game board
    _x: int, x-coordinate of the top-left corner of the square (px)
    _y: int, y-coordinate of the top-left corner of the square (px)
    _x_index: int, x index of the square on Gameboard's board list
    _y_index: int, y index of the square on Gameboard's board list
    _tile: Optional[Tile], Tile object, if placed on the square
    _tile_hint: Optional[Tile], Tile object, if outlined as hint on the square
    """
    BLACK_FILL = 0

    def __init__(self, gb, x, y, x_index, y_index, tile=None, tile_hint=None):
        self._gb = gb
        self._x = x
        self._y = y
        self._x_index = x_index
        self._y_index = y_index
        self._tile = tile
        self._tile_hint = tile_hint

    @property
    def gb(self):
        """getter method for self._gb"""
        return self._gb

    @property
    def x(self):
        """getter method for self._x"""
        return self._x

    @property
    def y(self):
        """getter method for self._y"""
        return self._y

    @property
    def x_index(self):
        """getter method for self._index_x"""
        return self._x_index

    @property
    def y_index(self):
        """getter method for self._index_y"""
        return self._y_index

    @property
    def tile(self):
        """getter method for self._tile"""
        return self._tile

    @tile.setter
    def tile(self, tile):
        """setter method for self._tile"""
        self._tile = tile

    @property
    def tile_hint(self):
        """getter method for self._tile_hint"""
        return self._tile_hint

    @tile_hint.setter
    def tile_hint(self, tile_hint):
        """setter method for self._tile_hint"""
        self._tile_hint = tile_hint

    @property
    def is_empty(self):
        """setter method for self._tile"""
        if self.tile:
            return False
        else:
            return True

    def display(self):
        """
        Function -- display
            Displays all components of the board square
        Parameters:
            None
        Returns:
            None
        """
        fill("#006900")
        stroke(self.BLACK_FILL)
        square(self.x, self.y, self.gb.SPACING)

        if self.tile:
            self.tile.display()

    def display_on_turn(self):
        """
        Function -- display_on_turn
            Displays components of the game square that are only relevant for
            a given player's turn:

            1. For each player turn, this function calls the display function
                of the tile_hint, if any.
        Parameters:
            None
        Returns:
            None
        """
        if self.tile_hint:
            self.tile_hint.display()
