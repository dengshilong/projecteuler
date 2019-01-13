

if __name__ == "__main__":
    n = 10 ** 7
    pentagonal = set(int(i * (3 * i - 1) / 2) for i in range(1, n))
    hexagonal = set(i * (2 * i - 1) for i in range(1, n))
    i = 286
    while True:
        t = int(i * (i + 1) / 2)
        if t in pentagonal and t in hexagonal:
            print(t)
            break
        i += 1
