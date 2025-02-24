import goblin_saga.xp as xp
import goblin_saga.battles_scripts as battles_scripts

unlocked_enemies = 20

battles = battles_scripts.battles

initial_speed = 6
initial_total_lifes = 3
initial_total_energies = 1
initial_energy_recovery_speed = 10

max_speed = 16
max_total_lifes = 10
max_total_energies = 6
min_energy_recovery_speed = 2

speed_upgrade = 2
total_lifes_upgrade = 1
total_energies_upgrade = 1
energy_recovery_speed_upgrade = 2

speed = initial_speed
total_lifes = initial_total_lifes
total_energies = initial_total_energies
energy_recovery_speed = initial_energy_recovery_speed

def check_if_can_increase_speed():
    global speed
    if speed < max_speed:
        return True
    else:
        return False
    
def increase_speed():
    global speed
    speed += speed_upgrade

def check_if_can_increase_total_lifes():
    global total_lifes
    if total_lifes < max_total_lifes:
        return True
    else:
        return False
    
def increase_total_lifes():
    global total_lifes
    total_lifes += total_lifes_upgrade

def check_if_can_increase_total_energies():
    global total_energies
    if total_energies < max_total_energies:
        return True
    else:
        return False
    
def increase_total_energies():
    global total_energies
    total_energies += total_energies_upgrade

def check_if_can_increase_energy_recovery_speed():
    global energy_recovery_speed
    if energy_recovery_speed > min_energy_recovery_speed:
        return True
    else:
        return False
    
def increase_energy_recovery_speed():
    global energy_recovery_speed
    energy_recovery_speed -= energy_recovery_speed_upgrade

def get_speed_label():
    total_steps = (max_speed - initial_speed) / speed_upgrade
    achieved_steps = (speed - initial_speed) / speed_upgrade
    return str(int(achieved_steps)) + " / " + str(int(total_steps))

def get_total_lifes_label():
    total_steps = (max_total_lifes - initial_total_lifes) / total_lifes_upgrade
    achieved_steps = (total_lifes - initial_total_lifes) / total_lifes_upgrade
    return str(int(achieved_steps)) + " / " + str(int(total_steps))

def get_total_energies_label():
    total_steps = (max_total_energies - initial_total_energies) / total_energies_upgrade
    achieved_steps = (total_energies - initial_total_energies) / total_energies_upgrade
    return str(int(achieved_steps)) + " / " + str(int(total_steps))

def get_total_energy_recovery():
    total_steps = (initial_energy_recovery_speed - min_energy_recovery_speed) / energy_recovery_speed_upgrade
    achieved_steps = (initial_energy_recovery_speed - energy_recovery_speed) / energy_recovery_speed_upgrade
    return str(int(achieved_steps)) + " / " + str(int(total_steps))


current_battle = 0
current_state_index = 0
current_dialogue_speech = 0



def load_player_values(loaded_speed, loaded_total_lifes, loaded_total_energies, loaded_energy_recovery_speed):
    global speed, total_lifes, total_energies, energy_recovery_speed
    speed = loaded_speed
    total_lifes = loaded_total_lifes
    total_energies = loaded_total_energies
    energy_recovery_speed = loaded_energy_recovery_speed


def get_player_values():
    global speed, total_lifes, total_energies, energy_recovery_speed
    return speed, total_lifes, total_energies, energy_recovery_speed


goblins_unlocked = 0


def update(goblin_level):
    global goblins_unlocked
    if (goblin_level == goblins_unlocked and goblins_unlocked < 5):
        goblins_unlocked += 1

def check_if_unlocked(goblin_level):
    global goblins_unlocked
    if goblin_level <= goblins_unlocked:
        return True
    else:
        return False

def load_goblins_unlocked(loaded_value):
    global goblins_unlocked
    goblins_unlocked = loaded_value

def get_goblins_unlocked():
    global goblins_unlocked
    return goblins_unlocked


def reset():
    global speed, total_lifes, total_energies, energy_recovery_speed
    speed = initial_speed
    total_lifes = initial_total_lifes
    total_energies = initial_total_energies
    energy_recovery_speed = initial_energy_recovery_speed
    global current_state_index, current_dialogue_speech
    current_state_index = 0
    current_dialogue_speech = 0
    global goblins_unlocked
    goblins_unlocked = 0
    xp.reset()
