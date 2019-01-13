

def power_digit_sum(a, b):
    s = a ** b
    return sum(int(i) for i in str(s))

if __name__ == "__main__":
    n = 100
    print(max(power_digit_sum(a, b) for a in range(1, n) for b in range(1, n)))
