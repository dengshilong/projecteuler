

"""经过观察，d[6]一定等于5，d[7] > 5"""
if __name__ == "__main__":
    n = 10
    x = [0] * (n + 1)
    x[6] = 5    # d[6]
    used = {5}
    result = []
    for a in [1, 2, 3, 6, 7, 8, 9]:   # d[7], d[8]
        if a <= 3:
            x[7] = a
            x[8] = a + 6
        else:
            x[7] = a
            x[8] = a - 5
        used.add(x[7])
        used.add(x[8])
        for b in range(0, n):   # 算d[9]
            if b in used:
                continue
            if (x[7] * 100 + x[8] * 10 + b) % 13 != 0:
                continue
            used.add(b)
            x[9] = b
            for c in range(0, n):   # d[10]
                if c in used:
                    continue
                if (x[8] * 100 + x[9] * 10 + c) % 17 != 0:
                    continue
                used.add(c)
                x[10] = c
                for d in range(0, n):    # d[5]
                    if d in used:
                        continue
                    if (d * 100 + x[6] * 10 + x[7]) % 7 != 0:
                        continue
                    used.add(d)
                    x[5] = d
                    for e in range(0, n, 2):    # d[4]
                        if e in used:
                            continue
                        used.add(e)
                        x[4] = e
                        for f in range(0, n):   # d[3]
                            if f in used:
                                continue
                            if (f * 100 + x[4] * 10 + x[5]) % 3 != 0:
                                continue
                            used.add(f)
                            x[3] = f
                            for g in range(1, n):   # d[1]
                                if g in used:
                                    continue
                                used.add(g)
                                x[1] = g
                                for h in range(0, n):   # d[2]
                                    if h in used:
                                        continue
                                    x[2] = h
                                    result.append(int(''.join([str(x[i]) for i in range(1, n + 1)])))
                                used.remove(g)
                            used.remove(f)
                        used.remove(e)
                    used.remove(d)
                used.remove(c)
            used.remove(b)
        used.remove(x[7])
        used.remove(x[8])
    print(result)
    print(sum(result))







