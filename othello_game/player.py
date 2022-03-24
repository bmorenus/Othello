from tile import Tile
import random
import copy


class Player:
    """
    Purpose:
    The Player class executes legal moves on the game board and also faciliates
    AI decision-making for the computer player on easy, medium, and hard modes.

    Methods:
    take_turn: allows player to place tile on board in specified location
    _place_tile: creates Tile object and adjusts tile counts on game board
    _flip_tiles: flips the color of the tile objects associated with a legal
        move's flippable tiles
    calculate_next_move_easy: AI algorithm that determines the computer's
        next move by randomly selecting a move from the legal moves available
    calculate_next_move_med: AI algorithm that determines the computer's
        next move by selecting the move that flips the most tiles
    calculate_next_move_hard: AI algorithm that determines the computer's
        next move by identifying the most favorable move according to the
        legal move objects' move_value attributes
    _process_legal_moves: Iterates through all legal moves available to the AI
        and returns the most favorable move
    _computer_move_calculator: Applies the MOVE_VALUE_DICT weights to the
        various considerations associated with a legal move for the legal moves
        available to the Computer AI at a given board recursion depth
    _player_move_calculator: Applies the MOVE_VALUE_DICT weights to the
        various considerations associated with a legal move for the legal moves
        available to the Player at a given board recursion depth
    _execute_legal_move: executes a given legal move to determine the legal
        moves available / tiles flipped  on the next recursively defined game
        board.

    Attributes:
    _gb: GameBoard, the Othello game board
    _name: str, the name of the player ("Player" or "Computer")
    _color: str, the color of the player tile
    _turn_complete: bool, represents whether the player has completed their
        turn or not
    """

    MOVE_VALUE_DICT = {
        # COMPUTER TURN WEIGHTS
        "CORNER_SQUARE_COMPUTER": 0.7,
        "EDGE_SQUARE_COMPUTER": 0.15,
        "X_SQUARE_COMPUTER": 0.7,
        "FLIPPED_TILE_COMPUTER": 0.1,
        "X_SQUARE_BLACK_TILE_FLIP": 0.2,
        "DIAGONAL_BLACK_TILE_FLIP": 0.15,

        # PLAYER TURN WEIGHTS
        "CORNER_SQUARE_PLAYER": 0.2,
        "EDGE_SQUARE_PLAYER": 0.1,
        "X_SQUARE_PLAYER": 0.4,
        "FLIPPED_TILE_PLAYER": 0.05,
    }

    MAX_RECURSION_DEPTH = 3

    def __init__(self, gb, name, color):
        self._gb = gb
        self._name = name
        self._color = color
        self._turn_complete = False

    @property
    def gb(self):
        """getter method for self._gb"""
        return self._gb

    @property
    def name(self):
        """getter method for self._name"""
        return self._name

    @property
    def color(self):
        """getter method for self._color"""
        return self._color

    @property
    def turn_complete(self):
        """getter method for self._turn_complete"""
        return self._turn_complete

    @turn_complete.setter
    def turn_complete(self, is_complete):
        """setter method for self._turn_complete"""
        self._turn_complete = is_complete

    def take_turn(self, x, y):
        """
        Function -- take_turn
            Accepts an x, y coordinate pair (px) and compares them to all legal
            moves for that turn. If the move is determined to be legal,
            a tile of the player's color is placed on the board square at that
            x, y grid. Sets the player's turn_complete attribute to True once
            the tile is placed.
        Parameters:
            x: int, the x coordinate of the player's move (px)
            y: int, the y coordinate of the player's move (px)
        Returns:
            None
        """
        for legal_move in self.gb.legal_moves:
            if self.turn_complete:  # player cannot place two tiles in one turn
                return

            elif (
                (x >= legal_move.player_square.x)
                and (x <= legal_move.player_square.x + self.gb.SPACING)
                and (y >= legal_move.player_square.y)
                and (y <= legal_move.player_square.y + self.gb.SPACING)
            ):

                self._place_tile(legal_move)
                self._flip_tiles(legal_move.flippable_squares)
                self.turn_complete = True

    def _place_tile(self, legal_move):
        """
        Function -- calculate_next_move
            Creates a tile object on the player square and adjusts tile counts
            on the game board
        Parameters:
            player_square: BoardSquare, the square on which the player placed
                a tile
        Returns:
            None
        """
        player_square = legal_move.player_square

        player_square.tile = Tile(
            player_square.x + self.gb.PIXEL_DISPLACEMENT,
            player_square.y + self.gb.PIXEL_DISPLACEMENT,
            self.color,
        )

        self.gb.empty_tiles -= 1

        if self.color == "black":
            self.gb.black_tiles += legal_move.total_flips + 1
            self.gb.white_tiles -= legal_move.total_flips

        elif self.color == "white":
            self.gb.white_tiles += legal_move.total_flips + 1
            self.gb.black_tiles -= legal_move.total_flips

    def _flip_tiles(self, flippable_squares):
        """
        Function -- _flip_tiles
            Changes the color of all tiles within the flippable_squares list
        Parameters:
            flippable_squares: list[BoardSquare], all board squares with
                flippable tiles inside them
        Returns:
            None
        """
        for adjacent_square in flippable_squares:

            if self.color == "black":
                adjacent_square.tile.color = "black"

            elif self.color == "white":
                adjacent_square.tile.color = "white"

    # EASY DIFFICULTY COMPUTER AI
    def calculate_next_move_easy(self):
        """
        Function -- calculate_next_move_easy
            Calculates the computer's next move according to the list of legal
            moves for that turn and the easy computer selection algorithm. The
            easy algorithm choses a random LegalMove from the list of legal
            moves and executest that move.
        Parameters:
            None
        Returns:
            None
        """
        if self.gb.legal_moves:
            move = random.randint(0, len(self.gb.legal_moves) - 1)
            return (
                (
                    self.gb.legal_moves[move].player_square.x
                    + self.gb.PIXEL_DISPLACEMENT
                ),
                (
                    self.gb.legal_moves[move].player_square.y
                    + self.gb.PIXEL_DISPLACEMENT
                ),
            )
        else:
            return None

    # MEDIUM DIFFICULTY COMPUTER AI
    def calculate_next_move_med(self):
        """
        Function -- calculate_next_move_med
            Calculates the computer's next move according to the list of legal
            moves for that turn and the medium computer selection algorithm.
            The medium algorithm choses the LegalMove instance that flips the
            highest number of tiles possible for the given turn.
        Parameters:
            None
        Returns:
            None
        """
        best_move = None

        for legal_move_sim in self.gb.legal_moves:

            if best_move is None:
                best_move = legal_move_sim

            elif len(best_move.flippable_squares) < len(
                legal_move_sim.flippable_squares
            ):
                best_move = legal_move_sim

        if best_move:
            return (
                best_move.player_square.x + self.gb.PIXEL_DISPLACEMENT,
                best_move.player_square.y + self.gb.PIXEL_DISPLACEMENT,
            )
        else:
            return None

    # HARD DIFFICULTY COMPUTER AI
    def calculate_next_move_hard(self):
        """
        Function -- calculate_next_move_hard
            Calculates the computer's next move according to the list of legal
            moves for that turn and the hard computer selection algorithm. The
            hard algorithm uses mutual recursion to recurse to the turn-depth
            specified by MAX_RECURSION_DEPTH, generating all possible game
            boards on the way down. As the recursion returns to top-level, all
            legal moves are examined and weighted based on a strategy that
            prioritizes corner and edge moves, avoids moves in the Othello
            X-squares, and maximizes tile flips. The move that best exemplifies
            that strategy is returned to inform the comparison of the next
            recursion level's legal moves. Once a final move is determined to
            be the best_move, it is returned an executed by the computer AI.
        Parameters:
            None
        Returns:
            next_move: tuple(int, int), the coordinates of the next move
        """
        game_board = copy.deepcopy(self.gb)
        computer_player = Player(game_board, "Computer", "white")
        recursion_depth = 0

        next_move = self._process_legal_moves(
            game_board, computer_player, recursion_depth
        )
        if next_move:
            return (
                next_move.player_square.x + self.gb.PIXEL_DISPLACEMENT,
                next_move.player_square.y + self.gb.PIXEL_DISPLACEMENT,
            )
        else:
            return None

    # HARD DIFFICULTY COMPUTER AI - Mutually Recursive Function
    def _process_legal_moves(self, game_board, current_turn, recursion_depth):
        """
        Function -- _process_legal_moves
            Runs a for-loop through the list of all legal moves for a given
            game board state and recursion depth. For each turn, the
            function checks for any prioritized/deprioritized moves and if
            found, adjust the respective legal move's move_value attribute
            based on pre-determined floating point values. The function then
            determines which legal move has the highest move value and returns
            it as the best move for the given recursion depth.
        Parameters:
            game_board: GameBoard, the current state of the Othello game board
            current_turn: Player, the player/computer whose turn it is
            recursion_depth: the depth level of the game board that is being
                processed from the current, active game board
        Returns:
            best_move: LegalMove, the determined best move for the current_turn
                player based on the algorithmic priorities
        """
        legal_moves = game_board.legal_moves

        recursion_depth += 1

        for legal_move in legal_moves:

            game_board_copy = copy.deepcopy(self.gb)
            player_1 = Player(game_board_copy, "Player", "black")
            player_2 = Player(game_board_copy, "Computer", "white")

            # Retrieves best move value and max tiles flipped for the move
            self._execute_legal_move(
                game_board_copy,
                legal_move,
                player_1,
                player_2,
                player_2,
                recursion_depth,
            )

            # Assign move values to legal moves
            if current_turn.name == "Computer":
                self._computer_move_calculator(legal_move, recursion_depth)
            else:
                self._player_move_calculator(legal_move, recursion_depth)

        if legal_moves:
            # Find the legal move with the highest move_value attribute
            best_move = max(legal_moves)
        else:
            best_move = None

        return best_move

    def _computer_move_calculator(self, legal_move, recursion_depth):
        """
        Function -- _computer_move_calculator
            Adjusts the legal move's move_value attribute to a final value
            based on the existence of pre-determined move conditions for the
            computer's turn
        Parameters:
            legal_move: LegalMove, a LegalMove object and associated attributes
            recursion_depth: the depth level of the game board that is being
                processed from the current, active game board
        Returns:
            None - only adjusts LegalMove move_value attribute
        """
        legal_move.move_value += (
            legal_move.max_tiles * (
                self.MOVE_VALUE_DICT["FLIPPED_TILE_COMPUTER"]) / (
                    recursion_depth))

        # Prioritizes moves in the corners of the board
        if legal_move.is_corner_move:
            legal_move.move_value += (
                self.MOVE_VALUE_DICT["CORNER_SQUARE_COMPUTER"] / (
                    recursion_depth))

        # Deprioritizes moves in the 3 squares around corner square
        elif legal_move.board_corner and (
            legal_move.board_corner.corner_square.is_empty
        ):
            legal_move.move_value -= (
                self.MOVE_VALUE_DICT["X_SQUARE_COMPUTER"] / recursion_depth)

        # Prioritizes moves on edge of board
        elif legal_move.is_edge_move:
            legal_move.move_value += (
                self.MOVE_VALUE_DICT["EDGE_SQUARE_COMPUTER"] / recursion_depth)

        for flippable_square in legal_move.flippable_squares:

            # Deprioritizes moves that flip black tiles when corner is empty
            for board_corner in self.gb.BOARD_CORNERS:
                if (
                    (flippable_square.x_index, flippable_square.y_index)
                    in board_corner.x_squares
                ) and (board_corner.corner_square.is_empty):
                    legal_move.move_value -= (
                        self.MOVE_VALUE_DICT["X_SQUARE_BLACK_TILE_FLIP"] / (
                            recursion_depth))

            # Prioritizes moves that flip black tiles on diagonals to corners
            if flippable_square in self.gb.BOARD_DIAGONALS:
                legal_move.move_value += (
                    self.MOVE_VALUE_DICT["DIAGONAL_BLACK_TILE_FLIP"] / (
                        recursion_depth))

    def _player_move_calculator(self, legal_move, recursion_depth):
        """
        Function -- _player_move_calculator
            Adjusts the legal move's move_value attribute to a final value
            based on the existence of pre-determined move conditions for the
            players's turn.
        Parameters:
            legal_move: LegalMove, a LegalMove object and associated attributes
            recursion_depth: the depth level of the game board that is being
                processed from the current, active game board
        Returns:
            None - only adjusts LegalMove move_value attribute
        """
        legal_move.move_value -= legal_move.max_tiles * (
            self.MOVE_VALUE_DICT["FLIPPED_TILE_PLAYER"] / recursion_depth)

        # Deprioritizes player move in the corners of the board
        if legal_move.is_corner_move:
            legal_move.move_value -= (
                self.MOVE_VALUE_DICT["CORNER_SQUARE_PLAYER"] / recursion_depth)

        # Prioritizes player moves in the 3 squares around corner square
        elif legal_move.board_corner and (
            legal_move.board_corner.corner_square.is_empty
        ):
            legal_move.move_value += (
                self.MOVE_VALUE_DICT["X_SQUARE_PLAYER"] / recursion_depth)

        # Deprioritizes player moves on the edge of the board
        elif legal_move.is_edge_move:
            legal_move.move_value -= (
                self.MOVE_VALUE_DICT["EDGE_SQUARE_PLAYER"] / recursion_depth)

    # HARD DIFFICULTY COMPUTER AI - Mutually Recursive Function
    def _execute_legal_move(self,
                            game_board,
                            legal_move,
                            player_1,
                            player_2,
                            current_turn,
                            recursion_depth):
        """
        Function -- _execute_legal_move
            Accepts the given game board state and a legal move and if it is
            not at the MAX RECURSION DEPTH, executes that legal move through
            the player whose current turn it is. After the move is executed,
            the function calculates the new legal moves for the game board and
            then calls _process_legal_moves with the new game board state and
            the next player turn. If it is at the MAX RECURSION DEPTH, it
            returns the total flips for the specified legal move.
        Parameters:
            game_board: GameBoard, the current state of the Othello game board
            legal_move: LegalMove, the given legal move for processing
            player_1: Player, the non-computer Player instance tied to the
                given game board
            player_2: Player, the computer Player instance tied to the given
                game board
            current_turn: Player, the player/computer whose turn it is
            recursion_depth: the depth level of the game board that is being
                processed from the current, active game board
        Returns:
            None, instead the function adjusts the max_tiles attribute of the
                given LegalMove instance for future decision-making
        """
        if recursion_depth == self.MAX_RECURSION_DEPTH:
            legal_move.max_tiles += legal_move.total_flips

        else:

            if current_turn == player_1:
                player_1.take_turn(
                    legal_move.player_square.x, legal_move.player_square.y
                )

                current_turn = player_2

            else:
                player_2.take_turn(
                    legal_move.player_square.x, legal_move.player_square.y
                )

                current_turn = player_1

            game_board.calculate_legal_moves(current_turn)

            best_move = self._process_legal_moves(
                game_board, current_turn, recursion_depth
            )

            if best_move:
                legal_move.max_tiles = best_move.max_tiles
                legal_move.move_value = best_move.move_value
