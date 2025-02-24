import pygame
import assets.variables as variables
import assets.colors as colors
import utils.game_state as game_state



class Button(pygame.sprite.Sprite):


    def __init__(self, function, text, font):
        super().__init__()


    def detect_mouseover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if not self.isOver:
                self.isOver = True
        else:
            self.isOver = False
    
    
    def execute_function(self):
        self.function(self)


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