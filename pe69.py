from common import get_primes


if __name__ == "__main__":
    n = 1000000
    primes = get_primes(n)
    p = 1
    for i in primes:
        if p * i > n:
            break
        p = p * i
    print(p)


