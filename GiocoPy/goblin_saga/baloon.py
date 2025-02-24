import pygame
import assets.variables as variables


class Baloon(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/goblin_saga/baloon.png")
        self.image = pygame.transform.scale(self.image, (600, 360))
        self.rect = pygame.Rect(
            (variables.SCREEN_WIDTH - 600) / 2,
            (variables.SCREEN_HEIGHT - 360) / 2,
            600,
            360
        )