# to play the game go to this link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# except running it to your local terminal.

# credit: At first I have solved this problem all on my own, but there was bug in the code
# It used to go infinite loop in some special cases the first while loop fixes that and second while loop
# is more readable than before. So, The credit goes to my course instructor Dr. Angela Yu to make this code more efficient.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()