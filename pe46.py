import math

from common import get_primes


if __name__ == "__main__":
    n = 10 ** 6
    primes = get_primes(n)
    i = 35
    while True:
        for p in primes:
            if p > i:
                print(i)
                exit()
            t = int((i - p) / 2)
            if t == int(math.sqrt(t)) ** 2:
                break
        i += 2



