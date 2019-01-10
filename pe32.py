import math


def is_pandigital(n, m):
    if len(str(n)) != m:
        return False
    for i in range(1, m + 1):
        if str(i) not in str(n):
            return False
    return True


if __name__ == "__main__":
    maximum = 10 ** 10
    n = 10000
    s = set()
    for i in range(1, int(math.sqrt(math.sqrt(maximum)))):
        for j in range(i + 1, min(int(math.sqrt(maximum / i ** 2)), n)):
            if is_pandigital(int(str(i) + str(j) + str(i * j)), 9):
                s.add(i * j)
    print(sum(s))

