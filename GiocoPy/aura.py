import pygame
import assets.variables as variables

# Carica tutte le immagini dell'aura in una lista
aura_images = [
    pygame.image.load("./images/player/aura/aura1.png"),
    pygame.image.load("./images/player/aura/aura2.png"),
    pygame.image.load("./images/player/aura/aura3.png"),
    pygame.image.load("./images/player/aura/aura4.png"),
    pygame.image.load("./images/player/aura/aura5.png"),
    pygame.image.load("./images/player/aura/aura6.png"),
    pygame.image.load("./images/player/aura/aura7.png"),
]

sub_aura_images = [
    pygame.image.load("./images/player/aura/super_aura1.png"),
    pygame.image.load("./images/player/aura/super_aura2.png"),
    pygame.image.load("./images/player/aura/super_aura3.png"),
    pygame.image.load("./images/player/aura/super_aura4.png"),
    pygame.image.load("./images/player/aura/super_aura5.png"),
    pygame.image.load("./images/player/aura/super_aura6.png"),
    pygame.image.load("./images/player/aura/super_aura7.png"),
]

class Aura(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 140, 180)
        self.index = 0  # Indice dell'immagine corrente
        self.image = pygame.transform.scale(aura_images[self.index], (140, 180))
        self.frame_delay = 5  # Numero di frame prima di cambiare immagine
        self.frame_counter = 0  # Contatore per gestire il delay
        self.first_cycle_complete = False

    def resetAnimation(self):
        self.index = 0
        self.image = pygame.transform.scale(aura_images[self.index], (140, 180))
        self.frame_counter = 0
        self.first_cycle_complete = False

    def update(self, x, y, isEvolved = False):
        self.rect.x = x - 10
        self.rect.y = y - 60
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.frame_counter = 0  # Reset del contatore

            if self.index == len(aura_images) - 1:  # Se siamo all'ultimo frame (7)
                self.first_cycle_complete = True  # Segniamo che il primo ciclo è finito
            
            if self.first_cycle_complete and self.index == len(aura_images) - 1:
                self.index = 4  # Torna all'indice 4 (0-based index)
            else:
                self.index = (self.index + 1) % len(aura_images)

            if isEvolved:
                self.image = pygame.transform.scale(sub_aura_images[self.index], (140, 180))
            else:
                self.image = pygame.transform.scale(aura_images[self.index], (140, 180))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
