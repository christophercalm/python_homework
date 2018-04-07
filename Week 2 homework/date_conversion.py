#Program to convert date from format mm/dd/yyyy to 
#Month Day, Year
#Christopher Calmes
#02/22/2018

def main():
    dateStr = input("Enter a date in the format (mm/dd/yyyy): ")
    monthStr, dayStr, yearStr = dateStr.split("/")

    months = ["January", "February", "March", "April", 
            "May", "June", "July", "August", "September", 
            "October", "November", "December"]

    monthStr = months[int(monthStr) - 1] #-1 because of indexing

    print ("Date in new format: ", monthStr, dayStr+",", yearStr)



if __name__=="__main__":
        main()
