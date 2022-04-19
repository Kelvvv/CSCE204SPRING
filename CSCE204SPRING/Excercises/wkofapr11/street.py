from house import House
import turtle
turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

myHouse = House("1 A Street", 0, 0, 50, "medium aquamarine", "hot pink", True, True, 3)
myHouse.draw(pen) 

turtle.done()
