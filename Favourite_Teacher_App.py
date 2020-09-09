# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:22:42 2020

@author: david_000
"""
print("Welcome to the Favourite Teacher App")

# initialise list and gather user input

favourites = []

teacher = input("Who is your first favourite teacher: ").title()
favourites.append(teacher)
teacher = input("Who is your second favourite teacher: ").title()
favourites.append(teacher)
teacher = input("Who is your third favourite teacher: ").title()
favourites.append(teacher)
teacher = input("Who is your fourth favourite teacher: ").title()
favourites.append(teacher)

# print list in various ways

print("\nYour favourite teachers ranked are: ", favourites)
print("Your favourite teachers alphabetically are: ", sorted(favourites))
print("Your favourite teachers in reverse alphabetical order are: ", sorted(favourites, reverse=True))

# print info about teachers list

print("\nYour top two teachers are:", favourites[0], "and", favourites[1])
print("Your next two favourite teachers are:", favourites[2], "and", favourites[3])
print("Your last favourite teacher is:", favourites[-1])
print("You have a total of", len(favourites), "favourite teachers.")

# append new favourite teacher to list and print list in various ways again

new_teacher = input("Oops, " + str(favourites[0]) + " is no longer your favourite teacher. Who is your new FAVOURITE teacher: ").title()
favourites.insert(0, new_teacher)

print("\nYour favourite teachers ranked are: ", favourites)
print("Your favourite teachers alphabetically are: ", sorted(favourites))
print("Your favourite teachers in reverse alphabetical order are: ", sorted(favourites, reverse=True))

# print info about teachers list

print("\nYour top two teachers are:", favourites[0], "and", favourites[1])
print("Your next two favourite teachers are:", favourites[2], "and", favourites[3])
print("Your last favourite teacher is:", favourites[-1])
print("You have a total of", len(favourites), "favourite teachers.")

# remove a teacher from the list based on user input

removed_teacher = input("You've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title()
favourites.remove(removed_teacher)

# print list again in various ways

print("\nYour favourite teachers ranked are: ", favourites)
print("Your favourite teachers alphabetically are: ", sorted(favourites))
print("Your favourite teachers in reverse alphabetical order are: ", sorted(favourites, reverse=True))

# print info about teachers list

print("\nYour top two teachers are:", favourites[0], "and", favourites[1])
print("Your next two favourite teachers are:", favourites[2], "and", favourites[3])
print("Your last favourite teacher is:", favourites[-1])
print("You have a total of", len(favourites), "favourite teachers.")


