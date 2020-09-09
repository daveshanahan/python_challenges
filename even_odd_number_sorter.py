


print("Welcome to the even odd number sorter app")

while True:
    # gather user input and initialise variables
    innums = input("Enter in a string of numbers separated by a comma (,): ")
    innums = innums.replace(" ", "")
    list_nums = innums.split(",")
    # using a list comp: list_nums = [int(i) for i in innums.split(",")]
    even = []
    odd = []
    # results summary table and append nums to lists
    print("\n----Result Summary----")
    for i in list_nums:
        i = int(i)
        if i % 2 == 0:
            print("\t" + str(i) + " is even!")
            even.append(i)
        else:
            print("\t" + str(i) + " is odd!")
            odd.append(i)
    # sort and print evens
    even.sort()
    print("\nThe following " + str(len(even)) + " numbers are even:")
    for i in even:
        print("\t" + str(i))
    # sort and print odds
    odd.sort()
    print("\nThe following " + str(len(odd)) + " numbers are odd:")
    for i in odd:
        print("\t" + str(i))
    # check if user wants to run program again
    choice = input("\nWould you like to run the program again (y/n): ")
    if choice != "y":
        break
print("Thanks for using the app. Goodbye!")