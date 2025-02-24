import pygame
import assets.variables as variables
from heart import Heart



class EnemyLife():
    

    def __init__(self, lifes):
        self.initial_lifes = lifes
        self.width = lifes * 20 + 20
        self.rect = pygame.Rect(variables.SCREEN_WIDTH - self.width - 10, 10, 220, 40)
        self.image = pygame.image.load("./images/life_container.png")
        self.image = pygame.transform.scale(self.image, (self.width, 40))
        self.hearts = []
        for i in range(lifes):
            heart = Heart(variables.SCREEN_WIDTH - self.width + i * 20, 20, 20, 20, "images/single_life.png")
            self.hearts.append(heart)
        

    def get_damage(self):
        if (len(self.hearts) > 0):
            self.hearts.pop()

        
    def is_lower_than_half(self):
        if (len(self.hearts) <= self.initial_lifes / 2):
            return True
        else:
            return False
        
    def full_recover(self):
        for i in range(self.initial_lifes):
            heart = Heart(variables.SCREEN_WIDTH - self.width + i * 20, 20, 20, 20, "images/single_life.png")
            self.hearts.append(heart)

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for heart in self.hearts:
            screen.blit(heart.image, heart.rect)
        