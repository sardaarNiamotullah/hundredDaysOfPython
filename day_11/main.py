from random import choice, randint
from os import system
from art import logo

deck = [1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10, 11]

playAgain = True

def score(currentDeck):
    point = 0
    for _ in currentDeck:
        point += _
    return point

while playAgain:
    system('clear')
    print(logo)
    playerHand = []
    comHand = []

    for _ in range(2):
        playerHand.append(choice(deck))
        comHand.append(choice(deck))

    comHit = randint(0, 3)
    for _ in range(comHit):
        comHand.append(choice(deck))
        comPoint = score(comHand)
        if comPoint > 21:
            break


    comPoint = score(comHand)


    def inputchecker(hitValue):
        invalid = True
        while invalid:
            if (hitValue == 'hit' or hitValue == 'stand'):
                return hitValue
            else:
                hitValue = input("Please enter a valid input to continue: ").lower()

    def playAgainChecker(play):
        invalid = True
        while invalid:
            if (play == 'y' or play == 'n'):
                return play
            else:
                play = input("Please enter a valid input to continue: ").lower()

    def gameChecker():

        playerPoint = score(playerHand)

        if (playerPoint > 21 and comPoint > 21):
            print("You and computer both went over.")
            print(f"Your final hand: {playerHand}, final score: {playerPoint}")
            print(f"Computer's final hand: {comHand}, final score: {comPoint}\nDRAW!")
            return False
        elif (playerPoint > 21):
            print("You went over!")
            print(f"Your final hand: {playerHand}, final score: {playerPoint}")
            print(f"Computer's final hand: {comHand}, final score: {comPoint}\nYou lose.")
            return False
        else:
            return True

    playerHit = True

    while playerHit:
        playerPoint = 0
        for _ in playerHand:
            playerPoint += _
        print(f"Your cards: {playerHand}, current score: {playerPoint}")
        print(f"Computer's first card: [{comHand[0]}]")
        hitValue = input("Type 'hit' to get another card, type 'stand' to pass: ").lower()
        hitValue = inputchecker(hitValue)

        if (hitValue == 'hit'):
            newCard = choice(deck)
            currentPoint = score(playerHand)
            if (newCard == 11 and (currentPoint+11) > 21):
                playerHand.append(1)
            else:
                playerHand.append(newCard)

            playerHit = gameChecker()
        else:
            playerPoint = 0
            for _ in playerHand:
                playerPoint += _
            if (comPoint > 21):
                print("The computer went over!")
                print(f"Your final hand: {playerHand}, final score: {playerPoint}")
                print(f"Computer's final hand: {comHand}, final score: {comPoint}\nYou Won.")
            elif (playerPoint > comPoint):
                print(f"Your final hand: {playerHand}, final score: {playerPoint}")
                print(f"Computer's final hand: {comHand}, final score: {comPoint}\nYou Won.")
            elif (playerPoint == comPoint):
                print(f"Your final hand: {playerHand}, final score: {playerPoint}")
                print(f"Computer's final hand: {comHand}, final score: {comPoint}\nDRAW!")
            else:
                print(f"Your final hand: {playerHand}, final score: {playerPoint}")
                print(f"Computer's final hand: {comHand}, final score: {comPoint}\nYou Lose.")

            playerHit = False

        if not playerHit:
            play = input("To play agian type 'y', to exit type 'n': ").lower()
            play = playAgainChecker(play)
            if (play != 'y'):
                playAgain = False