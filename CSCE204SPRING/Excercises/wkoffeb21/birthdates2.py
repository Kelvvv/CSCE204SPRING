from datetime import date, time, datetime

birthdays = {"Amy": date(2021, 3, 22),
            "Bobby": date(2021, 2, 10),
            "Carl": date(2021, 5, 29),
            "Dave": date(2021, 11, 21),
            "Erin": date(2021, 10, 22),
            "Fred": date(2021, 3, 2),
            "Gretta": date(2021, 6, 24),}

closestBirthday = date(2021, 12, 31)
closestFriend = " "

for friend in birthdays:
    birthday = birthdays[friend]
    daysTillBirthday = (birthday - date.today()).days
    daysTillCurrentClosest = (closestBirthday - date.today()).days

    #if birthday already occured
    if daysTillBirthday < 0:
        continue

    if daysTillBirthday < daysTillCurrentClosest:
        closestBirthday = birthday
        closestFriend = friend

print("The closest birthday is {friend}" + closestBirthday.strftime("%m/%d/%y"))