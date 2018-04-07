"""
Loop and a half
4/6/2018
"""

heating_days = 0
cooling_days = 0

average_daily_temp = input("Enter the average temperature for the day, press enter to quit ")
while(average_daily_temp != ""):
    temp = eval(average_daily_temp)
    print(temp)
    if temp > 80:
        heating_days += temp - 80
    if temp < 60:
        cooling_days +=  60 - temp

    print(heating_days)
    print(cooling_days)

    average_daily_temp = input("Enter the average temperature for the day, press enter to quit ")


