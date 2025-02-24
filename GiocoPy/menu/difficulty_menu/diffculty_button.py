import pygame
import opponents



class DifficultyButton():
    
    def __init__(self, x, y, color, enemy_number):

        self.rect = pygame.Rect(x, y, 140, 140)

        # enemy image
        if enemy_number == 1:
            self.enemy_image_path = "./images/enemies/prisoner/prisoner.png"
        if enemy_number == 2:
            self.enemy_image_path = "./images/enemies/golem/golem.png"
        if enemy_number == 3:
            self.enemy_image_path = "./images/enemies/wizard/wizard.png"
        if enemy_number == 4:
            self.enemy_image_path = "./images/enemies/boss/boss.png"
        if enemy_number == 5:
            self.enemy_image_path = "./images/enemies/final_boss/final_boss.png"

        self.enemy_image = pygame.image.load(self.enemy_image_path)
        self.enemy_image = pygame.transform.scale(self.enemy_image, (120, 120))

        self.color = color
        
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        image_rect = self.enemy_image.get_rect()
        image_rect.center = self.rect.center
        screen.blit(self.enemy_image, image_rect)