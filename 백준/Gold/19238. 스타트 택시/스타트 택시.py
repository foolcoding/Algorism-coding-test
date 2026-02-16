import sys
from collections import deque
input = sys.stdin.readline

bound = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def bfs(start_y, start_x, board, n):
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((start_y, start_x))
    dist[start_y][start_x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + bound[i][0], x + bound[i][1]
            if 0 <= ny < n and 0 <= nx < n and dist[ny][nx] == -1 and board[ny][nx] != 1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
    return dist

def find_person(taxi_y, taxi_x, board, n):
    dist = bfs(taxi_y, taxi_x, board, n)

    best_d = float('inf')
    best_y = best_x = -1
    best_id = -1

    for y in range(n):
        for x in range(n):
            pid = board[y][x]
            if pid >= 2 and dist[y][x] != -1:  # 승객이 있고 도달 가능
                d = dist[y][x]
                if d < best_d or (d == best_d and (y < best_y or (y == best_y and x < best_x))):
                    best_d = d
                    best_y, best_x = y, x
                    best_id = pid

    if best_id == -1:
        return -1, -1, -1, -1
    return best_id, best_y, best_x, best_d

def solve():
    N, M, fuel = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ty, tx = map(int, input().split())
    ty -= 1
    tx -= 1

    # 승객 번호 2번부터 하나씩 채우기
    # 승객 출발지만 원본 배열에 넣고
    # 도착지는 딕셔너리에 저장하기
    # 배열 한게에 다 넣으면 복잡하니깐?
    # 인덱스 바운드 에러나고 복잡해서 난리남
    dests = {}
    for num in range(2, M+2):
        sy, sx, dy, dx = map(int, input().split())
        sy -= 1
        sx -= 1
        dy -= 1
        dx -= 1
        board[sy][sx] = num
        dests[num] = (dy, dx)

    for _ in range(M):
        # 1. 가까운 승객 찾기
        num, py, px, d1 = find_person(ty, tx, board, N)
        if num == -1 or d1 > fuel:  # 승객이 없거나, 승객까지 못 감
            print(-1)
            return
        # 승객 태우러 이동
        fuel -= d1
        ty, tx = py, px

        # 2) 목적지까지 이동
        dy, dx = dests[num]
        dist = bfs(ty, tx, board, N)
        d2 = dist[dy][dx]
        if d2 == -1 or d2 > fuel:  # 목적지 도달 불가 또는 연료 부족
            print(-1)
            return

        # 목적지 도착: 연료 보상 (이동거리의 2배 충전 → 이미 d2 소모했으니 순증가 d2)
        fuel -= d2
        fuel += (2 * d2)

        # 택시 위치 업데이트, 승객 제거
        ty, tx = dy, dx
        board[py][px] = 0  # 태웠던 출발칸의 승객 제거

    print(fuel)

solve()
