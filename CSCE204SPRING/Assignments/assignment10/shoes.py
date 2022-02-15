#Author Kelvin Keller 

shoes = []
print("Shoe Inventory")

for i in shoes:
   shoes = input("Enter shoe name: ")
   restart = input("Would you like to add more shoe names? (Y)es or (N)o: ").lower().strip()
    if restart == "y":
       shoes = input("Enter shoe name: ")
    elif restart == "n":
        print("Here is your shoe inventory list:")
        print(shoes)
    else:
        print("Goodbye")
