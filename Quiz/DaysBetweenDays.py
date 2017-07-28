# Takes two dates as inputs, and calculates the
# number of days between them.

# Assumes that the dates are correct and
# the first date comes before the second date
# and you have not time traveled.

# Calendars are very complicated and they have changed over history.
# Dates are only valid for Gregorian Calendar (Started from 15 Oct. 1582)

def nextDate(year, month, date):
    """Warning: This version incorrectly assumes
        all months have 30 days!"""
    date += 1;
    if date < 30:
        return year, month, date + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDays(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1 and year2/month2/day2."""
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDate(year1, month1, day1)
        days += 1
    return days
