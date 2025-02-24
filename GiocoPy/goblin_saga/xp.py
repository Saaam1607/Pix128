
player_xp = 0
player_level = 0
available_points = 0
max_available_points = 20

def increase_level():
    global player_level
    global available_points
    player_level += 1
    available_points += 1

def increase_xp(gained_xp):
    if (player_level <= max_available_points):
        global player_xp
        player_xp += gained_xp
        max_xp = get_level_max_xp()
        if player_xp >= max_xp:
            player_xp -= max_xp
            increase_level()
            return True
    return False

def get_level_max_xp():
    global player_level
    progress_mapping = {
        0: 50,
        1: 50,
        2: 100,
        3: 100,
        4: 200,
        5: 200,
        6: 300,
        7: 300,
        8: 300,
        9: 350,
        10: 350,
        11: 350,
        12: 400,
        13: 400,
        14: 400,
        15: 500,
        16: 500,
        17: 600,
    }
    return progress_mapping.get(player_level, None)

def get_player_xp():
    global player_xp
    return player_xp

def get_player_level():
    global player_level
    return player_level

def load_player_xp(loaded_value):
    global player_xp
    player_xp = loaded_value

def load_player_level(loaded_value):
    global player_level
    player_level = loaded_value

def reset():
    global player_xp
    global player_level
    global available_points
    player_xp = 0
    player_level = 0
    available_points = 0