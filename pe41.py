from common import is_pandigital, get_primes

if __name__ == "__main__":
    """8位和9位的数能被3整除，所以直接找从7位的开始找, 7位的直接从7开头的开始找"""
    n = 10 ** 6 * 8
    PRIMES = set(get_primes(n))
    while True:
        if n in PRIMES and is_pandigital(n, 7):
            break
        n -= 1
    print(n)
