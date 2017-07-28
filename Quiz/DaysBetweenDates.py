# Takes two dates as inputs, and calculates the
# number of days between them.

# Assumes that the dates are correct and
# the first date comes before the second date
# and you have not time traveled.

# Calendars are very complicated and they have changed over history.
# Dates are only valid for Gregorian Calendar (Started from 15 Oct. 1582)

def isLeapYear(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10 or month == 12:
            return 31
    if month == 2:
        if isLeapYear(year):
            return 29
        return 28
    return 30

def nextDate(year, month, date):
    if date < daysInMonth(year, month):
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

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1 and year2/month2/day2."""
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDate(year1, month1, day1)
        days += 1
    return days

def test():
    assert daysBetweenDates(2014, 1, 1, 2014, 1, 1) == 0
    assert daysBetweenDates(2014, 1, 1, 2014, 1, 2) == 1
    assert daysBetweenDates(2100, 1, 1, 2101, 1, 1) == 365
    assert daysBetweenDates(2000, 1, 1, 2001, 1, 1) == 366
    assert nextDate(2014, 1, 30) == (2014, 1, 31)
    assert nextDate(2014, 2, 28) == (2014, 3, 1)
    assert nextDate(2014, 4, 30) == (2014, 5, 1)
    assert nextDate(2014, 12, 31) == (2015, 1, 1)
    assert isLeapYear(1600) == True
    assert isLeapYear(2000) == True
    assert isLeapYear(1700) == False
    assert isLeapYear(2100) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(2200) == False
    assert isLeapYear(1900) == False
    assert isLeapYear(2300) == False
    print "Tests passed successfully!"

test()
