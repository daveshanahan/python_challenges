print("Welcome to the average calculator app")

# gather user input
name = input("\nWhat is your name? ").title().strip()
num_grades = int(input("How many grades would you like to enter? "))
print("\n")

# initialise list and append number of grades depending on user input
grades = []
for i in range(num_grades):
    grades.append(int(input("Please enter a grade: ")))

# sort grades and print list of grades in descending order
grades.sort(reverse=True)
print("\nGrades Highest to Lowest: ")
for i in grades:
    print("\t" + str(i))

# calculate average grade
avg_grade = round(float(sum(grades)/len(grades)), 2)

# print summary table 
print("\n" + name + "'s Grade Summary:\n\tTotal number of grades: " + str(len(grades)) + "\n\tHighest grade: " + str(max(grades)) + "\n\tLowest grade: " + str(min(grades)) + "\n\tAverage grade: " + str(avg_grade))

# get user input to calculate grade needed to get new average
desired_avg = float(input("\nWhat is your desired average? "))
req_grade = (desired_avg*(len(grades)+1))-float(sum(grades))

# print req_grade message for user
print("\nGood luck " + name + "!\nYou will need to get a " + str(req_grade) + " on your next assignment to earn a " + str(desired_avg) + " average.")

print("\nLet's see what your average could have been if you did better/worse on an assignment.")

# make copy of list to use for rest of program
grades_two = grades.copy()

# gather user input to change grade
ch_grade = int(input("What grade would you like to change: "))
new_grade = int(input("What grade would you like to change " + str(ch_grade) + " to: "))

# remove old grade, add new grade
grades_two.remove(ch_grade)
grades_two.append(new_grade)

# sort grades and print list of grades in descending order
grades_two.sort(reverse=True)
print("\nGrades Highest to Lowest: ")
for i in grades_two:
    print("\t" + str(i))

# calculate new average grade
new_avg_grade = round(float(sum(grades_two)/len(grades_two)), 2)

# print summary again with new grades
print("\n" + name + "'s New Grade Summary:\n\tTotal number of grades: " + str(len(grades_two)) + "\n\tHighest grade: " + str(max(grades_two)) + "\n\tLowest grade: " + str(min(grades_two)) + "\n\tAverage grade: " + str(new_avg_grade))

# print comparison of average scores and last statements
print("Your new average would be a " + str(new_avg_grade) + " compared to your real average of " + str(avg_grade) + ".\nThat is a change of " + str(round(new_avg_grade-avg_grade, 2)) + " points!")
print("\nToo bad your original grades are still the same!\n" + str(grades) + "\nYou should go ask for extra credit!")

