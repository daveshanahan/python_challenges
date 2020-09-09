import cmath

# print introduction 
print("Welcome to the Quadratic Equation Solver App")
print("\nA Quadratic equation is of the form ax^2 + bx + c = 0.")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

# gather user input and create list to iterate over
num_equations = int(input("\nHow many equations would you like to solve today: "))
list_equations = list(range(0,num_equations))

#loop through interable to solve for roots of each equation
for i in list_equations:
    print("\nSolving equation #" + str(i + 1))
    print("----------------------------------")
    a = float(input("\nPlease enter your value of a (coefficient of x^2: "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))  
    d = (b**2)-(4*a*c) 
    print("\nThe solutions to " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 are:")
    x1 = (-b+cmath.sqrt(d))/2*a
    print("\nx1 = " + str(x1))
    x2 = (-b-cmath.sqrt(d))/2*a
    print("x2 = " + str(x2))

print("\nThank you for using the Quadratic Equation Solver App. Goodbye.")
