
if __name__ == "__main__":
    with open('pe13.txt') as f:
        print(str(sum([int(line.strip()) for line in f]))[:10])