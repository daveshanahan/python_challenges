import random

print("Welcome to the Guess My Number App")

# gather user input
name = input("\nHello! What is your name: ").title().strip()

# generate random number
print("Well " + name + ", I am thinking of a number between 1 and 20.")
random_num = random.randint(1,20)

# initialise guess counter and get user to take guesses
guess_count = 0

for i in range(5):
    guess = int(input("\nTake a guess: "))
    if guess < random_num:
        guess_count += 1
        print("Too low!")
    elif guess > random_num:
        guess_count += 1
        print("Too high!")
    else:
        guess_count += 1
        break

# print game recap statement
if guess == random_num:
    print("\nGood job, " + name + "! You guessed my number in " + str(guess_count) + " guesses.")
else:
    print("\nGame over! The number I was thinking of is " + str(random_num) + ".")


