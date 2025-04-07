import random
import colorgram
import turtle as t


def boarder(tr,size,w,h):
    tr.pencolor(colors[random.randint(0,9)].rgb)
    tr.goto(-w / 2, h/2)
    tr.pendown()
    tr.pensize(size)
    for _ in range(2):
        tr.forward(w)
        tr.right(90)
        tr.forward(h)
        tr.right(90)
    tr.pensize(1)
    tr.penup()
    tr.goto(0,0)

def draw_a_line(tr, nr_dots, step, rad, colors_list):
    for _ in range(nr_dots):
        tr.fd(step+radius*2)
        tr.pendown()
        tr.begin_fill()
        color = colors_list[random.randint(0,9)].rgb
        dot.pencolor(color)
        dot.fillcolor(color)
        tr.circle(rad)
        tr.end_fill()
        tr.penup()

def next_line(tr, nr_line, diameter, step_x, step_down):
    if nr_line%2 == 0:
        tr.right(90)
        tr.forward(step_down)
        tr.right(90)
        tr.bk(step_x+diameter)
    else:
        tr.left(90)
        tr.forward(step_down+diameter*2)
        tr.left(90)
        tr.bk(step_x+diameter)

images = ["1","2","3","4","5"]
colors = colorgram.extract(f"{random.choice(images)}.jpg", 10)


w = int(input("Screen width (int): "))
h = int(input("Screen height (int): "))
radius = int(input("Radius of each circle (int): "))
diameter = radius * 2
nr_lines = int(input(f"Number of lines (int), max {int(h/diameter)-1} lines: "))
nr_circles = int(input(f"Number of circles in line (int), max {int(w/diameter)-1} circles: "))


t.colormode(255)
screen = t.Screen()
screen.setup(width=w, height=h)
screen.title('Hirst painting')

dot = t.Turtle()
dot.ht()
dot.penup()
dot.speed("fastest")
# boarder(dot, 1, w, h)


step_x = (screen.window_width() -  nr_circles*diameter)/nr_circles
step_y = (screen.window_height() - nr_lines*diameter)/nr_lines

start_x = -(w / 2) - step_x/2 - radius
start_y = (h / 2) - (step_y/2+diameter)

dot.goto(start_x, start_y)

line = 1
while line <= nr_lines:
    draw_a_line(dot, nr_circles, step_x, radius, colors)
    line +=1
    next_line(dot, line, diameter, step_x, step_y)

screen.exitonclick()