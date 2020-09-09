# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:03:53 2020

@author: david_000
"""
import math

print("Welcome to the Right Triangle Solver App")

# get user input
a = float(input("What is the first leg of the triangle: "))
b = float(input("What is the second leg of the triangle: "))

# calculate hypotenuse "c" and area of triangle from given input
c = round(math.sqrt(a**2 + b**2), 3)
area = round(a*b/2, 3)

# return values based on given input
print("\nFor a triangle with legs of", a, "and", b, "the hypotenuse is", c)
print("For a triangle with legs of", a, "and", b, "the area is", area)