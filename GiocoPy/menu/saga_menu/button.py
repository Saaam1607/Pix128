import pygame
import assets.variables as variables
import utils.game_state as game_state
import sound_functions.selection_sounds as selection_sounds



class Button(pygame.sprite.Sprite):


    def __init__(self, function, image_path, active_image_path):
        super().__init__()

        self.function = function
        self.width = 730
        self.height = 150

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.active_image = pygame.image.load(active_image_path)
        self.active_image = pygame.transform.scale(self.active_image, (self.width, self.height))

        self.rect = pygame.Rect((variables.SCREEN_WIDTH - self.width) / 2, (variables.SCREEN_HEIGHT - self.height) / 2, self.width, self.height)

        self.isOver = False
        self.prev_mouse_state = True

        
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
        if self.isOver:
            screen.blit(self.active_image, self.rect)
        else:
            screen.blit(self.image, self.rect)