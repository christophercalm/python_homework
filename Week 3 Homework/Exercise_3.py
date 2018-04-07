# output squares of a file to a separate file
# 03/12/2018
# Christopher Calmes

fname = input("Enter the file in which the numbers are stored: ")
infile = open(fname, "r")

gname = input("Enter the file to which the squares should be written: ")
outfile = open(gname, "w")

data = infile.read()

for num in data.split():
    square = float(num) ** 2
    print(str(square), file = outfile)

infile.close()
outfile.close()
