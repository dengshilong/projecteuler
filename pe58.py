from common import is_prime

if __name__ == "__main__":
    assert is_prime(221) == False
    assert is_prime(1478657) == False
    assert is_prime(1467733) == False
    n = 3
    total = 1
    count = 0
    while True:
        total += 4
        for x in [n ** 2 - n + 1, (n - 1) ** 2 + 1, (n - 1) ** 2 - (n - 1) + 1]:
            if is_prime(x):
                count += 1
        if count / total < 0.1:
            print(n)
            exit()
        n += 2
