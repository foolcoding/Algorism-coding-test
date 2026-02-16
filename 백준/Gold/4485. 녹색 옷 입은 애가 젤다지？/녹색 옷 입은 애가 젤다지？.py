import sys, heapq

def solve():
    input = sys.stdin.readline
    case_no = 1
    while True:
        n = int(input().strip())
        if n == 0:
            break

        grid = [list(map(int, input().split())) for _ in range(n)]
        best = [[float("inf")] * n for _ in range(n)]
        best[0][0] = grid[0][0]

        pq = [(grid[0][0], 0, 0)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            cost, y, x = heapq.heappop(pq)

            if cost != best[y][x]:
                continue

            if (y, x) == (n - 1, n - 1):
                break

            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n:
                    nc = cost + grid[ny][nx]
                    if nc < best[ny][nx]:
                        best[ny][nx] = nc
                        heapq.heappush(pq, (nc, ny, nx))

        print(f"Problem {case_no}: {best[n-1][n-1]}")
        case_no += 1

solve()