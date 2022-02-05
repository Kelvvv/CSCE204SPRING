gradeTotal = 0 

for i in range(3):
    while True:
        grade = int(input("Enter grade: "))
        if(grade >= 0 and grade <= 100):
            break
        else:
            print("Invalid grade")
    gradeTotal