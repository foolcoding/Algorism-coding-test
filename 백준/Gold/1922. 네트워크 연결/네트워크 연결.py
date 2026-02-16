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
        return False
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry
    return True

V = int(input())
E = int(input())

parents = [i for i in range(V + 1)]
edges = []

for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])

cnt = 0
result = 0

for u, v, w in edges:
    if union(u, v):
        cnt += 1
        result += w
        if cnt == V - 1:
            break

print(result)
