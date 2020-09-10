import time
print("Welcome to the Prime Number App")

running = True
# run the program in while loop
while running:
    # get user input
    print("\nEnter 1 to determine if a specific number is prime.\nEnter 2 to determine all prime numbers within a set range.")
    option = input("Enter your choice 1 or 2: ")

    # determine if a single number is prime
    if option == "1":
        number = int(input("\nEnter a number to determine if it is prime or not: "))

        # prime status check
        prime_status = True
        for i in range(2, number):
            if number % i == 0:
                prime_status = False
                break

        # print summary
        if prime_status:
            print(str(number) + " is prime!")
        else:
            print(str(number) + " is not prime!")
        
    # determine primes within a range of values and time the calculations
    elif option == "2":
        l_bound = int(input("\nEnter the lower bound of your range: "))
        u_bound = int(input("\nEnter the upper bound of your range: "))

        primes = []

        # get the current time
        start_time = time.time()

        # check prime status of all numbers within l_bound and u_bound
        for x in range(l_bound, u_bound + 1):
            # 1 is not prime
            if x > 1:
                prime_status = True
                for i in range(2, x):
                    if x % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False
            # x is prime
            if prime_status:
                primes.append(x)
        
        # get current time
        end_time = time.time()

        # determine delta time
        delta = round(end_time-start_time, 4)

        print("\nCalculations took a total of " + str(delta) + " seconds.")
        print("The following numbers between " + str(l_bound) + " and " + str(u_bound) + " are prime: ")
        input("Press enter to continue.")

        for prime in primes:
            print(prime)

        # not a valid choice entered by the user
        else:
            print("\nThat is not a valid option.")

    # quit the program if enter something other than y
    choice = input("Would you like to run the program again (y/n): ").lower()
    if choice != "y":
        running = False
        print("\nShutting down.")     
