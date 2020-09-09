# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:43:40 2020

@author: david_000
"""

# import datetime and configure current date and time variables
from datetime import datetime
time = datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

groceries = ["Meat", "Cheese"]

# greet user, display date and time and display current grocery list
print("Welcome to the grocery list app")
print("Current date and time: " + str(month) + "/" + str(day) + " " + str(hour) + ":" + str(minute))
print("You currently have", groceries[0], "and", groceries[1], "in your list")

# gather user input
grocery = input("Type of food to add to the grocery list: ").title()
groceries.append(grocery)
print(groceries)
grocery = input("Type of food to add to the grocery list: ").title()
groceries.append(grocery)
print(groceries)
grocery = input("Type of food to add to the grocery list: ").title()
groceries.append(grocery)
print(groceries)

# print grocery list and sorted grocery list
print("\nHere is your grocery list:")
print(groceries)
print("Here is your sorted grocery list:")
groceries.sort()
print(groceries)

#simulate grocery shopping
print("\nSimulating grocery shopping...")

print("\nCurrent grocery list:", len(groceries), "items")
print(groceries)
bought = input("What food did you just buy: ").title()
groceries.remove(bought)
print("Removing", bought, "from list...")

print("\nCurrent grocery list:", len(groceries), "items")
print(groceries)
bought = input("What food did you just buy: ").title()
groceries.remove(bought)
print("Removing", bought, "from list...")

print("\nCurrent grocery list:", len(groceries), "items")
print(groceries)
bought = input("What food did you just buy: ").title()
groceries.remove(bought)
print("Removing", bought, "from list...")

# advise store is sold out of item and add something else
print("\nCurrent grocery list:", len(groceries), "items")
print(groceries)
sold_out = groceries.pop()
print("Sorry, the store is out of", sold_out)
bought = input("What would you like instead: ").title()
groceries.insert(0, bought)
print("Here is what remains on your grocery list:")
print(groceries)


