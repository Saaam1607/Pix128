import pygame

pygame.mixer.init()
win_sound = pygame.mixer.Sound("./sounds/win.mp3")
win_sound.set_volume(0.8)

def play():
    win_sound.play()