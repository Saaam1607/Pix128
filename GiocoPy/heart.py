import pygame
import assets.variables as variables



class Heart(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, heigth, image_path):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, heigth)
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, heigth))
