from common import get_divisors

def can_two_sum(numbers, n):
    i = 0
    j = len(numbers) - 1
    while i <= j:
        if numbers[i] + numbers[j] == n:
            return True
        elif numbers[i] + numbers[j] > n:
            j -= 1
        else:
            i += 1
    return False


if __name__ == "__main__":
    n = 28123
    abundant_number = [i for i in range(1, n + 1) if sum(get_divisors(i)) > i]
    print(abundant_number)
    print(sum([i for i in range(1, n + 1) if not can_two_sum(abundant_number, i)]))
