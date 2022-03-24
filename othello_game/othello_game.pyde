from game_controller import GameController

BOARD_SIZE = 800
if BOARD_SIZE == 800:
    SCREEN_HEIGHT = BOARD_SIZE + 100
else:
    SCREEN_HEIGHT = BOARD_SIZE
SCREEN_WIDTH = BOARD_SIZE
SCOREBOARD_HEIGHT = SCREEN_HEIGHT - BOARD_SIZE
SCOREBOARD_WIDTH = BOARD_SIZE
global gc


def setup():
    global gc
    size(SCREEN_WIDTH, SCREEN_HEIGHT)
    colorMode(RGB, 1)
    player_name = get_player_name()
    hint_preference = get_hint_preference()
    difficulty = get_difficulty_level()
    font_dict = {}
    font_dict["player_font"] = createFont("Arial", 24, True)
    font_dict["tile_font"] = createFont("Arial Bold", 30, True)
    font_dict["score_font"] = createFont("Arial", 34, True)
    font_dict["othello_font"] = createFont("Garuda", 24, True)
    font_dict["winner_font"] = createFont("Arial", 44, True)
    font_dict["remaining_tiles"] = createFont("Arial", 16, True)
    gc = GameController(BOARD_SIZE, 
                        SCOREBOARD_WIDTH, 
                        SCOREBOARD_HEIGHT, 
                        player_name,
                        hint_preference,
                        difficulty,
                        font_dict)


def get_player_name():
    name = None

    while not name:
        name = input('Enter your name:')

    print('Hi ' + name + ", welcome to Othello!")
    return name

def get_hint_preference():
    preference = None

    preference = input("Do you want move hints? [y/N]: ")

    if preference.lower() == "yes" or preference.lower() == "y":
        return "y"
    else:
        return "n"

def get_difficulty_level():
    difficulty = None

    preference = input("Please specify your difficulty level: [easy/medium/hard]: ")

    if preference.lower() == "easy" or preference.lower() == "e":
        return "e"
    elif preference.lower() == "medium" or preference.lower() == "m":
        return "m"
    else:
        return "h"


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def draw():
    background(0)
    gc.gb.display()
    if BOARD_SIZE == 800:
        gc.sb.display()
    gc.update()


def mouseClicked():
    if gc.active_turn is gc.player_1:
        gc.active_turn.take_turn(mouseX, mouseY)
