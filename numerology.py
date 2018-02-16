#Program to "determine a person's character" based on 
#The numberic value of their nameaq

name = input("Enter your name: ")
lowerName = name.lower()
listWords = lowerName.split()
pcount = 0
allWords = ""
for word in listWords:
    allWords += word

for letter in allWords:
    #ASCII value of letter
    pcount += (ord(letter) - 96) 


print(pcount)





