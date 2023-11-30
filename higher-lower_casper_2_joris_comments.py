#Imports
#import numpy as np
import random
import json
from art import logo, vs
from replit import clear
import sys
from pprint import pprint

#Functions

def load_json() -> list:
  """This function reads a json file with a list of dictionairies and returns that list."""
  with open('data.json', 'r') as file:
    data = json.load(file)
  return data

def random_answer(answer_list: list) -> dict:
  """This functions chooses a random item from a list and returns that item."""
  return random.choice(answer_list)

# def random_answer_np(answer_list: list, size: int) -> np.array:
#   """This function does the same as random_answer(), but it uses numpy instead of random. This make the function more versatile."""
#   return np.random.choice(
#     answer_list,
#     size=size,
#     replace=False
#   )
  

def ask_question() -> str:
  """Function takes user input. Input limited to 'a' or 'b'. Otherwise, the question is repeated by recursion."""
  user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
  if user_input not in ['a', 'b']:
    print("Wrong input: Choose between 'A' and 'B'. Please try again.")
    ask_question()
  else:
    return user_input

def print_user_interface() -> str:
  clear()
  print(logo)

#Load answer data
data = load_json()

#Pretty Print data
pprint(data)

#Set user score to zero
user_score = 0

#Print logo
print(logo)

#Choose two random variables from data and store in 'A' and 'B'
A = random_answer(data)
B = random_answer(data)

#Game
while True:
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(vs)
  print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")
  
  correct_answer = 'a' if A['follower_count'] > B['follower_count'] else 'b'
  user_answer = ask_question()
  
  if correct_answer != user_answer:
    print_user_interface()
    print(f"You're wrong! You lose! Final score: {user_score}")
    break
  else:
    user_score += 1
    print_user_interface()
    print(f"You're right! Current score: {user_score}.")
    A = B
    B = random_answer(data)
