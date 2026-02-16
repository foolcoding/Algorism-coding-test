import sys, heapq
input = sys.stdin.readline

def solve():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                sy, sx = i, j
                board[i][j] = 0
                break

    size = 2
    eaten = 0
    time_spent = 0
    bound = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    while True:
        pq = [(0, sy, sx)]
        visited = [[False] * N for _ in range(N)]
        found = None

        while pq:
            dist, y, x = heapq.heappop(pq)
            if visited[y][x]:
                continue
            visited[y][x] = True

            # 먹을수 있으면 이미 우선순위
            if 0 < board[y][x] < size:
                found = (dist, y, x)
                break

            for dy, dx in bound:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if board[ny][nx] <= size:
                        heapq.heappush(pq, (dist + 1, ny, nx))

        if not found:              # 더 이상 먹을 물고기 없음
            print(time_spent)
            return

        d, y, x = found
        time_spent += d
        eaten += 1
        board[y][x] = 0
        sy, sx = y, x

        if eaten == size:
            size += 1
            eaten = 0

solve()
