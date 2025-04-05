from tech import check_if_int
from money import process_payment
from available import menu, resources


def report():
    print("\n".join([f"{k}: {v}ml" for k, v in resources.items()]))


def check_resources(order):
    not_enough = [ingredient
                  for ingredient, qty in menu[order]["ingredients"].items()
                  if qty > resources.get(ingredient, 0)]
    if not_enough:
        print(f"\nSorry, there is not enough {', '.join(not_enough)}.")
        input("\n↵\n")
        return False
    return True


def make_a_drink(drink):
    if check_resources(drink) and process_payment(drink):
        for ingredient, value in menu[drink]["ingredients"].items():
            resources[ingredient] -= value
        input(f"...\nYour {drink} is ready. Have a nice day!\n↵\n")


def add_resources():
    list_keys = list(resources.keys())

    for key in list_keys:
        add = ""
        message = "Incorrect input. Please use positive whole numbers."
        while not check_if_int(add):
            try:
                add = input(f"Add {key}: ")
                if not check_if_int(add):
                    print(message)
                else:
                    resources[key] += int(add)
            except ValueError:
                print(message)