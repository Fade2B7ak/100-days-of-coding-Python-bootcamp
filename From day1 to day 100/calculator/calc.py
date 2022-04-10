from art import logo

#add
from turtle import showturtle


def add(n1, n2):
  return n1 + n2

#subtact
def subtract(n1, n2):
  return n1 - n2

#devide
def divide(n1, n2):
  return n1 / n2

#multiply
def multiply(n1, n2):
  return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,

}
def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  for symbol in operations:
      print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation from the line above:")
    num2 = float(input("What is the second number?: "))
    calculation_function = operations[operation_symbol]
    result = calculation_function(num1, num2)

    print(f'{num1} {operation_symbol} {num2} = {result}')

    if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:") == "y":
      num1 = result
      operation_symbol = input("Pick another operation:")
      num3 = float(input("What is the next number?: "))
      calculation_function = operations[operation_symbol]
      result2 = calculation_function(result, num3)
      print(f"{result} {operation_symbol} {num3} = {result2}")
    else:
      should_continue = False
      calculator()

calculator()