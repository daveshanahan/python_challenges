# my_values = range(1,10)

# print(my_values)

# for i in range(1,11):
#     print(i)

# for num in range(1, 15, 2):
#     print(num)

# my_string = "Hello World"
# list_word = list(my_string)
# print(my_string)
# print(list_word)

# new_word = " ".join(list_word)

# print(new_word)

numbers = list(range(10,1021,13))
print(numbers)

squares = []

for num in numbers:
    square = num**2
    squares.append(square)

print(squares)

print(min(squares))
print(max(squares))
print("The sum of all the elements is: " + str(sum(squares)))

names = ["jack", "john", "mark", "bill" ]
nums = [20,40,80,71]
floaters = [20.5,14.7,13.8,1.025]

for i in range(len(names)):
    print(names[i] + ": " + str(nums[i]) + " - " + str(floaters[i]))

for name, number, floater in zip(names, nums, floaters):
    print(name.title() + ": " + str(number) + " -- " + str(floater))