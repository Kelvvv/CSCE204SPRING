#Author Kelvin Keller Jr
class Movie:
    def __init__(self,title,description,actors,genre,rating):
        self.title = title
        self.description = description
        self.actors = actors
        self.genre = genre
        self.rating = rating

        self.actors = []
    
    def display(self):
        if self.title == True:
            print(""" ***{self.title}***
                        {self.description}
                        Stars: 
                        -{self.actors}
                        Genre: {self.genre}
                        Rating: {self.rating}""")
    
    def is_match(self,title):
        if title == self.title:
            return True

        return False
