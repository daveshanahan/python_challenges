print("Welcome to the Yes or No Issue Polling App")

# gather user input and initalise variables
voters_votes = {}
yes_count = 0
no_count = 0
issue = input("What is the yes or no issue you will be voting on today: ").strip()
num_voters = int(input("What is the number of voters you will allow on the issue: "))
password = input("Enter a password for polling results: ").strip()

#logic for looping through voting input
for i in range(num_voters):
    # gather user input
    name = input("\nEnter your full name: ").title().strip()
    if name in voters_votes.keys():
        print("Sorry, it seems that somebody with that name has already voted.")
    else:
        print("Here is our issue: " + issue)
        vote = input("What do you think... yes or no: ").lower()
        # return output based on vote, append to counters and correct answers
        if vote.startswith("y"):
            vote = "yes"
            yes_count += 1
            print("Thank you " + name + "! Your vote of yes has been recorded")
        elif vote.startswith("n"):
            vote = "no"
            no_count += 1
            print("Thank you " + name + "! Your vote of no has been recorded")
        else:
            print("That is not a yes or no answer, but okay... \nThank you " + name + "! Your vote of " + vote + " has been recorded")
        # append info to dict
        voters_votes[name] = vote

# display voters
print("\nThe following " + str(num_voters) + " people voted:")
for i in voters_votes.keys():
    print(i)

# display result of vote
print("\nOn the following issue: " + issue)
if yes_count > no_count:
    print("Yes wins! " + str(yes_count) + " votes to " + str(no_count) + ".")
elif no_count > yes_count:
    print("No wins! " + str(no_count) + " votes to " + str(yes_count) + ".")
else:
    print("It's a tie! " + str(yes_count) + " votes to " + str(no_count) + ".")

# enter password to view vote results
display = input("\nTo see the voting results enter the admin password: ")
if display == password:
    for keys, values in voters_votes.items():
        print("Voter: " + keys + "\t\t\tVote: " + values)
else:
    print("Sorry! You have entered an incorrect password.")

print("\nThank you for using the Yes or No Issue Polling App")