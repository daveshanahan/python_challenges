import time
flag = True


while True:
    print("Enter 1 to determine if a specific number is prime.\nEnter 2 to determine all prime numbers within a set range.")
    choice = input("Enter your choice 1 or 2: ")
    if choice == "1":
        # check if a number is prime
        num = int(input("\nEnter a number to check if it is prime:"))
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not prime!")
                    break
            else:
                print(num, "is prime!")

    elif choice == "2":
        # note time; gather input; initialise variables
        start = time.time()
        lower = int(input("\nEnter the lower bound of your range:"))
        upper = int(input("Enter the upper bound of your range:"))
        primes = []
        # loop through range and append to prime list
        for i in range(lower, upper + 1):
            for x in range(2,i):
                if(i % x == 0):
                    break
            else:
                primes.append(i)
        # note end time and change in time
        end = time.time()
        delta = round((end - start), 4)
        # primt summary
        print("\nCalculations took a total of " + str(delta) + " seconds")
        print("The following numbers between 1 and 100 are prime:")
        input("Press enter to continue.")
        for i in primes:
            print(i)   
    run_again = input("Would you like to run the program again (y/n):")
    if run_again != "y":
        break
print("Thank you for using the program. Goodbye")

