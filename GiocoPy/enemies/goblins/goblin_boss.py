import pygame
import utils.functions as functions
import assets.variables as variables
from enemies.enemy import Enemy
from enemies.special_attack_state import SpecialAttackState


special_attack_duration = 80
animation_frame_timer = 5
number_of_animation_frames = 4


class GoblinBoss(Enemy):


    def __init__(self):
        super().__init__()
        self.special_attack_state = SpecialAttackState.IDLE
        self.special_attack_duration = special_attack_duration
        self.animation_frame_timer = animation_frame_timer


    def create(self, lifepoints, enemy_image_path, enemy_jumping_image_path, enemy_image_path_shooting, enemy_jumping_shooting_image_path, bullet_speed, bullet_delay, bullet_image_path, bullet_width, bullet_height):
        super().create(lifepoints, enemy_image_path, enemy_jumping_image_path, enemy_image_path_shooting, enemy_jumping_shooting_image_path, bullet_speed, bullet_delay, bullet_image_path, bullet_width, bullet_height)
        self.initial_bullet_delay = self.bullet_delay
        self.initial_bullet_speed = self.bullet_speed
        self.animation_frame_index = 1

    
    def check_bullet_vs_bullets_collision(self, player_bullets_group):
        for bullet in self.bullets_group:
            for player_bullet in player_bullets_group:
                if (pygame.sprite.collide_mask(bullet, player_bullet)):
                    player_bullet.kill()
                    if (bullet.priority <= player_bullet.priority):
                        bullet.kill()


    def get_damage(self):
        super().get_damage()
        self.special_attack_state = SpecialAttackState.SPECIAL_ATTACK


    def shoot(self):
        if self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK:
            if self.special_attack_duration == special_attack_duration / 2:
                self.shootDelay = 0
                self.bullet_delay -= 25
                self.bullet_speed += 10
            self.special_attack_duration -= 1
            if self.special_attack_duration == 0:
                self.special_attack_state = SpecialAttackState.IDLE
                self.bullet_delay = self.initial_bullet_delay
                self.bullet_speed = self.initial_bullet_speed
                self.special_attack_duration = special_attack_duration
        super().shoot()


    def update_animation_frame(self):
        self.animation_frame_timer -= 1
        if self.animation_frame_timer == 0:
            self.animation_frame_timer = animation_frame_timer
            self.animation_frame_index += 1
            if self.animation_frame_index >= number_of_animation_frames + 1:
                self.animation_frame_index = 1


    def update_sprite(self):
        if self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK:
            self.update_animation_frame()

            self.image = pygame.image.load("./images/enemies/goblin_boss/goblin_boss_special_power.png")
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

            self.power_image = pygame.image.load("./images/enemies/goblin_boss/goblin_boss_special_power/" + str(self.animation_frame_index) + ".png")
            self.power_image = pygame.transform.scale(self.power_image, (self.width + 6, self.height + 6))
            
        else:
            super().update_sprite()

        
    def draw(self, screen):    
        super().draw(screen)
        if self.special_attack_state == SpecialAttackState.SPECIAL_ATTACK:
            screen.blit(self.power_image, pygame.Rect(self.rect.x - 3, self.rect.y - 3, self.width + 6, self.height + 6))
            
        