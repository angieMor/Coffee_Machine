class CoffeeMachine:

    def report(self, ingredients, money):
        print(f"Water: {ingredients['water']}ml\nMilk: {ingredients['milk']}ml\nCoffee: {ingredients['coffee']}g"
              f"\nMoney: ${money}\n")

    def ingredients_available(self, coffee, menu, ingredients_available):
        """Returns True when the coffee can be made, False when ingredients are not enough"""

        materials = menu[coffee]['ingredients']
        for key in materials:

            # Validating if the resources are minor for what we need to do
            if materials[key] > ingredients_available[key]:
                print(f"Sorry there is not enough {key} for this coffee")
                return False

        return True

    def making_coffee(self, coffee, menu, ingredients_available):
        """Shows when the coffee is ready and will take the ingredients from the machine"""
        materials = menu[coffee]['ingredients']
        for key in materials:
            ingredients_available[key] = ingredients_available[key]-materials[key]
        print(f"Here is your {coffee} ☕. Enjoy!\n")