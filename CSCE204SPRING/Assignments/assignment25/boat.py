#Author Kelvin Keller
class Boat:
    def __init__(self,x,y,height): #The constructor will take the following information:self, x, y, height, color
        self.x = x
        self.y = y
        self.height = height

        x = random.randint(-int(turtle.window_width()/2, int(turtle.window_height()/2)))
        y = random.randint(-int(turtle.window_width()/2, int(turtle.window_height()/2)))
        height = 100

    def draw(self,pen): #You will then have a method for drawing the boat: draw(self, pen)
        #draw boat 
        pen.up()
        pen.setpos(self.x,self.y) #x, y -> is where you will draw the boat (approximately the middle of the boat)
        pen.fillcolor("red")
        pen.down()
    
    def draw_frame(self, pen, x, y, width):
        #draw frame
        pen.up()
        pen.setpos(self.x,self.y)
        pen.down()
        pen.forward(100)
        pen.left(35)
        pen.forward(100)
        pen.left(35)
        pen.forward(100)
        pen.left(35)
        pen.forward(100)
        pen.left(35)


    def draw_pole(self, pen, x, y, width):
        #draw pole
        pen.up()
        pen.setpos(self.x,self.y)
        pen.down()
        pen.setheading(90)
        pen.forward(20)
    
    def draw_flag(self, pen, x, w, height):
    #draw flag
       pen.forward(20)
       pen.left(30)
       pen.forward(20)
       pen.left(30)
       pen.forward(20)
       

