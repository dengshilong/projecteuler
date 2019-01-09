
def is_fifth_power(n):
    return n != 1 and n == sum(int(i) ** 5 for i in str(n))


if __name__ == "__main__":
    print(sum(i for i in range(1, 10 ** 5 * 5) if is_fifth_power(i)))
