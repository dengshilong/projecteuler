

if __name__ == "__main__":
    n = 100
    print(len(set([i ** j for i in range(2, n + 1) for j in range(2, n + 1)])))