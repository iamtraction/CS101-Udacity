"""Takes two dates as inputs, and calculates the
    number of days between them."""

# Assumes that the dates are correct and
# the first date comes before the second date
# and you have not time traveled.

# Calendars are very complicated and they have changed over history.
# Dates are only valid for Gregorian Calendar (Started from 15 Oct. 1582)

def is_leap_year(year):
    """Checks if the given year is a leap year."""
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

def days_in_month(year, month):
    """Returns the number of days in a month of a given year."""
    if month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10 or month == 12:
        return 31
    if month == 2:
        if is_leap_year(year):
            return 29
        return 28
    return 30

def next_date(year, month, date):
    """Returns the next date of the given date."""
    if date < days_in_month(year, month):
        return year, month, date + 1
    if month < 12:
        return year, month + 1, 1
    return year + 1, 1, 1

def date_is_before(year1, month1, day1, year2, month2, day2):
    """Checks if the first date is before the second date."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def days_between_dates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1 and year2/month2/day2."""
    assert not date_is_before(year2, month2, day2, year1, month1, day1)
    days = 0
    while date_is_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = next_date(year1, month1, day1)
        days += 1
    return days

def test():
    """Assertion test of all the defined functions"""
    assert days_between_dates(2014, 1, 1, 2014, 1, 1) == 0
    assert days_between_dates(2014, 1, 1, 2014, 1, 2) == 1
    assert days_between_dates(2100, 1, 1, 2101, 1, 1) == 365
    assert days_between_dates(2000, 1, 1, 2001, 1, 1) == 366
    assert next_date(2014, 1, 30) == (2014, 1, 31)
    assert next_date(2014, 2, 28) == (2014, 3, 1)
    assert next_date(2014, 4, 30) == (2014, 5, 1)
    assert next_date(2014, 12, 31) == (2015, 1, 1)
    assert is_leap_year(1600)
    assert is_leap_year(2000)
    assert not is_leap_year(1700)
    assert not is_leap_year(2100)
    assert not is_leap_year(1800)
    assert not is_leap_year(2200)
    assert not is_leap_year(1900)
    assert not is_leap_year(2300)
    print "Tests passed successfully!"

test()
