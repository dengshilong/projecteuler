from common import get_primes, origin_sequence


def find_solution(n, start=1):
    primes = get_primes(10 ** n)
    prime_set = set(primes)
    for i in primes:
        if i <= start:
            continue
        for j in range(1, int(10 ** (n - 1) * 9 / 2)):
            if i + j > 10 ** n or i + 2 * j > 10 ** n or i + j not in prime_set or i + 2 * j not in prime_set or \
                    origin_sequence(i) != origin_sequence(i + j) or origin_sequence(i) != origin_sequence(i + 2 * j):
                continue
            return str(i) + str(i + j) + str(i + 2 * j)
    return 0

if __name__ == "__main__":
    assert find_solution(4) == str(148748178147)
    print(find_solution(4, 1487))




