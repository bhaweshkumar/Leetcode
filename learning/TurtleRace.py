import turtle
import random

turtles = list()


def setup():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290, 720)
    # screen.bgpic('pavement.gif')

    turtle_ycor = [-100, -50, 0, 50, 100]
    turtle_color = ['blue', 'red', 'purple', 'brown', 'pink']

    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.pensize(5)
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)


def draw_finish_line():
    line_turtle = turtle.Turtle()
    line_turtle.shape('circle')
    line_turtle.penup()
    line_turtle.pensize(5)
    line_turtle.setpos(555, 200)
    line_turtle.pendown()
    line_turtle.setpos(555, -200)


def race():
    global turtles
    winner = False
    finish_line = 550

    while not winner:
        for current_turtle in turtles:
            move = random.randint(0, 10)
            current_turtle.forward(move)

            xcor = current_turtle.xcor()
            if xcor >= finish_line:
                winner = True
                winner_color = current_turtle.color()
                print('The winner is', winner_color[0])


setup()
draw_finish_line()
race()
turtle.mainloop()
