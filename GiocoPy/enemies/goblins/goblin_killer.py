import pygame
import assets.variables as variables
import utils.functions as functions
import utils.entity_state as entity_state
from enemies.enemy_life import EnemyLife

import utils.functions as functions

from enemies.enemy import Enemy
from enemies.special_attack_state import SpecialAttackState


doubleShootDelay = 10

class GoblinKiller(Enemy):


    def __init__(self):
        super().__init__()
    

    def shoot(self):
        super().shoot()
        if (self.shootDelay == self.bullet_delay):  
            if functions.random_int(1, 4) == 1:
                self.shootDelay = doubleShootDelay
            