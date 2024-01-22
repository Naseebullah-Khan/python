from os import system as clear
import random
from art import logo

def drawn():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  choice = random.choice(cards)
  return choice

def add(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user, computer):
  if user > 21 and computer > 21:
    return "You went over. You lose."
  if user == computer:
    return "Draw."
  elif computer == 0:
    return "Lose, opponent has Blackjack"
  elif user == 0:
    return "Win with a Blackjack"
  elif computer > 21:
    return "Opponent went over, You win."
  elif user > 21:
    return "You went over,You lose."
  elif user > computer:
    return "You win."
  else:
    return "You lose."

def blackjack():
  
  print(logo)
  
  dealer = []
  user = []
  game_end = False
  
  for _ in range(2):
    dealer.append(drawn())
    user.append(drawn())
  
  while not game_end:
    user_score = add(user)
    computer_score = add(dealer)
    print(f"Your cards: {user}")
    print(f"computer's first card: {dealer[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_end = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user.append(drawn())
      else:
        game_end = True
  
  while computer_score != 0 and computer_score < 17:
    dealer.append(drawn())
    computer_score = add(dealer)
  
  print(f"Your final hand: {user}, final score: {user_score}")
  print(f"computer's final hand: {dealer}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear("cls")
  blackjack()