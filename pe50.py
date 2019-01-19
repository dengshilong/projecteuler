from common import get_primes

n = 10 ** 6


def solution(n):
    primes = get_primes(n)
    prime_set = set(primes)
    length = len(primes)

    a = [0] * length
    begin = 0
    s = primes[0]
    while s < n:
        begin += 1
        s += primes[begin]
    i = length - begin - 1
    for j in range(0, i):
        a[j] = sum(primes[j: length - i + j])
    print(sum(primes[:begin]), sum(primes[:begin - 1]), sum(primes[:begin - 2]))
    while True:
        print(a[:10])
        for j in range(i + 1, -1, -1):
            if j == i + 1:
                a[j] = a[j - 1] - primes[i]
            else:
                a[j] = a[j] - primes[length - i - 1 + j]
        if a[0] > n:
            i += 1
            continue
        for j in range(0, i + 1):
            if a[j] in prime_set:
                return a[j]
        i += 1


if __name__ == "__main__":
    print(solution(n))
