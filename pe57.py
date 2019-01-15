
root_convergent = {}


def square_root_convergent(n):
    numerator, denominator = _square_root_convergent(n)
    return (denominator + numerator, denominator)


def _square_root_convergent(n):
    if n in root_convergent:
        return root_convergent[n]
    if n == 1:
        root_convergent[1] = (1, 2)
        return root_convergent[1]
    numerator, denominator = _square_root_convergent(n - 1)
    numerator, denominator = denominator, 2 * denominator + numerator
    root_convergent[n] = (numerator, denominator)
    return root_convergent[n]



if __name__ == "__main__":
    assert square_root_convergent(1) == (3, 2)
    assert square_root_convergent(2) == (7, 5)
    n = 1000
    count = 0
    for i in range(1, n + 1):
        a, b = square_root_convergent(i)
        if len(str(a)) > len(str(b)):
            count += 1
    print(count)
