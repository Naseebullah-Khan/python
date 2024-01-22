from os import system as clear
from art import logo
print(logo)

bidders = {}

def max_bid(bidding):
  max_bid = 0
  winner = {}
  for bidder in bidding:
    if bidding[bidder] > max_bid:
      max_bid = bidding[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${max_bid}")

playing = True
while playing:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bidders[name] = bid
  continue_bidding = input("Is there any other bidders? Type 'yes' or 'no'.\n")
  if continue_bidding == "no":
    playing = False
    clear("cls")
    max_bid(bidders)
  else:
    clear("cls")