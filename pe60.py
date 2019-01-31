from common import get_primes, is_prime


def connect(a, b):
    return int(str(a) + str(b))


def _solution(primes, begin, present, k):
    if len(present) == 0:
        present.append(primes[begin])
        _solution(primes, begin + 1, present, k)
    if len(present) == k:
        return present
    for i in range(begin, len(primes)):
        flag = True
        for j in range(0, len(present)):
            if not is_prime(connect(primes[i], present[j])) or not is_prime(connect(present[j], primes[i])):
                flag = False
                break
        if flag:
            present.append(primes[i])
            result = _solution(primes, i + 1, present, k)
            if result:
                return result
            present.pop()


def solution(primes, k):
    for i in range(0, len(primes)):
        present = [primes[i]]
        result = _solution(primes, i + 1, present, k)
        if result:
            return result
        present.pop()




if __name__ == "__main__":
    n = 10000
    primes = get_primes(n)
    assert solution(primes, 4) == [3, 7, 109, 673]
    result = solution(primes, 5)
    print(result, sum(result))



