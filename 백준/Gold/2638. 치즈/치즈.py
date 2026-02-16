import sys
from collections import deque
input = sys.stdin.readline

bound = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def marking_air():
    # 바깥 공기를 True로 표시
    outside = [[False] * m for _ in range(n)]
    q = deque([(0, 0)])
    outside[0][0] = True

    while q:
        y, x = q.popleft()
        for dy, dx in bound:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                # 치즈는 통과 못하고, 공기만 이어짐
                if not outside[ny][nx] and lista[ny][nx] == 0:
                    outside[ny][nx] = True
                    q.append((ny, nx))
    return outside

def solve():
    hours = 0
    while True:
        # 아직 치즈가 남아있는지 확인
        has_cheese = False
        for row in lista:
            if 1 in row:
                has_cheese = True
                break

        # 치즈 없으면 끝
        if not has_cheese:
            print(hours)
            return

        # 1) 바깥 공기 마킹
        outside = marking_air()

        # 2) 녹일 치즈 찾기: 바깥 공기와 접한 면이 2 이상인 칸
        to_melt = []
        for y in range(n):
            for x in range(m):
                if lista[y][x] == 1:
                    touch = 0
                    for dy, dx in bound:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < m and outside[ny][nx]:
                            touch += 1
                    if touch >= 2:
                        to_melt.append((y, x))

        # 3) 한 시간에 동시에 녹이기
        for y, x in to_melt:
            lista[y][x] = 0
        hours += 1

n, m = map(int, input().split())
lista = [list(map(int, input().split())) for _ in range(n)]
solve()
