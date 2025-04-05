import money, resources
from tech import clear_screen
from available import menu


COFFEE_LIST = list(menu.keys())
TECH_LIST = ['report', 'add', 'off']


def order():
    option = ""
    clear_screen()
    while option not in COFFEE_LIST+TECH_LIST:
        clear_screen()
        option = input(f"What would you like to order? {"/".join(COFFEE_LIST)}\n[Technical options: {"/".join(TECH_LIST)}]\n").lower()
    return option


def report():
    resources.report()
    money.report()
    input("\n↵\n")
    return True


def add_resources():
    clear_screen()
    resources_or_money = input("What do you want to add: resources/money\n").lower()

    if resources_or_money not in ["resources", "money"]:
        input("Incorrect input. Operation is cancelled.\n↵\n")
        return True
    elif resources_or_money == "resources":
        resources.add_resources()
    elif resources_or_money == "money":
        money.add_money()
    clear_screen()
    print("All done! Current resources: ")
    report()
    return True


def off_machine():
    clear_screen()
    print("Goodbye!")
    return False


tech = {"add": add_resources, "off": off_machine, "report": report}