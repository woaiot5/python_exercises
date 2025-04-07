import turtle as t
import random


def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


def draw_shape(turtle_obj, n, steps):
    turtle_obj.begin_fill()
    angle = 360 / n
    for _ in range(n):
        turtle_obj.forward(steps)
        turtle_obj.right(angle)
    turtle_obj.end_fill()


def mandala(turtle_obj, nr, steps):
    turtle_obj.penup()
    turtle_obj.goto(-(steps/2),200)
    turtle_obj.pendown()
    i = nr
    while i > 2:
        turtle_obj.pencolor(rand_color())
        turtle_obj.fillcolor(rand_color())
        draw_shape(turtle_obj, i, steps)
        i -= 1


def random_walk(turtle_obj, nr, steps):
    angles = [0, 90, 180, 270]
    turtle_obj.pensize(10)
    for _ in range(nr):
        turtle_obj.pencolor(rand_color())
        if abs(turtle_obj.xcor()) < ((screen.window_width() / 2) - steps - 10) and abs(turtle_obj.ycor()) < (
                (screen.window_height() / 2) - steps - 10):
            turtle_obj.right(random.choice(angles))
            turtle_obj.forward(steps)
        else:
            turtle_obj.backward(steps)


def spirograph (turtle_obj, nr, radius):
    angle = 360/nr
    for _ in range(nr):
        turtle_obj.pencolor(rand_color())
        turtle_obj.circle(radius)
        turtle_obj.setheading(turtle_obj.heading()+angle)


options = {"mandala": mandala,
           "walk": random_walk,
           "circle": spirograph}

option = input("mandala/walk/circle: ")
number = int(input("number of repetitions (int): "))
step = int(input("step/radius (int): "))

dot = t.Turtle()
screen = t.Screen()
t.colormode(255)
screen.title('GUI Practice')
screen.setup(width=500, height=500, startx=0, starty=0)

dot.ht()
dot.speed("fastest")

options[option](dot, number, step)

screen.exitonclick()