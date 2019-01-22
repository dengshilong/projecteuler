from common import is_palindrome


def is_lychrel_number(n):
    i = 0
    while i < 50:
        i += 1
        t = n + int(str(n)[::-1])
        if is_palindrome(t):
            return False
        n = t


    return True

if __name__ == "__main__":
    assert is_lychrel_number(349) == False
    assert is_lychrel_number(47) == False
    assert is_lychrel_number(10677) == True
    assert is_lychrel_number(4994) == True
    n = 10 ** 4
    print(len([i for i in range(1, n) if is_lychrel_number(i)]))

