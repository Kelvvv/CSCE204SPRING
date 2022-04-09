from criminal import Criminal

def get_criminals():
    criminals = []

    while open(Excercises/wkofapr4/criminals.txt) as file:
        data = line.split(',')
        firstname = data[0].strip()
        lastname = data[1].strip()
        gender = data[2].strip().lower()
        crimetype = data[2].strip().lower()
        injail =  get_bool(data[4].strip())
        description = data[5].strip()
        criminals.append(Criminal(firstname,lastname,gender,crimetype,injail,description))
    return criminals

def get_bool(data):
    if data.lower()== "true":
        return True
    else:
        return False

criminals = get_criminals()

print("Welcome to our criminal system")

while True:
    command = input("Would you like to View, Search, or Quit: ").lower().strip()

    if command == "q":
        break
    if command == "v":
        for criminal in criminals:
            criminal.display()
    elif command == "s":
        gender = input("Enter male or female: ").strip().lower()
        crimetype = input("Enter robbery, assault, or murder:").lower().strip()

        print("Criminals that match your criteria: ")
        for criminal in criminals:
            if criminal.is_match(gender,crimetype):
                criminal.display()
            else:
                print("invalid")

print("Goodbye")