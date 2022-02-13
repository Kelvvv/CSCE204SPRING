#Author Kelvin Keller 
import turtle

turtle.bgcolor("skyblue")
turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")
pen.fillcolor("red")

#U-Haul Widths
uhaulWidth = 200
uhaulBoxWidth = uhaulWidth * 3/4
uhaulCabWidth = uhaulWidth - uhaulBoxWidth

#U-Haul Heights
uhaulHeight = uhaulWidth * 5/8
uhaulBoxHeight = uhaulHeight * 2/3
uhaulCabHeight = uhaulBoxHeight * 2/3
uhaulWheelRadius = (uhaulHeight - uhaulBoxHeight) /2

#Uhaul Box
pen.up()
pen.setpos(-uhaulWidth/2,-uhaulHeight/2 + uhaulWheelRadius * 2)
pen.down()
pen.begin_fill()
pen.forward(uhaulWidth)
pen.left(90)
pen.forward(uhaulCabHeight)
pen.left(90)
pen.forward(uhaulCabWidth)
pen.right(90)
pen.forward(uhaulBoxHeight - uhaulCabHeight)
pen.left(90)
pen.forward(uhaulBoxWidth)
pen.left(90)
pen.forward(uhaulBoxHeight)
pen.end_fill()

#left wheel
pen.up()
pen.setpos(-uhaulWidth/2 + uhaulWidth * 1/3 - uhaulWheelRadius, -uhaulHeight/2 + uhaulWheelRadius)
pen.down()
pen.fill_color("black")
pen.begin_fill()
pen.circle(uhaulWheelRadius)
pen.end_fill()


#Right wheel
pen.up()
pen.setpos(-uhaulWidth/2 + uhaulWidth * 2/3 -uhaulWheelRadius, -uhaulHeight/2 + uhaulWheelRadius)
pen.down()
pen.fill_color("black")
pen.begin_fill()
pen.circle(uhaulWheelRadius)
pen.end_fill()

turtle.done()
