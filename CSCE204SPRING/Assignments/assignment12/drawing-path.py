#Author Kelvin Keller
import turtle
import random

turtle.setup(1000,1000)
pen = turtle.Turtle()
turtle.bgcolor("burlywood")
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

prompt = int(turtle.numinput("Coordinates", "Enter Number of Coordinates: ", 5, 1, 10))

xs = []
ys = []

for i in range(prompt):
    promptX = int(turtle.numinput("Shapes", "Enter X 1: ", 5, -100, 100))
    xs.append(promptX)
    promptY = int(turtle.numinput("Shapes", "Enter Y 1:: ", 5, -100, 100))
    ys.append(promptY)
    for j in range(xs):
        pen.up()
        pen.setpos(xs[i], ys[i])
        pen.down()
        pen.forward()

        
    
        

        
        


turtle.done()
