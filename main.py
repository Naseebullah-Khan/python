import random
from os import system as clear
from hangman_word import word_list
from hangman_art import logo, stages

lives = 6

print(logo)

chosen_word = random.choice(word_list)


display = []
for _ in range(len(chosen_word)):
  display.append("_")

playing = True
while playing:
  
  guess = input("Guess a Letter: ").lower()

  clear("cls")
  
  for letter in display:
    if letter == guess:
      print(f"You've already guessed {guess}.")
      break
    
  for x in range(len(chosen_word)):
    if chosen_word[x] == guess:
      display[x] = guess

  print(f"{''.join(display)}")
  
  if guess not in display:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      playing = False
      print("You lose.")
    print(stages[lives])

  if "_" not in display:
    playing = False
    print("You Win!")