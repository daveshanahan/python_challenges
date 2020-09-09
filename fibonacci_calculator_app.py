print("Welcome to the Fibonacci Calculator App")

# gather user input
num = int(input("How many digits of the Fibonacci sequence would you like to generate? "))

# generate Fibonacci numbers based on user input

print("The first " + str(num) + " numbers in the Fibonacci sequence are:")
fib = [1,1]
for i in range(num-2):
    fib.append(fib[i]+fib[i+1])

# print fibonacci numbers
for i in fib:
    print(i)

# generate corresponding golden ratios
print("\nThe corresponding Golden Ratio values are:")
ratio = []
for i in range(len(fib)-1): # iterate through list of numbers so you can access indexes
    ratio.append(fib[i+1]/fib[i])

# print ratios
for i in ratio:
    print(i)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi: 1.618...")
    




