MONTH_DAY = {1: 31, 3: 31, 4: 30, 5: 31, 6:30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def is_leap_year(n):
    if n % 100 == 0:
        return n % 400 == 0
    return n % 4 == 0


def month_day(year, month):
    if month in MONTH_DAY:
        return MONTH_DAY[month]
    return 29 if is_leap_year(year) else 28


def year_day(year):
    return 366 if is_leap_year(year) else 365


def is_first_sunday(year, month):
    days = 1
    for i in range(1900, year):
        days += year_day(i)

    for i in range(1, month):
        days += month_day(year, i)
    return days % 7 == 0


if __name__ == "__main__":
    assert is_first_sunday(2019, 9)
    count = 0
    for year in range(1901, 2000 + 1):
        for month in range(1, 12 + 1):
            if is_first_sunday(year, month):
                count += 1
    print(count)

