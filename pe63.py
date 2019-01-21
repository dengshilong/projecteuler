

if __name__ == "__main__":
    n = 100
    print(len([i ** j for i in range(1, 100) for j in range(1, 100) if len(str(i ** j)) == j]))
