#Password Generator Project
#Assignment conditions

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

total_digits = nr_letters + nr_symbols + nr_numbers

dummy_password = []

for i in range(nr_letters):
  rand_let = letters[random.randint(0, len(letters)-1)]
  dummy_password.append(rand_let)
print(dummy_password)

for i in range(nr_numbers):
  rand_num = numbers[random.randint(0, len(numbers)-1)]
  dummy_password.append(rand_num)
print(dummy_password)

for i in range(nr_symbols):
  rand_sym = symbols[random.randint(0, len(symbols)-1)]
  dummy_password.append(rand_sym)
print(dummy_password)

password = ''.join(dummy_password)

#Test length
if total_digits == len(dummy_password):
  print("Length of password is correct.")
  print(f"Your password is: {password}")
    
else:
  print("Something is wrong with the length of your password.")

#Hard Level - Order of characters randomised (don't use .shuffle())
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_digits = nr_letters + nr_symbols + nr_numbers
dummy_password = []
index_list = []

for i in range(total_digits):
  dummy_password.append("*")
  index_list.append(i)

# print(f"Dummy password: {dummy_password}.")
# print(f"Index list: {index_list}.")

for i in range(nr_letters):
  rand_let = letters[random.randint(0, len(letters)-1)]
  rand_position = index_list[random.randint(0, len(index_list)-1)]
  # print(f"Rand position letter is {rand_position}")
  dummy_password[rand_position] = rand_let
  index_list.remove(rand_position)

# print(f"Dummy password: {dummy_password}.")
# print(f"Index list: {index_list}.")

for i in range(nr_numbers):
  rand_num = numbers[random.randint(0, len(numbers)-1)]
  rand_position = index_list[random.randint(0, len(index_list)-1)]
  # print(f"Rand position number is {rand_position}")
  dummy_password[rand_position] = rand_num
  index_list.remove(rand_position)

for i in range(nr_symbols):
  rand_sym = symbols[random.randint(0, len(symbols)-1)]
  rand_position = index_list[random.randint(0, len(index_list)-1)]
  # print(f"Rand position sumbol is {rand_position}")
  dummy_password[rand_position] = rand_sym
  index_list.remove(rand_position)

# print(f"Dummy password: {dummy_password}.")
# print(f"Index list: {index_list}.")

password = ''.join(dummy_password)

#Test length
if total_digits == len(dummy_password):
  # print("Length of password is correct.")
  print(f"Your password is: {password}")
    
else:
  print("Something is wrong with the length of your password.")
