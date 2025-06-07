import data
from data import MENU
import sys

money = 0
resources_left = data.resources


def report(temp_resources_left, temp_money):
    """Only prints resources that are remaining in the coffee machine"""
    print(f'Water: {temp_resources_left["water"]}')
    print(f'Milk: {temp_resources_left["milk"]}')
    print(f'Coffee: {temp_resources_left["coffee"]}')
    print(f"Money: ${temp_money}")


def greet_customer():
    """Only take input like 'report', 'off' or coffee type user specified and returns it"""
    return input("What would you like? (espresso/latte/cappuccino): ")


# noinspection PyInconsistentReturns
def check_input(temp_resources_left, temp_money):
    """Check what input the user gave by calling the greet_customer() function"""
    response = greet_customer()
    if response == "report":
        report(temp_resources_left, temp_money)  # prints report
        return "report"
    elif response == "off":  # turns coffee machine off
        print("Coffee Machine is off")
        sys.exit(0)
    else:  # return coffee type
        return response


# noinspection PyInconsistentReturns
def check_sufficient_resources(temp_coffee_type, temp_resources_left):
    if "water" in MENU[temp_coffee_type]["ingredients"] and temp_resources_left['water'] < \
            MENU[temp_coffee_type]["ingredients"]['water']:
        print(f"Sorry there is not enough water.")
        return 0
    elif "milk" in MENU[temp_coffee_type]["ingredients"] and temp_resources_left['milk'] < \
            MENU[temp_coffee_type]["ingredients"]['milk']:
        print(f"Sorry there is not enough milk.")
        return 0
    elif "coffee" in MENU[temp_coffee_type]["ingredients"] and temp_resources_left['coffee'] < \
            MENU[temp_coffee_type]["ingredients"]['coffee']:
        print(f"Sorry there is not enough coffee.")
        return 0
    else:
        print(f"There are enough resources")
        return 1


def process_coins(temp_coins_list):
    """coins_list will be a dictionary of all the coins the user entered,
    with keys being the coin type and value being the number of coins"""
    coins_value = (temp_coins_list['quarters'] * 0.25) + (temp_coins_list['dimes'] * 0.1) + (
            temp_coins_list['nickles'] * 0.05) + (temp_coins_list['pennies'] * 0.01)
    return round(coins_value, 2)


def check_transaction_successful(temp_coins_list, temp_coffee_type):
    global money
    money_user_gave = process_coins(temp_coins_list)  # stores total money user gave

    # print(coffee_type)

    # now we check if the money they gave is enough or not
    temp_actual_cost = MENU[temp_coffee_type]["cost"]
    if money_user_gave < temp_actual_cost:
        print(f"Sorry that's not enough money. Money refunded.")
        return -1  # If transaction not successful
    else:
        print("There's enough money")
        money += temp_actual_cost
        if money_user_gave > temp_actual_cost:
            change = round((money_user_gave - temp_actual_cost), 2)
            print(f"Here is ${change} in change.")
        return 1  # If transaction successful


def make_coffee(temp_coffee_type):
    successful = check_transaction_successful(coins_list, coffee_type)
    if successful == 1:
        # resources_left['water'] -= MENU[temp_coffee_type]['ingredients']['water']
        # resources_left['milk'] -= MENU[temp_coffee_type]['ingredients']['milk']
        # resources_left['coffee'] -= MENU[temp_coffee_type]['ingredients']['coffee']
        """The above code throws a value error for the espresso coffee type because it doesn't have milk as an 
        ingredient in the dictionary, the below code is better at solving this problem"""

        for ingredient in MENU[temp_coffee_type]['ingredients']:
            resources_left[ingredient] -= MENU[temp_coffee_type]['ingredients'][ingredient]

        print(f"Here is your {temp_coffee_type} ☕. Enjoy!")

        # report(resources_left, money)

    else:
        return 0


coffee_machine_on = True

while coffee_machine_on:
    coffee_type = check_input(resources_left, money)

    if coffee_type  in MENU:
        flag = check_sufficient_resources(coffee_type, resources_left)
        if flag == 0:  # if there are not enough resources, then the below lines should not b executed and while loops needs to start over again
            continue

        else: # there are enough resources to make coffee
            print(f"Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            coins_list = {"quarters": quarters, "dimes": dimes, "nickles": nickles, "pennies": pennies}

            user_money = process_coins(coins_list)
            # print(user_money)
            # check_transaction_successful(coins_list, coffee_type)
            flag = make_coffee(coffee_type)
            if flag == 0:
                coffee_machine_on = False

    elif coffee_type not in ['report', 'off']:
        print("Invalid input. Please try again.")