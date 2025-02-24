import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound("./sounds/music.mp3")
sound.set_volume(0.15)

def play():
    sound.play()

def stop():
    sound.stop()