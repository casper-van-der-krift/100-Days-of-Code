from art import logo
from replit import clear

#Define functions

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# Store functions in dictionairy

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

print(logo)
shutdown = False

number_1 = round(float(input("What's the first number?: ")), 1)

while not shutdown:
  
  for key in operations:
    print(key)
  operation_symbol = input("Pick an operator from the lines above: ")
  number_2 = round(float(input("What's the second number?: ")), 1)
  
  answer = operations[operation_symbol](number_1, number_2)
  
  print(f"{number_1} {operation_symbol} {number_2} = {answer}")
  
  continue_with_answer = input(f"Type 'y' to continue with {answer}, type 'n' to start a new calculation or type 'sd' to shutdown calculator: ")
  
  if continue_with_answer == 'y':
    number_1 = answer
  elif continue_with_answer == 'n':
    clear()
    number_1 = round(float(input("What's the first number?: ")), 1)
  elif continue_with_answer == 'sd':
    shutdown = True
    print("Calculator shutting down. Goodbye.")
    

