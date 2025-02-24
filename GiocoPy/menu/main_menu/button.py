import pygame
import assets.variables as variables
import utils.game_state as game_state
import sound_functions.selection_sounds as selection_sounds




class Button(pygame.sprite.Sprite):
    

    def __init__(self, function, text, y, center_x, color, hover_color, font):
        super().__init__()
        self.function = function
        self.text = text
        self.y = y
        self.center_x = center_x
        self.color = color
        self.hover_color = hover_color
        self.font = font
        self.isOver = False
        self.prev_mouse_state = True
        self.d_space = 30

        # text data
        self.text_surface = self.font.render(self.text, True, pygame.Color('white'))

        # adapt rectangle to text
        text_width = self.font.size(self.text)[0]
        text_height = self.font.size(self.text)[1]
        rect_width = self.d_space + text_width + self.d_space
        self.rect = pygame.Rect((variables.SCREEN_WIDTH - rect_width) / 2, self.y, rect_width, 60)

        # center text on the center of the rect
        dy = (self.rect.height - (self.font.get_ascent() + 2 * self.font.get_descent())) / 2        
        # center text on the top left corner of rect
        text_y = self.y - (self.font.get_ascent() + 2 * self.font.get_descent())

        self.text_rect = pygame.Rect((variables.SCREEN_WIDTH - rect_width) / 2 + self.d_space, text_y + dy, text_width, text_height)


    def detect_mouseover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if not self.isOver:
                self.isOver = True
                selection_sounds.play_selection_sound()
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
                selection_sounds.play_selection_confirmed_sound()
                self.execute_function()
        elif not mouse_state[0]:
            self.prev_mouse_state = False
    

    def update(self):   
        self.detect_mouseover()
        self.detect_click()


    def draw(self, screen):

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        screen.blit(self.text_surface, self.text_rect)