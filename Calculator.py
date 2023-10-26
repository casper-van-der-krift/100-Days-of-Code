from art import logo
from replit import clear

#Define function

def calculation(n1, operator, n2):
  """Takes a first number, an operator (addition, subtraction, multiplication and division)
  and a second number. Returns the result of "n1 -operator- n2". """
  if operator == '+':
    result = round(n1 + n2, 1)
    print(f"{n1} + {n2} = {result}")
    return result
  elif operator == '-':
    result = round(n1 - n2, 1)
    print(f"{n1} - {n2} = {result}")
    return result
  elif operator == '*':
    result = round(n1 * n2, 1)
    print(f"{n1} * {n2} = {result}")
    return result
  elif operator == '/':
    result = round(n1 / n2, 1)
    print(f"{n1} / {n2} = {result}")
    return result
  else:
    print("You've chosen an illegal operator. Please choose between + - * /.")
    return

# START CALCULATOR
# Print logo
print(logo)
# Set varable to control continuation with result in while loop
shut_down = False
# Begin with number 1 outside of while loop, because we do not have a result yet
number_1 = round(float(input("What's the first number?: ")), 1)

# Repeat as long as shut down of calculator is not initiated
while not shut_down:
  # Choose operation + - * /  
  operation = input("+\n-\n*\n/\nPick an operation: ")
  # Choose second number within while loop
  number_2 = round(float(input("What's the next number?: ")), 1)
  # Call operator function with positional arguments and store result in variable 'result'
  result = calculation(number_1, operation, number_2)
  # Ask user if they want to continue a calculation with the result of the previous calculation - yes or no - or if they want to shutdown the calculator
  continue_with_result = input(f"Type 'y' to continue with {result}, type 'n' to start a new calculation or type 'sd' to shutdown calculator: ")
  # If user wants to continue with the result, then the first number of the new calculation is set equal to the result of the previous one
  if continue_with_result == 'y':
    number_1 = result
  # If user wants to start a new calculation, the screen is cleared and the user is asked to input a new first number to start a calculation with
  elif continue_with_result == 'n':
    clear()
    number_1 = round(float(input("What's the first number?: ")), 1)
  # If user wants to shutdown, the shutdown variable is set to true, so that the while loop is broken.
  elif continue_with_result == 'sd':
    shut_down = True
    print("Calculator shutting down. Goodbye.")
