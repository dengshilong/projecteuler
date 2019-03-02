
one = {1}
other = {89}

def in_one(n):
    if n in one:
        return True
    if n in other:
        return False
    s = [n]
    while True:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in one:
            for i in s:
                one.add(i)
            return True
        elif n in other:
            for i in s:
                other.add(i)
            return False
        else:
            s.append(n)


if __name__ == "__main__":
    assert in_one(44) == True
    assert in_one(85) == False
    count = 0
    for i in range(1, 10 ** 7):
        flag = in_one(i)
        if not flag:
            count += 1
    print(count)
