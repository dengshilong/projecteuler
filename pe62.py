from collections import defaultdict

from common import origin_sequence

if __name__ == "__main__":
    n = 100
    smallest = {}
    origin_count = defaultdict(int)
    while True:
        t = n ** 3
        origin = origin_sequence(t)
        if origin not in smallest:
            smallest[origin] = t
        origin_count[origin] += 1
        if origin_count[origin] == 5:
            print(smallest[origin])
            break
        n += 1
