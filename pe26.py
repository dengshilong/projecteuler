def reciprocal_cycle(n):
    s = dict()
    factor = []
    remainder = 1
    i = 1
    while True:
        if remainder < n:
            if remainder in s:
                return i - s[remainder]
            s[remainder] = i
            remainder *= 10
        f = int(remainder / n)
        factor.append(f)
        if remainder % n == 0:
            return 0
        else:
            remainder = remainder % n
        i += 1


if __name__ == "__main__":
    n = 1000
    maximum = 0
    result = 0
    for i in range(1, n):
        temp = reciprocal_cycle(i)
        if temp > maximum:
            maximum = temp
            result = i
    print(result, maximum)


