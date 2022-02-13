#Author Kelvin Keller
import turtle
turtle.bgcolor("skyblue")
turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")

pen.up()
pen.setpos(100,100)
pen.down()
length = 100

#square 
pen.fillcolor("magenta")
pen.begin_fill()

for i in range(4):
    pen.forward(length)
    pen.left(90)

pen.end_fill()

pen.up()
pen.setpos(-200,100)
pen.down()

#draw triangle
for i in range(3):
    pen.forward(length)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-200,-100)
pen.down()

#draw upside down triangle
pen.begin_fill()


turtle.done()