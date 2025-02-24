from enum import Enum
import goblin_saga.saga_progress as saga_progress


# ---------- state ----------
class State(Enum):
    MAIN_MENU = 1
    SAGA_SELECTION = 2
    GOBLIN_SAGA = 3
    CASTLE_SAGA = 4

state = State(State.MAIN_MENU)


def open_main_menu(self):
    global state
    state = State.MAIN_MENU

def open_saga_selection_menu(self):
    global state
    state = State.SAGA_SELECTION

def open_goblin_saga(self):
    global state
    state = State.GOBLIN_SAGA

def open_castle_saga(self):
    global state
    state = State.CASTLE_SAGA