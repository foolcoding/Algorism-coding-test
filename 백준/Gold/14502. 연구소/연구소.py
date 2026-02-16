from collections import deque
from itertools import combinations
import copy
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

emt = []
vir = []
for y in range(n):
    for x in range(m):
        if lab[y][x] == 0:
            emt.append((y, x))
        elif lab[y][x] == 2:
            vir.append((y, x))

bound = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 벽의 모든 경우를 다 뽑아서 그때의 안전구역을 다 구해서 제일 안전구역 큰거 리턴
def bfs(walls):
    board = [row.copy() for row in lab]
    for y, x in walls:
        board[y][x] = 1

    q = deque(vir)
    while q:
        y, x = q.popleft()
        for dy, dx in bound:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
                board[ny][nx] = 2
                q.append((ny, nx))

    # 남은 안전 영역 개수
    safe = 0
    for row in board:
        safe += row.count(0)
    return safe

result = 0
for walls in combinations(emt, 3):
    # 모든 경우에 벽 세워보기
    result = max(result, bfs(walls))

print(result)