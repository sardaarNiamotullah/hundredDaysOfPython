from os import system
from art import logo
from random import randint

def inputChecker(difficultyLevel):
    validInput = False
    while not validInput:
        if (difficultyLevel == 'easy' or difficultyLevel == 'hard'):
            return difficultyLevel
        else:
            difficultyLevel = input("Please enter a vaild input to continue: ")
def inputChecker3(playAgain):
    validInput = False
    while not validInput:
        if (playAgain == 'y' or playAgain == 'n'):
            return playAgain
        else:
            playAgain = input("Please enter a vaild input to continue: ")

playAgain = True

while playAgain:
    system('clear')
    print(logo)
    print("Welcome to the Number Guessing Game!")

    difficultyLevel = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    print("Let's think of a number between 1 to 100.\n")
    difficultyLevel = inputChecker(difficultyLevel)
    theNumber = randint(1, 100)

    if (difficultyLevel == 'hard'):
        print("You have 5 guesses to figure out the number.")
        life = 5
        for _ in range(5):
            guess = int(input("Enter a number: "))
            if (guess > theNumber):
                print("The number is lower than you think.\n")
                life -= 1
            elif (guess < theNumber):
                print("The number is higher than you think.\n")
                life -= 1
            else:
                print("You have guessed right!\n\nYou won the game.\n")
                break

            if life == 1:
                print("You have only 1 guess left.")
            elif life == 0:
                print("Game Over!")
                print(f"The number is: {theNumber}\n")
                break
            else:
                print(f"You have {life} guesses left.")
    else:
        print("You have 10 guesses to figure out the number.")
        life = 10
        for _ in range(10):
            guess = int(input("Enter a number: "))
            if (guess > theNumber):
                print("The number is lower than you think.\n")
                life -= 1
            elif (guess < theNumber):
                print("The number is higher than you think.\n")
                life -= 1
            else:
                print("You have guessed right!\n\nYou won the game.\n")
                break

            if life == 1:
                print("You have only 1 guess left.")
            elif life == 0:
                print("Game Over!")
                print(f"The number is: {theNumber}\n")
                break
            else:
                print(f"You have {life} guesses left.")

    playAgain = input("Type 'y' to play again, or type 'n' to exit the game. ").lower()
    playAgain = inputChecker3(playAgain)

    if (playAgain == 'y'):
        continue
    else:
        break