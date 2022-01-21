#Author Kelvin Keller 
import turtle
import random 
turtle.setup(1000,1000)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.pensize(10)
pen.color("black")
pen.up()



#draw wheels
pen.setpos(200, -300)
pen.pendown()
pen.fillcolor("cyan2")
pen.begin_fill()
pen.circle(80)
pen.end_fill()

#other wheel
pen.up()
pen.setpos(-200, -300)
pen.down()
pen.color("black")
pen.fillcolor("cyan2")
pen.begin_fill()
pen.circle(80)
pen.end_fill()

#bars 
pen.up()
pen.setpos(-200, -200)
pen.down()
pen.forward(400)

pen.up()
pen.setpos(0,-200)
pen.down()
pen.setheading(90)
pen.forward(200)

pen.setheading(0)
pen.forward(150)

pen.setheading(90)
pen.forward(50)
pen.setheading(180)
pen.forward(20)

pen.up()
pen.setpos(0,-200)
pen.down()
pen.setheading(180)
pen.forward(150)
pen.setheading(70)




pen.penup()

turtle.done()