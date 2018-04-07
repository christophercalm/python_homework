fname = input("Enter the file in which the numbers are stored: ")
infile = open(fname, "r")

gname = input("Enter the file to which the sum should be written")
outfile = open(gname, "w")

data = infile.read()

#empty list for numbers
numList = []

for elem in data.split():
    numList.append(eval(elem))

print(sum(numList), file = outfile)

infile.close()
outfile.close()
