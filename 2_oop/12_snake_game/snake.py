from turtle import Turtle

DISTANCE = 20

class Snake:

    def __init__(self):
        self.body = []
        self.len = 0
        self.head_index = -1
        self.create_snake()



    def new_segment(self, x, y):
        sq = Turtle(shape="square")
        sq.color("grey20")
        sq.penup()
        sq.setpos(x,y)
        self.body.insert(0, sq)
        self.len += 1
        self.head_index += 1


    def create_snake(self):
        for i in range(3):
            self.new_segment(0 - (i - 1) * DISTANCE, 0)


    def add_segment(self):
        self.new_segment(self.body[0].xcor(), self.body[0].ycor())


    def right(self):
        self.body[self.head_index].setheading(0)

    def up(self):
        self.body[self.head_index].setheading(90)

    def left(self):
        self.body[self.head_index].setheading(180)

    def down(self):
        self.body[self.head_index].setheading(270)


    def change_directions(self):
        change_direction = {"Right": self.right,
                            "Up": self.up,
                            "Left": self.left,
                            "Down": self.down,
                            "w": self.up,
                            "s": self.down,
                            "a": self.left,
                            "d": self.right}
        return change_direction

    def move(self):
        for i in range(0, self.head_index):
            self.body[i].setpos(self.body[i + 1].pos())
        self.body[self.head_index].fd(DISTANCE)


    def check_wall_collision(self):
        head = self.body[self.head_index]
        return abs(head.xcor()) > 275 or head.ycor() < -265 or head.ycor() > 255


    def check_tail_collision(self):
        head = self.body[self.head_index]
        return any(round(head.distance(segment),0) < DISTANCE for segment in self.body[:self.head_index])
