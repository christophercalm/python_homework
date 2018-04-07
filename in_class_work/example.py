# Importing math libraries
# Christopher Calmes
# 1/31/2018
# Calculating the area of a circle

import math

def main():
   
    year = eval(input("Enter YEAR: "))
    
    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11* (year % 19)) % 30
    print("The Gregorian epact fot the year", epact, "is",epact)

main()

