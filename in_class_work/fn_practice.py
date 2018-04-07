#Collections of functions to practice

def eligibility(age, years):
    if age >= 30 and years >= 9:
        print("You are eligible to be a senator and a member of the house: ")
    elif age >= 25 and years >= 7:
        print("You are eligible to be a member of the house: ")

#eval(input(Enter 
eligibility(26,12)

def easterDate(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    
    print (d + e)
    if (d + e + 22) > 31:
        month = "April"
        day = str((d + e + 22) - 31)
    else:
        month = "March"
        day = str(d + e + 22)

    print("The date of Easter in: " + str(year)  + "is: " + month + "/" + day + "/" + str(year)) 

easterDate(1999)

def easterDateExpanded(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7

    if (d + e + 22) > 31:
        month = "April"
        day = (d + e + 22) - 31
    else:
        month = "March"
        day = (d + e + 22)

    #special cases
    specialCases = [1954, 1981, 2049, 2076]

    if year in specialCases:
        if (day - 7) < 0:
            month = "March"
            day = day - 7 + 31
        else:
            day = day - 7
    print("Easter in ", year, "falls on ", day, month)

easterDateExpanded(1954)
easterDateExpanded(1981)
