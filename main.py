import random
from os import system as clear
from art import logo, vs
from game_data import data


def format_data(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(guess, account_a_follower_count, account_b_follower_count):
  if account_a_follower_count > account_b_follower_count:
    return guess == "a"
  else:
    return guess == "b"


print(logo)

count = 0

account_a = random.choice(data)
account_b = random.choice(data)

while True:

  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against b: {format_data(account_b)}")

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  account_a_follower_count = account_a["follower_count"]
  account_b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, account_a_follower_count,
                            account_a_follower_count)

  clear("cls")
  print(logo)

  if is_correct:
    count += 1
    print(f"You're right! Current score: {count}")
  else:
    print(f"Sorry, You're wrong, final score: {count}")
    break
