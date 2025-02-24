import pygame
import utils.game_state as game_state
import assets.variables as variables
from menu.saga_menu.button import Button


class Menu():


    def __init__(self):

        self.rect = pygame.Rect(0, 0, variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT)
        self.image = pygame.image.load("./images/menu/main_menu/background.png")
        self.image = pygame.transform.scale(self.image, (variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT))

        self.buttons_group = pygame.sprite.Group()
        # self.buttons_group.add(Button(
        #     game_state.open_goblin_saga,
        #     "./images/menu/saga_selection_menu/goblin_saga.png",
        #     "./images/menu/saga_selection_menu/goblin_saga_active.png"
        # ))
        self.buttons_group.add(Button(
            game_state.open_castle_saga,
            "./images/menu/saga_selection_menu/goblin_saga.png",
            "./images/menu/saga_selection_menu/goblin_saga_active.png"
        ))


    def update(self):
        for button in self.buttons_group:
            button.update()

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for button in self.buttons_group:
            button.draw(screen)
