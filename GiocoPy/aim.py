import pygame



class Aim(pygame.sprite.Sprite):


    def __init__(self, mouse_pos):
        super().__init__()
        self.x = mouse_pos[0]
        self.y = mouse_pos[1]
        self.width = 70
        self.height = 70
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load("./images/aim.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image.set_alpha(100)


    def update(self, mouse_pos):
        self.rect.x = mouse_pos[0] - self.width / 2
        self.rect.y = mouse_pos[1] - self.height / 2