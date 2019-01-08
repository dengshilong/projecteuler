def spiral_diagonal(n):
    assert(n % 2 == 1)
    a = [i * i for i in range(1, n + 1, 2)]
    b = [i * i - i + 1 for i in range(1, n + 1, 2)]
    c = [i * i + 1 for i in range(0, n, 2)]
    d = [i * i - i + 1 for i in range(0, n, 2)]
    return sum(a) + sum(b) + sum(c) + sum(d) - 3

if __name__ == "__main__":
    assert(spiral_diagonal(5) == 101)
    print(spiral_diagonal(1001))
