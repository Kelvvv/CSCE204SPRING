#Author Kelvin Keller 
import turtle
turtle.bgcolor("black")
turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.speed(0)
pen.color("pink") #inside color is teal

hexagon = 100
insideHexagon = hexagon - 90

pen.up()
pen.setpos(0,0)
#draw hexagon
for i in range(6):
    pen.up()
    pen.fillcolor("pink")
    pen.begin_fill()
    pen.down()
    pen.forward(hexagon)
    pen.right(60)
pen.end_fill()

pen.up()
pen.setpos()



turtle.done()