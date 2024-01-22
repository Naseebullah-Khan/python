from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while True:
    order = input(f"What would you like? ({menu.get_items()}):")
    if order == "off":
        break
    elif order == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(order)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
