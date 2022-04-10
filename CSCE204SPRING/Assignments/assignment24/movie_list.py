from movie import Movie

#movies = ["Not Time To Die", "The Last Letter From Your Lover","Passing","Last Night In Soho"]

def textfile():
    with open("Assignments/assignment24/movies.txt") as file:
        for line in file:
            print(line)

while True:
    command = input("(L)ist all movies, get a movie (D)etails, or (Q)uit: ").lower().strip()

    if command == "q":
        break
    elif command == "l":
        for i in textfile:
            textfile.display()
    elif command == "d":
        for i in textfile:
            textfile.display()