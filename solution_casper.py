############### Blackjack Project #####################

# Setup

import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
  """Returns a random card from the deck, but the card is not removed from the deck."""
  card = random.choice(cards)
  return card

def get_score(hand):
  """Returns the sum of all the cards in a hand."""
  score = sum(hand)  
  return score

def start_deal():
  """Two cards are dealed to the player and the dealer to start the game.
  Both cards of the player are revealed and the score of those cards.
  For the dealers, only the first card is revealed."""
  player_hand.append(draw_card())
  dealer_hand.append(draw_card())
  player_hand.append(draw_card())
  dealer_hand.append(draw_card())

  print(f"\tYour cards: {player_hand}. Current score: {get_score(player_hand)}")
  print(f"\tDealer's first card: {dealer_hand[0]}")

def player_draw():
  """If user wishes to, a card is drawn from the deck and added to the player's hand.
  After each draw, the new hand is presented including the score.
  Afterwards, the player is presented with a new choice to draw another card.
  This process is repeated until the player stops drawing OR if the player goes over 21.
  If the player has an 11 AND goes over 21, the 11 is replaced by a 1.
  If the drawing stops, the final hand and score are presented."""
  hit_or_stand = input("Type 'y' to get another card. Type 'n' to pass.").lower()

  while hit_or_stand == 'y':
    player_hand.append(draw_card())
    print(f"\tYour cards: {player_hand}. Current score: {get_score(player_hand)}")
    print(f"\tDealer's first card: {dealer_hand[0]}")
    if get_score(player_hand) > 21 and 11 in player_hand:
      player_hand.remove(11)
      player_hand.append(1)
    elif get_score(player_hand) >= 21:
      hit_or_stand = 'n'  
    else:
      hit_or_stand = input("Type 'y' to get another card. Type 'n' to pass.").lower()
  
  print(f"\tYour final hand: {player_hand}. Final score: {get_score(player_hand)}")

def dealer_draw():
  """The dealer will continue to draw cards until it reaches a score of 17 or higher.
  If that point is reached, the drawing ends and the final hand and score are presented."""
  dealer_hit = True

  while dealer_hit:
    if get_score(dealer_hand) < 17:
      dealer_hand.append(draw_card())
    elif get_score(dealer_hand) > 21 and 11 in dealer_hand:
      for index, item in enumerate(dealer_hand):
        if item == 11:
          dealer_hand[index] = 1
          print("The dealer replaced an 11 by a 1, because he went over 21")
        else:
          None
    else:
      dealer_hit = False
      print(f"\tDealer's final hand: {dealer_hand}. Final score: {get_score(dealer_hand)}")

def det_winner():
  """Compares the score of the player and the dealer and determines who has won."""
  if get_score(player_hand) > 21:
    print("You went over! You lose!")
  elif get_score(dealer_hand) > 21 and get_score(player_hand) <= 21:
    print("Dealer went over! You win!")
  elif get_score(player_hand) == get_score(dealer_hand):
    print("Draw!")
  elif get_score(player_hand) > get_score(dealer_hand):
    print("You win!")
  elif get_score(dealer_hand) > get_score(player_hand):
    print("You lose!")

# GAME

game = input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no.")

if game == 'y':
  new_game = True

else:
  new_game = False
  print("Hope to see you again!")

while new_game:
  clear()
  player_hand = []
  dealer_hand = []
  print(logo)
  start_deal()
  player_draw()
  dealer_draw()
  det_winner()
  
  game = input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no.")

  if game == 'y':
    new_game = True

  else:
    new_game = False
    print("Hope to see you again!")
