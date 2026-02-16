import sys
input = sys.stdin.readline

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

N, M = map(int, input().split())
parents = [i for i in range(N + 1)]

edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

edges.sort(key=lambda x: x[2])

result = 0
cnt = 0

for u, v, w in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        result += w
        cnt += 1

        if cnt == N - 2:
            break

if N == 2:
    print(0)
else:
    print(result)