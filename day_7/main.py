import random
from os import system
from hangmanDB import wordDB
from hangmanArt import logo, hangmanState

print(logo)

life = 6
state = 0
gameOver = False

refWord = random.choice(wordDB)
refWordSorted = "".join(sorted(refWord))
refWordSorted = [*refWordSorted]
refWordSortedUnique = refWordSorted[:]

i = 0
while i < (len(refWordSortedUnique) - 1):

    if refWordSortedUnique[i] == refWordSortedUnique[i + 1]:
        refWordSortedUnique.remove(refWordSortedUnique[i + 1])
        continue
    i += 1

userWord = []
dashed = []
for _ in refWord:
    dashed.append("_ ")

while not gameOver:

    print(hangmanState[state])

    if life == 0:
        print("\nGame Over!")
        print(f"The answer is: {refWord}")
        break

    userLetter = input("Guess a letter: ")
    loopContinue = False
    guessRight = False
    system('clear')

    i = 0

    while i < len(dashed):
        if userLetter == refWord[i]:
            dashed[i] = userLetter + " "
        i += 1

    print("".join(map(str, dashed)))

    for _ in userWord:
        if _ == userLetter:
            print(f"You have already guessed {userLetter}.")
            loopContinue = True
            break

    if loopContinue:
        continue

    for _ in refWord:
        if _ == userLetter:
            guessRight = True
            print(f"You have guessed right letter!.")
            break

    if guessRight:
        userWord.append(userLetter)
        userWord = "".join(map(str, userWord))
        userWord = "".join(sorted(userWord))
        userWord = [*userWord]

        if userWord == refWordSortedUnique:
            print("\nYou won!")
            break
    else:
        life -= 1
        state += 1
        print(f"You guessed {userLetter}, that's not in the word. You lose a life!")
        continue