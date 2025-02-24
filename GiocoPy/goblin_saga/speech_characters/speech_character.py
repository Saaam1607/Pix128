import pygame
import assets.variables as variables


animation_delay = 5


class SpeechCharacter(pygame.sprite.Sprite):


    def __init__(self, position, number_of_frames):
        super().__init__()
        self.number_of_frames = number_of_frames
        self.frame_index = 1
        self.animation_delay = animation_delay
        self.rect = pygame.Rect(
            0,
            variables.SCREEN_HEIGHT - 100 - 240,
            240,
            240
        )
        if position == "left":
            self.rect.x = 300 - 240
        elif position == "right":
            self.rect.x = variables.SCREEN_WIDTH - 300


    def update_image_path(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (240, 240))


    def update_sprite(self):
        if self.number_of_frames > 1:

            if self.animation_delay == 0:
                self.frame_index += 1
                if (self.frame_index > self.number_of_frames):
                    self.frame_index = 1
                self.animation_delay = animation_delay
            else:
                self.animation_delay -= 1


    def update_image(self, dir_path):
        self.update_image_path(dir_path + "/" + str(self.frame_index) + ".png")


    def update(self):
        if self.number_of_frames > 1:
            self.update_image()
            self.update_sprite()