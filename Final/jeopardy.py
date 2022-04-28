#Author Kelvin Keller
from question import Question
import turtle
turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
turtle.bgcolor("white")
style = ("Courier", 10, "bold")

#Will read in the file questions.txt and return a list of question objects.  A sample qustions.txt is attached.  I'd prefer if you made your own to make it fun :)
def getQuestions():
    questiion = []
    textfile = "Final/questions.txt" #get it to return a list 
    with open(textfile) as file:
        for line in textfile:
            data = line.split(" : ")
            thequestion = data[0].strip()
            theanswer  = data[1].strip()
            userscurrentguess = data[2].strip()
            wongame = data[3].strip()
            questiion.append(Question(thequestion, theanswer,userscurrentguess,wongame))
    return questiion
def display_Questions(question):
    turtle.write(f"{question}") #displays the question

def display_Answer(question):
    turtle.write(question)    #Will display what the user has currently guessed, this will initially be all underscores


#gameboard
turtle.write(getQuestions, font = style)
turtle.onscreenclick("")


interface = int(turtle.textinput("Jeopardy", "Enter Letter"))

turtle.done()