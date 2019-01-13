

if __name__ == "__main__":
    d = [10 ** i for i in range(0, 7)]
    p = 1
    total = 0
    j = 0
    i = 1
    while j < len(d):
        if total + len(str(i)) >= d[j]:
            p *= int(str(i)[d[j] - total - 1])
            if total + len(str(i)) == d[j]:
                total += len(str(i))
                i += 1
            j += 1
        else:
            total += len(str(i))
            i += 1
    print(p)
