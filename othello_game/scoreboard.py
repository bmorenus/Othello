class Scoreboard:
    """
    Purpose:
    The Scoreboard class produces a scoreboard object that displays the current
    state of the Othello Game. It is during the entirety of the game and
    provides updates concerning game score, empty squares remaining on the
    board, and the current player's turn

    Methods:
    display: displays the banner object

    Attributes:
    gc: GameController, the Othello game controller
    gb: GameBoard, the Othello game board
    width: int, the width of the game board
    height: int, the height of the game board
    color: str, the color of the highlighted player box when it is a player's
        turn
    font_dict: dict, the dictionary of fonts used for scoreboard text
    """
    # Class variables for scoreboard features
    RECT_SCALE = 800
    SCOREBOARD_BACKGROUND_X = 0
    SCOREBOARD_BACKGROUND_Y = 0
    TEXT_SHIFT_SCORE = 9
    SCORE_FONT_SIZE = 30
    PLAYER_FONT_SIZE = 24
    REMAINING_TILES_LABEL_FONT_SIZE = 16
    REMAINING_TILES_LABEL_X = 336
    REMAINING_TILES_LABEL_Y = 65
    REMAINING_TILES_FONT_SIZE = 20
    REMAINING_TILES_X = 388
    REMAINING_TILES_Y = 88
    MIN_COLOR = 0
    MAX_COLOR = 255
    STROKE_WEIGHT = 2
    WHITE_FILL = 1
    BLACK_FILL = 0
    BOX_X_PLAYER = 16
    BOX_X_COMPUTER = 528
    BOX_Y = 10
    BOX_WIDTH = 256
    BOX_HEIGHT = 80
    BOX_BEVEL = 6
    PLAYER_TITLE_X = 112
    COMPUTER_TITLE_X = 600
    TITLE_Y = 40
    PLAYER_SCORE_X_SINGLE = 122
    PLAYER_SCORE_X_DOUBLE = 139
    COMPUTER_SCORE_X_SINGLE = 632
    COMPUTER_SCORE_X_DOUBLE = 653
    GAME_TITLE_FONT_SIZE = 24
    GAME_TITLE_BOX_X = 288
    GAME_TITLE_BOX_Y = 10
    GAME_TITLE_BOX_WIDTH = 224
    GAME_TITLE_BOX_HEIGHT = 35
    GAME_TITLE_X = 364
    GAME_TITLE_Y = 37
    SCORE_Y = 80

    def __init__(self, gc, gb, width, height, font_dict):
        self._gc = gc
        self._gb = gb
        self._width = width
        self._height = height
        self._color = "#808080"
        self._font_dict = font_dict

    @property
    def gc(self):
        """getter method for self._gc"""
        return self._gc

    @property
    def gb(self):
        """getter method for self._gb"""
        return self._gb

    @property
    def active_turn(self):
        """getter method for self._active_turn"""
        return self._active_turn

    @property
    def width(self):
        """getter method for self._width"""
        return self._width

    @property
    def height(self):
        """getter method for self._height"""
        return self._height

    @property
    def color(self):
        """getter method for self._color"""
        return self._color

    @property
    def font_dict(self):
        """getter method for self._font_dict"""
        return self._font_dict

    def display(self):
        """
        Function -- display
            Draws the scoreboard object
        Parameters:
            None
        Returns:
            None
        """
        # Scoreboard Background
        fill(self.color)
        stroke(self.BLACK_FILL)
        strokeWeight(self.STROKE_WEIGHT)
        rect(self.SCOREBOARD_BACKGROUND_X,
             self.SCOREBOARD_BACKGROUND_X,
             self.width,
             self.height)

        # Player 1 score box
        if self.gc.active_turn.name != "Computer":
            fill(self.MAX_COLOR, self.MAX_COLOR, self.MIN_COLOR)
        else:
            fill(self.WHITE_FILL)

        rect(self.BOX_X_PLAYER * (self.width / self.RECT_SCALE),
             self.BOX_Y, self.BOX_WIDTH * (self.width / self.RECT_SCALE),
             self.BOX_HEIGHT,
             self.BOX_BEVEL)

        fill(self.BLACK_FILL)

        textFont(self.font_dict["player_font"], self.PLAYER_FONT_SIZE)

        text(str(self.gc.player_1.name),
             self.PLAYER_TITLE_X * (self.width / self.RECT_SCALE),
             self.TITLE_Y)
        textFont(self.font_dict["score_font"], self.SCORE_FONT_SIZE)

        if self.gb.black_tiles > self.TEXT_SHIFT_SCORE:
            text(str(self.gb.black_tiles),
                 self.PLAYER_SCORE_X_SINGLE * (self.width / self.RECT_SCALE),
                 self.SCORE_Y)
        else:
            text(str(self.gb.black_tiles),
                 self.PLAYER_SCORE_X_DOUBLE * (self.width / self.RECT_SCALE),
                 self.SCORE_Y)

        # Player 2 score box
        if self.gc.active_turn.name == "Computer":
            fill(self.MAX_COLOR, self.MAX_COLOR, self.MIN_COLOR)
        else:
            fill(self.WHITE_FILL)

        rect(self.BOX_X_COMPUTER * (self.width / self.RECT_SCALE),
             self.BOX_Y, self.BOX_WIDTH * (self.width / self.RECT_SCALE),
             self.BOX_HEIGHT,
             self.BOX_BEVEL)

        fill(self.BLACK_FILL)

        textFont(self.font_dict["player_font"], self.PLAYER_FONT_SIZE)

        text(str(self.gc.player_2.name),
             self.COMPUTER_TITLE_X * (self.width / self.RECT_SCALE),
             self.TITLE_Y)

        textFont(self.font_dict["score_font"], self.SCORE_FONT_SIZE)

        if self.gb.white_tiles > self.TEXT_SHIFT_SCORE:
            text(str(self.gb.white_tiles),
                 self.COMPUTER_SCORE_X_SINGLE * (self.width / self.RECT_SCALE),
                 self.SCORE_Y)
        else:
            text(str(self.gb.white_tiles),
                 self.COMPUTER_SCORE_X_DOUBLE * (self.width / self.RECT_SCALE),
                 self.SCORE_Y)

        # Game Title
        fill(self.BLACK_FILL)

        rect(self.GAME_TITLE_BOX_X * (self.width / self.RECT_SCALE),
             self.GAME_TITLE_BOX_Y,
             self.GAME_TITLE_BOX_WIDTH * (self.width / self.RECT_SCALE),
             self.GAME_TITLE_BOX_HEIGHT,
             self.BOX_BEVEL)

        fill(self.WHITE_FILL)
        textFont(self.font_dict["othello_font"], self.GAME_TITLE_FONT_SIZE)

        text(str("Othello"),
             self.GAME_TITLE_X * (self.width / self.RECT_SCALE),
             self.GAME_TITLE_Y)

        # Remaining Tiles
        fill(self.BLACK_FILL)

        textFont(self.font_dict["remaining_tiles"],
                 self.REMAINING_TILES_LABEL_FONT_SIZE)
        text(str("Remaining Tiles"),
             self.REMAINING_TILES_LABEL_X * (self.width / self.RECT_SCALE),
             self.REMAINING_TILES_LABEL_Y)

        textFont(self.font_dict["remaining_tiles"],
                 self.REMAINING_TILES_FONT_SIZE)
        text(str(self.gb.empty_tiles),
             self.REMAINING_TILES_X * (self.width / self.RECT_SCALE),
             self.REMAINING_TILES_Y)
