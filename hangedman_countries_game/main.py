import random
from stages import stages
import json

STARS = "***********************"

def letters_to_chose():
    keyboard = "qwertyuiopasdfghjklzxcvbnm".upper()
    all_letters = []
    for letter in keyboard:
        all_letters.append(letter)
    all_letters.sort()
    return all_letters


def letters_in_word(input_word):
    word_dict = {}
    for letter in input_word:
        guess = "_"
        if letter == " ": guess = letter
        word_dict[len(word_dict)] = {"letter": letter, "guess": guess}
    return word_dict


def def_display_line (input_word):
    line = ""
    for item in input_word:
        line += input_word[item]["guess"]
    return line


def update_guess (input_word, guessed_letter):
    for item in input_word:
        if input_word[item]["letter"] == guessed_letter:
            input_word[item]["guess"] = guessed_letter
    return input_word


def give_a_hint(hints_list, country):
    hints_dict = {
        0: f"{STARS} HINT: this country is located in {country["region"]} {STARS}",
        1: f"{STARS} HINT: official currency of this country is {country["currency"]["code"]} : {country["currency"]["name"]} {STARS}",
        2: f"{STARS} HINT: capital of this country is {country["capital"]} {STARS}",
        3: f"{STARS} HINT: official language of this country is {country["language"]["name"]} {STARS}"
    }
    hint_nr = random.choice(hints_list)
    hints_list.remove(hint_nr)
    print(hints_dict[hint_nr])


letters = letters_to_chose()

with open('countries.json') as country_json:
  country_dict = json.load(country_json)


game_on = True

while game_on:
    lives = 7
    hints = [0, 1, 2, 3]

    selected_country = random.choice(country_dict)
    country_name = selected_country["name"].upper()
    country_letters = letters_in_word(country_name)

    display = def_display_line(country_letters)
    print(f'{STARS} Lets play Hanged Man! {STARS}\n{STARS} Guess a country {STARS}\n{len(country_name)} symbols:\n{display}')

    game_over = False
    correct_letters = []
    all_guesses = []

    while not game_over:
        print(f"{STARS} {lives}/{len(stages)-1} LIVES LEFT {STARS} ")
        guess = input("Guess a letter or country name: ").upper()

        while guess in all_guesses:
            guess = input("This letter has been already guessed, enter another letter: ").upper()
        all_guesses.append(guess)

        country_letters = update_guess(country_letters, guess)
        display = def_display_line(country_letters)

        if guess == country_name:
            display = country_name
        print(display)

        if guess not in display:
            lives -= 1
            if len(guess) == 1:
                print(f"Letter *{guess.upper()}* is not in the word, you lose a life.")
            else:
                print(f"{guess} is incorrect guess, you lose a life.")

            if lives < 4:
                give_a_hint(hints, selected_country)

            if lives == 0:
                game_over = True
                print(f"{STARS} IT WAS <{country_name.upper()}>! YOU LOSE {STARS} ")
        print(stages[lives])

        if "_" not in display:
            game_over = True
            print(f"{STARS}  YOU WIN {STARS}")

    print(f"\n{country_name} is located in {selected_country["region"]}, it's capital is {selected_country["capital"]}, "
                      f"official language is {selected_country["language"]["name"]} and currency is {selected_country["currency"]["name"]}!\n")

    try_again = input("Press 'Y' to play again, press any other key to exit: ").lower()
    if try_again != "y":
        game_on = False

print(f"{STARS} Bye-bye! {STARS}")