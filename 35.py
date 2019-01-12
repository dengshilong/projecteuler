from common import get_primes
MAXIMUM = 1000000
PRIMES = set(get_primes(MAXIMUM))

def is_circular_prime(n):
    for i in range(0, len(str(n))):
        if int(str(n)[i:n] + str(n)[0:i]) not in PRIMES:
            return False
    return True

if __name__ == "__main__":
    assert is_circular_prime(719) == True
    n = 1000000
    print(len([i for i in range(1, n) if is_circular_prime(i)]))



