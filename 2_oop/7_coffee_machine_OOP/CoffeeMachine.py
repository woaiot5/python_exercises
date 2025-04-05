from os import system, name


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def check_if_int(string_value):
    try:
        result = (int(string_value) >= 0)
    except ValueError:
        result = False
    return result


class CoffeeMachine:
    def __init__(self, coffee_maker):
        self.coffee_list = list(coffee_maker.menu.keys())
        self.tech_list = ['report', 'add', 'off']


    def order(self):
        option = ""
        clear_screen()
        while option not in self.coffee_list+self.tech_list:
            clear_screen()
            option = input(f"What would you like to order? {"/".join(self.coffee_list)}"
                           f"\n[Technical options: {"/".join(self.tech_list)}]\n").lower()
        return option


    def report(self, coffee_maker, money_machine):
        coffee_maker.report()
        money_machine.report()
        input("\n↵\n")
        return True


    def add_resources(self, coffee_maker, money_machine):
        resources_or_money = input("What do you want to add: resources/money\n").lower()
        clear_screen()
        if resources_or_money not in ["resources", "money"]:
            input("Incorrect input. Operation is cancelled.\n↵\n")
            return True
        elif resources_or_money == "resources":
            coffee_maker.add_resources()
        elif resources_or_money == "money":
            money_machine.add_money()
        clear_screen()
        print("All done! Current resources: ")
        self.report(coffee_maker, money_machine)
        return True


    def off_machine(self, coffee_maker, money_machine):
        print("Goodbye!")
        return False


    def action(self, option):
        return self.add_resources if option == "add" else self.off_machine if option == "off" else self.report