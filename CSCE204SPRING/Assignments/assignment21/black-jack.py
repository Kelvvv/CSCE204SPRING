#Author Kelvin Keller 
import random
import string

def getScore():
    filename = "Assignments/assignment21/scores.txt"
    with open (filename) as file:
        score = file.readline(filename)
    return score

def saveScore(score):
    filename = "Assignments/assignment21/scores.txt"
    with open (filename,"w") as file:
      filename + 1

def playRound():
    chance = 0
    computerHand = random.randint(14,23)
    userhand = random.randint(1,11)
    print(f"Your Hand Total: {userhand + userhand}")   
    input = print("Do you want another card (Y)es or (N)o?").lower().strip()

    for i in chance:
        if input == "y":
            print(f"{userhand}")
        elif input == "n":
            print(f"Computer's Hand Total: {computerHand}")
        else:
            print("Invalid Input")
        
    if computerHand > 21:
        print("User wins!")
        return 1
    elif computerHand == 21:
        print("Computer Wins!")
        return -1
    elif userhand > 21:
        print("Computer Wins!")
        return -1
    elif userhand == 21:
        print("User Wins!")
        return 1
    else:
        print("Its a tie!")
        return 0

print("Lets play Black Jack")
game = print(input("(P)lay or (Q)uit: ")).lower().strip()

if game == "p":
    playRound()
else:
    print()

    






