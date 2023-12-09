# Starting points in dictionaries (machine.py) or json files (menu.json and recourse.json)
#    Espresso: 50 ml water, 18g coffee, $1,50
#    Latte: 200 ml water, 24g coffee, 150 ml milk, $2,50
#    Cappuccino: 250 ml water, 24 coffee, 100 ml milk, $3,00
#    Resources at the start: 300 ml water, 200 ml milk, 100g coffee, $0,00
#    Coin operated. Works with: $0,01, $0,05, $0,10, $0,25


# Program requirements:
#    1. Report function:
#        Print report with resources that are left and total transferred money. Activate by typing 'report'.
#    2. Ordering a drink + updating resources:
#        Check if resources are sufficient for requested recipe and give feedback.
#        Process coins:
#            Check if inserted money is sufficient for requested recipe.
#                Yes: give drink, give change, give feedback: "Here is your {requested drink} ☕. Enjoy!"
#                No: give feedback: "Sorry, {amount of money} is not enough for {requested drink}. Money refunded.
#        After giving a drink, reduce the used resources from the resources-balance
#        Keep running


# Imports:
import numpy as np
import random
import json
import sys
from pprint import pprint


# Function definitions


# TODO: Make a function that loads data from a .json file and returns it as a dictionary.


def open_json(file_name: str) -> dict:
    """This function loads a json file with a nested dictionary and returns the dictionary."""
    with open(f"{file_name}", 'r') as file:
        data = json.load(file)
    return data


# TODO: Make a function that asks the user which drink to prepare. Keep asking if an invalid answer is given.


def ask_drink_choice() -> str:
    """Takes user input which drink is requested. Keeps asking if invalid answer is given. Returns the choice"""
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice not in ['espresso', 'latte', 'cappuccino', 'report']:
        print("Invalid choice. Please choose between (espresso/latte/cappuccino): ")
        return ask_drink_choice()
    else:
        return choice


# TODO: Make a function that takes an amount of each coins ($0,01, $0,05, $ 0,10, $0,25) and returns the total value.


def enter_coins() -> float:
    """Runs a series of user input to obtain the amount of coins and returns the total value of the coins."""
    print("Please insert coins.")
    quarters = int(input("\tHow many quarters?: "))
    dimes = int(input("\tHow many dimes?: "))
    nickles = int(input("\tHow many nickles?: "))
    pennies = int(input("\tHow many pennies?: "))

    total_coin_value = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

    return round(total_coin_value, 2)


# TODO: Make a function that takes the drink of choice, the amount of money put in the machine. Gives change/feedback.


def payment(drink_name: str, coin_value: float) -> [bool, float]:
    """Takes the drink of choice, the value of coins and computes the amount of change.
    Returns a boolean that indicates if the payment was successful AND the transferred amount of money."""
    drink_price = round(menu[drink_name]['cost'], 2)
    success = coin_value >= drink_price
    if not success:
        print(f"Sorry, ${coin_value} is not enough money for {drink_name} that costs ${drink_price}. Money Refunded.")
        return success, drink_price
    else:
        change = round((coin_value - drink_price), 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink_name} ☕. Enjoy!")
        return success, drink_price


# TODO: Make a function that updates the resources after an order.


def update_resources(drink_name: str, resource_balance: dict) -> dict:
    """Takes the drink of choice, looks up the ingredients in the menu,
     and subtracts that amount from the resource balance. Returns the updated resource balance."""
    ingredients = menu[drink_name]['ingredients']
    for ingredient in ingredients:
        resource_balance[ingredient] -= ingredients[ingredient]
    return resource_balance


# TODO: Make a function that checks the resource balance with the recipe. Returns a boolean if recipe is possible.


def check_resources(drink_name: str, resource_balance: dict) -> bool:
    ingredients = menu[drink_name]['ingredients']
    for ingredient in ingredients:
        success = resource_balance[ingredient] >= ingredients[ingredient]
        if not success:
            print(f"Sorry, there is not enough {ingredient}.")
            return success
        else:
            # print("There are enough ingredients.")
            return success


# Program


# Load data


menu = open_json('menu.json')

resources = open_json('resources.json')

money_counter = 0


# Run Program

while True:

    drink_of_choice = ask_drink_choice()

    if drink_of_choice == 'report':
        print("Resource balance:")
        for i in resources:
            print(f"\t{i.capitalize()}: {resources[i]}")
        print(f"Transferred value:")
        print(f"\tMoney: ${money_counter}")
    else:
        sufficient_resources = check_resources(drink_of_choice, resources)
        if sufficient_resources:
            money = enter_coins()
            payment_success, transfer_amount = payment(drink_of_choice, money)
            if payment_success:
                update_resources(drink_of_choice, resources)
                money_counter += transfer_amount
