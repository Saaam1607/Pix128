import pygame
import utils.game_state as game_state
import assets.fonts as fonts
import assets.variables as variables
from menu.saga_menu.button import Button
import castle_saga.saga_state as saga_state
import castle_saga.xp as xp


class Menu():


    def __init__(self):

        self.width = 370
        self.height = 450
        x = (variables.SCREEN_WIDTH - self.width) / 2
        y = (variables.SCREEN_HEIGHT - self.height) / 2

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image = pygame.image.load("./images/menu/win_menu/win_image.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.skip_dimension = 50
        x += 160
        y += 360

        self.skip_rect = pygame.Rect(x, y, self.skip_dimension, self.skip_dimension)
        self.skip_image = pygame.image.load("./images/menu/win_menu/skip_button.png")
        self.skip_image = pygame.transform.scale(self.skip_image, (self.skip_dimension, self.skip_dimension))

        self.opacity_layer = pygame.Surface((self.skip_dimension, self.skip_dimension))
        self.opacity_layer.set_alpha(50)

        self.isOver = False
        self.prev_mouse_state = False

        self.ticks_number = 0


    def gain_xp(self, gained_xp):
        xp.increase_xp(gained_xp)
        max_xp = xp.get_level_max_xp()
        tick_xp = max_xp / 24
        self.ticks_number = int(xp.player_xp / tick_xp)
        self.xp_text_surface = fonts.custom_font.render(("+ " + str(gained_xp) + " xp"), True, pygame.Color('black'))
        self.points_text_surface = fonts.custom_font.render(("Available Pts: " + str(xp.available_points)), True, pygame.Color('black'))


    def detect_mouseover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if not self.isOver:
                self.isOver = True
        else:
            self.isOver = False

    
    def execute_function(self):
        # self.function(self)
        saga_state.open_chapter_menu(self)



    def detect_click(self):
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0] and not self.prev_mouse_state:
            mouse_pos = pygame.mouse.get_pos()
            self.prev_mouse_state = True
            if self.rect.collidepoint(mouse_pos):
                self.execute_function()
        elif not mouse_state[0]:
            self.prev_mouse_state = False


    def update(self):   
        self.detect_mouseover()
        self.detect_click()

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.skip_image, self.skip_rect)
        if self.isOver:
            self.opacity_layer.fill((255, 255, 255))
            screen.blit(self.opacity_layer, self.rect)
        x = (variables.SCREEN_WIDTH - self.width) / 2 + 60
        y = (variables.SCREEN_HEIGHT - self.height) / 2 + 240
        if self.ticks_number > 0:
            rect_width = 0
            for i in range(self.ticks_number):
                rect_width += 10
            pygame.draw.rect(screen, (255, 255, 255), (x, y, rect_width, 10))
            screen.blit(self.xp_text_surface, (x, y - 65))
        screen.blit(self.points_text_surface, (x - 10, y + 40))