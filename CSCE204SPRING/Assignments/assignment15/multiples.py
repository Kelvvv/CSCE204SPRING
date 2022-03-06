#Author Kelvin Keller

def displayMultiples():
    interface = input("(L)ist Multiples, or (Q)uit: ").lower().strip()

    if interface == "l":
        number = int(input("Enter Number:"))
        for i in range(1,100):
            print(number*i, end=" ")
    elif interface == "q":
        print("Goodbye")
    else:
        print("Invalid Input")
        return

displayMultiples()
        