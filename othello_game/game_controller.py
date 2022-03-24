from game_board import GameBoard
from player import Player
from banner import Banner
from scoreboard import Scoreboard

import re
import sys


class GameController:
    """
    Purpose:
    The GameController class controls the game logic and alternation of player
    turns. It monitors the game score and the number of remaining tiles on the
    board. Once all tiles or legal moves have been exhausted, the game
    controller declares a winner and displays the winner information on the
    screen and updates scores.txt

    Methods:
    update: alternates player turns and declares winner at game end
    declare_winner: assigns self.winner based on tile count
    read_winner: reads scores.txt and finds the correct placement for the
        latest game score update
    write_winner: writes the latest score update to scores.txt
    print_winner: prints the winner and the game score to stdout

    Attributes:
    _gb: GameBoard, the Othello game board
    _player_1: Player, the human player is player 1
    _player_2: Player, the computer player is player 1
    _active_turn: Player, designates the player whose turn it is
    _hint_preference: str, specifies whether tile hints will be shown for
        the player during his/her turn
    _difficulty: str, the difficulty of the game (easy, medium, hard)
    _passed_turn_counter: int, the number of turns passed in the game without
        a move available to a player
    _display_counter: int, the number of calls to update() to permit several
        GameController functionalities to include AI pause and game exit
    _font_dict: dict, dictionary of loaded Processing fonts for display texts
    _sb: Scoreboard, scoreboard object that displays game state
    _winner: Optional[Player], declared winner of the game
    _winner_printed: bool, states whether the winner has already been printed
        to the screen to prevent repeated printings
    """
    SCOREBOARD_DISPLAY_SIZE = 800
    ENDGAME_DISPLAY_TIME = 500
    COMPUTER_AI_WAIT_TIME = 100
    MAX_TURN_PASS = 2

    def __init__(self,
                 game_board_size,
                 score_board_width,
                 score_board_height,
                 player_name,
                 hint_preference,
                 difficulty,
                 font_dict):
        self._gb = GameBoard(game_board_size)
        self._player_1 = Player(self.gb, name=player_name, color="black")
        self._player_2 = Player(self.gb, name="Computer", color="white")
        self._active_turn = self._player_1
        self._hint_preference = hint_preference
        self._difficulty = difficulty
        self._passed_turn_counter = 0
        self._display_counter = 0
        self._font_dict = font_dict
        self._sb = Scoreboard(self,
                              self.gb,
                              score_board_width,
                              score_board_height,
                              self.font_dict)
        self._winner = None
        self._winner_printed = False

    @property
    def gb(self):
        """getter method for self._gb"""
        return self._gb

    @property
    def player_1(self):
        """getter method for self._player_1"""
        return self._player_1

    @property
    def player_2(self):
        """getter method for self._player_2"""
        return self._player_2

    @property
    def active_turn(self):
        """getter method for self._active_turn"""
        return self._active_turn

    @active_turn.setter
    def active_turn(self, active_turn):
        """setter method for self._active_turn"""
        self._active_turn = active_turn

    @property
    def hint_preference(self):
        """getter method for self._hint_preference"""
        return self._hint_preference

    @property
    def difficulty(self):
        """getter method for self._difficulty"""
        return self._difficulty

    @property
    def passed_turn_counter(self):
        """getter method for self._passed_turn_counter"""
        return self._passed_turn_counter

    @passed_turn_counter.setter
    def passed_turn_counter(self, passed_turn_counter):
        """setter method for self._passed_turn_counter"""
        self._passed_turn_counter = passed_turn_counter

    @property
    def display_counter(self):
        """getter method for self._display_counter"""
        return self._display_counter

    @display_counter.setter
    def display_counter(self, display_counter):
        """setter method for self._display_counter"""
        self._display_counter = display_counter

    @property
    def font_dict(self):
        """getter method for self._font_dict"""
        return self._font_dict

    @property
    def sb(self):
        """getter method for self._sb"""
        return self._sb

    @property
    def winner(self):
        """getter method for self._winner"""
        return self._winner

    @property
    def winner_printed(self):
        """getter method for self._winner_printed"""
        return self._winner_printed

    @winner_printed.setter
    def winner_printed(self, winner_printed):
        """setter method for self._winner_printed"""
        self._winner_printed = winner_printed

    def update(self):
        """
        Function -- update
            Is repeatedly called by draw() in Processing file. Monitors and
            updates the state of the game by alternating player turns, running
            game logic, and declaring winner at game end.
        Parameters:
            None
        Returns:
            None
        """
        # Game Ends
        if self.gb.empty_tiles == 0 or self.passed_turn_counter >= (
             self.MAX_TURN_PASS):
            self.display_counter += 1

            if not self.winner:
                self.declare_winner()
                if not self.winner_printed:  # Print final score only once
                    self.print_winner()
                    self.winner_printed = True

            if self.gb.board_size == self.SCOREBOARD_DISPLAY_SIZE:
                self.winner_banner.display()

            # Display end-game banner for a period, then close game
            if self.display_counter >= self.ENDGAME_DISPLAY_TIME:
                sys.exit()

        # Player Turn
        elif self.active_turn == self.player_1:

            if self.player_1.turn_complete:
                self.gb.legal_moves = []
                self.player_2.turn_complete = False
                self.active_turn = self.player_2

            elif not self.gb.legal_moves:
                self.gb.calculate_legal_moves(self.active_turn)

                if not self.gb.legal_moves:
                    self.player_1.turn_complete = True
                    self.passed_turn_counter += 1
                else:
                    self.passed_turn_counter = 0

            else:
                if self.hint_preference == "y":
                    self.gb.display_on_turn(self.active_turn)

        # Computer Turn
        elif self.active_turn == self.player_2:
            self.display_counter += 1

            # Simulate short delay for computer player response
            if self.display_counter == self.COMPUTER_AI_WAIT_TIME:

                if not self.gb.legal_moves:
                    self.gb.calculate_legal_moves(self.active_turn)

                if self.difficulty == "e":
                    next_move = self.player_2.calculate_next_move_easy()
                elif self.difficulty == "m":
                    next_move = self.player_2.calculate_next_move_med()
                else:
                    next_move = self.player_2.calculate_next_move_hard()

                if next_move:
                    self.player_2.take_turn(*next_move)
                    self.passed_turn_counter = 0
                else:
                    self.passed_turn_counter += 1

                self.gb.legal_moves = []
                self.display_counter = 0
                self.player_1.turn_complete = False
                self.active_turn = self.player_1

    def declare_winner(self):
        """
        Function -- declare_winner
            Compares black and white tile counts on the game board and declares
            the player with the most tile counts at game end the winner.
            Creates a Banner object that announces the winner and the final
            score.
        Parameters:
            None
        Returns:
            None
        """
        if self.gb.black_tiles > self.gb.white_tiles:
            self._winner = self.player_1
        elif self.gb.black_tiles < self.gb.white_tiles:
            self._winner = self.player_2
        else:
            self._winner = None

        if self.winner.name != "Computer":
            player_scores = self.read_winner()
            self.write_winner(player_scores)

        self.winner_banner = Banner(
            self.gb,
            self._winner,
            self.gb.black_tiles,
            self.gb.white_tiles,
            self.font_dict,
        )

    def read_winner(self):
        """
        Function -- read_winner
            Reads the current state of scores.txt and identified the
            appropriate placement of the end-game score. Returns a string
            with the score and player name in the appropriate place.
        Parameters:
            None
        Returns:
            player_scores: String, an updated string of all past player scores
        """
        try:
            f = open(r"scores.txt", "r")
        except FileNotFoundError:
            print("Could not read scores of scores.txt")
        else:
            score_list = []
            for line in f:
                score_list.append(line)

            top_score = re.search(r"\d+", score_list[0])

            if int(top_score.group()) < self.gb.black_tiles:
                score_list.insert(0,
                                  str(self.winner.name) + ", " +
                                  str(self.gb.black_tiles) + "\n")
            else:
                score_list.append(str(self.winner.name) + ", " +
                                  str(self.gb.black_tiles) + "\n")

            player_scores = "".join(score_list)

            return player_scores

        finally:
            f.close()

    def write_winner(self, player_scores):
        """
        Function -- write_winner
            Opens a writable file handle and writes the revised player scores
            string to scores.txt
        Parameters:
            player_scores: String, an updated string of all past player scores
        Returns:
            None
        """
        try:
            f = open(r"scores.txt", "w")
        except FileNotFoundError:
            print("Could not write scores to scores.txt")
        else:
            f.write(player_scores)
        finally:
            f.close()

    def print_winner(self):
        """
        Function -- print_winner
            Prints the winner and score of the game to the stdout
        Parameters:
            None
        Returns:
            None
        """
        if self.winner:
            print(str(self.winner.name) + " Wins!")
        else:
            print("Tie Game!")
        print(str(self.gb.black_tiles) + " - " + str(self.gb.white_tiles))
