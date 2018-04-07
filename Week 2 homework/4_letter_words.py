#Replace all four and five letter workds in a string with equivalent
#Number of asterists

i_string = input("Enter a string that you want to censor: \n")

listWords = i_string.split()

newString = ""

for word in listWords:
    if len(word) == 4 or len(word) == 5: 
        newString += ("*" * len(word) + " ")
    else:
        newString += (word + " ")

print(newString)
