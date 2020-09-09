print("Welcome to the Voter Registration App")

parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]
# gather user input
name = input("\nPlease enter your name: ").title().strip()
age = (int(input("Please enter your age: ")))

# not old enough to vote
if age < 18:
    print("\nYou are not old enough to register to vote.")
# old enough to vote
else:
    print("\nCongratulations " + name + "! You are old enough to register to vote.")
    # loop through list of parties and print result 
    print("\nHere is a list of parties to join:")
    for i in parties:
        print("-" + i)
    # gather input for what party to join and logic to return statement depending on input
    joined = input("\nWhat party would you like to join: ").title().strip()
    if joined == "Republican" or joined == "Democratic":
        print("\nCongratulations " + name + "! You have joined the " + joined + " party.\nThat is a major party!")
    elif joined == "Independent":
        print("\nCongratulations " + name + "! You have joined the " + joined + " party.\nYou are an independent person!")
    elif joined == "Libertarian" or joined == "Green":
        print("\nCongratulations " + name + "! You have joined the " + joined + " party.\nThat is not a major party!")
    else:
        print("Sorry, but your chosen party is not on the ticket.")

