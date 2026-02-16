import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 찾기 (두 줄, 첫 칸이 -1)
purifiers = []
for i in range(R):
    if A[i][0] == -1:
        purifiers.append(i)
top = purifiers[0]
bottom = purifiers[1]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def spread():
    """확산 후 새 배열 반환"""
    nxt = [[0] * C for _ in range(R)]
    nxt[top][0] = -1
    nxt[bottom][0] = -1

    for r in range(R):
        for c in range(C):
            if A[r][c] > 0:
                amount = A[r][c] // 5
                if amount == 0:
                    nxt[r][c] += A[r][c]
                    continue

                cnt = 0
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                        nxt[nr][nc] += amount
                        cnt += 1
                nxt[r][c] += A[r][c] - amount * cnt
    return nxt

def operate():
    # 윗부분(반시계)
    # 왼쪽 위로
    for r in range(top - 1, 0, -1):
        A[r][0] = A[r - 1][0]
    # 위쪽 왼쪽으로
    for c in range(0, C - 1):
        A[0][c] = A[0][c + 1]
    # 오른쪽 아래로
    for r in range(0, top):
        A[r][C - 1] = A[r + 1][C - 1]
    # 아래쪽 오른쪽으로
    for c in range(C - 1, 1, -1):
        A[top][c] = A[top][c - 1]
    A[top][1] = 0

    # 아랫부분(시계)
    # 왼쪽 아래로
    for r in range(bottom + 1, R - 1):
        A[r][0] = A[r + 1][0]
    # 아래쪽 왼쪽으로
    for c in range(0, C - 1):
        A[R - 1][c] = A[R - 1][c + 1]
    # 오른쪽 위로
    for r in range(R - 1, bottom, -1):
        A[r][C - 1] = A[r - 1][C - 1]
    # 위쪽 오른쪽으로
    for c in range(C - 1, 1, -1):
        A[bottom][c] = A[bottom][c - 1]
    A[bottom][1] = 0

for _ in range(T):
    A = spread()
    operate()

# 미세먼지 합
total = 0
for r in range(R):
    for c in range(C):
        # 공기청정기 제외
        if A[r][c] > 0:
            total += A[r][c]

print(total)