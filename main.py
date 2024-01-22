MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert Coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_transaction(money_received, drink_cost):
    """Returns True when money is sufficient otherwise returns False."""
    if money_received >= drink_cost:
        cost = round(money_received - drink_cost, 2)
        print(f"Here is ${cost} dollars in change")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


while True:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "off":
        break
    elif request == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[request]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(request, drink["ingredients"])
