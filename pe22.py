from common import load_names, name_score

if __name__ == "__main__":
    assert name_score("COLIN") == 53
    names = load_names('pe22.txt')
    names.sort()
    print(sum((i + 1) * name_score(names[i]) for i in range(len(names))))
