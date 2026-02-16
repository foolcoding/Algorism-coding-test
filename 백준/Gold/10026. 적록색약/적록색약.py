from collections import deque

def blind_check(c1, c2, blind):
    if not blind:
        return c1 == c2
    if (c1 in ('R', 'G')) and (c2 in ('R', 'G')):
        return True
    return c1 == c2

def solve(n, arr, blind):
    bound = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0] * n for _ in range(n)]

    result = 0
    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                continue
            result += 1
            color = arr[y][x]
            q = deque([(y, x)])
            visited[y][x] = True

            while q:
                cy, cx = q.popleft()
                for dy, dx in bound:
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                        if blind_check(color, arr[ny][nx], blind):
                            visited[ny][nx] = True
                            q.append((ny, nx))
    return result

n = int(input())
arr = [input() for _ in range(n)]
result = solve(n, arr, False)
result_blind = solve(n, arr, True)
print(result, result_blind)