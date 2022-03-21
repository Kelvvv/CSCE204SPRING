#Author Kelvin Keller 
import turtle
import random

turtle.bgcolor("grey")
turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)

def street(x,y):
    #drawing the street
    pen.color("yellow")
    pen.up()
    pen.setpos(x,0)
    pen.down()
    pen.forward(50)
turtle.onscreenclick(street)



def cars(x,y):
    pen.color("black")
    pen.fillcolor("red")
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    pen.forward(200)
    pen.left(90)
    pen.forward(50)
    pen.forward(200)
    pen.left(90)
    pen.forward(50)
    pen.end_fill()

    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color("black")
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color("black")
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
turtle.onscreenclick(cars)

    







turtle.done()
