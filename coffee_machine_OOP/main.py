from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine
from CoffeeMachine import CoffeeMachine, clear_screen

turn_on = True
coffee = CoffeeMaker()
money = MoneyMachine()
machine = CoffeeMachine(coffee)

while turn_on:
    option = machine.order()

    if option in machine.coffee_list:
        coffee.make_a_drink(option, money, coffee)

    elif option in machine.tech_list:
        clear_screen()
        turn_on = machine.action(option)(coffee, money)
