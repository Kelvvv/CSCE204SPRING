#Author Kelvin Keller Jr
from datetime import date, time, datetime

classname = {"CSCE 247": time(8, 30),
                "CSCE 204": time(3, 00),
                "CSCE 240": time(8, 30),
                "CSCE 145": time(12, 00),
                "CSCE 146": time(3, 30),
                "ITEC 101": time(4, 30),
                "CSCE 201": time(5, 00)
                }

for exam in classname:
    if datetime.today().date() == classname.date():
        examDate = classname[exam]
        print(f"Todays Exam: {classname}" + examDate.strftime("%H,%M,%p"))
    else datetime.today().date() < classname.date():
        examDate = classname[exam]
        print(f"Future Exam: {classname}" + examDate.strftime("%H,%M,%p"))


   