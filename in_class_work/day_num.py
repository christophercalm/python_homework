#Program that gives the number of days previous to a certain date
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

def isValidDate(m, d, y):
    
    if isLeap(y) and m == 2 and d > 29: #february with leap year
        return False
    elif isLeap == False and m == 2 and d > 28: #February no leap year
        return False
    elif m in {1,3,5,7,8,10,12} and d > 31: #31 month days
        return False
    elif m in [4, 6, 9, 11] and d>30:
        return False
    else:
        return True #all other dates are valid

date = input("Enter a date in mm/dd/yyyy format: ") #string in mm/dd/yyyy format

mm,dd,yyyy = date.split("/")

#Test for the leading 0
if mm[0] == "0":
    mm = eval(mm[1]) #Use the number after the leading zero for mm.
else:
    mm = eval(mm) #If no leading zero, eval is sufficient.


if dd[0] == "0":
    dd= eval(dd[1]) #Use the number after the leading zero for dd.
else:
    dd = eval(dd) #If no leading zero, eval is sufficient.
    
yyyy = eval(yyyy)



if isValidDate(mm,dd,yyyy):
    dayNum = 31 * (mm -1) + dd
    if mm > 1:
        dayNum = dayNum - (4 * mm + 23) // 10
    if mm > 1 and isLeap(yyyy):
        dayNum = dayNum + 1

    print("The number of days up to that date is: ", dayNum)
        

else:
    print("The date entered is not valid: ")
    


        
    
