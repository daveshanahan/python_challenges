print("Welcome to the Binary Hexadecimal Converter App")

# gather user input cast as int

upper = int(input("Compute binary and hexadecimal values up to the following decimal number: "))

# create decimal list, appending actual value given in input
decimal = list(range(0,upper + 1))
input("Generating lists.... complete!")

input("\nUsing slices, we will now show a portion of each list.")

# gather user input for the slicing and create list based on input
lower_slice = int(input("\nWhat decimal number would you like to start at: "))
upper_slice = int(input("What decimal number would you like to stop at: "))
sliced_list = list(range(lower_slice,upper_slice + 1))

# print decimal list
print("\nDecimal values from " + str(lower_slice) + " to " + str(upper_slice) + ":")
for i in sliced_list:
    print(i)

# print binary list 
print("\nBinary values from " + str(lower_slice) + " to " + str(upper_slice) + ":")
for i in sliced_list:
    print(bin(i))

# print hex list
print("\nHexadecimal values from " + str(lower_slice) + " to " + str(upper_slice) + ":")
for i in sliced_list:
    print(hex(i))

# loop through complete original list from index 1 with bin and hex conversions
new_decimal = decimal.remove(0)
input("\nPress Enter to see all values from 1 to " + str(upper) + ".")
print("Decimal---Binary---Hexadecimal")
print("--------------------------------------------")

for i in range(len(decimal)):
    print(str(decimal[i]) + "---" + str(bin(decimal[i])) + "---" + str(hex(decimal[i])))
 