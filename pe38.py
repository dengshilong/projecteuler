from common import is_pandigital


def max_pandigital_multiple(n):
    result = 0
    p = int(9 / n)
    for i in range(10 ** (p - 1), 10 ** p):
        s = ''.join(str(i * j) for j in range(1, n + 1))
        if len(s) > 9:
            break
        if is_pandigital(s, 9) and int(s) > result:
            result = int(s)
    return result


if __name__ == "__main__":
    print(max(max_pandigital_multiple(i) for i in range(2, 10)))
