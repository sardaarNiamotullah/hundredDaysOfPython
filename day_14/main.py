from game_data import data
from art import logo, vs
from os import system
from random import choice

dataLength = len(data)

def inputChecker(playerInput):
    invalid = True
    while invalid:
        if playerInput == 'a' or playerInput == 'b':
            return playerInput
        else:
            playerInput = input("Please enter a valid input: ").lower()
def sameComparison(a, b):
    invalid = True
    while invalid:
        if a == b:
            b = choice(data)
        else:
            return b
def inputChecker2(playerInput):
    invalid = True
    while invalid:
        if playerInput == 'y' or playerInput == 'n':
            return playerInput
        else:
            playerInput = input("Please enter a valid input: ").lower()


playAgain = True

while playAgain:
    system('clear')
    print(logo)
    currentScore = 0
    a = choice(data)
    b = choice(data)
    b = sameComparison(a, b)

    gameOver = False

    while not gameOver:
        if currentScore > 0:
            system('clear')
            print(logo)
            print(f"You are right, current score: {currentScore}.")

        print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")
        print(vs)
        print(f"Againest B: {b['name']}, {b['description']}, {b['country']}")
        playerInput = input("Who has more followers? Type 'a' or 'b': ").lower()
        playerInput = inputChecker(playerInput)

        if a['follower_count'] > b['follower_count']:
            if playerInput == 'a':
                currentScore += 1
                a = b.copy()
                b = choice(data)
                b = sameComparison(a, b)
            else:
                system('clear')
                print(logo)
                print(f"You have guessed wrong!\nGame Over. And your final score is: {currentScore}")
                break
        else:
            if playerInput == 'b':
                currentScore += 1
                a = b.copy()
                b = choice(data)
                b = sameComparison(a, b)
            else:
                system('clear')
                print(logo)
                print(f"You have guessed wrong!\nGame Over. And your final score is: {currentScore}")
                break

    playAgain = input("\nWant to play again? type 'y' or to exit type 'n': ").lower()
    playAgain = inputChecker2(playAgain)
    if playAgain == 'y':
        continue
    else:
        break
