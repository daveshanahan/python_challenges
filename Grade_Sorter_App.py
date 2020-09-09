# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 20:41:23 2020

@author: david_000
"""
print("Welcome to the Grade Sorter App")

# create empty grades list and accept user input, appending each input to the list as an integer
grades = []
grades.append(int(input("What is your first grade (0-100): ")))
grades.append(int(input("What is your second grade (0-100): ")))
grades.append(int(input("What is your third grade (0-100): ")))
grades.append(int(input("What is your fourth grade (0-100): ")))

# display user's grades list
print("\nYour grades are: " + str(grades))

# sort list from highest to lowest and display for user
grades.sort(reverse=True)

print("\nYour grades from highest to lowest are: ", grades)

# remove lowest two grades
print("\nThe lowest two grades will now be dropped.")

first_removed = grades.pop()
second_removed = grades.pop()

print("Removed grade: ", first_removed)
print("Removed grade: ", second_removed)

# return remaining grades and highest grade
print("\nYour remaining grades are: ", grades)
print("Nice work! Your highest grade is a", grades[0])



