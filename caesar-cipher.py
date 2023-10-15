#Import ASCII logo from other file
from art import logo

#Double alphabet in case user wants to shift across 'z' i.e. boundary of alphabet.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Define function that takes a start text, shifts the letters by a specified amountm and the direction of the shift; forward in case of encoding, backwards in case of decoding.
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  #Reverses the shift direction from positive (i.e. forward) to negative (i.e. backwards) in case of decoding. In case of encoding, keep shift direction as specified (i.e. positive/forward).
  if cipher_direction == "decode":
    shift_amount *= -1
  #Loop through characters and shift letters in specified direction by specified amount.
  for char in start_text:
    #Only letters are shifted! Numbers, spaces and symbols will be returned unchanged.
    if char in alphabet:
      position = alphabet.index(char) 
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
        
  print(f"Here's the {cipher_direction}d result: {end_text}")

#Start
print(logo)
print("Welcome to Caesar Cipher!")

#Set variable continue_game to create option for restarting cipher in case user wishes to do so.
continue_game = True
while continue_game:

  #Store user input in variables that will be arguments for our function
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  
  #Make sure user chooses correctly between two specified options for fuction parameter 'direction'.
  if direction != 'encode' and direction != 'decode':
    print("You must choose between 'encode' and 'decode'. Please choose again.")
  else:    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))   

    #In case user inputs a shift value larger than 26, we compute the effective shift by moduling by 26 (i.e. length of alphabet).
    shift_effective = shift % 26

    #Call function with keyword parameters set to user input arguments
    caesar(start_text=text, shift_amount=shift_effective, cipher_direction=direction)
    restart = input("Would you like to continue cyphering? Yes or No?")
    if restart == 'No':
      continue_game = False
  
