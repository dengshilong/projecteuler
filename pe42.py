from common import load_names, name_score

if __name__ == "__main__":
    triangle_numbers = set([int(i * (i + 1) / 2) for i in range(1, 100)])
    names = load_names('pe42.txt')
    print(len([name for name in names if name_score(name) in triangle_numbers]))