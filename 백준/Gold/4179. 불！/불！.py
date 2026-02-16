import sys
from collections import deque
input = sys.stdin.readline

def solve():
    R, C = map(int, input().split())
    lista = [list(input()) for _ in range(R)]

    INF = float("inf")
    fire = [[INF] * C for _ in range(R)]
    qa = deque()
    jy = jx = -1

    for y in range(R):
        for x in range(C):
            if lista[y][x] == 'F':
                fire[y][x] = 0
                qa.append((y, x))
            elif lista[y][x] == 'J':
                jy, jx = y, x

    # 각칸에 불이 도달하는 시간
    bound = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while qa:
        y, x = qa.popleft()
        for dy, dx in bound:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                if lista[ny][nx] != '#' and fire[ny][nx] == INF:
                    fire[ny][nx] = fire[y][x] + 1
                    qa.append((ny, nx))

    # 불보다 먼저 도달 가능한 칸
    qb = deque()
    qb.append((jy, jx, 0))
    visited = [[False] * C for _ in range(R)]
    visited[jy][jx] = True

    # 시작이 가장자리에 있으면 1분 만에 탈출 가능
    # if jy == 0 or jx == R-1 or jx == 0 or jx == C-1:
    #     print(1)
    #     return

    while qb:
        y, x, t = qb.popleft()

        for dy, dx in bound:
            ny, nx = y + dy, x + dx
            nt = t + 1

            if not (0 <= ny < R and 0 <= nx < C):
                print(nt)
                return

            # 벽이 아니고, 아직 방문 안 했고, 불보다 먼저 도착 가능해야 함
            if lista[ny][nx] != '#' and not visited[ny][nx] and nt < fire[ny][nx]:
                visited[ny][nx] = True
                qb.append((ny, nx, nt))

    print("IMPOSSIBLE")

solve()
