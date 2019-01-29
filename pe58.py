import random


def power_mod(a, b, m):
    r = 1
    while b:
        if b & 1:
            r = r * a % m
        a = a * a % m
        b >>= 1
    return r


def witness(n, r, d, a):
    x = power_mod(a, d, n)
    if x == 1 or x == n - 1:
        return False
    while r > 0:
        x = x ** 2 % n
        if x == n - 1:
            return False
        r -= 1
    return True


def miller_labin(n, k=5):
    if n <= 1:
        return False
    r = 0
    d = n - 1
    while d & 1 == 0:
        d = d >> 1
        r += 1
    while k > 0:
        a = random.randint(2, n - 1)
        if witness(n, r, d, a):
            return False
        k -= 1
    return True


if __name__ == "__main__":
    assert miller_labin(221) == False
    assert miller_labin(1478657) == False
    assert miller_labin(1467733) == False
    n = 3
    total = 1
    count = 0
    while True:
        total += 4
        for x in [n ** 2 - n + 1, (n - 1) ** 2 + 1, (n - 1) ** 2 - (n - 1) + 1]:
            if miller_labin(x):
                count += 1
        if count / total < 0.1:
            print(n)
            exit()
        n += 2
