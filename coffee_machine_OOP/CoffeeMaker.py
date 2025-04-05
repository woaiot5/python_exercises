from CoffeeMachine import check_if_int


class CoffeeMaker:
    def __init__(self):
        self.menu = {
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
        self.resources = {"water": 300, "milk": 200, "coffee": 100}


    def report(self):
        print("\n".join([f"{k}: {v}ml" for k, v in self.resources.items()]))


    def check_resources(self, order):
        not_enough = [ingredient
                      for ingredient, qty in self.menu[order]["ingredients"].items()
                      if qty > self.resources.get(ingredient, 0)]
        if not_enough:
            print(f"\nSorry, there is not enough {', '.join(not_enough)}.")
            input("\n↵\n")
            return False
        return True


    def make_a_drink(self, drink, money_machine, coffee_maker):
        if self.check_resources(drink) and money_machine.process_payment(drink, coffee_maker):
            for ingredient, value in self.menu[drink]["ingredients"].items():
                self.resources[ingredient] -= value
            input(f"...\nYour {drink} is ready. Have a nice day!\n↵\n")


    def add_resources(self):
        list_keys = list(self.resources.keys())

        for key in list_keys:
            add = ""
            message = "Incorrect input. Please use positive whole numbers."
            while not check_if_int(add):
                try:
                    add = input(f"Add {key} ml: ")
                    if not check_if_int(add):
                        print(message)
                    else:
                        self.resources[key] += int(add)
                except ValueError:
                    print(message)