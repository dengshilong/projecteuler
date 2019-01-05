

def get_divisors(n):
    if n == 1:
        return [1]
    return [i for i in range(1, int(n/2) + 1) if n % i == 0]

if __name__ == "__main__":
    print(get_divisors(220), get_divisors(284))
    print(sum(get_divisors(220)), sum(get_divisors(284)))
    n = 10000
    result = set()
    d = {}
    for i in range(1, n):
        d[i] = sum(get_divisors(i))
    for i in range(1, n):
        if d[i] != i and d[i] < n and d[d[i]] == i:
            result.add(i)
            result.add(d[i])
    print(sum(result))
