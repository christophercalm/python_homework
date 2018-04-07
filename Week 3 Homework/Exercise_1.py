#Replace all four letter workds in a file with the first letter and three asterisks
# 03/12/2018
# Christopher Calmes

fname = input("Enter the file in which the words are stored: ")
infile = open(fname, "r")

gname = input("Enter the file to which the words should be written: ")
outfile = open(gname, "w")

data = infile.read()


for word in data.split():
    if len(word) == 4:
        print(word[0][:1] + "***", file=outfile)
    else:
        print(word, file = outfile)

infile.close()
outfile.close()

