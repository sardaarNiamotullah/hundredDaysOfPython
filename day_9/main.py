from os import system
from logo import logo

def invalidBidChecker(bidAmount):

    invalidInput = True
    while invalidInput:
        try:
            bidAmount = int(bidAmount)
        except:
            bidAmount = input("Please enter a valid bid amount 10, 23, 302 ...: ")
        else:
            return bidAmount

def invalidinputChecker(otherBidder):

    invalidInput = True
    while invalidInput:
        if otherBidder == 'yes' or otherBidder == 'no':
            return otherBidder
        else:
            otherBidder = input("Please insert a valid input. ").lower()

print(logo)

print("Welcome to the secret auction program.")

bidDict = {}
endAuction = True

while endAuction:
    name = input("What's your name?: ")
    bidAmount = input("What's your bid?: $")
    bidAmount = invalidBidChecker(bidAmount)

    bidDict[name] = bidAmount

    otherBidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    otherBidder = invalidinputChecker(otherBidder)

    system('clear')
    print(logo)

    if otherBidder == 'yes':
        continue
    else:
        break

winnerSbid = 0
winner = ""

for _ in bidDict:
    if bidDict[_] > winnerSbid:
        winnerSbid = bidDict[_]
        winner = _

print(f"The winner is {winner} with a bid of ${winnerSbid}")

