import pygame
import assets.variables as variables


class SpeechChief(pygame.sprite.Sprite):


    def __init__(self, number_of_frames):
        super().__init__()
        self.number_of_frames = number_of_frames
        self.frame_index = 1
        self.chief_image_rect = pygame.Rect(
            300 - 240,
            variables.SCREEN_HEIGHT - 100 - 240,
            240,
            240
        )

    
    def update_frame_index(self):
        self.frame_index += 1
        if (self.frame_index > self.number_of_frames):
            self.frame_index = 1


    def update_sprite(self):
        self.image = pygame.image.load("./images/goblin_saga/chief/" + str(self.frame_index) + ".png")


    def update(self):
        self.update_frame_index()
        self.update_sprite()