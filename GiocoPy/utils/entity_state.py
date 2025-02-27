from enum import Enum

class State(Enum):
    GROUND = 1
    JUMPING = 2
    DOUBLE_JUMPING = 3

class EvolutionState(Enum):
    BASE = 1
    EVOLVED = 2

class AttackState(Enum):
    IDLE = 1
    SHOOTING = 2
    SHOOTING_COMBO = 3
    RECOVERING = 3
    END_RECOVERING1 = 4
    END_RECOVERING2 = 5

class AttackComboState(Enum):
    COMBO_IDLE = 1
    COMBO_1 = 2
    COMBO_2 = 3
    COMBO_3 = 4

class AuraState(Enum):
    IDLE = 1
    START_RECOVERING = 2
    RECOVERING = 3
    SUB_RECOVERING = 4
    END_RECOVERING1 = 5
    END_RECOVERING2 = 6