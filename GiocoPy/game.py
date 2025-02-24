import pygame
import json
import os


import assets.fonts

from player import Player
from enemies.enemy import Enemy
from menu.main_menu.menu import Menu
from menu.difficulty_menu.difficulty_menu import DifficultyMenu
from menu.saga_menu.menu import Menu as SagaMenu
from menu.game_load_menu.menu import Menu as GameLoadMenu
import assets.variables as variables
import utils.game_state as game_state
import sound_functions.win_sound as win_sound
import opponents
from aim import Aim
from battle import Battle
from goblin_saga.goblin_saga import GoblinSaga
from castle_saga.castle_saga import CastleSaga
import goblin_saga.saga_progress as saga_progress
import goblin_saga.xp as xp



# pygame initialization
pygame.init()
# screen = pygame.display.set_mode((variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT), pygame.FULLSCREEN)
screen = pygame.display.set_mode((variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# framerate
clock = pygame.time.Clock()
FPS = 60

pygame.mouse.set_visible(False)

running = True
game_over = False


# menu
saga_menu = SagaMenu()
difficulty_menu = DifficultyMenu("./fonts/Pixeled.tff")
menu = Menu()


aim_group = pygame.sprite.GroupSingle()
aim_group.add(Aim(pygame.mouse.get_pos()))

goblinSaga = GoblinSaga(screen)
castleSaga = CastleSaga(screen)

filename = 'game_progress.json'


def load_game_progress():

    if not os.path.exists(filename):
        return
        
    with open(filename, 'r') as file:

        data = json.load(file)
        goblins_unlocked = data['goblins_unlocked']
        speed = data['speed']
        total_lifes = data['total_lifes']
        total_energies = data['total_energies']
        energy_recovery_speed = data['energy_recovery_speed']
        player_xp = data['player_xp']
        player_level = data['player_level']

        saga_progress.load_goblins_unlocked(goblins_unlocked)
        saga_progress.load_player_values(speed, total_lifes, total_energies, energy_recovery_speed)
        xp.load_player_xp(player_xp)
        xp.load_player_level(player_level)


def save_game_progress():
    with open(filename, 'w') as file:

        goblins_unlocked = saga_progress.get_goblins_unlocked()
        speed, total_lifes, total_energies, energy_recovery_speed = saga_progress.get_player_values()
        player_xp = xp.get_player_xp()
        player_level = xp.get_player_level()

        data = {
            'goblins_unlocked': goblins_unlocked,
            'speed': speed,
            'total_lifes': total_lifes,
            'total_energies': total_energies,
            'energy_recovery_speed': energy_recovery_speed,
            'player_xp': player_xp,
            'player_level': player_level
        }

        json.dump(data, file)


load_game_progress()
        

while running:

    clock.tick(FPS)

    if game_state.state == game_state.State.MAIN_MENU:
        menu.update()
        menu.draw(screen)

    if game_state.state == game_state.State.SAGA_SELECTION:
        saga_menu.update()
        saga_menu.draw(screen)

    if game_state.state == game_state.State.GOBLIN_SAGA:
        goblinSaga.play()

    if game_state.state == game_state.State.CASTLE_SAGA:
        castleSaga.play()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    aim_group.update(pygame.mouse.get_pos())
    aim_group.draw(screen)

    pygame.display.flip()



save_game_progress()