with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    contents = letter.read()
    for name in names:
        new_name = name.strip()
        new_letter = contents.replace("[name]", new_name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as letters_to_send:
            letters_to_send.write(new_letter)
