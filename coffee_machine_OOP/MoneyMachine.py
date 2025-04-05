import CoffeeMachine

COINS = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

ZERO_COINS = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0, "total": 0.0}


class MoneyMachine:
    def __init__(self):
        self.money = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0, "total": 0}

    def report(self):
        print("\n".join([f"{k}: ${v}" if k == "total" else f"{k}: {v}" for k, v in self.money.items()]))


    def add_or_deduct_money(self, coins_dict, plus_minus):
        """Select list of coins (+total), which needs to be added or deducted to/from available money.
        To add, pass 'plus', to deduct, pass 'minus' to the second argument."""
        sign = -1 if plus_minus == "minus" else 1 if plus_minus == "plus" else 0
        for coin_type, value in coins_dict.items():
            self.money[coin_type] = round(self.money[coin_type]+(sign*value),2)


    def process_coins(self, order, coffee_maker):
        """When cancelled, returns -1 and a message that money are returned,
        else returns change amount in format 0.00"""
        inserted_coins = ZERO_COINS.copy()
        drink_cost = coffee_maker.menu[order]["cost"]
        CoffeeMachine.clear_screen()
        header = f"\n*** You ordered {order} ***\nPlease insert ${drink_cost}. Type 'cancel' to cancel transaction."
        print(header)
        while inserted_coins["total"] < drink_cost:
            for coin_type, value in COINS.items():
                if inserted_coins["total"] < drink_cost:
                    customer_input = ""
                    error_message = "Incorrect input. Please use positive numbers or type 'cancel' to cancel the transaction."
                    while customer_input != 'cancel' and not(CoffeeMachine.check_if_int(customer_input)):
                        try:
                            customer_input = input(f"\nNumber of {coin_type} ${value}: ").lower()
                            if customer_input == 'cancel':
                                print("Your money are returned. Transaction is cancelled.")
                                input("\n↵\n")
                                return -1
                            else:
                                number = int(customer_input)
                                amount = round(number*value,2)
                                if amount < 0.0:
                                    print(error_message)
                                else:
                                    inserted_coins[coin_type] += number
                                    inserted_coins["total"] += amount
                        except ValueError:
                            print(error_message)
                    if inserted_coins["total"] < drink_cost:
                        CoffeeMachine.clear_screen()
                        print(f"{header}\n___\nYou inserted ${inserted_coins["total"]:.2f}.\n"
                              f"You still need to insert ${drink_cost-inserted_coins["total"]:.2f}\n___\n")

        change = round(inserted_coins["total"] - drink_cost,2)
        CoffeeMachine.clear_screen()
        print(f"\n*** You ordered {order} ***\nYou inserted ${inserted_coins["total"]:.2f}.")

        self.add_or_deduct_money(inserted_coins, "plus")

        return change


    def calculate_change(self, change_amt):
        """Calculates how the change can be returned with available money.
        Returns a list with types of coins and total amount if change is available, otherwise returns -1"""
        return_coins = ZERO_COINS.copy()
        money_return = self.money.copy()
        for coin_type, value in COINS.items():
            change_in_coin_type = int(change_amt/value)
            if change_amt > 0:
                number = money_return[coin_type] if change_in_coin_type >= money_return[coin_type] else change_in_coin_type
                amount = round(value*(money_return[coin_type]*value if change_in_coin_type >= money_return[coin_type] else change_in_coin_type),2)
                return_coins[coin_type] += number
                return_coins["total"] = round(return_coins["total"]+ amount,2)
                money_return[coin_type] -= number
                money_return["total"] = round(money_return["total"]-amount,2)
                change_amt = round(change_amt-amount,2)
        return return_coins if change_amt == 0 else -1


    def process_payment(self, order, coffee_maker):
        """Processes the payment:
        if payment is cancelled - no money added/returned to available money and function returns False,
        if not enough change (ex. no available coins to return full change) - all inserted money are returned and function returns False,
        else - change is deducted from available money and functions returns True"""

        processed = 0
        change = self.process_coins(order, coffee_maker)
        if change != -1:
            return_coins = self.calculate_change(change)
            if return_coins != -1:
                print(f"Your change: ${change}")
                processed = 1
            else:
                inserted_total = change + coffee_maker.menu[order]["cost"]
                return_coins = self.calculate_change(inserted_total)
                input(f"Not enough money for the change, please get back ${inserted_total}\nSee you next time!\n↵\n")

            self.add_or_deduct_money(return_coins, "minus")
            #Deduct change or all inserted money from available money

        return processed == 1


    def add_money(self):
        list_keys = list(COINS.keys())

        for key in list_keys:
            add = ""
            message = "Incorrect input. Please use positive whole numbers."
            while not CoffeeMachine.check_if_int(add):
                try:
                    add = input(f"Add {key}: ")
                    if not CoffeeMachine.check_if_int(add):
                        print(message)
                    else:
                        self.money[key] += int(add)
                        self.money["total"] += int(add) * COINS[key]
                except ValueError:
                    print(message)
            self.money["total"] = round(self.money["total"],2)
