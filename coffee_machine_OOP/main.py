from machine import order, tech, COFFEE_LIST, TECH_LIST
from resources import make_a_drink

turn_on = True

while turn_on:
    option = order()

    if option in COFFEE_LIST:
        make_a_drink(option)

    elif option in TECH_LIST:
        turn_on = tech[option]()
