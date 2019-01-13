from common import product_n


def combinatoric(n, r):
    return int(product_n(n) / (product_n(r) * product_n(n - r)))

if __name__ == "__main__":
    assert combinatoric(5, 3) == 10
    assert combinatoric(23, 10) >= 10 ** 6
    x = 100
    print(len([combinatoric(n, r) for n in range(1, x + 1) for r in range(1, n + 1) if combinatoric(n, r) > 10 ** 6]))