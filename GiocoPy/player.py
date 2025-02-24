import pygame
import assets.variables as variables
import utils.entity_state as entity_state
from bullet import Bullet
from heart import Heart
from energy_bar import EnergyBar



class Player(pygame.sprite.Sprite):

    def __init__(self, lifepoints, speed, energies, energy_recovery_delay, bullet_speed, bullet_delay, bullet_image_path):
        super().__init__()
        self.width = 120
        self.height = 120
        self.rect = pygame.Rect(0, variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.height, self.width, self.height)
        self.speed = speed
        self.energies = energies
        self.bullet_speed = bullet_speed
        self.bullet_delay = bullet_delay
        self.bullet_image_path = bullet_image_path

        self.x = 0
        self.y = variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.height
        self.state = entity_state.State.GROUND
        self.canJump = True
        self.gravity = 0
        self.bullets_group = pygame.sprite.Group()
        self.hearts_group = pygame.sprite.Group()
        for i in range(lifepoints):
            self.hearts_group.add(Heart(10 + 80 * i, 10, 70, 60, "./images/hearth.png"))
        self.energy = EnergyBar(energies, energy_recovery_delay)
        self.shootDelay = variables.BULLET_DELAY
        self.attack_state = entity_state.AttackState.IDLE


    def get_center(self):
        return (self.rect.x + self.width / 2, self.rect.y + self.height / 2)
    

    def play_damage_sound(self):
        sound = pygame.mixer.Sound("./sounds/hurt.mp3")
        sound.play()

    def play_bullets_sound(self):
        sound = pygame.mixer.Sound("./sounds/bullet.mp3")
        sound.play()

    def play_death_sound(self):
        sound = pygame.mixer.Sound("./sounds/death.mp3")
        sound.play()

    def play_jump_sound(self):
        sound = pygame.mixer.Sound("./sounds/jump.wav")
        sound.play()

        
    def shoot(self):
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0]:
            if (self.energy.get_available_energy() >= 5 and self.shootDelay == 0):
                self.attack_state = entity_state.AttackState.SHOOTING
                mouse_pos = pygame.mouse.get_pos()
                self.bullets_group.add(
                    Bullet(
                        self.rect.x + self.width, 
                        self.rect.y + self.height / 2 - 60 / 2,
                        60,
                        60, 
                        "rigth",
                        self.bullet_speed,
                        1.2 * self.bullet_speed,
                        self.bullet_delay,
                        "./images/bullet.png",
                        mouse_pos[0],
                        mouse_pos[1],
                        0, # gravity
                        1
                    )
                )
                self.energy.consume_energy()
                self.shootDelay = variables.BULLET_DELAY
                self.play_bullets_sound()
        else:
            self.attack_state = entity_state.AttackState.IDLE
            if (self.energy.get_available_energy() < self.energies):
                self.energy.recover_energy()
            if (self.shootDelay > 0):
                self.shootDelay -= 1


    def bullets_move(self):
        self.bullets_group.update()


    def check_bullet_collision(self, enemy_bullets_group):
        for bullet in enemy_bullets_group:
            if (pygame.sprite.collide_mask(bullet, self)):
                bullet.kill()
                last_heart = self.hearts_group.sprites()[-1]
                last_heart.kill()
                if (len(self.hearts_group) > 0):
                    self.play_damage_sound()
                else:
                    self.play_death_sound()


    def check_bullet_out(self):
        for bullet in self.bullets_group:
            if (bullet.rect.x > variables.SCREEN_WIDTH + 50):
                bullet.kill()
            elif (bullet.rect.x < - 50):
                bullet.kill()
            elif (bullet.rect.y > variables.SCREEN_HEIGHT + 50):
                bullet.kill()


    def move(self):

        dx = 0
        dy = 0

        # handle movement keys
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            if (self.rect.x > 0):
                dx -= self.speed
        if key[pygame.K_d]:
            if (self.rect.x < variables.SCREEN_WIDTH - self.width):
                dx += self.speed
        if key[pygame.K_SPACE or pygame.K_w]:
            if (self.state == entity_state.State.JUMPING and self.canJump):
                self.state = entity_state.State.DOUBLE_JUMPING
                self.canJump = False
                self.gravity = 0 
                self.play_jump_sound()
                dy -= variables.PLAYER_JUMP_SPEED
            if (self.state == entity_state.State.GROUND and self.canJump):
                self.state = entity_state.State.JUMPING
                self.canJump = False
                self.gravity = 0 
                dy -= variables.PLAYER_JUMP_SPEED
                self.play_jump_sound()
        else:
            if (self.state == entity_state.State.JUMPING):
                self.canJump = True
        
        # gravity
        self.gravity += 1
        dy += self.gravity

        self.rect.x += dx

        self.rect.y = min((self.rect.y + dy), (variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.height))
        self.rect.y = max(self.rect.y, 0)
        if (self.rect.y == variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.height):
            self.state = entity_state.State.GROUND
            self.gravity = 0
            self.canJump = True


    def update_sprite(self):
        if (self.attack_state == entity_state.AttackState.IDLE and self.state == entity_state.State.GROUND):
            self.image = pygame.image.load("./images/player/player.png")
        if (self.attack_state == entity_state.AttackState.IDLE and (self.state == entity_state.State.JUMPING or self.state == entity_state.State.DOUBLE_JUMPING)):
            self.image = pygame.image.load("./images/player/player_jumping.png")
        if (self.attack_state == entity_state.AttackState.SHOOTING):
            self.image = pygame.image.load("./images/player/player_shooting.png")
        if (self.attack_state == entity_state.AttackState.SHOOTING and (self.state == entity_state.State.JUMPING or self.state == entity_state.State.DOUBLE_JUMPING)):
            self.image = pygame.image.load("./images/player/player_jumping_shooting.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    
    def update_bullets(self, enemy, enemy_bullets_group):
        self.bullets_move()
        self.check_bullet_out()
        self.check_bullet_collision(enemy_bullets_group)

    def update(self):
        self.move()
        self.update_sprite()
        self.shoot()
        
        
    def draw(self, screen):
        self.bullets_group.draw(screen)
        self.hearts_group.draw(screen)
        self.energy.draw(screen)
        screen.blit(self.image, self.rect)