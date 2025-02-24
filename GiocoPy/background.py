import assets.variables as variables
import pygame


class Background(pygame.sprite.Sprite):
    
    
    def __init__(self, image_path):
        super().__init__()
        self.rect = pygame.Rect(0, 0, variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT))
