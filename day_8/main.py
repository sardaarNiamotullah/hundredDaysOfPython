from os import system
from logo import logo

def caesarCipher(operationMode, message, shiftNumber):
    _ = 0
    if operationMode == 'encode':
        while _ < len(message):
            if (ord(message[_]) > 96) and (ord(message[_]) < 123):
                if shiftNumber + ord(message[_]) < 123:
                    message[_] = chr(ord(message[_]) + shiftNumber)
                else:
                    reverse = shiftNumber + ord(message[_]) - 122 + 96
                    message[_] = chr(reverse)
            _ += 1

        message = "".join(map(str, message))
        print(f"Here's the encoded result: {message}")
    else:
        while _ < len(message):
            if (ord(message[_]) > 96) and (ord(message[_]) < 123):
                if ord(message[_]) - shiftNumber > 96:
                    message[_] = chr(ord(message[_]) - shiftNumber)
                else:
                    reverse = ord(message[_]) - shiftNumber + 26
                    message[_] = chr(reverse)
            _ += 1

        message = "".join(map(str, message))
        print(f"Here's the decoded result: {message}")


playAgain = True

while playAgain:
    print(logo)

    operationMode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    invalidInput = True
    while invalidInput:
        if (operationMode == 'encode') or (operationMode == 'decode'):
            break
        else:
            operationMode = input("Please enter a valid input: ").lower()

    message = input("Type your message: ").lower()
    message = [*message]

    shiftNumber = input("Type the shift number: ")
    invalidInput = True
    while invalidInput:
        try:
            shiftNumber = int(shiftNumber) % 26
        except:
            shiftNumber = input("Please enter a valid input number like 1, 2, 3 ...: ")
        else:
            break

    caesarCipher(operationMode, message, shiftNumber)

    playagain = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    invalidInput = True
    while invalidInput:
        if (playagain == 'yes') or (playagain == 'no'):
            break
        else:
            playagain = input("Please enter a valid input: ").lower()

    if playagain == 'yes':
        system('clear')
        continue
    else:
        print("Goodbye!")
        break