from menu import MenuAndIngredients
from coffee_machine import CoffeeMachine
from money_machine import MoneyMachine

menu = MenuAndIngredients().Menu
ingredients = MenuAndIngredients().Resources
money_machine = MoneyMachine()
coffee_machine = CoffeeMachine()

initial_money = 0

off = False

while not off:
    order = input("  What would you like to order? (espresso/latte/cappuccino): ")
    # Secret admin command #1
    if order == "report":
        coffee_machine.report(ingredients, initial_money)
    # Secret admin command #2
    elif order == "off":
        off = True
        print("\n--> You've turned off the machine!\n")
    else:
        if (order == 'espresso') or (order == 'latte') or (order == 'cappuccino'):
            # Check resources, sufficient?
            selected_coffee = coffee_machine.ingredients_available(order, menu, ingredients)

            # Transaction is successfully to afford a coffee?
            if selected_coffee and money_machine.enough_money(menu[order]['cost']):
                initial_money += menu[order]['cost']
                # Make coffee
                coffee_machine.making_coffee(order, menu, ingredients)
        else:
            # User typed and option that was not given
            print('\nPlease only type one of the three options given, in order to give you some coffee 🧁\n')