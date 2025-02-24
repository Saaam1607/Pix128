import pygame
import utils.functions
import assets.variables as variables



class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, center_x, center_y, width, height, direction, bullet_speed, bullet_max_speed, bullet_delay, image_path, aim_x, aim_y, gravity, priority):
        super().__init__()
        
        self.center_x = center_x
        self.center_y = center_y

        self.x = center_x - width/2
        self.y = center_y - height/2

        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.direction = direction
        self.bullet_speed = bullet_speed
        self.bullet_max_speed = bullet_max_speed
        self.bullet_delay = bullet_delay
        self.current_time = 0
        self.aim_x = aim_x
        self.aim_y = aim_y
        self.gravity = gravity
        self.priority = priority

        self.initial_vertical_speed = utils.functions.calculate_initial_vertical_speed(
            self.center_y, # y_i
            self.aim_y, # y_f
            self.gravity, # g
            utils.functions.compute_time(self.center_x, self.aim_x, self.bullet_speed), # duration
            - self.bullet_max_speed
        )
        
        
    def update(self):
        new_center_y = utils.functions.calculate_vertical_position(self.center_y, self.initial_vertical_speed, self.gravity, self.current_time)
        self.rect.y = new_center_y - self.rect.height/2
        self.current_time += 1
        if (self.direction == "rigth"):
            self.rect.x += self.bullet_speed
        if (self.direction == "left"):
            self.rect.x -= self.bullet_speed