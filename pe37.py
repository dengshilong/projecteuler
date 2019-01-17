from common import get_primes

n = 10 ** 7
primes = set(get_primes(n))

def truncatable_prime(n):
    n = str(n)
    for i in range(1, len(n)):
        if int(n[0:i]) not in primes:
            return False
        if int(n[-i:]) not in primes:
            return False
    return int(n) in primes


if __name__ == "__main__":
    assert truncatable_prime(3797) == True
    s = [i for i in range(10, n) if truncatable_prime(i)]
    print(s, sum(s))