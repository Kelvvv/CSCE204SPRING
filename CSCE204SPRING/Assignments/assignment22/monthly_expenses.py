#Author Kelvin Keller
from tracemalloc import stop
def readExpense():
    eInfo = {}
    textfile = "Assignments/assignment22/expenses.txt"
    with open(textfile) as file:
        for line in textfile:
            eInfo = {textfile}
        return eInfo
def writeExpenses(eInfo):
    textfile = "Assignments/assignment22/expenses.txt"
    with open(textfile,"w") as file:
        for line in eInfo:
            file.write(f"{eInfo} \n")
        return eInfo
def listExpenses(eInfo):
    textfile = "Assignments/assignment22/expenses.txt"
    with open(textfile) as file:
        for line in eInfo:
            print(f"{eInfo} \n")
def addExpense(eInfo):
    expenseName = print(input("Enter Expense Name: "))
    expenseCost = print(input("Enter Expense Cost: "))
    if expenseName == eInfo:
        print("This expense is already documented!")
    else:
        return expenseName

program = print(input("Enter (L)ist, (A)dd, (Q)uit: ")).lower().strip()

if program == "l":
    listExpenses()
elif program == "a":
    addExpense()
else:
    print("Goodbye")
    stop


