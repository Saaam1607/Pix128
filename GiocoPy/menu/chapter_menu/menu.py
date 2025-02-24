import pygame
import assets.variables as variables
import assets.colors as colors
import assets.fonts as fonts
import castle_saga.xp as xp

import castle_saga.saga_state as saga_state
import castle_saga.saga_progress as saga_progress

from menu.chapter_menu.button import Button
from menu.chapter_menu.improvement_button import ImprovementButton



class Menu():


    def __init__(self):

        # bg image
        self.background_rect = pygame.Rect(0, 0, variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT)
        self.background_image = pygame.image.load("./images/menu/chapter_selection_menu/background.png")
        self.background_image = pygame.transform.scale(self.background_image, (variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT))

        # chapter buttons
        self.battle_buttons_group = pygame.sprite.Group()
        self.battle_buttons_group.add( Button(100, 95, "./images/menu/chapter_selection_menu/goblin_battle_1.png", saga_state.init_chapter, 0) )
        self.battle_buttons_group.add( Button(100, 95 + 110, "./images/menu/chapter_selection_menu/goblin_battle_2.png", saga_state.init_chapter, 1) )
        self.battle_buttons_group.add( Button(100, 95 + 220, "./images/menu/chapter_selection_menu/goblin_battle_3.png", saga_state.init_chapter, 2) )
        self.battle_buttons_group.add( Button(100, 95 + 330, "./images/menu/chapter_selection_menu/goblin_battle_4.png", saga_state.init_chapter, 3) )
        self.battle_buttons_group.add( Button(100, 95 + 440, "./images/menu/chapter_selection_menu/goblin_battle_5.png", saga_state.init_chapter, 4) )

        self.player_card_width = 560
        self.player_card_height = 540
        self.player_card_rect = pygame.Rect((variables.SCREEN_WIDTH / 2), (variables.SCREEN_HEIGHT - self.player_card_height) / 2, self.player_card_width, self.player_card_height)
        self.player_card_image = pygame.image.load("./images/menu/chapter_selection_menu/player_board.png")
        self.player_card_image = pygame.transform.scale(self.player_card_image, (self.player_card_width, self.player_card_height))

        self.improvement_buttons = []
        self.improvement_buttons.append( ImprovementButton("+ Life", saga_progress.check_if_can_increase_total_lifes, saga_progress.increase_total_lifes, saga_progress.get_total_lifes_label, self.player_card_rect.x + 30, self.player_card_rect.y + 220, colors.main_color, colors.main_color_ligther, colors.main_color_darker, fonts.custom_font) )        
        self.improvement_buttons.append( ImprovementButton("+ Speed", saga_progress.check_if_can_increase_speed, saga_progress.increase_speed, saga_progress.get_speed_label, self.player_card_rect.x + 30, self.player_card_rect.y + 220 + 70, colors.main_color, colors.main_color_ligther, colors.main_color_darker, fonts.custom_font) )
        self.improvement_buttons.append( ImprovementButton("+ Max Energies", saga_progress.check_if_can_increase_total_energies, saga_progress.increase_total_energies, saga_progress.get_total_energies_label, self.player_card_rect.x + 30, self.player_card_rect.y + 220 + 140, colors.main_color, colors.main_color_ligther, colors.main_color_darker, fonts.custom_font) )
        self.improvement_buttons.append( ImprovementButton("+ Energy Recov.", saga_progress.check_if_can_increase_energy_recovery_speed, saga_progress.increase_energy_recovery_speed, saga_progress.get_total_energy_recovery, self.player_card_rect.x + 30, self.player_card_rect.y + 220 + 210, colors.main_color, colors.main_color_ligther, colors.main_color_darker, fonts.custom_font) )


    def update(self):
        for button in self.battle_buttons_group:
            button.update()
        max_xp = xp.get_level_max_xp()
        tick_xp = max_xp / 24
        self.ticks_number = int(xp.player_xp / tick_xp)
        self.points_text_surface = fonts.custom_font.render(("Available Pts: " + str(xp.available_points)), True, pygame.Color('black'))
        
        for button in self.improvement_buttons:
            button.update()


    def draw(self, screen):
        screen.blit(self.background_image, self.background_rect)
        for button in self.battle_buttons_group:
            button.draw(screen)
        screen.blit(self.player_card_image, self.player_card_rect)
        screen.blit(self.points_text_surface, (self.player_card_rect.x + 190, self.player_card_rect.y + 30))

        if self.ticks_number > 0:
            rect_width = 0
            for i in range(self.ticks_number):
                rect_width += 10
            pygame.draw.rect(screen, (255, 255, 255), (self.player_card_rect.x + 200, self.player_card_rect.y + 110, rect_width, 10))

        for button in self.improvement_buttons:
            button.draw(screen)