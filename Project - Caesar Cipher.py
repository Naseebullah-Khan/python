from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def repeat():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(text, shift, direction)

def caesar(text, shift, diriction):
  inner_text = ""
  if diriction == "decode":
      shift *= -1
  for letter in text:
    if letter not in alphabet:
      inner_text += letter
    else:
      position = alphabet.index(letter)
      new_position = position + shift
      inner_text += alphabet[new_position]
  print(f"The {direction}d text is {inner_text}")
  again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if again == "yes":
    repeat()
  else:
    print("Good Bye!")
  

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift = shift % 26

caesar(text, shift, direction)