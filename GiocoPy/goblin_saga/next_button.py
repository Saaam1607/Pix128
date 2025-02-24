import pygame



class NextButton(pygame.sprite.Sprite):


    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("./images/goblin_saga/next_button.png")
        self.image = pygame.transform.scale(self.image, (40, 50))
        self.rect = pygame.Rect(
            x,
            y,
            40,
            50
        )    
    

    def detect_click(self):
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                return True
        return False