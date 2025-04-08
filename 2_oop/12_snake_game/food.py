from turtle import Turtle
from random import randint

class Food:
    def __init__(self):
        self.food = Turtle(shape="square")
        self.food.penup()
        self.food.shapesize(0.7)
        self.food.color("grey20")
        self.place_food()
        self.eaten = False

    def place_food(self):
        self.food.setpos(randint(-27, 24) * 10, randint(-27, 25) * 10)

    def check_food_eaten(self, snake):
        if self.food.distance(snake.body[snake.head_index].pos()) < 15:
            self.eaten = True
        return self.eaten

    def move_food(self):
        self.food.clear()
        self.place_food()
        self.eaten = False