#Author Kelvin Keller 
import math

print("Lets calculate the cost of your road trip!")

#First ask the users for:
numberMiles = float(input("Enter the number of miles you are traveling: "))
numberDays = float(input("Enter the number of day(s) you are traveling: "))

#prices
priceperG = 3.159
milesperG = 24.9
breakfastCost = 10 * numberDays
lunchCost = 12.50 * numberDays
dinnerCost = 20 * numberDays
hotelCost = 103.25 * numberDays

priceofGas = numberMiles / milesperG * priceperG

#total 
meals = breakfastCost + lunchCost + dinnerCost
total = priceofGas + meals + hotelCost

print(f"Travel Cost is: {total}")