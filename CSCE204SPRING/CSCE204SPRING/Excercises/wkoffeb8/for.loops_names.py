#Author Kelvin Keller 
import turtle
import random
turtle.bgcolor("skyblue")
turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.speed(0)
style.color("black")
style = ("Arial", 12, "normal")
turtle.colormode(255)

userName = turtle.textinput("Names", "Enter Name")
numName = int(turtle.numinput("Names", "Enter Number of Names",10, 1, 100))

pen.write(userName, font = style)

for i in range(numName):
    x = random.randint(- turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(- turtle.window_height()//2, turtle.window_height()//2)
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)
    pen.color(r,g,b)

    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.write(userName, font = style)

turtle.done()