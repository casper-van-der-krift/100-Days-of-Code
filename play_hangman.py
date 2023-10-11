#Imports
from replit import clear
import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Start
print("Welcome to Hangman!")
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()  

    clear()

    #Let user know if they're guessing a letter that has already been correctly guessed.
    if guess in display:
      print(f"You've already guessed the letter {guess}.")

    #Check guessed letter and replace _ by the letter if correct
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong
    if guess not in chosen_word:
        print(f"The letter {guess} you've guessed is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Print display with a space between characters
    print(f"{' '.join(display)}")

    #Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Print the ASCII-art stage of the hangman
    print(stages[lives])
