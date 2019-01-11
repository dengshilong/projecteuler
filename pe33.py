from common import product_number


def cancelling_fraction(n, d):
    if n >= d:
        return False
    if n % 10 == 0 or d % 10 == 0:
        return False
    a = set([int(i) for i in str(n)])
    b = set([int(i) for i in str(d)])
    if len(a) != 2 or len(b) != 2:
        return False
    if len(a.intersection(b)) != 1:
        return False
    x = (a - b).pop()
    y = (b - a).pop()
    return x * d == y * n
    # if x * d == y * n:
    #     print(n, d)
    #     return True
    # return False


if __name__ == "__main__":

    print(product_number([j / i for i in range(10, 100) for j in range(i + 1, 100) if cancelling_fraction(i, j)]))
