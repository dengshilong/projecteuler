
def load_data():
    with open('pe11.txt') as f:
        board = [[int(d) for d in line.strip().split(' ')] for line in f]
        return board

def find_max_product_continuous(board, num):
    x = len(board)
    y = len(board[0])
    result = 0
    for i in range(x):
        for j in range(y):
            if j + num <= y:    # 横线
                p = 1
                for k in range(num):
                    p *= board[i][j + k]
                result = max(p, result)
            if i + num <= x:    # 竖线
                p = 1
                for k in range(num):
                    p *= board[i + k][j]
                result = max(p, result)
            if i + num <= x and j + num <= y:   # 左上右下对角线
                p = 1
                for k in range(num):
                    p *= board[i + k][j + k]
                result = max(p, result)
            if i - num >= 0 and j + num <= y:   # 左下右上对角线
                p = 1
                for k in range(num):
                    p *= board[i - k][j + k]    
                result = max(p, result)
    return result


if __name__ == "__main__":
    board = load_data()
    print(find_max_product_continuous(board, 4))
