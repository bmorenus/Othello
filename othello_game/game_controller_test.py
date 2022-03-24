from player import Player
from game_controller import GameController
from game_board import GameBoard
from scoreboard import Scoreboard

import pytest


def test_constructor():
    gc: GameController = GameController(game_board_size=800,
                                        score_board_width=800,
                                        score_board_height=100,
                                        player_name="Brian",
                                        hint_preference="y",
                                        difficulty="h",
                                        font_dict=None)
    assert isinstance(gc.gb, GameBoard)
    assert isinstance(gc.player_1, Player)
    assert isinstance(gc.player_2, Player)
    assert isinstance(gc.active_turn, Player)
    assert isinstance(gc.sb, Scoreboard)
    assert gc.gb.board_size == 800
    assert gc.player_1.name == "Brian"
    assert gc.player_1.color == "black"
    assert gc.player_2.name == "Computer"
    assert gc.player_2.color == "white"
    assert gc.active_turn == gc.player_1
    assert gc.passed_turn_counter == 0
    assert gc.display_counter == 0
    assert gc.winner is None
    assert gc.winner_printed is False


def test_turn_handoff():
    gc: GameController = GameController(game_board_size=800,
                                        score_board_width=800,
                                        score_board_height=100,
                                        player_name="Brian",
                                        hint_preference="y",
                                        difficulty="h",
                                        font_dict=None)

    # Confirm the current turn is with player 1 on game start
    assert gc.active_turn == gc.player_1
    # Confirm the current turn remains with player 1 until turn complete
    gc.update()
    assert gc.active_turn == gc.player_1
    gc.player_1.turn_complete = True
    gc.update()
    # Confirm the current turn goes to player 2 after player 1 turn complete
    assert gc.active_turn == gc.player_2
    # Confirm the player 1 turn complete is reverted to False
    assert gc.player_1.turn_complete is True
    # Confirm the current turn remains with player 2 until turn complete
    gc.update()
    assert gc.active_turn == gc.player_2
    gc.display_counter = 99
    gc.update()
    # Confirm the current turn goes to player 1 after player 2 turn complete
    assert gc.active_turn == gc.player_1
    # Confirm the player 2 turn complete is reverted to False
    assert gc.player_2.turn_complete is True


@pytest.mark.skip(reason="Banner class is called requiring display functions")
def test_passed_turn_counter():
    gc: GameController = GameController(game_board_size=800,
                                        score_board_width=800,
                                        score_board_height=100,
                                        player_name="Brian",
                                        hint_preference="y",
                                        difficulty="h",
                                        font_dict=None)

    assert gc.active_turn == gc.player_1
    gc.passed_turn_counter += 1
    gc.player_1.turn_complete = True
    gc.update()
    assert gc.passed_turn_counter == 1
    assert gc.player_2.turn_complete is False
    assert gc.active_turn == gc.player_2
    gc.passed_turn_counter += 1
    gc.player_2.turn_complete = True
    assert gc.passed_turn_counter == 2
    gc.update()
    assert gc.active_turn is None
