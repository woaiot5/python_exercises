from os import path
import json

with open(f'{path.dirname( __file__ )}/countries.json') as country_json:
    COUNTRIES_INFO = json.load(country_json)

def letters_to_chose():
    keyboard = "qwertyuiopasdfghjklzxcvbnm".upper()
    all_letters = []
    for letter in keyboard:
        all_letters.append(letter)
    all_letters.sort()
    return all_letters

LETTERS = letters_to_chose()
STARS = "***********************"
STAGES = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
      |
      |
      |
      |
      |
=========
''']
NR_STAGES = len(STAGES) - 1