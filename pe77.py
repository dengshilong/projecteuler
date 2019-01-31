from common import get_primes
n = 10 ** 5
COINS = get_primes(n)


summation = {}
def prime_summation(n):
    return _prime_summation(n, n)


def _prime_summation(n, maximum):
    key = '{}-{}'.format(n, maximum)
    if key in summation:
        return summation[key]
    if n < 0:
        return 0
    if n == 0:
        return 1
    value = sum(_prime_summation(n - i, i) for i in COINS if i <= maximum)
    summation[key] = value
    return value


if __name__ == "__main__":
    assert prime_summation(10) == 5
    for i in range(1, n):
        if prime_summation(i) >= 5000:
            print(i)
            break

