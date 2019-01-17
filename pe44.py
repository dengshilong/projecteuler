
def pentagon_number(n):
    return int(n * (3 * n - 1) / 2)


def get_pentagon_number(n):
    return [pentagon_number(i) for i in range(1, n + 1)]


if __name__ == "__main__":
    n = 10 ** 4
    minimum = 10 ** 10
    pentagons = set(get_pentagon_number(n))
    for i in range(1, n):
        a = pentagon_number(i)
        for j in range(i + 1, n):
            b = pentagon_number(j)
            if b - a in pentagons and b + a in pentagons:
                minimum = min(minimum, b - a)
    print(minimum)

