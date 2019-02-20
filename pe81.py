
MAX = 10 ** 10
def load_data(filename):
    with open(filename) as f:
        return [[int(i) for i in line.strip().split(',')] for line in f]

def max_path_sum(board):
    length = len(board)
    new_board = [[board[i][j] for j in range(0, length)] for i in range(0, length)]
    board = new_board
    for i in range(0, length):
        for j in range(0, i + 1):
            temp = MAX
            if i - j - 1 >= 0:
                temp = min(temp, board[i - j - 1][j])
            if j - 1 >= 0:
                temp = min(temp, board[i - j][j - 1])
            if temp != MAX:
                board[i - j][j] += temp
    for k in range(length - 1, 0, -1):
        for m in range(0, k):
            i = length - 1 - m
            j = length - 1 - k + m + 1
            temp = MAX
            if i - 1 >= 0:
                temp = min(temp, board[i - 1][j])
            if j - 1 >= 0:
                temp = min(temp, board[i][j - 1])
            board[i][j] += temp
    return board[length - 1][length - 1]

if __name__ == "__main__":
    board = [[131, 673, 234, 103, 18],
             [201, 96, 342, 965, 150],
             [630, 803, 746, 422, 111],
             [537, 699, 497, 121, 956],
             [805, 732, 524, 37, 331]]
    print(max_path_sum(board))
    assert max_path_sum(board) == 2427
    board = load_data('pe81.txt')
    print(max_path_sum(board))

