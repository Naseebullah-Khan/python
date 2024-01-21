# # Data Types
# print("Hello"[4])
# print("123" + "456")
# # Integer
# print(123 + 456)
# print(123_456_7890)
# # Float
# print(3.14159)
# # Boolean
# print(True)
# print(False)
# num_char = len(input("What is your name? "))
# print("Your name has " + str(num_char) + " characters.")

# a = float(123)
# print(type(a))
# print(70 + float("100.5"))
# print(str(70)+str(100.5))

# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 2
# 2 ** 3

# PEMDAS
# Parentheses -> ()
# Exponents -> **
# Multiplication -> * or Division -> /
# Addition -> + or Subtraction -> -

# print(3 * (3 + 3) / 3 - 3)

print(8 / 3)
print(int(8 / 3))
print(round(8 / 3, 2))

# Floor division
print(8 // 3)
# class int
print(type(8 // 3))
# class float
print(type(8 / 3))

result = 16 / 4
result /= 2
print(result)

# f-String
score = 3
height = 1.8
isWinning = True
print("Your score is " + str(score) + ", your height is " + str(height) + ", you are winning " + str(isWinning))
# or
print(f"Your score is {score}, your height is {height}, you are winning {isWinning}")