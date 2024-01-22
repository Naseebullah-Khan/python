import random

attempts = 0

def easy():
  global attempts
  attempts = 10
  while attempts > 0:
    if attempts == 10:
      print(f"You have {attempts} attempts remaining to guess the number.")
    else:
      print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a Guess: "))
    if guess == number:
      print(f"you got it! The answer {number}")
      break
    elif guess > number:
      print("Too high.")
    else:
      print("Too low.")
    attempts -= 1
    if attempts == 0:
      print("You have run out of guesses, you lose.")

def hard():
  global attempts
  attempts = 5
  while attempts > 0:
    if attempts == 5:
      print(f"You have {attempts} attempts remaining to guess the number.")
    else:
      print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a Guess: "))
    if guess == number:
      print(f"you got it! The answer {number}")
      break
    elif guess > number:
      print("Too high.")
    else:
      print("Too low.")
    attempts -= 1
    if attempts == 0:
      print ("You have run out of guesses, you lose.")

print("Welcome to the Number Guessing Game!")
number = random.choice(range(101))

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "hard":
  hard()
elif difficulty == "easy":
  easy()