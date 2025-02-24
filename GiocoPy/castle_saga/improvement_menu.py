import pygame
import assets.colors as colors
import castle_saga.saga_progress as saga_progress
from menu.chapter_menu.improvement_button import ImprovementButton



class ImprovementMenu():

    def __init__(self):
        pass


    def __init__(self, x, y, font):
        self.buttons = []
        self.buttons.append(
            ImprovementButton(
                self.upgrade_life,
                "+ Life",
                x,
                y + 150,
                colors.main_color,
                colors.main_color_ligther,
                font
            )
        )
        self.buttons.append(
            ImprovementButton(
                self.upgrade_speed,
                "+ Speed",
                x,
                y + 150 + 50,
                colors.main_color,
                colors.main_color_ligther,
                font
            )
        )
        self.buttons.append(
            ImprovementButton(
                self.upgrade_energy,
                "+ Energy",
                x,
                y + 150 + 100,
                colors.main_color,
                colors.main_color_ligther,
                font
            )
        )
        self.buttons.append(
            ImprovementButton(
                self.upgrade_energy_recovery_speed,
                "+ Energy Recovery",
                x,
                y + 150 + 150,
                colors.main_color,
                colors.main_color_ligther,
                font
            )
        )


    def upgrade_life(self):
        saga_progress.total_lifes += 1

    def upgrade_speed(self):
        saga_progress.speed += 3

    def upgrade_energy(self):
        saga_progress.total_energies += 1

    def upgrade_energy_recovery_speed(self):
        saga_progress.energy_recovery_speed -= 2


    def update(self):   
        for button in self.buttons:
            button.update()


    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)