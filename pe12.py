from common import prime_factor


def divisors(n):
    if n == 1:
        return 1
    d = prime_factor(n)
    p = 1
    for v in d.values():
        p *= v + 1
    return p


if __name__ == "__main__":
    result = 1
    n = 1
    while True:
        n += 1
        s = n * (n + 1) / 2
        result = divisors(s)
        if result > 500:
            print(n, s, result, prime_factor(s))
            break
    # for n in range(1, 20):
    #     v = n * (n + 1) / 2
    #     print(v, divisors(v))
