# file = open("new_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
# or
#
# with open("new_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
with open("./file.txt", mode="w") as file:
    file.write("New file is created using open method with the mode of 'W'")

with open("./file.txt") as file:
    contents = file.read()
    print(contents)

# with open("new_file.txt", mode="a") as file:
#     file.write("\nI am currently in my last year of bachelor degree.")

# with open("new_file.txt") as file:
#     contents = file.read()
#     print(contents)
