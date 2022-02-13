#Author Kelvin Keller 

import random


print("Welcome to our Question Answer Game")

enter = input("Ask a yes or no question: ")
again = input("Would you like to ask another question? (Y)es or (N)o:").lower().strip()    
answer = random.randint(1,3)

for i in range(answer):
    while True:
        if answer == 1:
            print("Yes")
        elif answer == 2:
            print("No")
        else:
            print("Maybe")
        if again == "y":
            print(enter)
        else:
            print("Goodbye")
        
