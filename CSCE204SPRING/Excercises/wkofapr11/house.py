class House: 
    def __init__(self, address, x, y, width, buildingcolor, roofcolor, chimney, doubledoors, numwindows):
        self.address = address
        self.x = x 
        self.y = y
        self.width = width
        self.buildingcolor = buildingcolor
        self.roofcolor = roofcolor
        self.chimney = chimney
        self.doubledoors = doubledoors
        self.numwindows = numwindows
        self.style =  ("Arial", int(width /4), "bold")

    def draw(self, pen):
        pen.up()
        pen.setpos(self.x - self.width/2, self.y - self.width/2)
        pen.down()
        pen.fillcolor(self.buildingcolor)

        pen.begin_fill():
        for i in range(4):
            pen.forward(self.width)
            pen.left(90)
        pen.endfill():

        roofwidth = self.width * 1.2
        pen.up()
        pen.setpos(self.x - roofwidth/2, self.y + self.width/2)
        pen.down()
        pen.fillcolor(roofcolor)
        pen.begin_fill()
        for i in range(3):
            pen.forward(roofwidth)
            pen.left(120)
        pen.end_fill()

        if self.chimney:
            chimneywidth = self.width *.2
            chimneyheight = chimneywidth *.3
            pen.up()
            pen.setpos(self.x -self.width * .4, self.y + self.width * .7)
            pen.down()
            pen.fillcolor(self.buildingcolor)
            pen.begin_fill()
            for i in range(4):
                if i % 2 == 0:
                    pen.forward(chimneywidth)
                else:
                    pen.forward(chimneyheight)
                pen.left(90)
            pen.end_fill()

    roofwidth = self.width * 1.2
    pen.up()
    pen.setpos(self.x - roofwidth/2, self.y + self.width/2)
    pen.down()
    pen.fillcolor()
    for i in range(3):
        pen.forward(roofwidth)
        pen.left(120)
    pen.end_fill()