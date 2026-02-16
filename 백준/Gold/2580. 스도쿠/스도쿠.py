import sys

def solve():
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    zeros = []
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                zeros.append((y, x))

    def is_possible(y, x, num):
        for i in range(9):
            if board[y][i] == num:
                return False

        for i in range(9):
            if board[i][x] == num:
                return False

        s_row = (y // 3) * 3
        s_col = (x // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[s_row + i][s_col + j] == num:
                    return False
        return True

    def dfs(index):
        if index == len(zeros):
            for row in board:
                print(*row)
            sys.exit(0)

        y, x = zeros[index]

        for num in range(1, 10):
            if is_possible(y, x, num):
                board[y][x] = num
                dfs(index + 1)
                board[y][x] = 0
    dfs(0)

solve()