#Author Kelvin Keller 

debtN = []
debtV = []

print("List of Companies With Internship")

interface = input("(V)iew, (A)dd, (R)emove or (Q)uit:").lower().strip()

while True:

    if interface == "v":
        for i in debtN:
            print(f"{debtN}: ${debtV}")
    elif interface == "a":
        name = input("Enter Debt Name: ")
        amount = input("Enter Debt Amount: ")
        debtN.append(name)
        debtV.append(amount)

    elif interface == "r":
        print("Sorry life doesn't work like that :)")

    elif interface == "q":
        print("Goodbye")
        break

    else:
        print("Invalid input!")
        break


