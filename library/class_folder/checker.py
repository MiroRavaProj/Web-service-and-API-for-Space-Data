from datetime import date, datetime


def isValidDate(value):
    x = True
    try:
        datetime.strptime(value, '%Y-%m-%d')
    except ValueError:
        x = False
    return x


def int_check(value):
    isInt = True
    try:
        int(value)
    except ValueError:
        isInt = False
    return isInt

def float_check(value):
    isFloat = True
    try:
        float(value)
    except ValueError:
        isFloat = False
    return isFloat


def isValidDateFlight(value):
    x = True
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        x = False
    return x