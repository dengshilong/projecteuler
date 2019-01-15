from common import origin_sequence

if __name__ == "__main__":
    i = 0
    while True:
        flag = True
        for j in range(2, 7):
            if origin_sequence('1' + str(i)) != origin_sequence(int('1' + str(i)) * j):
                flag = False
                break
        if flag:
            print('1' + str(i))
            break
        i += 1

