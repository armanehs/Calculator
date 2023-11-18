# this project is basic calculator. we take 2 number and operator and return the result for user.

def addtion(number1, number2):
    return number1 + number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2


def subtraction(number1, number2):
    return number1 - number2


number1 = float(input("Enter the first number: "))
operator = input("Choose an operator: ")
number2 = float(input("Enter the second number: "))

if operator == "+":
    print(addtion(number1, number2))
elif operator == "*":
    print(multiplication(number1, number2))
elif operator == "/":
    print(division(number1, number2))
elif operator == "-":
    print(subtraction(number1, number2))