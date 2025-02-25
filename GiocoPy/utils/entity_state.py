from enum import Enum

class State(Enum):
    GROUND = 1
    JUMPING = 2
    DOUBLE_JUMPING = 3

class AttackState(Enum):
    IDLE = 1
    SHOOTING = 2
    RECOVERING = 3
    END_RECOVERING1 = 4
    END_RECOVERING2 = 5