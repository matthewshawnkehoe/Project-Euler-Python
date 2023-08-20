'''
Project Euler : Problem 19
@author: Matthew Kehoe
'''
from datetime import datetime
import time
start = time.time()

def find_sundays(year1, year2, day):
    total = 0
    dayofweek = convert_day_to_int(day)
    months = range(1, 13)
    for year in range(year1, year2):
        for month in months:
            # Sunday is the 6th day in .weekday()
            if datetime(year, month, 1).weekday() == dayofweek:
                total += 1
    return total

def convert_day_to_int(day):
    if day == "Monday":
        return 0
    if day == "Tuesday":
        return 1
    if day == "Wednesday":
        return 2
    if day == "Thursday":
        return 3
    if day == "Friday":
        return 4
    if day == "Saturday":
        return 5
    if day == "Sunday":
        return 6
    else:
        print("Enter a valid day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.")

val = find_sundays(1901, 2001, "Sunday")

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))