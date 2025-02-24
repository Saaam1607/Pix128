import pygame
import assets.variables as variables
import assets.fonts as fonts
import assets.colors as colors
import castle_saga.saga_state as saga_state


from menu.main_menu.button import Button

class Menu():


    def __init__(self):
        self.background_rect = pygame.Rect(0, 0, variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT)
        self.background_image = pygame.image.load("./images/menu/game_load_menu/goblin_saga_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT))

        self.buttons_group = pygame.sprite.Group()
        self.buttons_group.add(Button(
            saga_state.open_new_chapter_menu,
            "NEW GAME",
            (variables.SCREEN_HEIGHT) / 2 - 50,
            (variables.SCREEN_WIDTH) / 2,
            colors.main_color,
            colors.main_color_ligther,
            fonts.custom_font
        ))
        self.buttons_group.add(Button(
            saga_state.open_chapter_menu,
            "LOAD GAME",
            (variables.SCREEN_HEIGHT) / 2 + 50,
            (variables.SCREEN_WIDTH) / 2,
            colors.main_color,
            colors.main_color_ligther,
            fonts.custom_font
        ))


    def update(self):
        for button in self.buttons_group:
            button.update()

    
    def draw(self, screen):
        screen.blit(self.background_image, self.background_rect)
        for button in self.buttons_group:
            button.draw(screen)