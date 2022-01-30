#Author Kelvin Keller 

#Interface
print("***** Monthly Fortune Telling *****")
usersChoice = input("What would you like to do? (V)iew signs, or see class (F)ortune:").lower().strip()

#conditions 
if usersChoice == "v":
    print("""Astrological Signs and Dates:
            - Aries: March 21 - April 19
            - Taurus: April 20 - May 20 
            - Gemini: May 21 - June 21
            - Cancer: June 22 - July 22
            - Leo: July 23 - August 22
            - Virgo: August 23 - September 22
            - Libra: September 23 - October 23 
            - Scorpius: October 24 - November 21 
            - Sagittarius : November 22 - December 21 
            - Capricoronous: December 22 - January 19 
            - Aquarius: January 20 - February 18 
            - Pisces: February 19 - March 20""")
elif usersChoice == "f":
    signFortune = input("Enter your astrological sign: ").lower().strip()
    if signFortune == "aries":
        print("You are a nuturing person.")
    elif signFortune == "taurus":
        print("You have a radiant personallity.")
    elif signFortune == "gemini":
        print("You are independent.")
    elif signFortune == "cancer":
        print("You are strong willed.")
    elif signFortune == "leo":
        print("You are the littiest person in the entire world don't for get it! :) ")
    elif signFortune == "virgo":
        print("You are calm like still water. ")
    elif signFortune == "libra":
        print("You are cautious. ")
    elif signFortune == "scorpius":
        print("You are mean. ")
    elif signFortune == "sagittarius":
        print("You are loveable. ")
    elif signFortune == "capricoronous":
        print("You're a comedian  ")
    elif signFortune == "aquarius":
        print("You are weird in your own right ")
    elif signFortune == "pisces":
        print("You are smart. ")
else:
    print("INVALID INPUT!")

print("Goodbye, Have a nice day!")

    