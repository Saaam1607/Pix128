import pygame
import assets.variables as variables
from menu.difficulty_menu.diffculty_button import DifficultyButton

main_color_ligther = (177, 219, 217)
main_color = (120, 190, 186)


class DifficultyMenu():
    
    def __init__(self, open_main_menu, font):
        self.open_main_menu = open_main_menu
        self.width = 740
        self.height = 230
        self.rect = pygame.Rect(
            (variables.SCREEN_WIDTH - self.width) / 2,
            (variables.SCREEN_HEIGHT - self.height) / 2,
            self.width,
            self.height
        )
        self.image = pygame.image.load("./images/menu/difficulty_menu/background.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.buttons = []
        for i in range(5):
            self.buttons.append(DifficultyButton(
                self.open_main_menu,
                str(i + 1),
                (variables.SCREEN_WIDTH - self.width) / 2 + 40 + 90 * i,
                (variables.SCREEN_HEIGHT - self.height) / 2 + 110,
                70,
                main_color,
                main_color_ligther,
                font,
                self.change_difficulty
            ))
        self.label_font = font
        self.label_text = "Select Difficulty"
        self.label_color = main_color
        self.label_position = (
            variables.SCREEN_WIDTH // 2,
            (variables.SCREEN_HEIGHT - self.height) // 2 + 50
        )


    def update(self):
        for button in self.buttons:
            button.update()


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        label_surface = self.label_font.render(self.label_text, True, self.label_color)
        label_rect = label_surface.get_rect(center=self.label_position)
        screen.blit(label_surface, label_rect)
        for button in self.buttons:
            button.draw(screen)