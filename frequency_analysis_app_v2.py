from collections import Counter

# gather user input
key_phrase_1 = input("Please enter a phrase to be analysed: ").strip().lower()

# filter out all non alpha characters from input and join to new string
phrase_filter = filter(str.isalpha, key_phrase_1)
filter_phrase_1 = "".join(phrase_filter).lower()

total_occurrences = len(filter_phrase_1)

# create counter for letters
letter_count = Counter(filter_phrase_1)

#print analysis results
print("\nLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
    print(key + "\t\t" + str(value) + "\t\t" + str(round(((value/total_occurrences)*100), 2)) + "%")

# print letters in order of highest to lowest occurrence
ordered_letter_count = letter_count.most_common()

print("\nLetters ordered from highest occurrence to lowest:")
for i in ordered_letter_count:
    print(i[0], end="")

# gather user input
key_phrase_2 = input("\n\nEnter another phrase to be analysed: ")

# filter out all non alpha characters from input and join to new string
phrase_filter_2 = filter(str.isalpha, key_phrase_2)
filter_phrase_2 = "".join(phrase_filter_2).lower()

total_occurrences_2 = len(filter_phrase_2)

# create counter for letters
letter_count_2 = Counter(filter_phrase_2)

#print analysis results
print("\nLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count_2.items()):
    print(key + "\t\t" + str(value) + "\t\t" + str(round(((value/total_occurrences_2)*100), 2)) + "%")

# print letters in order of highest to lowest occurrence
ordered_letter_count_2 = letter_count_2.most_common()

print("\nLetters ordered from highest occurrence to lowest:")
for i in ordered_letter_count_2:
    print(i[0], end="")