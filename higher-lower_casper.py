import random

from game_data import data

from art import logo, vs

from replit import clear

#Randomly pick answer A and B

def random_answer(answer_dict):
    """Chooses a random item from a list and returns it."""
    return random.choice(answer_dict)

#Choose two random dictionairies from the data list and store one in A and one in B
A = random_answer(data)

B = random_answer(data)

#Define variable to quit game when an answer is false
end_game = False

#Start user score is zero
user_score = 0

print(logo)

while not end_game:

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

    correct_answer = A['follower_count'] > B['follower_count']

    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_input == 'A':
      user_answer = True
    elif user_input == 'B':
      user_answer = False
    else:
      print("Wrong input: Choose between 'A' and 'B'.")

    #Print statements for testing
    #print(f"The correct answer A > B is: {correct_answer}")
    #print(f"The user answer A > B is: {user_answer}")

    if correct_answer != user_answer:
      end_game = True
      clear()
      print(logo)
      print(f"You're wrong! You lose! Final score: {user_score}")
    elif correct_answer == user_answer:
      user_score += 1
      clear()
      print(logo)
      print(f"You're right! Current score: {user_score}.")
      A = B
      B = random_answer(data)
      
    #Print statements for testing
    #print(f"End game = {end_game}, user_score = {user_score}")
