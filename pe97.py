from common import power_mod

if __name__ == "__main__":
    n = 10 ** 10
    print((28433 * power_mod(2, 7830457, n) + 1) % n)
