

def right_triangle(p):
    count = 0
    for i in range(1, int(p / 3)):
        for j in range(i, int(p / 2)):
            if i ** 2 + j ** 2 == (p - i - j) ** 2:
                count += 1
    return count


if __name__ == "__main__":
    assert right_triangle(120) == 3
    n = 1000
    maximum = 0
    p = 0
    for i in range(1, n + 1):
        temp = right_triangle(i)
        if temp > maximum:
            maximum = temp
            p = i
    print(p, maximum)