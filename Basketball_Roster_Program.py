# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:50:33 2020

@author: david_000
"""
print("Welcome to the Basketball Roster Program")

# initialize empty list and gather user input

team = []

member = input("Who is your point guard: ").title()
team.append(member)
member = input("Who is your shooting guard: ").title()
team.append(member)
member = input("Who is your small forward: ").title()
team.append(member)
member = input("Who is your power forward: ").title()
team.append(member)
member = input("Who is your center: ").title()
team.append(member)

# display team based on user input

print("\tYour starting 5 for the upcoming basketball season")
print("\t\t\tPoint Guard: \t\t\t" + team[0])
print("\t\t\tShooting Guard: \t\t" + team[1])
print("\t\t\tSmall Forward: \t\t\t" + team[2])
print("\t\t\tPower Forward: \t\t\t" + team[3])
print("\t\t\tCenter: \t\t\t\t" + team[4])

# advise that index 2 is injured, remove from list and display number of team members left

print("\nOh no, " + team[2] + " is injured.")
removed = team.pop(2)
print("Your roster only has " + str(len(team)) + " members.")
new_member = input("Who will take " + removed + "'s spot: ").title()
team.insert(2, new_member)

# display new team based on user input

print("\tYour starting 5 for the upcoming basketball season")
print("\t\t\tPoint Guard: \t\t\t" + team[0])
print("\t\t\tShooting Guard: \t\t" + team[1])
print("\t\t\tSmall Forward: \t\t\t" + team[2])
print("\t\t\tPower Forward: \t\t\t" + team[3])
print("\t\t\tCenter: \t\t\t\t" + team[4])

# wish new member good luck and restate list length

print("\nGood luck " + team[2] + " you will do great!")
print("Your roster now has " + str(len(team)) + " players.")

