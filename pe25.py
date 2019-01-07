def fibonacci():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b



if __name__ == "__main__":
    for i, value in enumerate(fibonacci()):
        if len(str(value)) >= 1000:
            print(i + 1, value)
            break
