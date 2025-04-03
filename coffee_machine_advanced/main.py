from os import system, name

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COINS = {"quarters": 0.25
         ,"dimes": 0.10
         ,"nickles": 0.05
         ,"pennies": 0.01}

COFFEE_LIST = list(MENU.keys())

TECH_LIST = ['report', 'add', 'off']

resources = {
    "water": 300
    ,"milk": 200
    ,"coffee": 100
}

money = {"quarters": 0
         ,"dimes": 0
         ,"nickles": 0
         ,"pennies": 0
         ,"total":0
}


def clear_screen():
    system('cls' if name == 'nt' else 'clear')
    
    
def check_if_int(string_value):
    try:
        result = (int(string_value) >= 0)
    except ValueError:
        result = False
    return result


def round_two(value):
    return round(value,2)


def report():
    global resources, money
    print("\n")
    for key in resources:
        print(f"{key}: {resources[key]}ml")
    for key in money:
        sign = ""
        if key == "total": sign = "$"
        print(f"{key}: {sign}{money[key]}")
    input("\n↵\n")


def order():
    global COFFEE_LIST, TECH_LIST
    option = ""
    clear_screen()
    while option not in COFFEE_LIST and option not in TECH_LIST:
        clear_screen()
        option = input(f"What would you like to order? {"/".join(COFFEE_LIST)}\n[Technical options: {"/".join(TECH_LIST)}]\n").lower()
    return option


def check_resources(my_order, resources_now):
    errors = 0
    not_enough = []
    for ingredient in MENU[my_order]["ingredients"]:
        if (MENU[my_order]["ingredients"][ingredient]) > (resources_now[ingredient]):
            not_enough.append(ingredient)
            errors +=1
    if errors > 0:
        print(f"\nSorry, there is not enough {', '.join(not_enough)}.")
        input("\n↵\n")
    return errors == 0


def process_coins(my_order):
    global money
    inserted = 0.0
    inserted_coins = {"quarters": 0
        , "dimes": 0
        , "nickles": 0
        , "pennies": 0
        , "total": 0.0}

    drink_cost = MENU[my_order]["cost"]
    clear_screen()
    print(f"\n*** You ordered {my_order} ***\nPlease insert ${drink_cost}. Type 'cancel' to cancel transaction.")
    while inserted < drink_cost:
        for coin_type in COINS:
            if inserted < drink_cost:
                cust_input = ""
                inserted_value = 0
                error_message = "Incorrect input. Please use positive numbers or type 'cancel' to cancel the transaction."
                while cust_input != 'cancel' and not(check_if_int(cust_input)):
                    try:
                        cust_input = input(f"\nNumber of {coin_type} ${COINS[coin_type]}: ").lower()
                        if cust_input == 'cancel':
                            print("Your money are returned. Transaction is cancelled.")
                            input("\n↵\n")
                            return -1
                        inserted_value = int(cust_input)*COINS[coin_type]
                        inserted_coins[coin_type] += int(cust_input)
                        if inserted_value < 0.0:
                            print(error_message)
                    except ValueError:
                        print(error_message)
                inserted += round_two(inserted_value)
                inserted_coins["total"] += round_two(inserted_value)
                if inserted < drink_cost:
                    clear_screen()
                    print(f"\n*** You ordered {my_order} ***\nPlease insert ${drink_cost}. Type 'cancel' to cancel transaction.")
                    print(f"\n___\nYou inserted ${round_two(inserted)}.\nYou still need to insert ${round_two(drink_cost-inserted)}\n___\n")
    my_change = round_two(inserted - drink_cost)
    print(f"\n*** You ordered {my_order} ***\nYou inserted ${round_two(inserted)}.")

    for coin_type in inserted_coins:
        money[coin_type] += round_two(inserted_coins[coin_type])

    return my_change


def calculate_change(change_amt):
    global money
    return_coins = {"quarters": 0
        , "dimes": 0
        , "nickles": 0
        , "pennies": 0
        , "total": 0.0}

    money_return = {}
    for key in money:
        money_return[key] = money[key]

    for coin_type in COINS:
        change_in_coin_type = int(change_amt/COINS[coin_type])
        if 0< change_in_coin_type >= money_return[coin_type]:
            number = money_return[coin_type]
            amount = money_return[coin_type]*COINS[coin_type]
            return_coins[coin_type] += number
            return_coins["total"] += amount
            money_return[coin_type] = 0
            money_return["total"] -= amount
            change_amt -= amount

        elif change_amt > 0:
            number = change_in_coin_type
            amount = change_in_coin_type * COINS[coin_type]
            return_coins[coin_type] += number
            return_coins["total"] += amount
            money_return[coin_type] -= number
            money_return["total"] -= amount
            change_amt -= amount
        change_amt = round_two(change_amt)

    return_coins["total"] = round_two(return_coins["total"])
    return return_coins


def return_change(return_coins):
    global money
    for coin_type in return_coins:
        money[coin_type] -= return_coins[coin_type]


def order_payed(my_order, my_change, change_to_return):
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
    global resources
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"...\nYour {drink} is ready. Have a nice day!")
    input("\n↵\n")


def add_resources():
    global resources, money
    clear_screen()
    resources_or_money = input("What do you want to add: resources/money\n")

    if resources_or_money.lower() == "resources":
        list_keys = list(resources.keys())
    elif resources_or_money.lower() == "money":
        list_keys = list(COINS.keys())
    else:
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
                   if resources_or_money.lower() == "resources":
                       resources[key] += int(add)
                   elif resources_or_money.lower() == "money":
                       money[key] += int(add)
                       money["total"] += round_two(int(add)*COINS[key])
            except ValueError:
                print(message)
    clear_screen()
    print("All done! Current resources: ")
    report()



turn_on = True

while turn_on:
    selected_option = order()
    if selected_option in COFFEE_LIST:
        if check_resources(selected_option, resources):
            money_to_return = process_coins(selected_option)
            if money_to_return != -1:
                can_return = calculate_change(money_to_return)["total"]
                if order_payed(selected_option, money_to_return, can_return):
                    make_a_drink(selected_option)
    elif selected_option == 'report':
        report()
    elif selected_option == 'add':
        add_resources()
    elif selected_option == 'off':
        clear_screen()
        print("Goodbye!")
        turn_on = False
