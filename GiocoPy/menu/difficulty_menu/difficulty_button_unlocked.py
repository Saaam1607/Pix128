import pygame
import utils.game_state as game_state
from menu.difficulty_menu.diffculty_button import DifficultyButton
import sound_functions.selection_sounds as selection_sounds




class DifficultyButtonUnlocked(DifficultyButton):

    def __init__(self, x, y, color, hover_color, enemy_number):
        
        super().__init__(x, y, color, enemy_number)

        self.hover_color = hover_color
        self.main_color = color
        self.hover_color = hover_color
        self.isOver = False
        self.enemy_number = enemy_number
        self.prev_mouse_state = True


    def detect_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False
        

    def check_click(self):
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0]:
            return True
        else:
            return False
    

    def update(self):
        if self.detect_mouse_over():

            if not self.isOver:
                self.isOver = True
                selection_sounds.play_selection_sound()                
            
            # update color
            self.color = self.hover_color

            if self.check_click():
                if not self.prev_mouse_state:
                    self.prev_mouse_state = True

                    # play sound
                    selection_sounds.play_selection_confirmed_sound()

                    # execute functions
                    game_state.open_main_menu(self)
                    game_state.change_difficulty(self.enemy_number)

                    # reset color
                    self.color = self.main_color
            else:
                self.prev_mouse_state = False

        else:
            self.isOver = False
            self.color = self.main_color