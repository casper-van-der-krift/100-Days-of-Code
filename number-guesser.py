from art import logo

print(logo)

from random import randint

print("I'm thinking of a number between 1 and 100.")

answer = randint(1,100)

#print(f"Pssst, the answer is {answer}")

difficulty = input("Choose a difficulty: type 'easy' or 'hard': ").lower()

if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts = 5

def game_on():

  global attempts
  
  print(f"You have {attempts} attempts remaining to guess the number.")
  
  guess = int(input("Make a guess: "))
  
  if guess == answer:
    print(f"You got it! The answer was {answer}. You win!")
     
  else:
    if attempts == 1:
      if guess > answer:
        print("Too high!\nYou've run out of guesses, you lose.")
      elif guess < answer:
        print("Too low!\nYou've run out of guesses, you lose.")
    elif attempts > 1:                         
      if guess > answer:
        print("Too high!\nGuess again!")
      elif guess < answer:
        print ("Too low!\nGuess again!")
      
      attempts -= 1
      
      game_on()

game_on()


  



    

  

  
  
