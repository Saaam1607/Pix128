import pygame
import assets.variables as variables
import assets.fonts as fonts
import castle_saga.saga_progress as saga_progress
import opponents
from player import Player
from battle import Battle
from castle_saga.improvement_menu import ImprovementMenu
from menu.game_load_menu.menu import Menu as GameLoadMenu
from menu.chapter_menu.menu import Menu as ChapterMenu
from menu.win_menu.menu import Menu as WinMenu
import utils.game_state as game_state

from castle_saga.baloon import Baloon
from castle_saga.next_button import NextButton
from background import Background

from castle_saga.speech_characters.speech_character import SpeechCharacter

import castle_saga.saga_state as saga_state



pygame.init()

# chief sprite talking
chief_talking_group = pygame.sprite.GroupSingle()
chief_talking_group.add(SpeechCharacter("left", 10))

# enemy sprite talking
enemy_talking_group = pygame.sprite.GroupSingle()
enemy_talking_group.add(SpeechCharacter("right", 1))

game_load_menu = GameLoadMenu()
chapter_menu = ChapterMenu()
win_menu = WinMenu()
battle = Battle()


class CastleSaga():

    def __init__(self, screen):
        self.isPlaying = False
        self.typing_delay = 0 
        self.typing_index = 0
        self.canSkip = True
        self.background_group = pygame.sprite.GroupSingle()
        self.screen = screen
        self.game_over = False
        self.can_update = False 
        

    # render text
    def render_text(self, text, font, max_width):
        lines = text.split("\n")
        rendered_lines = []
        for line in lines:
            words = line.split()
            space_width, _ = font.size(" ")
            space_width *= 0.8
            current_line = ""
            for word in words:
                test_line = current_line + word + " "
                test_line_width, _ = font.size(test_line)
                if test_line_width > max_width:
                    rendered_lines.append(current_line)
                    current_line = word + " "
                else:
                    current_line = test_line
            rendered_lines.append(current_line)
        return rendered_lines 


    def update_state(self):
        state_label = saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["type"]
        saga_state.state = saga_state.get_saga_state(state_label)


    def update(self):

        if self.can_update == True:
            self.update_state()
            self.can_update = False 

        if saga_state.state == saga_state.State.GAME_LOAD_SELECTION:
            game_load_menu.update()

        if saga_state.state == saga_state.State.CHAPTER_MENU:
            chapter_menu.update()

        if saga_state.state == saga_state.State.CHAPTER_INIT:
            self.update_state()

        if saga_state.state == saga_state.State.DIALOGUE or saga_state.state == saga_state.State.ENEMY_DIALOGUE:

            if saga_state.state == saga_state.State.DIALOGUE:
                self.directory_path = saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["directory_path"]
                chief_talking_group.sprite.update_image(self.directory_path)
                chief_talking_group.sprite.update_sprite()
            elif saga_state.state == saga_state.State.ENEMY_DIALOGUE:
                self.character_path = saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["character_path"]
                enemy_talking_group.sprite.update_image_path(self.character_path)

            self.background_group.add(Background(saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["background_path"]))
            
            # baloon and text
            self.dialogue_group = pygame.sprite.Group()
            self.dialogue_group.add(Baloon())
            self.dialogue_group.add(NextButton((variables.SCREEN_WIDTH - 600) / 2 + 500, (variables.SCREEN_HEIGHT - 360) / 2 + 280))
            self.text = self.render_text(saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["speech"][saga_progress.current_dialogue_speech], fonts.dialogue_font, 500)
            
            if self.isPlaying == False:
                if "voice_path" in saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index] and saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["voice_path"]:
                    self.voice = pygame.mixer.Sound(
                        saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["voice_path"] + "/" + str(saga_progress.current_dialogue_speech + 1) + ".mp3"
                    )
                    self.voice.play()
                    self.isPlaying = True

            # skip click detection
            if self.dialogue_group.sprites()[1].detect_click():

                if (saga_progress.current_dialogue_speech) < len(saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["speech"]):
                    if self.canSkip:

                        saga_progress.current_dialogue_speech += 1
                        if (saga_progress.current_dialogue_speech) == len(saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["speech"]):
                            saga_progress.current_dialogue_speech = 0
                            saga_progress.current_state_index += 1
                            self.can_update = True
                        if self.isPlaying:
                            self.voice.stop()
                        self.isPlaying = False
                        self.canSkip = False

                        skip_sound = pygame.mixer.Sound("./sounds/next.mp3")
                        skip_sound.play()

            else:
                self.canSkip = True
        
        if saga_state.state == saga_state.State.PREPARING_BATTLE:
            battle.create(
                self.game_over,
                Player(saga_progress.total_lifes, saga_progress.speed, saga_progress.total_energies * 5, saga_progress.energy_recovery_speed, variables.BULLET_SPEED, variables.BULLET_DELAY, "./images/bullet.png"),
                opponents.create_enemy(saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["enemy_number"]),
                opponents.get_enemy_background(saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["enemy_number"]),
                "./sounds/music.mp3"
            )
            self.game_over = False
            self.enemy_xp = int(saga_progress.battles[saga_state.selected_chapter][saga_progress.current_state_index]["xp_reward"])
            saga_progress.current_state_index += 1
            self.can_update = True


        if saga_state.state == saga_state.State.BATTLE:

            if not self.game_over:

                battle.update()

                battle.draw(self.screen)

                if battle.check_win():
                    self.game_over = True
                    saga_progress.current_state_index = 0
                    saga_progress.current_dialogue_speech = 0
                    saga_progress.update(saga_state.selected_chapter)
                    win_menu.gain_xp(self.enemy_xp)
                    saga_state.open_win_menu(self)
                    # win_sound.play()

                if battle.check_loose():
                    self.game_over = True
                    saga_progress.current_state_index = 0
                    saga_progress.current_dialogue_speech = 0
                    saga_state.state = saga_state.State.CHAPTER_MENU
                    
            else:
                saga_progress.current_state_index += 1
        
        if saga_state.state == saga_state.State.WIN:
            win_menu.update()

    
    def draw(self):

        if saga_state.state == saga_state.State.GAME_LOAD_SELECTION:
            game_load_menu.draw(self.screen)

        if saga_state.state == saga_state.State.CHAPTER_MENU:
            chapter_menu.draw(self.screen)

        if saga_state.state == saga_state.State.DIALOGUE or saga_state.state == saga_state.State.ENEMY_DIALOGUE:

            self.background_group.draw(self.screen)

            if saga_state.state == saga_state.State.DIALOGUE:
                chief_talking_group.draw(self.screen)
            elif saga_state.state == saga_state.State.ENEMY_DIALOGUE:
                enemy_talking_group.draw(self.screen)
            
            self.dialogue_group.draw(self.screen)
                
            for i in range(len(self.text)):
                self.text_surface = fonts.dialogue_font.render(self.text[i], True, pygame.Color('black'))
                self.screen.blit(self.text_surface, ((variables.SCREEN_WIDTH - 600) / 2 + 50, (variables.SCREEN_HEIGHT - 360) / 2 + (30 * i) + 50))
            i += 1

        if saga_state.state == saga_state.State.WIN:
            battle.draw(self.screen)
            win_menu.draw(self.screen)

        
    def play(self):
        self.update()
        self.draw()