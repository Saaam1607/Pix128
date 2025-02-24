import pygame
import assets.variables as variables
import assets.fonts as fonts
import assets.colors as colors
import utils.game_state as game_state

from menu.main_menu.button import Button

class Menu():


    def __init__(self):
        self.rect = pygame.Rect(
            0,
            0,
            variables.SCREEN_WIDTH,
            variables.SCREEN_HEIGHT
        )
        self.image = pygame.image.load("./images/menu/main_menu/background.png")
        self.image = pygame.transform.scale(self.image, (variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT))

        self.buttons = []
        self.buttons.append(Button(
            game_state.open_saga_selection_menu,
            "PLAY",
            (variables.SCREEN_HEIGHT) / 2 - 100,
            (variables.SCREEN_WIDTH) / 2,
            colors.main_color,
            colors.main_color_ligther,
            fonts.custom_font
        ))
        self.buttons.append(Button(
            game_state.open_main_menu,
            "ABOUT",
            (variables.SCREEN_HEIGHT) / 2 - 100 + 80,
            (variables.SCREEN_WIDTH) / 2,
            colors.main_color,
            colors.main_color_ligther,
            fonts.custom_font
        ))


    def update(self):
        for button in self.buttons:
            button.update()

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for button in self.buttons:
            button.draw(screen)