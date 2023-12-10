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

from typing import List


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

    """
    Onderstaande aanpassingen zijn gedaan om de aanpassingen in `check_resources()` te ondersteunen
    """
    menu_items = list(menu.keys())
    menu_items_str = "/".join(list(menu.keys()))

    choice = input(f"What would you like? ({menu_items_str}): ").lower()
    if choice not in menu_items + ['report']:
        print(f"Invalid choice. Please choose between ({menu_items_str}): ")
        return ask_drink_choice()
    else:
        return choice


# TODO: Make a function that takes an amount of each coins ($0,01, $0,05, $ 0,10, $0,25) and returns the total value.
def drink_price(drink_name: str) -> float:
    """ Heb hier een functie van gemaakt omdat we het twee keer gebruiken"""
    return round(menu[drink_name]['cost'], 2)


def enter_coins(drink_name: str) -> float:
    """Runs a series of user input to obtain the amount of coins and returns the total value of the coins."""

    """Heel klein dingetje, maar ik wist niet hoe duur mijn drankje was voor ik d'r voor moest betalen. 
    Die :.2f aan het eind forceert de string print om altijd 2 decimalen te printen (zodat je dus $2.50 krijgt ipv 2.5)
    Dit heet String Formatting en je kunt dat bijvoorbeeld ook gebruiken als je 0.8 wilt printen als 80%, dan doe je {value * 100:.0f}%
    """
    drink_price = drink_price(drink_name)

    print(f"Please insert coins. Your {drink_name} costs ${drink_price:.2f}")
    quarters = int(input("\tHow many quarters?: "))
    """ 
    Ik vind eigenlijk dat je na iedere coin entry moet checken of je al genoeg geld hebt, maar dat zou je hele design veranderen, dus doe dat maar niet
    """
    dimes = int(input("\tHow many dimes?: "))
    nickles = int(input("\tHow many nickles?: "))
    pennies = int(input("\tHow many pennies?: "))

    total_coin_value = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

    return round(total_coin_value, 2)


# TODO: Make a function that takes the drink of choice, the amount of money put in the machine. Gives change/feedback.


def payment(drink_name: str, coin_value: float) -> List[bool, float]:  # <- kleine technicality hier, je moet List gebruiken (hierboven geimporteerd). Vraag me niet waarom.
    """Takes the drink of choice, the value of coins and computes the amount of change.
    Returns a boolean that indicates if the payment was successful AND the transferred amount of money."""
    drink_price = drink_price(drink_name)
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
            """
            Je hebt op dit moment geen manier om het script te beindigen. 
            Dit kan je natuurlijk op verschillende manieren doen:
            - Als deze success False is
            - Als er voor geen enkele type koffie nog resources zijn. 
                Stel je hebt nog 100ml water, en iemand besteld een latte, dan kan je nog wel aanbieden om een espresso te maken
            - Of, wss de beste optie, je haalt items van de menu kaart als er geen resources meer voor zijn en als
                er dan niks meer op het menu staat breek je uit je While True loop.
                Dit heb ik hieronder gedaan met `menu.pop(drink_name)` dit gooit het juiste item uit menu.
                Enige probleempje, vind ik, is dat je nu pas na de bestelling kijkt of er nog resources zijn, maar ach :)
            """
            menu.pop(drink_name)
            return success
        else:
            # print("There are enough ingredients.")
            return success


# Program
"""
deze if __name__ == "__main__: ziet er altijd een beetje raar uit, maar het is gebruikelijk om
dit toe tevoegen aan je Python script. Dit is goed voor 2 dingen:
- Alles onder deze regel kun je lezen als het "niet-functie-deel" van je script, het deel waar je je functies execute
- Stel je script opzet ziet er anders uit en je hebt bijvoorbeeld twee files, functions.py en helpers.py. 
    Stel functions.py is een exacte kopie van jou versie van deze main.py (ik noem hem ff anders omdat je normaal niet van main.py importeerd in een andere file ;-)
    Als je dan vervolgens in helpers.py iets doet als `from functions import *` als je bijvoorbeeld `ask_drink_of_choice()` zou willen aanroepen in helpers.py
    Dan zou hij, omdat je met dat import statement de functions.py file aanroep, hij ook de onderstaande code runnen. 
    Dat wil je uiteraard niet, want je wilt alleen die ene functie importeren.
    Doordat je if __name__ == "__main__": hebt gebruikt wordt de code die daar in valt alleen uitgevoerd als die file de "main" file is, dus alleen als je
    python functions.py (of main.py) doet en dus niet als je de file importeerd.
"""
if __name__ == "__main__":

    # Load data


    menu = open_json('menu.json')

    resources = open_json('resources.json')

    money_counter = 0


    # Run Program

    while len(menu) > 0:

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
                money = enter_coins(drink_of_choice)
                payment_success, transfer_amount = payment(drink_of_choice, money)
                if payment_success:
                    update_resources(drink_of_choice, resources)
                    money_counter += transfer_amount

    print("Sorry, no resources available...")