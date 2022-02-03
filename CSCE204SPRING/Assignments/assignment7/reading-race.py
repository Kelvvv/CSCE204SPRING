#Author Kelvin Keller 
import turtle
import random 
turtle.setup(1000,1000)
turtle.bgcolor("white")
pen = turtle.Turtle()
style = ("Arial", 30, "normal") #turtle.write("0%". font = style)

outerEdge = 100
innerEdge = 80


#Asking the user to enter the number of books they have read this month
booksR= int(turtle.numinput("Reading Log","How many books have you read this month:", 0, 0, 999))

#if they have read x amount of books
if booksR >= 30:
    pen.up()
    pen.color("DarkGoldenrod")
    pen.fillcolor("DarkGoldenrod")
    pen.begin_fill()
    pen.setpos(0,0)
    pen.down()
    pen.circle(outerEdge)
    pen.end_fill()

    pen.up()
    pen.color("DarkGoldenrod1")
    pen.fillcolor("DarkGoldenrod1")
    pen.begin_fill()
    pen.sety(20)
    pen.down()
    pen.circle(innerEdge)
    pen.end_fill()

    turtle.up()
    turtle.color("DarkGoldenrod")
    turtle.fillcolor("DarkGoldenrod")
    turtle.begin_fill()
    turtle.setpos(-30,80)
    turtle.down()
    turtle.write("$10", font = style)
    turtle.end_fill()

elif booksR >= 15:
    pen.up()
    pen.color("azure4")
    pen.fillcolor("azure4")
    pen.begin_fill()
    pen.setpos(0,0)
    pen.down()
    pen.circle(outerEdge)
    pen.end_fill()

    pen.up()
    pen.color("azure3")
    pen.fillcolor("azure3")
    pen.begin_fill()
    pen.sety(20)
    pen.down()
    pen.circle(innerEdge)
    pen.end_fill()

    turtle.up()
    turtle.color("azure4")
    turtle.fillcolor("azure4")
    turtle.begin_fill()
    turtle.setpos(-30,80)
    turtle.down()
    turtle.write("$5", font = style)
    turtle.end_fill()

elif booksR >= 5:
    pen.up()
    pen.color("chocolate4")
    pen.fillcolor("chocolate4")
    pen.begin_fill()
    pen.setpos(0,0)
    pen.down()
    pen.circle(outerEdge)
    pen.end_fill()

    pen.up()
    pen.color("chocolate3")
    pen.fillcolor("chocolate3")
    pen.begin_fill()
    pen.sety(20)
    pen.down()
    pen.circle(innerEdge)
    pen.end_fill()

    turtle.up()
    turtle.color("chocolate4")
    turtle.fillcolor("chocolate4")
    turtle.begin_fill()
    turtle.setpos(-30,80)
    turtle.down()
    turtle.write("$2", font = style)
    turtle.end_fill()

else:
    pen.up()
    pen.color("red")
    pen.fillcolor("red")
    pen.begin_fill()
    pen.setpos(0,0)
    pen.down()
    pen.circle(outerEdge)
    pen.end_fill()

    pen.up()
    pen.color("white")
    pen.fillcolor("white")
    pen.begin_fill()
    pen.sety(20)
    pen.down()
    pen.circle(innerEdge)
    pen.end_fill()

    turtle.up()
    turtle.color("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.setpos(-30,80)
    turtle.down()
    turtle.write("$0", font = style)
    turtle.end_fill()

    



turtle.done()
