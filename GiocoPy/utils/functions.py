import random
import assets.variables as variables


def random_float(min_value, max_value):
    return random.uniform(min_value, max_value)


def random_int(min_value, max_value):
    return random.randint(min_value, max_value)


def compute_time(x_i, x_f, speed):
    time = (abs(x_f) - abs(x_i)) / speed
    return abs(time)


def calculate_initial_vertical_speed(y_i, y_f, g, duration, max_speed):
    speed = (y_f - y_i + (0.5 * g * duration ** 2)) / duration
    if speed < max_speed:
        speed = max_speed
    return speed


def calculate_vertical_position(y_i, v_i, g, t):
    return y_i + (v_i * t) - (0.5 * g * (t ** 2))