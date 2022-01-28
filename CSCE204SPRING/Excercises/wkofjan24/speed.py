#Author Kelvin Keller 
speed = float(input("Enter Speed: "))
ticketPrice = 0

if speed >= 90:
    print ("Time for a ticket")
elif speed >= 80:
    print("Warning!")
elif speed > 70:
    print("Slow down")
elif speed > 60:
    print 