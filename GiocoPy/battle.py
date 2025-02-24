import pygame
import assets.variables as variables
from enemies.enemy import Enemy
from background import Background
import opponents as opponents


class Battle():


    def __init__(self):
        pass


    def create(self, game_over, player, enemy, background_image_path, music_path):
        self.game_over = game_over
        self.player = player
        self.enemy = enemy
        self.background_group = pygame.sprite.GroupSingle()
        self.background_group.add(Background(background_image_path))
        self.music = pygame.mixer.Sound(music_path)
        self.music.play()


    def update(self):
        self.player.update()
        self.player.update_bullets(self.enemy, self.enemy.bullets_group)
        self.enemy.update_bullets(self.player.bullets_group)
        self.enemy.take_aim(*self.player.get_center())
        self.enemy.update()
        

    def draw(self, screen):
        self.background_group.draw(screen)
        self.player.draw(screen)
        self.enemy.draw(screen)


    def check_win(self):
        if (self.enemy.life.hearts == []):
            self.music.stop()
            return True
        else:
            return False
        

    def check_loose(self):
        if (len(self.player.hearts_group) == 0): 
            self.music.stop()
            return True
        else:
            return False