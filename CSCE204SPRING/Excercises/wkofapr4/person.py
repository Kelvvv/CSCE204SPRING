class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"Hello {self.first_name} {self.last_name}")


friend =  Person("Amy", "Smith")
friend.display()