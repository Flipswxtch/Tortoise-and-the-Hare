import turtle
import random

turtles = list()
hare = turtle.Turtle()

def turtle_setup():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290, 720)
    screen.bgpic('pavement.gif')

    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ['blue', 'red', 'pink', 'yellow', 'green']

    for i in range (0, len(turtle_ycor)):
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
    global turtles
    winner = False
    finishline = 540
    turtles.append(hare)

    while not winner:
        for current_turtle in turtles:
            move = random.randint(2, 6)
            if current_turtle == turtles[-1]:
                move = random.randint(8, 12)
                if hare.xcor() >= -100:
                    move = .5
                    hare.forward(move)
            if current_turtle == turtles[0:-2]:
                move
            current_turtle.forward(move)
            xcor = current_turtle.xcor()
            if (xcor >= finishline):
                winner = True
                winner_color = current_turtle.color()
                print('The winner is', winner_color[0], '!')
turtle_setup()
race()