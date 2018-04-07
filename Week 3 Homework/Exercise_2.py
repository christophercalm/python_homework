# Gets statistics on a text file
# 03/12/2018
# Christopher Calmes

fname = input("Enter the file in which the words are stored: ")
infile = open(fname, "r")

gname = input("Enter the file to which the statistics should be written: ")
outfile = open(gname, "w")

data = infile.read()

numWords = 0
numChar = 0
wordLength = []
numSentences = 0
endPunctuation = [".", "?", "!" ]

for word in data.split():

    numWords = numWords + 1
    wordLength.append(len(word)) #for average word length

    for char in word:
            numChar = numChar + 1

    for thing in endPunctuation:
        if thing in word:
            numSentences = numSentences + 1
    
        
averageLength = sum(wordLength) / numWords

#output
print("Number of Words: " + str(numWords), file = outfile)
print("Number of chars: " + str(numChar), file = outfile)
print("Average word Length: " + str(averageLength), file = outfile)
print("Number of sentences: " + str(numSentences), file = outfile)

infile.close()
outfile.close()
