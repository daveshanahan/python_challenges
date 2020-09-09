# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 19:17:21 2020

@author: david_000
"""
print("Welcome to the different types of lists program")

# define lists
num_strings = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [2.5, 0.0452, 82.45, 100.54786]
num_lists = [[1,2,3], [4,5,6], [7,8,9]]

# print summary table 
print("\n\t\tSummary Table")

print("\nThe variable num_strings is a", type(num_strings))
print("It contains the elements", num_strings)
print("The element", num_strings[0], "is a", type(num_strings[0]))

print("\nThe variable num_ints is a", type(num_ints))
print("It contains the elements", num_ints)
print("The element", num_ints[0], "is a", type(num_ints[0]))

print("\nThe variable num_floats is a", type(num_floats))
print("It contains the elements", num_floats)
print("The element", num_floats[0], "is a", type(num_floats[0]))

print("\nThe variable num_lists is a", type(num_lists))
print("It contains the elements", num_lists)
print("The element", num_lists[0], "is a", type(num_lists[0]))

# sort num_strings and num_ints and return values
print("\nNow sorting num_strings and num_ints")
num_strings.sort()
print("Sorted num_strings:", num_strings)
num_ints.sort()
print("Sorted num_ints:", num_ints)
print("\nStrings are sorted alphabetically while integers are sorted numerically!")
