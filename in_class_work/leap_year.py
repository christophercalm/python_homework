#Program to determine whether a given year is a leap year
#Christopher Calmes
#03/14/2018

def isLeap(year):
    
    isLeap = False
    if year % 4 == 0:
        if (year % 100 == 0) and (year % 400 != 0):
            isLeap = False

        else:
            isLeap = True

    return isLeap   

def isValidDate(month, day, year)


