

print("Welcome to the factor generator app")
flag = True

while True:
    # gather user input and initialise variables
    num = int(input("\nEnter a number to determine all factors of that number: "))
    numbers = list(range(1, num + 1))
    factors = []
    # print factors
    print("\nFactors of " + str(num) + " are: ")
    for i in numbers:
        if num % i == 0:
            factors.append(i)
            print(i)
        else:
            continue
    # print summary table of multiplication
    print("\nIn summary:")
    for i in range(int(len(factors)/2)):
        print(str(factors[i]) + "*" + str(factors[-i-1]))
    # ask user if they want to run the program again
    choice = input("\nRun again (y/n): ").lower()
    if choice != "y":
        break

print("\nThank you for using the program. Have a great day.")
