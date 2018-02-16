# Ceasar Cipher

str = input("Enter a string to encode: ")
key = eval(input("Enter a character shift: ")) 

str.lower()
#ASCII value of lowercase a = 97
for c in str:
   print(chr((ord(c) -97 + key) % 26 + 97), end ="") 

    
