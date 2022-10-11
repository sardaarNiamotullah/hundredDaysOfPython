import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

print("Welcome to Rock Paper Scissors game!")
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 or Scissors.")

infinite = True
while infinite:
    you = input()

    if len(you) == 1:
        you = ord(you)
        if you > 50 or you < 48:
            print("Please enter a valid number.")
        else:
            you = int(chr(you))
            break
    else:
        print("Please enter a valid number.")

you = rps[you]
computer = random.choice(rps)

print("You choose...")
print(you)
print("Computer chooses...")
print(computer)

if computer == you:
    print("It's a draw!")
elif you == scissors and computer == paper:
    print("You won!")
elif computer == scissors and you == paper:
    print("You lose!")
elif computer == scissors and you == rock:
    print("You won!")
elif you == scissors and computer == rock:
    print("You lose!")
elif you == rock and computer == paper:
    print("You lose!")
elif you == paper and computer == rock:
    print("You won!")
