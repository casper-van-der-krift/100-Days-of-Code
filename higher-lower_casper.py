import numpy as np

import json 

from art import logo, vs

from replit import clear

from pprint import pprint

import sys

# Ik heb 'type-hints' toegevoegd aan alle functies. Dit is nieuw in Python sinds versie 3.8 ofzo.
# Het is niet perse nodig om dit te doen, als je bijvoorbeeld niet een dictionary type geeft aan 'answer_dict' in de random_answer() function
# dat geeft hij geen error. Maar in gecompliceerde code is dit handig om overzichtelijk te houden wat voor typen variabelen worden doorgegeven

# omdat jsons cool zijn heb ik je game_data 'data' variable in een json bestand gezet, die wordt hieronder geladen. 
# gewoon, omdat het kan :)
def load_json() -> list:
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data


# Heb deze functie in Numpy gezet, is verder geen 'beter' oplossing, maar een simpelweg een andere manier om dit te doen
# np.random.choice is ook meer 'versatile' omdat je bijvoorbeeld ook nog een waarde kan mee geven (met dezelfde lengte als je dictionary)
# voor wanneer je gewogen random picks wil doen. Dus stel answer_dict heeft 3 waardes, dan kun je doen p=[0.5, 0.3, 0.2] en dan wegen die anders
def random_answer(answer_dict: dict, size: int) -> np.array:
    """Chooses a random item from a list and returns it."""
    return np.random.choice(
       answer_dict,
       size=size,
       replace=False
    )

# nit-picky, maar we hebben repetitive code, dus soms kan je dat in een functie zetten
def print_user_interface() -> None:
    clear()
    print(logo)

# door de vraagstelling in een functie te zetten kan je bij een fout antwoord de vraag nog een keer stellen (recursion)
# in jou code kreeg je een error als je niet 'a' of 'b' invoerde omdat je dan geen 'user_answer' variable creerde
def ask_question() -> str:
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()  # het is iets logischer om .lower() te doen, maar boeit niet veel
    if user_input not in ['a', 'b']:
       print("Wrong input: Choose between 'A' and 'B'. Please try again...")
       ask_question()
    else:
       return user_input
        
  
data = load_json()
# pretty print is handig voor jsons etc, is een ingebouwde package (zie import hierboven)
pprint(data)

#Choose two random dictionairies from the data list and store one in A and one in B
A, B = random_answer(data, size=2)

#Start user score is zero
user_score = 0

print(logo)

# Ik heb je 'end_game' variable d'r uit gesloopt, om te laten zien hoe 't ook kan.
# Ik ben trouwens van mening dat boolean variables altijd moeten beginnen met 'is_'. Dus in jouw geval zou ik 'end_game' eindigen naar 'is_game_over'. 
while True:
    #Formulate comparison in following setup: Compare A: {name}, a {profession} from {country}.
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

    #Print statement for testing
    print(f"Pssst! A has {A['follower_count']} followers, while B as {B['follower_count']}")

    #Check answer:
      #If user inputs A, that means user_answer = True
      #If user inputs B, that means user_answer = False
      #actual_answer = A{follower_count} > B{followers}
      #Check if user_answer = actual_answer

    # mogelijk een iets meer condensed manier om dit te doen, zodat je niet 4/5 lines nodig hebt met if else
    correct_answer = 'a' if A['follower_count'] > B['follower_count'] else 'b'

    user_answer = ask_question()

    if correct_answer != user_answer:
      print_user_interface()
      print(f"You're wrong! You lose! Final score: {user_score}")
      break # je kunt uit loops breaken met 'break' dit werkt ook voor for-loops. Dan stop de loop en gaat hij daarna verder. 
      # In dit geval gebeurd er niks omdat er na de while loop verder geen code staat.
      # sys.exit() # dit is een andere manier om uit je while loop te breken. Dit werkt uiteraard alleen als je daarna je hele python script will stoppen

    else: 
      # omdat er maar 2 opties mogelijk zijn, kan je gewoon else doen. 
      # als je een if, elif doet dan hoor je eigenlijk ook een else: te doen, maar dat is hier niet nodig want je checkt alleen 'True' of 'False'
      user_score += 1
      print_user_interface()
      print(f"You're right! Current score: {user_score}.")
      A = B
      B = random_answer(data, size=1)[0]
      
    #Print statements for testing
    #print(f"End game = {end_game}, user_score = {user_score}")
