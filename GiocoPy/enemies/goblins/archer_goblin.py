import pygame
import utils.functions as functions
import assets.variables as variables
import utils.entity_state as entity_state

from enemies.enemy import Enemy
from enemies.special_attack_state import SpecialAttackState


special_attack_duration = 210
lower_duration = 60


class ArcherGoblin(Enemy):


    def __init__(self):
        super().__init__()
        self.special_attack_state = SpecialAttackState.IDLE
        self.special_attack_duration = special_attack_duration
        self.mustJump = False
        self.lower_duration = False
        self.lower_duration = 0

    
    def create(self, lifepoints, enemy_image_path, enemy_jumping_image_path, enemy_image_path_shooting, enemy_jumping_shooting_image_path, bullet_speed, bullet_delay, bullet_image_path, bullet_width, bullet_height):
        super().create(lifepoints, enemy_image_path, enemy_jumping_image_path, enemy_image_path_shooting, enemy_jumping_shooting_image_path, bullet_speed, bullet_delay, bullet_image_path, bullet_width, bullet_height)
        self.up_rect = self.rect
        self.low_rect = pygame.Rect(self.rect.x, self.rect.y + 60, self.width, self.height - 60)
        self.bullet_delay = bullet_delay



    def check_bullet_collision(self, bullets):
        super().check_bullet_collision(bullets)
        for bullet in bullets:
            
            collision_rect_upper = pygame.Rect(self.rect.x - 5, self.rect.y - 50, 5, 50)
            collision_rect_lower = pygame.Rect(self.rect.x - 5, self.rect.y, 5, self.height)

            if collision_rect_lower.colliderect(bullet.rect):
                self.mustJump = True
            elif collision_rect_upper.colliderect(bullet.rect):
                if self.lower_duration == 0:
                    self.rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height - 60)
                    self.rect.y += 60
                self.lower_duration = lower_duration



    def shoot(self):
        if self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK:
            self.special_attack_duration -= 1
            if self.special_attack_duration == 0:
                self.bullet_delay += 25
                self.special_attack_state = SpecialAttackState.IDLE
                self.special_attack_duration = special_attack_duration
        if self.special_attack_state == SpecialAttackState.IDLE:
            if functions.random_float(0, 120) > 119:
                self.special_attack_state = SpecialAttackState.SPECIAL_ATTACK
                self.bullet_delay -= 25
        super().shoot()

    
    def move(self):
        if (self.special_attack_state == SpecialAttackState.IDLE):
            super().move()
        elif (self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK):
            self.check_if_is_on_ground()
            dy = 0
            if (self.state == entity_state.State.GROUND and self.mustJump == True):
                dy -= 650
                self.state = entity_state.State.JUMPING
                self.mustJump = False
            self.vertical_weight += 1
            dy += self.vertical_weight
            # update position
            self.rect.y = min((self.rect.y + dy), (variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.rect.height))
            self.rect.y = max(self.rect.y, 0)
            if (self.rect.y == variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.rect.height):
                self.vertical_weight = 0


    def update_sprite(self):
        if self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK or self.lower_duration > 0:
            if self.lower_duration > 0:
                self.lower_duration -= 1
                if self.attack_state == entity_state.AttackState.IDLE:
                    self.image = pygame.image.load("./images/enemies/archer_goblin/goblin_lowered.png")
                elif self.attack_state == entity_state.AttackState.SHOOTING:
                    self.image = pygame.image.load("./images/enemies/archer_goblin/goblin_lowered_shooting.png")
                if (self.lower_duration == 0):
                    self.rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height + 60)
            else:
                if (self.attack_state == entity_state.AttackState.IDLE and self.state == entity_state.State.GROUND):
                    self.image = pygame.image.load("./images/enemies/archer_goblin/archer_goblin_special_power.png")
                if (self.attack_state == entity_state.AttackState.IDLE and (self.state == entity_state.State.JUMPING or self.state == entity_state.State.DOUBLE_JUMPING)):
                    self.image = pygame.image.load("./images/enemies/archer_goblin/archer_goblin_special_power_jumping.png")
                if (self.attack_state == entity_state.AttackState.SHOOTING):
                    self.image = pygame.image.load("./images/enemies/archer_goblin/archer_goblin_special_power_shooting.png")
                if (self.attack_state == entity_state.AttackState.SHOOTING and (self.state == entity_state.State.JUMPING or self.state == entity_state.State.DOUBLE_JUMPING)):
                    self.image = pygame.image.load("./images/enemies/archer_goblin/archer_goblin_special_power_jumping_shooting.png")
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        else:
            super().update_sprite()