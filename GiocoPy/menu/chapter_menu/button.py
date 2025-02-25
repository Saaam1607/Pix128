import pygame
import assets.variables as variables
import assets.colors as colors
import utils.game_state as game_state
import castle_saga.saga_progress as saga_progress



class Button(pygame.sprite.Sprite):


    def __init__(self, x, y, image_path, function, index):
        super().__init__()

        self.width = 450
        self.height = 90
        self.isOver = False
        self.prev_mouse_state = False
        self.function = function
        self.index = index

        # bg image
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.locked_image = pygame.image.load("./images/menu/chapter_selection_menu/locked_battle.png")
        self.locked_image = pygame.transform.scale(self.locked_image, (self.width, self.height))

        self.opacity_layer = pygame.Surface((self.width, self.height))
        self.opacity_layer.set_alpha(50)
        

    def detect_mouseover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if not self.isOver:
                self.isOver = True
        else:
            self.isOver = False
    
    
    def execute_function(self):
        if saga_progress.check_if_unlocked(self.index):
            self.function(self, self.index)


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
        if saga_progress.check_if_unlocked(self.index) == True:
            screen.blit(self.image, self.rect)
            if self.isOver:
                self.opacity_layer.fill((255, 255, 255))
                screen.blit(self.opacity_layer, self.rect)
        else:
            screen.blit(self.locked_image, self.rect)