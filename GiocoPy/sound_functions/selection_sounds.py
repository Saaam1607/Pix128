import pygame

pygame.mixer.init()
selection_sound = pygame.mixer.Sound("./sounds/select1.mp3")
selection_sound.set_volume(0.5)
selection_confirmed_sound = pygame.mixer.Sound("./sounds/select2.mp3")
selection_confirmed_sound.set_volume(0.5)

def play_selection_sound():
    selection_sound.play()
        
def play_selection_confirmed_sound():
    selection_confirmed_sound.play()