non_letters = ['1','2','3','4','5','6','7','8','9','0',' ',
'.','?','!',',','"',"'",':',';','(',')','%','$','&','#','-', '_','\n','\t']

key_phrase_1 = input("Enter a word or phrase to count the occurrence of each letter: ").lower().strip()

for i in non_letters:
    key_phrase_1 = key_phrase_1.replace(i, "")

print(key_phrase_1)