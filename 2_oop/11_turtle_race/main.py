from turtle import Turtle, Screen
from random import randint


def prepare_turtles(colors_list, w, h):
    new_turtles = []
    for i in range(0, len(colors_list)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors_list[i])
        new_turtle.shapesize(2)
        new_turtle.penup()
        new_turtle.setpos(-w / 2 + 30, h / 2 - 100 - i * 100)
        new_turtles.append(new_turtle)
    return new_turtles


def draw_line_height(turtle, color, size):
    turtle.pencolor(color)
    turtle.pensize(size)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(height)
    turtle.penup()


def draw_finish_line(start_color, finish_color):
    finish_line = Turtle(visible=False)
    finish_line.ht()
    finish_line.penup()
    finish_line.speed("fastest")
    x = width / 2 - 50
    y = height / 2
    finish_line.goto(x, y)
    draw_line_height(finish_line, finish_color, 5)
    x = -width / 2 + 50
    finish_line.goto(x, y)
    draw_line_height(finish_line, start_color, 2)


def random_forward(turtle):
    turtle.forward(randint(5,25))


def turtles_run(all_turtles):
    global winner
    max_x = all_turtles[0].xcor()

    while max_x < width / 2 - 60:
        for i in range(0, len(colors)):
            random_forward(all_turtles[i])
            if all_turtles[i].xcor() > max_x:
                max_x = all_turtles[i].xcor()
                winner = all_turtles[i].pencolor()
            elif all_turtles[i].xcor() == max_x:
                winner += f" and {all_turtles[i].color()[0]}"


screen = Screen()
width = 700
colors = ["red", "green", "blue"]
height = len(colors)*100+100
screen.setup(width=width, height=height)
score = 0
games_played = 0
game_on = True


while game_on:
    screen.title(f"Turtle Race! Your score: {score}/{games_played}")
    draw_finish_line("grey", "orange")
    turtles = prepare_turtles(colors,width,height)

    my_bet = screen.textinput("Bet", f"Bet on a turtle!\n{"/".join(colors)}:")

    winner = ''
    turtles_run(turtles)


    if my_bet.lower() in winner:
        result = "right"
        score += 1
    else:
        result = "wrong"

    play_again = screen.textinput(f"You were {result}! {winner.capitalize()} won!", "Play again? Y/N: ")
    if play_again.lower() != "y":
        game_on = False

    games_played+=1
    screen.clear()

screen.bye()