from common import get_primes

PRIMES = set(get_primes(10000000))
def quadratic_prime(a, b):
    i = 0
    while True:
        s = i ** 2 + a * i + b
        if s not in PRIMES:
            return i
        i += 1

if __name__ == "__main__":
    n = 1000
    a = 0
    b = 0
    maximum = 0
    for i in range(-n + 1, n):
        for j in range(-n, n + 1):
            print(i, j)
            temp = quadratic_prime(i, j)
            if temp > maximum:
                maximum = temp
                a = i
                b = j
    print(a, b, a * b)

