"""This module is a fun take on using Turtle graphics. Outcome of the program is based on the classic story of
The Tortoise and the Hare - slow and steady wins the race."""

# import turtle, random, and time modules for use.
import turtle
import random
import time

# create an empty list by the name of 'turtles'. create two variables that will be used for the background screen's width and height.
turtles = list()
hare = turtle.Turtle()
screen_size_width = 1290
screen_size_height = 720

# create variable known as hare to create a turtle object that will have attributes assigned to it later.
hare = turtle.Turtle()

# Lastly, create three more variables signifying the left and right edges of the screen as well as dead center.
screen_left = - (screen_size_width // 2)
screen_middle = 0
screen_right = screen_size_width // 2


def turtle_setup():
    """This function is used to create five turtles. Two lists are then used to assign starting coordinates and colors
    to each respective turtle. The hare is also created and given specific attributes within this function."""
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(screen_size_width, screen_size_height)
    screen.bgpic('pavement.gif')

    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ['blue', 'red', 'pink', 'yellow', 'green']

    for i in range (len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)

    rabbit = "thehare.gif"
    hare_ycor = -125
    screen.addshape(rabbit)
    hare.shape(rabbit)
    hare.penup()
    hare.setpos(startline, hare_ycor)
    hare.pencolor('white')
    hare.pendown()

def race():
    """This function is used to start and end the race itself. Movement for the turtles and hare is determined by picking random integers between 
    specified parameters. The parameters set do not allow the hare to ever win! """
    global turtles
    winner = False
    finishline = screen_right - 105
    turtle_move_max = 6
    turtle_move_min = 2
    hare_move_max = 12
    hare_move_min = 8

    # have turtles take turns moving forward until the finish line has been crossed. Once the finish line is crossed, print the winner's color
    # to the screen. The hare will move forward until they are 100 pixels in front of dead center, at which point the hare will slow to
    # allow the turtles to surpass and win.
    while not winner:
        for current_turtle in turtles:
            move = random.randint(turtle_move_min, turtle_move_max)
            current_turtle.forward(move)
            xcor = current_turtle.xcor()
            if (xcor >= finishline):
                winner = True
                winner_color = current_turtle.color()
                print('The winner is', winner_color[0], '!')
        if hare.xcor() >= screen_middle - 100:
            move = .5
        else:
            move = random.randint(hare_move_min, hare_move_max)
        hare.forward(move)

# program is only ran if it is run as the main program. do not want the program to run if this is ever to be imported by another user
if __name__ == '__main__':
    turtle_setup()
    race()
    time.sleep(5)