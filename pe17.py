
NUMBER = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

UNIT = {
    100: 'husdred',
    1000: 'thousand'
}


def transfor_number(n):
    return _transfor_number(n, 1000)


def _transfor_number(n, unit):
    if n in NUMBER:
        return NUMBER[n]
    if n < 100:
        return NUMBER[int(n / 10) * 10] + "-" + NUMBER[n % 10]
    if n >= unit:
        temp = NUMBER[int(n / unit)] + " " + UNIT[unit]
        if n % unit == 0:
            return temp
        return temp + " and " + _transfor_number(n % unit, int(unit / 10))
    else:
        return _transfor_number(n, int(unit / 10))


def letter_length(number):
    return len([c for c in number if c != ' ' and c != '-'])


if __name__ == "__main__":
    assert(letter_length(transfor_number(342)) == 23)
    assert(letter_length(transfor_number(115)) == 20)
    n = 1000
    for i in range(1, n + 1):
        print(i, transfor_number(i), letter_length(transfor_number(i)))
    print(sum([letter_length(transfor_number(i)) for i in range(1, n + 1)]))
