
def name_score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)

if __name__ == "__main__":
    print(name_score("COLIN"))
    data = ''
    with open('pe22.txt') as f:
        data = f.read()
        data = ''.join(c for c in data.strip() if c != '"')
    names = data.split(",")
    names.sort()
    for i in range(len(names)):
        print(i + 1, names[i], name_score(names[i]))
    print(sum((i + 1) * name_score(names[i]) for i in range(len(names))))
