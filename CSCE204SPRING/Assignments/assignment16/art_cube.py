#Author Kelvin Keller
import turtle
import random

turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def draw_triangle():
    width = 10
    color = turtle.textinput("Drawing", "Enter color names", 1, 1, 20)
    x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2)- width)
    y = random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2)- width)

def draw_art_cube():
    x = random.randint()
    y = random.randint()
    size = 20
    x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2)- width)
    y = random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2)- width)

turtle.done()