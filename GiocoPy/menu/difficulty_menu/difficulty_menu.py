import pygame
import assets.variables as variables
import assets.colors as colors
import utils.game_state as game_state
import castle_saga.saga_progress as saga_progress
from menu.difficulty_menu.difficulty_button_unlocked import DifficultyButtonUnlocked
from menu.difficulty_menu.difficulty_button_locked import DifficultyButtonLocked



class DifficultyMenu():
    
    def __init__(self, font):
        self.font = font
        self.rect = pygame.Rect(
            0,
            0,
            variables.SCREEN_WIDTH,
            variables.SCREEN_HEIGHT,
        )
        self.image = pygame.image.load("./images/menu/difficulty_menu/background.png")
        self.image = pygame.transform.scale(self.image, (variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT))
        self.buttons = []
        self.update_buttons()
            
        self.label_font = font
        self.label_text = "Select Difficulty"
        self.label_color = colors.main_color
        self.label_position = (
            variables.SCREEN_WIDTH / 2,
            variables.SCREEN_HEIGHT / 2 - 150
        )
        self.can_select_countdown = 3 # to avoid click collisions

    def update_buttons(self):
        for i in range(5):
            if i < saga_progress.unlocked_enemies:
                self.buttons.append(DifficultyButtonUnlocked(
                    variables.SCREEN_WIDTH /2 - 500 + 150 * i,
                    variables.SCREEN_HEIGHT / 2 - 50,
                    colors.main_color,
                    colors.main_color_ligther,
                    i + 1,
                ))
            else:
                self.buttons.append(DifficultyButtonLocked(
                    variables.SCREEN_WIDTH /2 -500 + 150 * i,
                    variables.SCREEN_HEIGHT / 2 - 50,
                    colors.main_color_darker,
                    i + 1
                ))

    def refresh(self):
        self.can_select_countdown = 3
    

    def update(self):
        if (self.can_select_countdown == 0):
            for button in self.buttons:
                if isinstance(button, DifficultyButtonUnlocked):
                    button.update()
        else:
            self.can_select_countdown -= 1

    def update_unlocked_enemies(self, unlocked_enemies):
        self.unlocked_enemies = unlocked_enemies
        self.update_buttons()



    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # label_surface = self.label_font.render(self.label_text, True, self.label_color)
        # label_rect = label_surface.get_rect(center=self.label_position)
        # screen.blit(label_surface, label_rect)
        for button in self.buttons:
            button.draw(screen)