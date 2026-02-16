import sys
from collections import deque
input = sys.stdin.readline

def solve():
    # 레이저 찾기
    cs = []
    for i in range(h):
        for j in range(w):
            if lista[i][j] == 'C':
                cs.append((i, j))
    (sx, sy), (ex, ey) = cs

    # 상우하좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    INF = float("inf")
    dist = [[[INF] * 4 for _ in range(w)] for _ in range(h)]

    dq = deque()
    # 시작 위치는 4방향 다 거울 0개
    for d in range(4):
        dist[sx][sy][d] = 0
        dq.append((sx, sy, d))

    while dq:
        x, y, d = dq.popleft()
        cur = dist[x][y][d]

        if cur > dist[x][y][d]:
            continue

        # 전진
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < h and 0 <= ny < w and lista[nx][ny] != '*':
            if dist[nx][ny][d] > cur:
                dist[nx][ny][d] = cur
                dq.appendleft((nx, ny, d))

        # 90도 회전
        for nd in ((d + 1) % 4, (d + 3) % 4):
            nx = x + dx[nd]
            ny = y + dy[nd]
            if 0 <= nx < h and 0 <= ny < w and lista[nx][ny] != '*':
                cost = cur + 1
                if dist[nx][ny][nd] > cost:
                    dist[nx][ny][nd] = cost
                    dq.append((nx, ny, nd))

    answer = min(dist[ex][ey])
    print(answer)

w, h = map(int, input().split())
lista = [list(input()) for _ in range(h)]
solve()
