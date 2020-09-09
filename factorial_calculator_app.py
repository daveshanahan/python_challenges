import math

print("Welcome to the Factorial Calculator App")

# gather user input and create the list; remove zero from the list as it is not needed
target = int(input("\nWhat number would you like to calculate the factorial of? "))

# print the representation of the factorial for the user
print(str(target) + "! = ", end="")
for i in range(1,target):
    print(str(i), end="*")
print(str(target), end="\n")


# initialise result and append requested number to list; loop over list to get the factorial
result = 1

for i in range(1,target + 1):
    result = result * i


f_from_lib = math.factorial(target)
# print result from math library
print("\nHere is the result from the Math Library:\nThe factorial of " + str(target) + " is: " + str(f_from_lib) + "!")

# print result from my own method
print("\nHere is the result from my own algorithm:\nThe factorial of " + str(target) + " is: " + str(result) + "!")

print("\nIt is shown twice that " + str(target) + "! = " + str(f_from_lib) + " (with excitement)")

