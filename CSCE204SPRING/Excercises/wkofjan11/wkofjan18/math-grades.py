#Author Kelvin Keller 

#grade calculator 
assignments = float(input("Assignments Grade: "))
excercises = float(input("Excercises Grade: "))
midterm = float(input("Midterm Grade: "))
final = float(input("Final Grade: "))

finalGrade = assignments * .5 + excercises * .2 + midterm * .15 + final *.15

print(f"Final grade is {finalGrade}")