import pygame
import assets.variables as variables
import utils.functions as functions
import utils.entity_state as entity_state
from enemies.enemy_life import EnemyLife

from enemies.enemy import Enemy
from enemies.special_attack_state import SpecialAttackState



class CowardGoblin(Enemy):


    def __init__(self):
        super().__init__()
        self.special_attack_state = SpecialAttackState.IDLE


    def create(self, lifepoints, enemy_image_path, enemy_jumping_image_path, enemy_image_path_shooting, enemy_jumping_shooting_image_path, bullet_speed, bullet_delay, bullet_image_path, bullet_width, bullet_height):
        super().create(lifepoints, enemy_image_path, enemy_jumping_image_path, enemy_image_path_shooting, enemy_jumping_shooting_image_path, bullet_speed, bullet_delay, bullet_image_path, bullet_width, bullet_height)
        self.initial_bullet_speed = self.bullet_speed
        self.special_attack_duration = self.bullet_delay + 1
        self.initial_bullet_image_path = self.bullet_image_path
        self.initial_bullet_width = self.bullet_width
        self.initial_bullet_height = self.bullet_height
        self.inital_gravity = self.gravity


    def check_bullet_vs_bullets_collision(self, player_bullets_group):
        for bullet in self.bullets_group:
            for player_bullet in player_bullets_group:
                if (pygame.sprite.collide_mask(bullet, player_bullet)):
                    player_bullet.kill()
                    if (bullet.priority <= player_bullet.priority):
                        bullet.kill()
    

    def shoot(self):
        
        if self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK:
            self.special_attack_duration -= 1
            if self.special_attack_duration == 0:
                self.special_attack_state = SpecialAttackState.IDLE
                self.bullet_image_path = self.initial_bullet_image_path
                self.bullet_width = self.initial_bullet_width
                self.bullet_height = self.initial_bullet_height
                self.gravity += 0.3
                self.bullet_priority -= 1
        
        if self.shootDelay == self.bullet_delay and self.special_attack_state == SpecialAttackState.IDLE: # has immediatley shot and it's IDLE
            if functions.random_int(1, 2) == 1:
                self.special_attack_state = SpecialAttackState.SPECIAL_ATTACK
                self.bullet_image_path = "./images/enemies/coward_goblin/bullet_special_power.png"
                self.bullet_width = 110
                self.bullet_height = 110
                self.gravity -= 0.3
                self.bullet_priority += 1
                self.special_attack_duration = self.bullet_delay + 1

        super().shoot()


    def update_sprite(self):
        if self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK:
            if self.attack_state == entity_state.AttackState.IDLE:
                self.image = pygame.image.load("./images/enemies/coward_goblin/coward_goblin_special_power.png")
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            elif self.attack_state == entity_state.AttackState.SHOOTING:
                self.image = pygame.image.load("./images/enemies/coward_goblin/coward_goblin_special_power_shooting.png")
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
        else:
            super().update_sprite()