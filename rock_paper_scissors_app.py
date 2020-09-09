import random

print("Welcome to the Rock Paper Scissors game")

# gather user input for number of rounds
rounds = int(input("\nHow many rounds would you like to play: "))

# initialise counters for player and computer; initialise moves list
player = 0
computer = 0
moves = ["rock", "paper", "scissors"]

# game logic
for i in range(1,rounds+1):
    computer_move = random.choice(moves)
    print("\nRound " + str(i) + "\nPlayer: " + str(player) + "\tComputer: " + str(computer))
    my_choice = input("Time to choose... rock, paper, scissors: ").lower().strip()
    print("\tComputer: " + computer_move + "\n\tPlayer: " + my_choice)
    # computer chooses rock
    if computer_move == "rock" and my_choice == "paper":
        player += 1
        print("\tPaper covers rock!\n\tYou win round " + str(i) + ".")
    elif computer_move == "rock" and my_choice == "scissors":
        computer += 1
        print("\tRock beats scissors!\n\tComputer gets the point!")
    # computer chooses paper
    elif computer_move == "paper" and my_choice == "rock":
        computer += 1 
        print("\tPaper covers rock!\n\tComputer gets the point!")
    elif computer_move == "paper" and my_choice == "scissors":
        player += 1
        print("\tScissors cuts paper!\n\tYou win round " + str(i) + ".")
    # computer chooses scissors
    elif computer_move == "scissors" and my_choice == "paper":
        computer += 1
        print("\tScissors cuts paper!\n\tComputer gets the point!")
    elif computer_move == "scissors" and my_choice == "rock":
        player += 1
        print("\tRock beats scissors!\n\tYou win round " + str(i) + ".")
    # capturing other combinations
    elif my_choice == computer_move:
        print("\tIt's a tie, how boring!\n\tThis round was a tie.")
    elif my_choice != "rock" or my_choice != "paper" or my_choice != "scissors":
        computer += 1
        print("\tSorry, that is not a valid move.\n\t Computer gets the point!")

# print final results stats
print("\nFinal game results\n\tRounds played: " + str(rounds) + "\n\tPlayer Score: " + str(player) + "\n\tComputer Score: " + str(computer))
if player > computer:
    print("\tWinner: PLAYER!!!")
elif player == computer:
    print("\tIt's a tie!!!")
else:
    print("\tWinner: Computer :-(")