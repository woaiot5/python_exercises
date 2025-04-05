from os import system, name


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def check_if_int(string_value):
    try:
        result = (int(string_value) >= 0)
    except ValueError:
        result = False
    return result