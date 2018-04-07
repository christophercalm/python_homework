import sys
import re
import os

#fname = input("Enter the file in which the numers are stored: ")

fname = str(sys.argv[1])

infile = open(fname, "r")

gname = input("Enter the file to which the sum should be written: ")

outfile = open(gname, "w")

a = []

#takes the first 5 lines and adds them to a list
for i in range(5):
    line = infile.readline()
    a.append(line[:-1]) #strips the \n1


#convert list of strive about to list of nunbers

numList = []

for  i  in  range(len(a)):
    numList.append(eval(a[i]))

print(sum(numList), file = outfile)

infile.close()
outfile.close()

