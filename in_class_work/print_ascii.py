# program to ask the user for a string and
# output the ASCII values of characters in the string

str = input("Enter a string that you want to translate to ASCII: ")

for c in str:
    print (hex(ord(c))) 

    


