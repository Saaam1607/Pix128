import pygame
import goblin_saga.saga_progress as saga_progress
import goblin_saga.xp as xp



class ImprovementButton():

    def __init__(self, text, check_function, increse_function, get_label_function, x, y, color, hover_color, darker_color, font):
        self.check_function = check_function
        self.increse_function = increse_function
        self.get_label_function = get_label_function
        self.text = text
        self.x = x
        self.y = y
        self.width = 300
        self.color = color
        self.hover_color = hover_color
        self.darker_color = darker_color
        self.font = font
        self.d_space = 10
        self.isOver = False

        # text data
        self.text_surface = self.font.render(self.text, True, pygame.Color('white'))

        # adapt rectangle to text
        text_width, text_height = self.font.size(self.text)
        rect_width = self.width
        self.rect = pygame.Rect(self.x, self.y, rect_width, 50)

        font_height = self.font.get_ascent() + 2 * self.font.get_descent()
        
        # center text on the top left corner of rect
        text_y = self.y - font_height

        dy = (self.rect.height - font_height) / 2     
        self.text_rect = pygame.Rect(self.x + self.d_space, text_y + dy, text_width, text_height)


    def detect_mouseover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if not self.isOver:
                self.isOver = True
        else:
            self.isOver = False
    

    def detect_click(self):
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos) and self.check_function() and xp.available_points > 0:
                # function
                self.increse_function()
                xp.available_points -= 1


    def update(self):   
        self.detect_mouseover()
        self.detect_click()


    def draw(self, screen):
        if self.check_function() and xp.available_points > 0:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, self.hover_color, self.rect)
            else:
                pygame.draw.rect(screen, self.color, self.rect)
        else:
            pygame.draw.rect(screen, self.darker_color, self.rect)


        screen.blit(self.text_surface, self.text_rect)
        screen.blit(self.font.render(self.get_label_function(), True, pygame.Color('white')), (self.x + 310, self.y))