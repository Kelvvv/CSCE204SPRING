#Author Kelvin Keller Jr
from xmlrpc.client import Boolean
def getBoolean(item):
    item = Boolean(True)

def getGuests():
    with open("Assignments/assignment19/guest_list.txt") as file:
        for line in file:
            print(line,end="")
        print()
            
        
def displayGuests(guests, coming):
    if coming == True:
        print("Jenny, Kim, Mason, Cindy, Charlotte, Tyler")
    else:
        print("Bradley, Tim, Alex, Brent")


print("Let's plan our party!")
print(input("View (A)ttending, (N)ot attending, or (Q)uit: ")).lower().strip()

