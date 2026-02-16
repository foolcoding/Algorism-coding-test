import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

bound = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(y, x):
    # 이미 계산된 적 있으면 바로 반환
    if rem[y][x] != 0:
        return rem[y][x]

    # 최소 1일은 버틸 수 있음
    rem[y][x] = 1

    # 4방향 탐색
    for dy, dx in bound:
        ny = y + dy
        nx = x + dx

        if 0 <= ny < n and 0 <= nx < n:
            if arr[ny][nx] > arr[y][x]:
                rem[y][x] = max(rem[y][x], 1 + dfs(ny, nx))

    return rem[y][x]

def solve():
    answer = 0
    for i in range(n):
        for j in range(n):
            answer = max(answer, dfs(i, j))
    print(answer)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
rem = [[0] * n for _ in range(n)]
solve()