class Criminal:
    def __init__(self,firstname,lastname,gender,crimetype,injail,descrtiption):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.crimetype = crimetype
        self.injail = injail
        self.descrtiption = descrtiption
    def is_match(self,gender,crimetype):
        if self.injail == True:
            return False

        if gender == self.gender and crimetype == self.crimetype:
            return True

        return False

    def display(self):
        jail_desc = "Not Incarcerated"

        if self.injail == True:
            jail_desc = "Incarcerated"

        print(f"""{self.firstname} {self.lastname}
        Gender: {self.gender}
        Crime: {self.crimetype}
        {jail_desc}
        {self.descrtiption}
        """)