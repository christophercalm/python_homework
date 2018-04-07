#Program to count the number of words in a file

fname = input("Enter the file in which the data is stored")

infile = open(fname, "r")

outfile = open("ofile", "w")
data = infile.read()
wordList = data.split()

print("There are ", len(wordlist), "words in", fname, file = outFile)
