COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def coin_sum(n):
    return _coin_sum(n, n)


def _coin_sum(n, maximum):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return sum(_coin_sum(n - i, i) for i in COINS if i <= maximum)


if __name__ == "__main__":
    assert(coin_sum(3) == 2)
    assert(coin_sum(4) == 3)
    assert(coin_sum(5) == 4)
    print(coin_sum(200))
