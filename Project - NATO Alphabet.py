from pandas import DataFrame, read_csv

# TODO 1. Create a dictionary in this format:
file = read_csv("./nato_phonetic_alphabet.csv")
new_dict = {row.values[0]: row.values[1] for (index, row) in file.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a Word: ").upper()
char_list = [new_dict.get(letter) for letter in word]
print(char_list)