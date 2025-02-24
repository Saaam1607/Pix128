import pygame
from menu.difficulty_menu.diffculty_button import DifficultyButton



class DifficultyButtonLocked(DifficultyButton):


    def __init__(self, x, y, color, enemy_number):
        super().__init__(x, y, color, enemy_number)

        self.image = pygame.image.load("./images/menu/difficulty_menu/lock.png")
        self.image = pygame.transform.scale(self.image, (60, 75))

        self.lock_rect = pygame.Rect(x + (14 - 6) * 10 / 2, y + (14 - 7.5) * 10 / 2, 120, 150)


    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.image, self.lock_rect)