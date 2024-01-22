from os import system as clear
from art import logo

def add(num1, num2):
  return num1 + num2
  
def sub(num1, num2):
  return num1 - num2
  
def mul(num1, num2):
  return num1 * num2
  
def div(num1, num2):
  if num2 != 0:
    return num1 / num2

operations = {
  "+": add, 
  "-": sub, 
  "*": mul, 
  "/": div,
}

# while True:
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for operator in operations:
    print(operator)

  flag = True
  while flag:
    operator = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculate = operations[operator]
    answer = calculate(num1, num2)
    print(f"{num1} {operator} {num2} = {answer}")
    if input("Type 'y' to continue calculating with reselt or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      # clear("cls")
      flag = False
      calculator()

calculator()