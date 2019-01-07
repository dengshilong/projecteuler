from common import product_n


def nth_permution(nums, n):
    if n == 0:
        return ''.join(str(i) for i in nums)[::-1]
    s = [i for i in nums]
    p = product_n(len(s) - 1)
    if n % p == 0:
        i = int(n / p)
        x = s[i - 1]
        s.remove(x)
        return str(x) + nth_permution(s, 0)
    elif n < p:
        x = s[0]
        s.remove(x)
        return str(x) + nth_permution(s, n)
    else:
        i = int(n / p)
        x = s[i]
        s.remove(x)
        return str(x) + nth_permution(s, n - i * p)


if __name__ == "__main__":
    assert(nth_permution([0, 1, 2], 2) == '021')
    assert(nth_permution([0, 1, 2, 3], 2) == '0132')
    print(nth_permution([i for i in range(0, 10)], 1000000))
