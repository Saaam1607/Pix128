import pygame
import assets.variables as variables
import utils.entity_state as entity_state
from bullet import Bullet
from heart import Heart
from energy_bar import EnergyBar
from sub_energy_bar import SubEnergyBar
from aura import Aura

fullRecoverAnimationDelay = 14
recoverStartDelay = 15
subEnergyRequired = 30

class Player(pygame.sprite.Sprite):

    def __init__(self, lifepoints, speed, energies, energy_recovery_delay, bullet_speed, bullet_max_speed, bullet_image_path):
        super().__init__()
        self.width = 120
        self.height = 140
        self.rect = pygame.Rect(0, variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.height, self.width, self.height)
        self.speed = speed
        self.energies = energies
        self.sub_energies = 0
        self.bullet_speed = bullet_speed
        self.bullet_max_speed = bullet_max_speed
        self.bullet_image_path = bullet_image_path
        self.full_recover_animation_delay = fullRecoverAnimationDelay
        self.shooting_animation_delay = variables.BULLET_COMBO_DELAY
        self.recover_start_delay = recoverStartDelay

        self.x = 0
        self.y = variables.SCREEN_HEIGHT - variables.TERRAIN_HEIGHT - self.height
        self.state = entity_state.State.GROUND
        self.canJump = True
        self.gravity = 0
        self.jump_speed = variables.PLAYER_JUMP_SPEED
        self.bullets_group = pygame.sprite.Group()
        self.hearts_group = pygame.sprite.Group()
        for i in range(lifepoints):
            self.hearts_group.add(Heart(10 + 80 * i, 10, 70, 60, "./images/hearth.png"))
        self.energy = EnergyBar(energies, energy_recovery_delay - 1)
        self.sub_energy = SubEnergyBar(subEnergyRequired, energy_recovery_delay + 1)
        
        self.bullet_delay = variables.BULLET_DELAY
        self.bullet_long_delay = variables.BULLET_LONG_DELAY

        self.shootDelay = self.bullet_delay
        self.combo_shoot_delay = variables.BULLET_COMBO_DELAY
        self.attack_state = entity_state.AttackState.IDLE
        self.combo_state = entity_state.AttackComboState.COMBO_IDLE
        self.evolution_state = entity_state.EvolutionState.BASE
        self.aura_state = entity_state.AuraState.IDLE
        
        self.aura = Aura(self.rect.x - 10, self.rect.y - 10)

        self.recover_scream = pygame.mixer.Sound("./sounds/recover_scream.mp3")

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

    def play_recover_sound(self):
        self.recover_scream.play()

    def stop_recover_sound(self):
        self.recover_scream.stop()

    def play_aura_end_sound(self):
        sound = pygame.mixer.Sound("./sounds/aura_end.mp3")
        sound.play()

        
    def shoot(self):
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0] and self.aura_state == entity_state.AuraState.IDLE:
            if (self.energy.get_available_energy() >= 5 and self.shootDelay == 0):
                
                if (self.combo_state == entity_state.AttackComboState.COMBO_IDLE or self.combo_shoot_delay == 0):
                    self.combo_state = entity_state.AttackComboState.COMBO_1
                elif (self.combo_state == entity_state.AttackComboState.COMBO_1):
                    self.combo_state = entity_state.AttackComboState.COMBO_2
                elif (self.combo_state == entity_state.AttackComboState.COMBO_2):
                    self.combo_state = entity_state.AttackComboState.COMBO_3

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
                        self.bullet_max_speed,
                        "./images/bullet.png",
                        mouse_pos[0],
                        mouse_pos[1],
                        0, # gravity
                        1
                    )
                )
                self.energy.consume_energy()
                
                if (self.combo_state != entity_state.AttackComboState.COMBO_3):
                    self.shootDelay = self.bullet_delay
                else:
                    self.shootDelay = self.bullet_long_delay

                self.combo_shoot_delay = variables.BULLET_COMBO_DELAY
                self.play_bullets_sound()
        else:
            if (self.shootDelay > 0):
                self.shootDelay -= 1
            if (self.combo_shoot_delay > 0):
                self.combo_shoot_delay -= 1

            if (self.aura_state == entity_state.AuraState.RECOVERING):
                if (self.energy.get_available_energy() < self.energies):
                    self.energy.recover_energy()
            elif (self.aura_state == entity_state.AuraState.SUB_RECOVERING):
                if (self.sub_energy.get_available_energy() < subEnergyRequired):
                    self.sub_energy.recover_energy()

    def bullets_move(self):
        self.bullets_group.update()

    def bustStats(self):
        self.speed -= 3
        self.bullet_speed -= 5
        self.bullet_delay += 2
        self.bullet_long_delay += 5
        self.jump_speed += 30

    def resetStats(self):
        self.speed += 3
        self.bullet_speed += 5
        self.bullet_delay -= 2
        self.bullet_long_delay -= 5
        self.jump_speed -= 30

    def check_bullet_collision(self, enemy_bullets_group):
        for bullet in enemy_bullets_group:
            if (pygame.sprite.collide_mask(bullet, self)):
                bullet.kill()
                last_heart = self.hearts_group.sprites()[-1]
                if (last_heart.image_path == "./images/energy_hearth.png"):
                    self.evolution_state = entity_state.EvolutionState.BASE
                    self.bustStats()
                    self.sub_energy.consume_energy()
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

    def updateAuraState(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_s]: 
            if (self.aura_state == entity_state.AuraState.IDLE):
                if (self.gravity == 0):
                    if (self.energy.get_available_energy() != self.energies or self.sub_energy.get_available_energy() != subEnergyRequired):
                        self.aura_state = entity_state.AuraState.START_RECOVERING
                    elif (self.sub_energy.get_available_energy() == subEnergyRequired and self.evolution_state == entity_state.EvolutionState.BASE):
                        self.aura_state = entity_state.AuraState.SUB_RECOVERING
                    
            elif (self.aura_state == entity_state.AuraState.START_RECOVERING):
                if (self.recover_start_delay > 0):
                    self.recover_start_delay -= 1
                else:
                    if (self.energy.get_available_energy() != self.energies):
                        self.aura_state = entity_state.AuraState.RECOVERING
                        self.recover_start_delay = recoverStartDelay
                        self.play_recover_sound()
                        self.aura.resetAnimation()
                    elif (self.sub_energy.get_available_energy() != subEnergyRequired):
                        self.aura_state = entity_state.AuraState.SUB_RECOVERING
                        self.recover_start_delay = recoverStartDelay
                        self.play_recover_sound()
                        self.aura.resetAnimation()
        elif (self.aura_state == entity_state.AuraState.START_RECOVERING or self.aura_state == entity_state.AuraState.RECOVERING or self.aura_state == entity_state.AuraState.SUB_RECOVERING):
            self.aura_state = entity_state.AuraState.IDLE
            self.stop_recover_sound()
        if (self.aura_state == entity_state.AuraState.RECOVERING):
            if (self.energy.get_available_energy() == self.energies):
                self.aura_state = entity_state.AuraState.END_RECOVERING1
                self.stop_recover_sound()
                self.play_aura_end_sound()
        elif (self.aura_state == entity_state.AuraState.SUB_RECOVERING):
            if (self.sub_energy.get_available_energy() == subEnergyRequired):
                self.aura_state = entity_state.AuraState.END_RECOVERING1
                self.stop_recover_sound()
                self.play_aura_end_sound()
                self.evolution_state = entity_state.EvolutionState.EVOLVED
                self.resetStats()
                self.hearts_group.add(Heart(10 + 80 * len(self.hearts_group), 10, 70, 60, "./images/energy_hearth.png"))

        elif (self.aura_state == entity_state.AuraState.END_RECOVERING1):
            if (self.full_recover_animation_delay > 0):
                self.full_recover_animation_delay -= 1
            else:
                self.full_recover_animation_delay = fullRecoverAnimationDelay
                self.aura_state = entity_state.AuraState.END_RECOVERING2
        elif (self.aura_state == entity_state.AuraState.END_RECOVERING2):
            if (self.full_recover_animation_delay > 0):
                self.full_recover_animation_delay -= 1
            else:
                self.full_recover_animation_delay = fullRecoverAnimationDelay
                self.aura_state = entity_state.AuraState.IDLE
        
    def move(self):

        dx = 0
        dy = 0

        if (self.attack_state == entity_state.AttackState.SHOOTING):
            if (self.shooting_animation_delay > 0):
                self.shooting_animation_delay -= 1
            else:
                self.shooting_animation_delay = variables.BULLET_COMBO_DELAY
                self.attack_state = entity_state.AttackState.IDLE

        # handle movement keys
        if (self.aura_state != entity_state.AuraState.RECOVERING and self.aura_state != entity_state.AuraState.SUB_RECOVERING):
            key = pygame.key.get_pressed()
            self.stop_recover_sound()
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
                    dy -= self.jump_speed
                if (self.state == entity_state.State.GROUND and self.canJump):
                    self.state = entity_state.State.JUMPING
                    self.canJump = False
                    self.gravity = 0 
                    dy -= self.jump_speed
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

        image_path = "./images/player/player.png"

        if (self.aura_state == entity_state.AuraState.START_RECOVERING):
            image_path = "./images/player/player_recovering_start.png"
        elif (self.aura_state == entity_state.AuraState.RECOVERING or self.aura_state == entity_state.AuraState.SUB_RECOVERING):
            image_path = "./images/player/player_recovering.png"
        elif (self.aura_state == entity_state.AuraState.END_RECOVERING1):
            image_path = "./images/player/player_recovering_full1.png"
        elif (self.aura_state == entity_state.AuraState.END_RECOVERING2):
            image_path = "./images/player/player_recovering_full2.png"
        elif (self.attack_state == entity_state.AttackState.IDLE and self.state == entity_state.State.GROUND):
            image_path = "./images/player/player.png"
        elif (self.attack_state == entity_state.AttackState.IDLE and (self.state == entity_state.State.JUMPING or self.state == entity_state.State.DOUBLE_JUMPING)):
            image_path = "./images/player/player_jumping.png"
        elif (self.combo_state == entity_state.AttackComboState.COMBO_1):
            image_path = "./images/player/player_shooting.png"
        elif (self.combo_state == entity_state.AttackComboState.COMBO_2):
            image_path = "./images/player/player_shooting2.png"
        elif (self.combo_state == entity_state.AttackComboState.COMBO_3):
            image_path = "./images/player/player_shooting3.png"
        elif (self.attack_state == entity_state.AttackState.SHOOTING):
            image_path = "./images/player/player_shooting.png"
        elif (self.attack_state == entity_state.AttackState.SHOOTING and (self.state == entity_state.State.JUMPING or self.state == entity_state.State.DOUBLE_JUMPING)):
            image_path = "./images/player/player_jumping_shooting.png"
        if (self.evolution_state == entity_state.EvolutionState.EVOLVED):
            image_path = image_path.replace(".png", "_evo.png")

        self.image = pygame.image.load(image_path)


        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    
    def update_bullets(self, enemy, enemy_bullets_group):
        self.bullets_move()
        self.check_bullet_out()
        self.check_bullet_collision(enemy_bullets_group)

    def update(self):
        self.updateAuraState()
        self.move()        
        self.update_sprite()
        self.shoot()

        if (self.aura_state == entity_state.AuraState.RECOVERING or self.aura_state == entity_state.AuraState.SUB_RECOVERING):
            if (self.evolution_state == entity_state.EvolutionState.BASE):
                self.aura.update(self.rect.x, self.rect.y, False)
            elif (self.evolution_state == entity_state.EvolutionState.EVOLVED):
                self.aura.update(self.rect.x, self.rect.y, True)
        
        
    def draw(self, screen):
        self.bullets_group.draw(screen)
        self.hearts_group.draw(screen)
        self.energy.draw(screen)
        self.sub_energy.draw(screen)
    
        screen.blit(self.image, self.rect)
        if (self.aura_state == entity_state.AuraState.RECOVERING or self.aura_state == entity_state.AuraState.SUB_RECOVERING):
            self.aura.draw(screen)