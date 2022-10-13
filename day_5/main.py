import random

print("Welcome to the password generator!")
print("How many letters would you like in your password?")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

infinite = True

while infinite:
    charCount = input()
    forChecker = True

    for letter in charCount:
        if ord(letter) < 47 or ord(letter) > 58:
            print("Please enter a valid number.")
            forChecker = False
            break

    if forChecker:
        if int(charCount) < 6:
            print("Your password should be at least 6 characters long.")
        else:
            charCount = int(charCount)
            break

print("How many special characters would like to be in your password?")

while infinite:
    symbol = input()
    forChecker = True

    for letter in symbol:
        if ord(letter) < 47 or ord(letter) > 58:
            print("Please enter a valid number.")
            forChecker = False
            break

    if forChecker:
        if int(symbol) > charCount:
            print("Number of special characters can't be bigger than your whole password!")
        else:
            symbol = int(symbol)
            break


print("How many numbers would like to be in your password?")

while infinite:
    number = input()
    forChecker = True

    for letter in number:
        if ord(letter) < 47 or ord(letter) > 58:
            print("Please enter a valid number.")
            forChecker = False
            break

    if forChecker:
        if int(number) + symbol > charCount:
            print("Addition of number and special character can't be bigger than your whole password!")
        else:
            number = int(number)
            break

letter = charCount - number - symbol

password = []

for _ in range(0, number):
    password.append(random.randint(0, 9))

for _ in range(0, symbol):
    password.append(random.choice(symbols))

for _ in range(0, letter):
    password.append(random.choice(letters))

random.shuffle(password)
password = "".join(map(str, password))

print(f"Here is your password: {password}")