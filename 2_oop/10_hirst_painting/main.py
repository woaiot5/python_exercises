import random
from colorgram import extract
import turtle as t
from os import listdir


def random_image_extract(nr_clrs):
    global img
    dir_list = listdir("./images")
    images = []
    for item in dir_list:
        if ".jpg" in item:
            images.append(item)
    img = random.choice(images)
    print("Image selected\n...")
    colors_list = extract(f"./images/{img}", nr_clrs)
    print("Colors extracted")
    return colors_list


def random_color(colors_list):
    return colors_list[random.randint(0,len(colors_list) - 1)].rgb


def boarder(tr, width, height, clrs):
    tr.pencolor(random_color(clrs))
    tr.goto(-width / 2, height / 2)
    tr.pendown()
    for _ in range(2):
        tr.forward(width)
        tr.right(90)
        tr.forward(height)
        tr.right(90)
    tr.penup()


def draw_a_line(tr, nr_dots, step, rad, clrs):
    for _ in range(nr_dots):
        tr.fd(step+radius*2)
        tr.pendown()
        tr.dot(rad*2, random_color(clrs))
        tr.penup()


def next_line(tr, nr_line, rad, step_back, step_down):
    right_or_left = {
        "right": tr.right,
        "left": tr.left}
    rl = "right" if nr_line%2 == 0 else "left"

    right_or_left[rl](90)
    tr.forward(step_down + rad*2)
    right_or_left[rl](90)
    tr.bk(step_back + rad*2)


def start(tr, width, height, st_x, st_y, rad, clrs):
    tr.ht()
    tr.penup()
    tr.speed("fastest")
    boarder(tr, width, height, clrs)
    start_x = -(width / 2) - st_x / 2 - rad
    start_y = (height / 2) - st_y / 2 - rad
    tr.goto(start_x, start_y)


def draw_dots(tr, nr_l, nr_cir, st_x, st_y, rad, clrs):
    line = 1
    while line <= nr_l:
        draw_a_line(tr, nr_cir, st_x, rad, clrs)
        line += 1
        next_line(tr, line, rad, st_x, st_y)


img = ''


nr_colors = int(input("How many colors? (int): "))
colors = random_image_extract(nr_colors)

w = int(input("Screen width (int): "))
h = int(input("Screen height (int): "))
radius = int(input("Radius of each circle (int): "))
diameter = radius * 2
nr_lines = int(input(f"Number of lines (int), max {int(h/diameter)-1} lines: "))
nr_circles = int(input(f"Number of circles in line (int), max {int(w/diameter)-1} circles: "))
step_x = (w -  nr_circles*diameter)/nr_circles
step_y = (h - nr_lines*diameter)/nr_lines


t.colormode(255)
dot = t.Turtle()
screen = t.Screen()
screen.setup(width=w, height=h)
screen.title(f'Hirst painting - {img}')


start(dot, w, h, step_x, step_y, radius, colors)
draw_dots(dot, nr_lines, nr_circles, step_x, step_y, radius, colors)

screen.exitonclick()