from datetime import date, time, datetime
from typing import Counter

assignments = {"Python Intro": date(2021, 1, 22),
                "Learning Math": date(2021, 1, 30),
                "If statements": date(2021, 2, 5),
                "While Loops": date(2021, 2, 14),
                "For Loops": date(2021, 3, 27),
                "Lists": date(2021, 3, 2),
                "Tuples": date(2021, 3, 7)}

#loop through and display the list of assignments
counter = 1

for assignment in assignments:
    dueDate = assignments[assignment]
    print(f"{counter}. {assignment} - Due: " + dueDate.strftime("%m/%d/%y"))
    counter +=1