#Author Kelvin Keller
import math
import random
#card function 
def deal():
    #initializing cards 
    card = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    #get a random card
    randomPull = random.randint(0,12)
    for i in card:
        if randomPull == 0:
            print("Ace")
            return 1
        elif randomPull == 1:
            print("2 Card")
            return 2
        elif randomPull == 2:
            print("3 Card")
            return 3
        elif randomPull == 3:
            print("4 Card")
            return 4   
        elif randomPull == 4:
            print("5 Card")
            return 5
        elif randomPull == 5:
            print("6 Card")
            return 6
        elif randomPull == 6:
            print("7 Card")
            return 7
        elif randomPull == 7:
            print("8 Card")
            return 8
        elif randomPull == 8:
            print("9 Card")
            return 9
        elif randomPull == 9:
            print("10 Card")
            return 10
        elif randomPull == 10:
            print("Jack")
            return 10
        elif randomPull == 11:
            print("Queen")
            return 10
        else:
            print("King")
            return 10

def user():
    #call deal to display the card the user dealt
    print(f"Your card value is : {deal()}")

def computer():
    #call deal to display the card the computer dealt
    print(f"Computer card value is: {deal()}")

while True:
    print("Welcome to our Awesomne Card Game!")
    user()
    computer()
    if user > computer:
        print("""You win!
                Your Score: 1
                Computer Score: 0""")
        game = input("Would you like to play again (Y)es or (N)o?").strip().lower()
    elif user < computer:
        print("""Computer wins!
                Your Score: 0
                Computer Score: 1""")
        game = input("Would you like to play again (Y)es or (N)o?").strip().lower()
    else:
        print("Tie!")
        game = input("Would you like to play again (Y)es or (N)o?").strip().lower()
    
    





        