import pygame
import assets.variables as variables
import utils.functions as functions
import utils.entity_state as entity_state
from enemies.enemy_life import EnemyLife

from enemies.enemy import Enemy
from enemies.special_attack_state import SpecialAttackState

animation_frame_timer = 6
number_of_animation_frames = 3


class GoblinWarrior(Enemy):


    def __init__(self):
        super().__init__()
        self.has_special_attacked = False
        # self.special_attack_duration = 400
        self.special_attack_duration = 0
        self.animation_frame_timer = animation_frame_timer
        self.special_attack_state = SpecialAttackState.IDLE


    def create(self, lifepoints, enemy_image_path, enemy_jumping_image_path, enemy_image_path_shooting, enemy_jumping_shooting_image_path, bullet_speed, bullet_delay, bullet_image_path, bullet_width, bullet_height):
        super().create(lifepoints, enemy_image_path, enemy_jumping_image_path, enemy_image_path_shooting, enemy_jumping_shooting_image_path, bullet_speed, bullet_delay, bullet_image_path, bullet_width, bullet_height)
        self.initial_bullet_speed = bullet_speed
        self.initial_bullet_delay = bullet_delay
        self.animation_frame_index = 1
        self.opacity = 0
        self.power_opacity = 15

    
    def check_bullet_vs_bullets_collision(self, player_bullets_group):
        for bullet in self.bullets_group:
            for player_bullet in player_bullets_group:
                if (pygame.sprite.collide_mask(bullet, player_bullet)):
                    player_bullet.kill()
                    if (bullet.priority <= player_bullet.priority):
                        bullet.kill()


    def shoot(self):
        if self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK:
            # self.special_attack_duration -= 1
            self.special_attack_duration += 1
            # if self.special_attack_duration == 0:
            #     self.special_attack_state = entity_state.AttackState.IDLE
            #     self.bullet_speed = self.initial_bullet_speed
            #     self.bullet_delay = self.initial_bullet_delay

        if self.state == entity_state.State.GROUND and self.attack_state == entity_state.AttackState.IDLE and self.life.is_lower_than_half() and not self.has_special_attacked:
            if functions.random_float(0, 20) > 19:
                self.special_attack_state = SpecialAttackState.SPECIAL_ATTACK
                self.bullet_speed += 0
                self.bullet_delay -= 25
                self.life.full_recover()
                self.has_special_attacked = True
            else:
                super().shoot()
        else:
            super().shoot()


    def update_animation_frame(self):
        self.power_image = pygame.image.load("./images/enemies/goblin_warrior/power_animation/" + str(self.animation_frame_index) + ".png")
        self.power_image = pygame.transform.scale(self.power_image, (self.width, self.height))
        if self.special_attack_duration < 50:
            self.power_opacity += 10
        # if self.special_attack_duration < 50:
        #     self.power_opacity -= 10
        self.power_image.set_alpha(self.power_opacity)
        self.animation_frame_timer -= 1
        if self.animation_frame_timer == 0:
            self.animation_frame_timer = animation_frame_timer
            self.animation_frame_index += 1
            if self.animation_frame_index >= number_of_animation_frames + 1:
                self.animation_frame_index = 1


    def update_sprite(self):
        if self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK:
            self.update_animation_frame()
            self.image = pygame.image.load("./images/enemies/goblin_warrior/goblin_preparing_special_power.png")
            self.lower_image = pygame.transform.scale(pygame.image.load("./images/enemies/goblin_warrior/prova.png"), (self.width, self.height))
            
            if self.special_attack_duration < 100:
                if self.opacity <= 255:
                    self.opacity += 4
            # if self.special_attack_duration > 300:
            #     if self.opacity <= 255:
            #         self.opacity += 4
            # if self.special_attack_duration < 50:
            #     if self.opacity <= 0:
            #         self.opacity += 8
            self.image.set_alpha(self.opacity)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        else:
            super().update_sprite()

        
    def draw(self, screen):    
        if self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK:
            screen.blit(self.lower_image, pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            screen.blit(self.power_image, pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
        super().draw(screen)