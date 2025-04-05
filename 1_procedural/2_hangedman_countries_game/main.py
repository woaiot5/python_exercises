from os import system, name
import random
from constants import STARS, LETTERS, STAGES, NR_STAGES, COUNTRIES_INFO


def letters_in_word(input_word):
    """Returns a dictionary where the key is a sequence number of a letter or a symbol in an input string,
    and value is a nested dictionary of 'symbol' and 'display'.
    Alphabet letters are displayed as '_', other symbols stay the same."""

    word_dict = {}
    for letter in input_word:
        answer = "_"
        if letter not in LETTERS:
            answer = letter
        word_dict[len(word_dict)] = {"symbol": letter, "display": answer}
    return word_dict


def def_display_line (input_word):
    line = ""
    for item in input_word:
        line += input_word[item]["display"]
    return line


def print_header(lives_left, country):
    system('cls' if name == 'nt' else 'clear')
    print(f'{STARS} Lets play Hanged Man! {STARS}')
    print(f"{STARS} {lives_left}/{NR_STAGES} LIVES LEFT {STARS} ")
    print(f"{STARS} Guess a country {STARS}")
    print(f"{len(country["name"].upper())} symbols:\n{country["display"]}")
    print(STAGES[lives])


def update_guess (input_word, guessed_letter):
    for item in input_word:
        if input_word[item]["symbol"] == guessed_letter:
            input_word[item]["display"] = guessed_letter
    return input_word


def give_a_hint(hints_list, country):
    hints_dict = {
        0: f"\n{STARS} HINT: this country is located in {country["region"]} {STARS}",
        1: f"\n{STARS} HINT: official currency of this country is {country["currency"]["code"]} {country["currency"]["symbol"]} {STARS}",
        2: f"\n{STARS} HINT: capital of this country is {country["capital"]} {STARS}",
        3: f"\n{STARS} HINT: official language of this country is {country["language"]["name"]} {STARS}"
    }
    hint_nr = random.choice(hints_list)
    hints_list.remove(hint_nr)
    print(hints_dict[hint_nr])
    return hints_dict[hint_nr]


def lose_or_win(lives_left, is_game_over):
    if lives_left == 0:
        is_game_over = True
        system('cls' if name == 'nt' else 'clear')
        print(f"{STARS} YOU LOSE {STARS}\n{STARS} IT WAS <{selected_country["name"].upper().upper()}>! {STARS} ")

    if "_" not in selected_country["display"]:
        is_game_over = True
        system('cls' if name == 'nt' else 'clear')
        print(f"{STARS} YOU WIN {STARS}")

    return is_game_over


def give_country_info(country):
    print(
        f"\n{country["name"]} is located in {country["region"]}, it's capital is {country["capital"]}, "
        f"official language is {country["language"]["name"]} and currency is {country["currency"]["name"]}!\n"
    )


def print_footer():
    system('cls' if name == 'nt' else 'clear')
    print(f"{STARS} Bye-bye! {STARS}")


game_on = True
wins = 0
loses = 0
streak = 0

while game_on:
    game_over = False
    lives = len(STAGES) - 1
    hints = [0, 1, 2, 3]
    all_guesses = []
    my_hints = []
    result = ""
    selected_country = random.choice(COUNTRIES_INFO)
    selected_country["letters"] = letters_in_word(selected_country["name"].upper())
    selected_country["display"] = def_display_line(selected_country["letters"])

    while not game_over:

        print_header(lives,selected_country)

        if len(all_guesses) > 0:
            print(f"Your guesses: {', '.join(str(x) for x in all_guesses)}")

        if len(my_hints) > 0:
            print(*my_hints, sep='\n')

        guess = input(f"\nGuess a letter or country name: ").upper()

        while guess in all_guesses:
            guess = input("This letter has been already guessed, enter another letter: ").upper()
        all_guesses.append(guess)

        selected_country["letters"] = update_guess(selected_country["letters"], guess)
        selected_country["display"] = def_display_line(selected_country["letters"])

        if guess == selected_country["name"].upper():
            selected_country["display"] = selected_country["name"].upper()

        if guess not in selected_country["display"]:
            lives -= 1
            if len(guess) == 1:
                print(f"Letter *{guess.upper()}* is not in the word, you lose a life.")
            else:
                print(f"{guess} is incorrect guess, you lose a life.")
            if 1 <= lives <= 4:
                my_hints.append(give_a_hint(hints, selected_country))

        game_over = lose_or_win(lives, game_over)

    if "_" in selected_country["display"]:
        loses += 1
        streak = 0
    else:
        wins += 1
        streak += 1

    give_country_info(selected_country)
    print(f"\nWins: {wins}\nLoses: {loses}\nStreak: {streak}")
    game_on = input("\nPress 'Y' to play again, press any other key to exit: ").lower() == "y"

print_footer()