from common import product_n


def is_factorial_digit(n):
    if n == 1 or n == 2:
        return False
    return sum([product_n(int(i)) for i in str(n)]) == n


if __name__ == "__main__":
    assert is_factorial_digit(145) == True
    n = 1
    while product_n(9) * n > 10 ** n:
        n += 1
    print(sum(i for i in range(1, product_n(9) * (n - 1)) if is_factorial_digit(i)))
