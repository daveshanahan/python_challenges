# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 20:22:46 2020

@author: david_000
"""
print("Welcome to the temperature conversion program")

# get user input
f_temp = float(input("What is the given temperature in degrees farenheit: "))

# conversions for each temperature type
c_temp = float((f_temp-32)*5/9)
k_temp = float((f_temp+459.67)*5/9)

# return a value rounded to 4 decimal places for each temperature type
print("\nDegrees Farenheit:", "\t", f_temp, "\nDegrees Celcius:" "\t", round(c_temp, 4), "\nDegrees Kelvin:", "\t", round(k_temp, 4))
