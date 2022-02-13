#Author Kelvin Keller 
import turtle
turtle.bgcolor("skyblue")
turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")

trunkWidth = turtle.window_width()//10
lgTri = trunkWidth *3
mdTri = lgTri * 2/3
smTri = mdTri * 2/3
starWidth = smTri /2
bottomY = - lgTri * 3/2

pen.up()
pen.setpos(-trunkWidth / 2, bottomY)
pen.down()

#draw trunk
pen.color("brown")
pen.begin_fill()
for i in range(4):
    pen.forward(trunkWidth)
    pen.left(90)
pen.end_fill()

pen.up()
pen.setpos(-lgTri/2, bottomY + trunkWidth)
pen.down()
pen.color("forest green")

#draw large triangle 
pen.begin_fill()
for i in range(3):
    pen.forward(lgTri)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-smTri/2, bottomY + trunkWidth + lgTri / 2 + mdTri / 2)
pen.down()

#draw medium triangle 
pen.begin_fill()
for i in range(3):
    pen.forward(mdTri)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-smTri/2, bottomY + trunkWidth + lgTri / 2 + mdTri / 2)
pen.down()

#draw small triangle
pen.begin_fill()
for i in range(3):
    pen.forward(smTri)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-starWidth/2, bottomY + trunkWidth + lgTri / 2 + mdTri / 2 + smTri * .8 + starWidth / 2)
pen.down()

#draw star
pen.color("gold")
pen.begin_fill()
for i in range(3):
    pen.forward(starWidth)
    pen.right(120)
    pen.end_fill()

pen.up()
pen.setpos(-starWidth/2, bottomY + trunkWidth + lgTri / 2 + mdTri / 2 + smTri * .8 + starWidth / 2)
pen.down()

#draw star
pen.color("gold")
pen.begin_fill()
for i in range(3):
    pen.forward(starWidth)
    pen.right(120)
    pen.end_fill()




turtle.done()