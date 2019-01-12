from common import is_palindrome


def is_double_base_palindrome(n):
    return n > 0 and is_palindrome(str(n)) and is_palindrome(int(bin(n)[2:]))


if __name__ == "__main__":
    assert is_double_base_palindrome(0) == False
    assert is_double_base_palindrome(585) == True
    n = 1000000
    print(sum(i for i in range(1, n) if is_double_base_palindrome(i)))