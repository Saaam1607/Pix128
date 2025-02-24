import pygame



class EnergyTick(pygame.sprite.Sprite):


    def __init__(self, x, y, width, height, image_path):
        super().__init__()
        self.rect = pygame.Rect(x, y,width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))