#Author Kelvin Keller 
import turtle
import random

#I ran into an error and im not too sure what it is but I feel like I was close

turtle.setup(1000,1000)
pen = turtle.Turtle()
turtle.bgcolor("black")
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
pen.color("white")
style = ("Arial", 12, "normal")
#create two empty list
starnames = []
starcolors = []
x = 0
y = random.randint
#ask the user how many stars they have (between 0 and 10)
prompt1 = int(turtle.numinput("Beautiful Stars", "Enter How Many Stars You Want: ", 1, 1, 10))
turtle.write("Beautiful Stars", font = style)
#For each star ask the user for it's name, and color using input boxes
for i in range(prompt1):
    prompt2 = turtle.textinput("Beautiful Stars", "Enter The Name of Stars You Want: ")
    starnames.append(prompt2)
    prompt3 = turtle.textinput("Beautiful Stars", "Enter The Color of Stars: ")
    starcolors.append(prompt3)
   
#draw stars
    for j in (starnames):
        turtle.up()
        turtle.setpos(x,y)
        turtle.down()
        turtle.write("{starnames}", font = style)
        for k in (starcolors):
            pen.up()
            pen.begin_fill()
            pen.setpos(x,y)
            pen.down()
            pen.forward(50)
            pen.right(72)
            pen.forward(50)
            pen.right(72)
            pen.forward(50)
            pen.right(72)
            pen.forward(50)
            pen.right(72)
            pen.forward(50)
            pen.right(72)
        pen.end_fill()

turtle.done()