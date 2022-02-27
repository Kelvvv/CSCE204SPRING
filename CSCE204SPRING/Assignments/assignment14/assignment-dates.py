#Author Kelvin Keller Jr
from datetime import date, time, datetime
from typing import Counter

assignments = {"Intro": date(2022, 1, 21),
                "Multiplication": date(2022, 1, 29),
                "Subtraction": date(2022, 2, 4),
                "Division": date(2022, 2, 13),
                "Algebra": date(2022, 3, 25),
                "Triginometry": date(2022, 3, 1),
                "Statistics": date(2022, 3, 7),
                "Calculus": date(2022, 3, 10),
                "Business Calculus": date(2022, 3, 15),
                "Practice Test": date(2022, 3, 20)}

counter = 1 

for assignment in assignments:
    if assignment < date(2022, 3, 25):
        dueDate = assignments[assignment]
        print(f"- Ass {counter} - {assignment}, Past Due: " + dueDate.strftime("%b/%d"))
        counter +=1
    elif assignment == date(2022, 3, 25):
        dueDate = assignments[assignment]
        print(f"- Ass {counter} - {assignment} - Due Today: " + dueDate.strftime("%b/%d"))
        counter +=1
    elif assignment > date(2022, 3, 25):
        dueDate = assignments[assignment]
        print(f"- Ass {counter} - {assignment} - Due Today: " + dueDate.strftime("%b/%d"))
        counter +=1
    else:
        print(f"- Ass {counter} - {assignment}, Past Due: " + dueDate.strftime("%b/%d"))