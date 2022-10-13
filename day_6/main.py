#to play the game go to this link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#except running it to your local terminal.


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        while front_is_clear():
            move()
            if right_is_clear():
                turn_right()
    else:
        if front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
        else:
            turn_left()