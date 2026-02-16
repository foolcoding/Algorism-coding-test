import sys
from collections import deque
input = sys.stdin.readline

def solve():
    group = [[0] * m for _ in range(n)]
    group_size = [0]      # 0번 인덱스는 사용 안 함
    bound = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 1) 0 영역을 그룹핑 + 크기 저장
    gid = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 and group[i][j] == 0:
                gid += 1
                q = deque()
                q.append((i, j))
                group[i][j] = gid
                cnt = 1

                while q:
                    x, y = q.popleft()
                    for dx, dy in bound:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if arr[nx][ny] == 0 and group[nx][ny] == 0:
                                group[nx][ny] = gid
                                q.append((nx, ny))
                                cnt += 1

                group_size.append(cnt)

    # 2) 각 칸에 대해 결과 계산
    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:   # 벽인 칸만 계산
                adj_groups = set()
                for dx, dy in bound:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        g = group[nx][ny]
                        if g != 0:
                            adj_groups.add(g)

                total = 1  # 자기 자신 포함
                for g in adj_groups:
                    total += group_size[g]
                res[i][j] = total % 10
            else:
                res[i][j] = 0

    out_lines = []
    for i in range(n):
        out_lines.append(''.join(str(res[i][j]) for j in range(m)))
    print('\n'.join(out_lines))

n, m = map(int, input().split())
# arr = [list(input()) for _ in range(n)]
arr = [list(map(int, input().strip())) for _ in range(n)]
solve()
