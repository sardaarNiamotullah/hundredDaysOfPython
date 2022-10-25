from os import system
from logo import logo

def addition(firstNumber, secondNumber):
    '''Adds two number and returns the value of it.'''
    return firstNumber + secondNumber

def subtraction(firstNumber, secondNumber):
    '''subtracts the second number from the first one and returns the value of it.'''
    return firstNumber - secondNumber

def multiplication(firstNumber, secondNumber):
    '''multiplies two number and returns the value of it.'''
    return firstNumber * secondNumber

def division(firstNumber, secondNumber):
    '''divides the first number with the second number and returns the value of it.'''
    return firstNumber / secondNumber

def modulo(firstNumber, secondNumber):
    '''Returns the remainder of a division.'''
    return firstNumber % secondNumber

def power(firstNumber, secondNumber):
    return firstNumber ** secondNumber

oprationDict = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "%": modulo,
    "**": power
}

def inputChecker(number):
    validInput = False
    while not validInput:
        try:
            number = float(number)
        except:
            number = input("Please insert a valid number: ")
        else:
            return number

def operationChecker(operation):
    validInput = False
    while not validInput:
        for _ in oprationDict:
            if _ == operation:
                return operation
        operation = input("Please insert a valid operation mood: ")

def continuityChecker(sContinue):
    validInput = False
    while not validInput:
        if sContinue == 'y' or sContinue == 'n' or sContinue == 'e':
            return sContinue
        else:
            sContinue = input("Please enter a valid input: ").lower()

def calculator():
    system('clear')
    print(logo)

    result = 0
    firstNumber = input("What's the first number?: ")
    firstNumber = inputChecker(firstNumber)
    for _ in oprationDict:
        print(_)

    shouldContinue = True
    while shouldContinue:
        operation = input("Pick an operation: ")
        operation = operationChecker(operation)
        print(operation)
        nextNumber = input("What's the next number?: ")
        nextNumber = inputChecker(nextNumber)

        result = round(oprationDict[operation](firstNumber, nextNumber), 3)
        print(f"{firstNumber} {operation} {nextNumber} = {result}")

        sContinue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. Otherwise type 'e' to switch off the calculator.:\n").lower()
        sContinue = continuityChecker(sContinue)

        if sContinue == 'y':
            firstNumber = result
            continue
        elif sContinue == 'n':
            calculator()
            break
        elif sContinue == 'e':
            print("Bye Bye!!!")
            break

calculator()