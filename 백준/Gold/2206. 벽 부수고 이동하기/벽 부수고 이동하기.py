from collections import deque

def solve():
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    visited = [[[0] * 2 for __ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0)])
    bound = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        y, x, b = q.popleft()

        if (y, x) == (n-1, m-1):
            return visited[n-1][m-1][b]
        for dy, dx in bound:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < m): continue
            if arr[ny][nx] == '0' and visited[ny][nx][b] == 0:
                visited[ny][nx][b] = visited[y][x][b] + 1
                q.append((ny, nx, b))

            elif arr[ny][nx] == '1' and visited[ny][nx][1] == 0 and b == 0:
                visited[ny][nx][1] = visited[y][x][b] + 1
                q.append((ny, nx, 1))


    return -1


print(solve())