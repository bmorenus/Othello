class Banner:
    """
    Purpose:
    The Banner class produces a banner object that displays the winner of the
    game and the game's final score. It is displayed once the end-game
    conditions are met in game_controller

    Methods:
    display: displays the banner object

    Attributes:
    gb: GameBoard, the Othello game board
    winner: Player, the winner of the game
    player_1_score: int, the number of black tiles on the game board
    player_2_score: int, the number of white tiles on the game board
    font_dict: dict, the dictionary of fonts for banner text
    """
    # Class variables for Banner specs
    BANNER_SCALE = 800
    WHITE_FILL = 1
    BLACK_FILL = 0
    BANNER_FONT_SIZE = 44
    BANNER_RECT_X = 112
    BANNER_RECT_Y = 225
    BANNER_RECT_WIDTH = 575
    BANNER_RECT_HEIGHT = 150
    BANNER_RECT_BEVEL = 7
    WINNER_TEXT_X_PLAYER = 270
    WINNER_TEXT_X_COMPUTER = 225
    WINNER_TEXT_X_TIE = 275
    WINNER_TEXT_Y = 282
    SCORE_TEXT_X = 320
    SCORE_TEXT_Y = 350

    def __init__(self, gb, winner, player_1_score, player_2_score, font_dict):
        self.gb = gb
        self.winner = winner
        self.player_1_score = player_1_score
        self.player_2_score = player_2_score
        self.font_dict = font_dict

    def display(self):
        """
        Function -- display
            Draws the banner object
        Parameters:
            None
        Returns:
            None
        """
        # Banner rectangle
        fill(self.WHITE_FILL)
        stroke(self.BLACK_FILL)
        strokeWeight(2)
        rect(self.BANNER_RECT_X * (self.gb.board_size / self.BANNER_SCALE),
             self.gb.board_start_y + self.BANNER_RECT_Y * (
                 self.gb.board_size / self.BANNER_SCALE),
             self.BANNER_RECT_WIDTH * (self.gb.board_size / self.BANNER_SCALE),
             self.BANNER_RECT_HEIGHT,
             self.BANNER_RECT_BEVEL)

        # Winner Declaration
        fill(self.BLACK_FILL)
        textFont(self.font_dict["winner_font"], self.BANNER_FONT_SIZE)

        # Winning Game
        if self.winner.name == "Computer":
            text(str(self.winner.name) + " Wins!",
                 self.WINNER_TEXT_X_COMPUTER * (
                     self.gb.board_size / self.BANNER_SCALE),
                 self.gb.board_start_y + self.WINNER_TEXT_Y * (
                     self.gb.board_size / self.BANNER_SCALE))

        elif self.winner.name != "Computer":
            text(str(self.winner.name) + " Wins!",
                 self.WINNER_TEXT_X_PLAYER * (
                     self.gb.board_size / self.BANNER_SCALE),
                 self.gb.board_start_y + self.WINNER_TEXT_Y * (
                     self.gb.board_size / self.BANNER_SCALE))

        # Tie Game
        else:
            text("Tie Game!",
                 self.WINNER_TEXT_X_TIE * (
                     self.gb.board_size / self.BANNER_SCALE),
                 self.gb.board_start_y + self.WINNER_DECLARATION_Y * (
                     self.gb.board_size / self.BANNER_SCALE))

        # Score Declaration
        textFont(self.font_dict["tile_font"], self.BANNER_FONT_SIZE)
        text(str(self.player_1_score) + " - " + str(self.player_2_score),
             self.SCORE_TEXT_X * (
                 self.gb.board_size / self.BANNER_SCALE),
             self.gb.board_start_y + self.SCORE_TEXT_Y * (
                 self.gb.board_size / self.BANNER_SCALE))
