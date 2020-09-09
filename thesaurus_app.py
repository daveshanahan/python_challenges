import random

# Welcome message
print("Welcome to the Thesaurus App!")
print("\nChoose a word from the Thesaurus and I will give you a synonym.")

# initialise thesaurus dictionary
thesaurus = {
    "hot":["balmy", "summery", "tropical", "boiling", "scorching"],
    "cold":["chilly", "cool", "freezing", "frigid", "polar"],
    "happy":["content", "cheery", "merry", "jovial", "jocular"],
    "sad":["unhappy", "downcast", "miserable", "glum", "melancholy"],
    }

# Print thesaurus entries with a loop
print("\nHere are the words in the Thesaurus: ")
for i in thesaurus:
    print("\t- " + i)

# gather user input and print synonym or message stating word is not found
word = input("\nWhat word would you like a synonym for: ").lower().strip()

if word in thesaurus:
    print("\nA synonym for " + word + " is " + random.choice(thesaurus[word]) + ".")
else:
    print("\nThe word you have chosen is not in the thesaurus.")

# ask if user would like to see whole thesaurus and display output
view = input("\nWould you like to see the whole thesaurus (yes/no): ").lower()

if view.startswith("y"):
    for key, value in thesaurus.items():
        print("\n" + key + " synonyms are: ")
        for value in values:
            print("\t- " + value)
else:
    print("I hope you enjoyed the program. Thank you!")

