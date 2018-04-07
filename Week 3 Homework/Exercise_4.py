# PRogram to generate usernames
# 03/12/2018
# Christopher Calmes


def main():

    print("This program creates a file of usernanmes from a")
    print("file of names.")

    #get the files names
    fname = input("Enter the file in which the names are stored: ")
    infile = open(fname, "r")

    gname = input("Enter the file to which the usernames should be written: ")
    outfile = open(gname, "w")

    for line in infile:
        #first and last names
        first, last = line.split()
        #make username
        uname = (first[0] + last[:7]).lower()
        #write to file
        print(uname, file = outfile)

    infile.close()
    outfile.close()

main()
        
