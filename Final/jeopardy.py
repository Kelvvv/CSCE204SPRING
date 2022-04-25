#Author Kelvin Keller
#Will read in the file questions.txt and return a list of question objects.  A sample qustions.txt is attached.  I'd prefer if you made your own to make it fun :)
def get_Questions():
    textfile = "Final/questions.txt"
    with open(textfile) as file:
        for line in textfile:
            #get it to return a list 

def display_Questions(question):
    #displays the question

def display_Answer(question):
    #Will display what the user has currently guessed, this will initially be all underscores