from common import prime_factor, get_primes

PRIMES = set(get_primes(10 ** 8))


def find_smallest(t):
    i = 1
    while True:
        if i in PRIMES:
            i += 1
            continue
        flag = True
        for j in range(0, t):
            if i + j in PRIMES or len(prime_factor(i + j)) != t:
                flag = False
                break
        if flag:
            return i
        i += 1


if __name__ == "__main__":
    assert find_smallest(2) == 14
    assert find_smallest(3) == 644
    print(find_smallest(4))