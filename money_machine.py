class MoneyMachine:

    def total_of_money(self):
        """Returns the total calculated from the coins inserted"""

        print('Please insert coins.')
        quarters = 0.25 * int(input('How many quarters?: '))
        dimes    = 0.10 * int(input('How many dimes?: '))
        nickles  = 0.05 * int(input('How many nickles?: '))
        pennies  = 0.01 * int(input('How many pennies?: '))

        total_received = round(quarters + dimes + nickles + pennies, 2)
        return total_received

    def enough_money(self, cost_of_coffee):
        """Returns True when the payment is accepted and shows the change,
        False if the money is not enough to afford the coffee selected"""
        money = self.total_of_money()

        if money >= cost_of_coffee:
            change = round(money - cost_of_coffee, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded ✨\n")
            return False
