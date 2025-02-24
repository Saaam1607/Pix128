from enum import Enum
import goblin_saga.saga_progress as saga_progress

class State(Enum):
    GAME_LOAD_SELECTION = 1
    CHAPTER_MENU = 2
    CHAPTER_INIT = 3
    DIALOGUE = 4
    ENEMY_DIALOGUE = 5
    PREPARING_BATTLE = 6
    BATTLE = 7
    WIN = 8

state = State.GAME_LOAD_SELECTION
selected_chapter = 0

def open_new_chapter_menu(self):
    saga_progress.reset()
    global state
    state = State.CHAPTER_MENU

def open_chapter_menu(self):
    global state
    state = State.CHAPTER_MENU

def init_chapter(self, number):
    global state, selected_chapter
    state = State.CHAPTER_INIT
    selected_chapter = number

def open_win_menu(self):
    global state
    state = State.WIN

def get_saga_state(saga_progress_label):
    progress_mapping = {
        "dialogue": State.DIALOGUE,
        "enemy_dialogue": State.ENEMY_DIALOGUE,
        "preparing_battle": State.PREPARING_BATTLE,
        "battle": State.BATTLE,
    }
    return progress_mapping.get(saga_progress_label, None)