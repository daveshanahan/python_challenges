import random

# gather user input
num_flips = int(input("How many times would you like to flip the coin? "))
visible = input("Would you like to see the result of each flip? ")

# define variables to hold count of each flip 
heads_count = 0
tails_count = 0

# logic for the coin flip - first part where you choose to see the result of each flip
if visible.startswith("y"):
    for i in range(num_flips):
        flips = random.randint(0,1)
        if flips == 0:
            heads_count += 1
            if heads_count == tails_count:
                print("At " + str(i + 1) + " flips, the number of heads and tails were equal at " + str(heads_count) + " each.")
            else:
                print("Heads")
        else:
            tails_count += 1
            if tails_count == heads_count:
                print("At " + str(i + 1) + " flips, the number of heads and tails were equal at " + str(heads_count) + " each.")
            else:
                print("Tails")

# if you choose not to see the results of each flip
else:
    for i in range(num_flips):
        flips = random.randint(0,1)
        if flips == 0:
            heads_count += 1
        else:
            tails_count += 1

print("\nResults of flipping a coin " + str(num_flips) + " times:")
print("\nSide\t\tCount\t\tPercentage\nHeads\t\t" + str(heads_count) + "/" + str(num_flips) + "\t\t" + format((heads_count/num_flips)*100, ".2f") + "%\nTails\t\t" + str(tails_count) + "/" + str(num_flips) + "\t\t" + format((tails_count/num_flips)*100, ".2f") + "%")




