#Author Kelvin Keller 
class Question:#create a question class
    def __init__(self, thequestion, theanswer, userscurrentguess, wongame): #The Question holds the question, the answer, the users current guess, if they have won...
        self.thequestion = thequestion
        self.theanswer = theanswer
        self.userscurrentguess = userscurrentguess
        self.wongame = wongame
    #You will add methods to this class, in order to get the required information. e.g.
    def get_question(self):
        return self.thequestion

    def get_answer(self):
        return self.theanswer

