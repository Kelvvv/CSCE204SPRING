#Author Kelvin Keller 
import turtle
import random

turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
turtle.bgcolor("blue")


def getScene():
    textFile = []
    with open("Assignments/assignment20/scene.txt") as file:
        for line in file:
            txf = line.replace("\n","")
            textFile.append(txf)

def drawFlower(x,y,size):
    x = 0
    y = random.randrange(1,50)
    size = 50
    pen.color("green")
    pen.up()
    pen.setpos()
    pen.down(x,y)
    pen.setheading(90)
    pen.forward(20)
    pen.color("pink")
    pen.circle(size)

def drawTree(x,y,size):
    x = 0
    y = random.randrange(1,50)
    size = 20
    pen.color("brown")
    pen.up()
    pen.setpos()
    pen.begin_fill()
    pen.down(x,y)
    pen.setheading(90)
    pen.forward(20)
    pen.color("green")
    pen.circle(size)
    pen.end_fill()

scene = getScene()
flower = drawFlower()
tree = drawTree()

for i in scene:
    flower
    tree
turtle.done()