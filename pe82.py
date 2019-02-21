
def load_data(filename):
    with open(filename) as f:
        return [[int(i) for i in line.strip().split(',')] for line in f]

def min_path_sum(board):
    length = len(board)
    result = [[0] * length for i in range(0, length)]
    for i in range(0, length):
        result[i][0] = board[i][0]

    for j in range(1, length):
        for i in range(0, length):
            result[i][j] = board[i][j] + result[i][j - 1]
        for i in range(0, length):
            if i - 1 >= 0:
                result[i][j] = min(result[i][j], result[i - 1][j] + board[i][j])
            if i + 1 < length:
                result[i][j] = min(result[i][j], result[i + 1][j] + board[i][j])
        for i in range(length - 1, 0, -1):
            if i - 1 >= 0:
                result[i][j] = min(result[i][j], result[i - 1][j] + board[i][j])
            if i + 1 < length:
                result[i][j] = min(result[i][j], result[i + 1][j] + board[i][j])
    res = result[0][length - 1]
    for i in range(1, length):
        res = min(res, result[i][length - 1])
    return res


if __name__ == "__main__":
    board = [[131, 673, 234, 103, 18],
             [201, 96, 342, 965, 150],
             [630, 803, 746, 422, 111],
             [537, 699, 497, 121, 956],
             [805, 732, 524, 37, 331]]
    assert min_path_sum(board) == 994
    board = load_data('pe82.txt')
    print(min_path_sum(board))

