import pygame
import assets.variables as variables
import random
import utils.entity_state as entity_state
from bullet import Bullet
from enemies.enemy_life import EnemyLife



class Enemy(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()


    def create(self, lifepoints, enemy_image_path, enemy_jumping_image_path, enemy_image_path_shooting, enemy_jumping_shooting_image_path, bullet_speed, bullet_delay, bullet_image_path, bullet_width, bullet_height):
        self.enemy_image_path = enemy_image_path
        self.enemy_jumping_image_path = enemy_jumping_image_path
        self.enemy_image_path_shooting = enemy_image_path_shooting
        self.enemy_jumping_shooting_image_path = enemy_jumping_shooting_image_path
        self.state = entity_state.State.GROUND
        self.attack_state = entity_state.AttackState.IDLE
        self.bullet_speed = bullet_speed
        self.bullet_delay = bullet_delay
        self.bullet_image_path = bullet_image_path
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.width = 240
        self.height = 240
        self.rect = pygame.Rect(
            variables.SCREEN_WIDTH - self.width,
            variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.height,
            self.width,
            self.height
        )
        self.image = pygame.image.load(self.enemy_image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.vertical_weight = 0
        self.bullets_group = pygame.sprite.Group()
        self.shootDelay = 5
        self.shoot_animation_delay = 0
        self.life = EnemyLife(lifepoints)
        self.aim_x = 0
        self.aim_y = 0
        self.gravity = variables.REAL_GRAVITY
        self.bullet_priority = 1


    def play_damage_sound(self):
        hit_sound = pygame.mixer.Sound("./sounds/hit.wav")
        hit_sound.play()
        damage_sound = pygame.mixer.Sound("./sounds/goblin_damage.mp3")
        damage_sound.play()


    def check_bullet_collision(self, bullets):
        for bullet in bullets:
            if (pygame.sprite.collide_mask(bullet, self)):
                bullet.kill()
                self.get_damage()
                self.play_damage_sound()


    def get_damage(self):
        self.life.get_damage()


    def play_swosh_sound(self):
        sound = pygame.mixer.Sound("./sounds/whoosh.flac")
        sound.set_volume(0.25)
        sound.play()


    def take_aim(self, x, y):
        self.aim_x = x
        self.aim_y = y


    def shoot(self):
        if (self.shootDelay == 0):
            self.bullets_group.add(
                Bullet(
                    self.rect.x + self.rect.width / 2,
                    self.rect.y + self.rect.width / 2,
                    self.bullet_width,
                    self.bullet_height,
                    "left",
                    self.bullet_speed,
                    10000,
                    self.bullet_delay,
                    self.bullet_image_path,
                    self.aim_x,
                    self.aim_y,
                    self.gravity,
                    self.bullet_priority
                )
            )
            self.shootDelay = self.bullet_delay
            self.play_swosh_sound()
            self.shoot_animation_delay = variables.BULLET_ENEMY_ANIMATION_DELAY
            self.attack_state = entity_state.AttackState.SHOOTING
        else:
            if (self.shoot_animation_delay > 0):
                self.shoot_animation_delay -= 1
            else:
                self.attack_state = entity_state.AttackState.IDLE
            self.shootDelay -= 1

            
    def bullets_move(self):
        for bullet in self.bullets_group:
            bullet.update()
            if (bullet.rect.x < 0):
                bullet.kill()


    def check_bullet_vs_bullets_collision(self, player_bullets_group):
        for bullet in self.bullets_group:
            for player_bullet in player_bullets_group:
                if (pygame.sprite.collide_mask(bullet, player_bullet)):
                    bullet.kill()
                    player_bullet.kill()


    def check_if_is_on_ground(self):
        if (self.rect.y == variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.rect.height):
            self.state = entity_state.State.GROUND


    def move(self):

        self.check_if_is_on_ground()
        dy = 0

        if (self.state == entity_state.State.GROUND):
            if (random.randint(1, 20) == 20 ):
                dy -= random.randint(1, 20) * 20
                self.state = entity_state.State.JUMPING

        self.vertical_weight += 1
        dy += self.vertical_weight

        # update position
        self.rect.y = min((self.rect.y + dy), (variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.rect.height))
        self.rect.y = max(self.rect.y, 0)

        if (self.rect.y == variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.rect.height):
            self.vertical_weight = 0


    def update_sprite(self):
        if (self.attack_state == entity_state.AttackState.IDLE and self.state == entity_state.State.GROUND):
            self.image = pygame.image.load(self.enemy_image_path)
        if (self.attack_state == entity_state.AttackState.IDLE and (self.state == entity_state.State.JUMPING)):
            self.image = pygame.image.load(self.enemy_jumping_image_path)
        if (self.attack_state == entity_state.AttackState.SHOOTING):
            self.image = pygame.image.load(self.enemy_image_path_shooting)
        if (self.attack_state == entity_state.AttackState.SHOOTING and (self.state == entity_state.State.JUMPING)):
            self.image = pygame.image.load(self.enemy_jumping_shooting_image_path)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

    
    def update_bullets(self, player_bullets):
        self.bullets_move()
        self.check_bullet_collision(player_bullets)
        self.check_bullet_vs_bullets_collision(player_bullets)


    def update(self):
        self.move()
        self.shoot()
        self.update_sprite()
        

    def draw(self, screen):        
        self.bullets_group.draw(screen)
        self.life.draw(screen)
        screen.blit(self.image, self.rect)