from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


def boarder(width, height, color, bg_color):
    tr = Turtle(visible=False)
    tr.pencolor(color)
    tr.fillcolor(bg_color)
    tr.penup()
    tr.pensize(5)
    tr.goto(-width/2+5, height / 2 - 30)
    x = width-20
    y = height-45
    tr.pendown()
    tr.begin_fill()
    for _ in range(4):
        where = x if _%2==0 else y
        tr.forward(where)
        tr.right(90)
    tr.end_fill()
    tr.penup()


screen = Screen()
screen.title("Snake Game")
screen.setup(600, 600)


new_game = True

while new_game:
    screen.tracer(0)
    screen.listen()
    screen.bgcolor("grey20")
    boarder(600, 600, "grey20", "DarkSeaGreen4")
    screen.update()

    snake = Snake()

    for key in snake.change_directions():
        screen.onkey(key=key, fun=snake.change_directions()[key])

    new_food = Food()
    score_board = ScoreBoard()

    game_is_on = True
    while game_is_on:
        # sleep_time = 0.08 if score_board.score < 10 else 0.05 if score_board.score < 20 else 0.03
        sleep_time = 0.8
        time.sleep(sleep_time)
        snake.move()
        new_food.check_food_eaten(snake)
        if new_food.eaten:
            new_food.move_food()
            score_board.show_score(1)
            snake.add_segment()
        screen.update()
        game_is_on = not (snake.check_wall_collision()) and not (snake.check_tail_collision())

    score_board.game_over()
    if screen.textinput("New game?", "Y/N: ").lower() == "y":
        screen.clear()
    else:
        new_game = False

screen.exitonclick()

