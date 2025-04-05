from os import system, name

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

COINS = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

COFFEE_LIST = list(MENU.keys())

TECH_LIST = ['report', 'add', 'off']

resources = {"water": 300, "milk": 200, "coffee": 100}

money = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0, "total":0}


def clear_screen():
    system('cls' if name == 'nt' else 'clear')
    
    
def check_if_int(string_value):
    try:
        result = (int(string_value) >= 0)
    except ValueError:
        result = False
    return result


def report():
    print("\n".join([f"{k}: {v}ml" for k, v in resources.items()]))
    print("\n".join([f"{k}: ${v}" if k == "total" else f"{k}: {v}" for k, v in money.items()]))
    input("\n↵\n")


def order():
    option = ""
    clear_screen()
    while option not in COFFEE_LIST+TECH_LIST:
        clear_screen()
        option = input(f"What would you like to order? {"/".join(COFFEE_LIST)}\n[Technical options: {"/".join(TECH_LIST)}]\n").lower()
    return option


def check_resources(order):
    not_enough = [ingredient for ingredient, qty in MENU[order]["ingredients"].items() if qty > resources.get(ingredient, 0)]
    if not_enough:
        print(f"\nSorry, there is not enough {', '.join(not_enough)}.")
        input("\n↵\n")
        return False
    return True


def process_coins(my_order):
    inserted = 0.0
    inserted_coins = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0, "total": 0.0}

    drink_cost = MENU[my_order]["cost"]
    clear_screen()

    header = f"\n*** You ordered {my_order} ***\nPlease insert ${drink_cost}. Type 'cancel' to cancel transaction."
    print(header)

    while inserted < drink_cost:
        for coin_type, value in COINS.items():
            if inserted < drink_cost:
                cust_input = ""
                inserted_value = 0
                error_message = "Incorrect input. Please use positive numbers or type 'cancel' to cancel the transaction."
                while cust_input != 'cancel' and not(check_if_int(cust_input)):
                    try:
                        cust_input = input(f"\nNumber of {coin_type} ${value}: ").lower()
                        if cust_input == 'cancel':
                            print("Your money are returned. Transaction is cancelled.")
                            input("\n↵\n")
                            return -1
                        inserted_value = int(cust_input)*value
                        inserted_coins[coin_type] += int(cust_input)
                        if inserted_value < 0.0:
                            print(error_message)
                    except ValueError:
                        print(error_message)
                inserted_value = round(inserted_value,2)
                inserted += inserted_value
                inserted_coins["total"] += inserted_value
                if inserted < drink_cost:
                    clear_screen()
                    print(f"{header}\n___\nYou inserted ${inserted:.2f}.\nYou still need to insert ${drink_cost-inserted:.2f}\n___\n")
    my_change = round(inserted - drink_cost,2)
    print(f"\n*** You ordered {my_order} ***\nYou inserted ${inserted:.2f}.")

    for coin_type, value in inserted_coins.items():
        money[coin_type] += round(value,2)

    return my_change


def calculate_change(change_amt):
    return_coins = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0, "total": 0.0}
    money_return = money.copy()

    for coin_type, value in COINS.items():
        change_in_coin_type = int(change_amt/value)
        if change_amt > 0:
            if change_in_coin_type >= money_return[coin_type]:
                number = money_return[coin_type]
                amount = money_return[coin_type]*value
            else:
                number = change_in_coin_type
                amount = change_in_coin_type * value
            return_coins[coin_type] += number
            return_coins["total"] += amount
            money_return[coin_type] -= number
            money_return["total"] -= amount
            change_amt -= amount
        change_amt = round(change_amt,2)

    return_coins["total"] = round(return_coins["total"],2)
    return return_coins


def return_change(return_coins):
    for coin_type, value in return_coins.items():
        money[coin_type] -= value


def order_is_successful(my_order, my_change, change_to_return):
    if my_change == change_to_return:
        return_change(calculate_change(my_change))
        print(f"Your change: ${my_change}")
        return True
    else:
        inserted_total = my_change + MENU[my_order]["cost"]
        return_change(calculate_change(inserted_total))
        input(f"Not enough money for the change, please get back ${inserted_total}\nSee you next time!\n↵\n")
        return False


def make_a_drink(drink):
    if check_resources(drink):
        inserted_coins = process_coins(drink)
        if inserted_coins != -1:
            available_change = calculate_change(inserted_coins)["total"]
            if order_is_successful(drink, inserted_coins, available_change):
                for ingredient, value in MENU[drink]["ingredients"].items():
                    resources[ingredient] -= value
                input(f"...\nYour {drink} is ready. Have a nice day!\n↵\n")


def add_resources():
    clear_screen()
    resources_or_money = input("What do you want to add: resources/money\n").lower()
    list_keys = list(resources.keys()) if resources_or_money == "resources" else list(COINS.keys()) if resources_or_money == "money" else []

    if len(list_keys) == 0:
        input("Incorrect input. Operation is cancelled.\n↵\n")
        return ""

    for key in list_keys:
        add = ""
        message = "Incorrect input. Please use positive whole numbers."
        while not check_if_int(add):
            try:
               add = input(f"Add {key}: ")
               if not check_if_int(add):
                   print(message)
               else:
                   if resources_or_money == "resources":
                       resources[key] += int(add)
                   elif resources_or_money == "money":
                       money[key] += int(add)
                       money["total"] += round(int(add)*COINS[key],2)
            except ValueError:
                print(message)

    clear_screen()
    print("All done! Current resources: ")
    report()


def off_machine():
    global turn_on
    clear_screen()
    print("Goodbye!")
    turn_on = False

tech = {"add": add_resources, "off": off_machine, "report": report}

turn_on = True

while turn_on:
    selected_option = order()
    if selected_option in COFFEE_LIST:
        make_a_drink(selected_option)
    elif selected_option in TECH_LIST:
        tech[selected_option]()
