'''
Program to calculate the price of a babysitter
Christopher Calmes
03/27/2018
'''

early_rate = 2.5
late_rate = 1.75


def main():

    #Get input
    try:
        startTime, startMeridian = input("Enter a starting time (ex. 9:30 AM): ").split()
        startHour, startMin = startTime.split(":")
        endTime, endMeridian = input("Enter an ending time (ex. 9:30 PM): ").split()
        endHour, endMin = endTime.split(":")
        name = input("Enter your name: ")
    except TypeError:
        main()

    #typecasting
    startHour = int(startHour)
    startMin = int(startMin)
    endHour = int(endHour)
    endMin = int(endMin)
    
    #initialize Values
    hoursBefore9 = 0
    minsBefore9 = 0
    hoursAfter9 = 0
    minsAfter9 = 0

    #starting time before noon
    if startMeridian == 'AM':
        minsBefore9 += (12 * 60) - (startHour * 60 + startMin)
        if endHour < 9  and endMeridian == 'PM':
            minsBefore9 += 60 * endHour + endMin
        elif endHour >= 9 and endMeridian == 'PM':
            minsBefore9 += 60 * 9
            minsAfter9 += 60 * (endHour - 9) + endMin

    #starting time after noon
    if startMeridian == 'PM':
        if endHour < 9:
            minsBefore9 += 60 * (endHour - startHour) + (endMin - startMin)
        elif endHour >= 9:
            minsBefore9 += 60 * (9 - startHour)  
            minsAfter9 += 60 * (endHour - 9) + (endMin - startMin)
    

    #charges
    costBefore9 = (minsBefore9 / 60) * early_rate
    costAfter9 = (minsAfter9 / 60) * late_rate
    totalCost = costBefore9 + costAfter9

    #convert back to hours and get total
    hoursBefore9 = minsBefore9 // 60
    minsBefore9 = minsBefore9 % 60

    hoursAfter9 = minsAfter9 // 60
    minsAfter9 = minsAfter9 % 60

    totalHours = hoursBefore9 + hoursAfter9 + (minsBefore9 + minsAfter9) // 60
    
    if minsBefore9 + minsAfter9 >= 60:
        totalMins = (minsBefore9 + minsAfter9) - 60
    else:
        totalMins = minsBefore9 + minsAfter9

    #output
    print("\n\nSummary for : ", name)
    print("Total time of service: " + str(totalHours) + ":" + str(totalMins)+ "\n\n")
    print("Time before 9:00 PM: " + str(hoursBefore9) + ":" + str(minsBefore9))
    print("Charges until 9:00 PM: $" + str(costBefore9) + "\n\n")
    print("Time After 9:00 PM: " + str(hoursAfter9) + ":" + str(minsAfter9))
    print("Charges after 9:00 PM: $" + str(costAfter9) + "\n\n")
    print("Total Charges: $" + str(totalCost))

main()
