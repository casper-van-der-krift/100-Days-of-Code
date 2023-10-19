from replit import clear
from art import logo

def add_bid():
  clear()
  name = input("What is your name?\n")
  bid = float(input("What is your bid? \n$"))
  bidders[name] = bid

def winning_bid(total_bids):
  max_value = 0
  max_name = "None"
  for name in total_bids:
    if total_bids[name] > max_value:
      max_value = total_bids[name]
      max_name = name
  print(f"The winner is {max_name}, who's bid of ${max_value} was the highest.")

print(logo)
print("Welcome to the blind auction!")
participate = input("Do you want to participate in the auction? Yes or No?\n").lower()
bidders = {}
end_auction = False

if participate == 'no' and len(bidders) == 0:
  end_auction = True
  print("No bids were submitted. The auction ends.")

while not end_auction:
  add_bid()
  more_participants = input("Is there another person that wants to participate in the auction?").lower()
  if more_participants == "no" and len(bidders) != 0:
    end_auction = True
    print(f"No more bids have been submitted. Out of the {len(bidders)} submitted bids, we will now determine the winner.")
    winning_bid(bidders)
