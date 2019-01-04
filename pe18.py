
def load_data():
    with open('pe18.txt') as f:
        return [[int(i) for i in line.strip().split(' ')] for line in f]

def max_path_sum(board):
    depth = len(board[len(board) - 1])
    s = [0] * (len(board[len(board) - 1]) + 1)
    for i in range(depth - 1, -1, -1):
        for j in range(0, len(board[i])):
            s[j] = max(board[i][j] + s[j], board[i][j] + s[j + 1])
    return s[0]

if __name__ == "__main__":
    board = load_data()
    print(max_path_sum(board))

