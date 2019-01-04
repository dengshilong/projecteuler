
def collatz_sequence(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1
    return count


if __name__ == "__main__":
    m = 0
    result = 0
    for i in range(1, 1000000):
        c = collatz_sequence(i)
        if c > m:
            m = c
            result = i
        print(i, c, result)

    print(result, m)



