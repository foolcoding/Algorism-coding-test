import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float("inf")

def dijkstra(start, graph, n):
    best = [INF] * (n + 1)
    best[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if d != best[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < best[v]:
                best[v] = nd
                heappush(pq, (nd, v))
    return best

def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a].append((b, c))
        g[b].append((a, c))

    v1, v2 = map(int, input().split())

    dist1 = dijkstra(1, g, n)
    distv1 = dijkstra(v1, g, n)
    distv2 = dijkstra(v2, g, n)

    path1 = dist1[v1] + distv1[v2] + distv2[n]
    path2 = dist1[v2] + distv2[v1] + distv1[n]
    result = min(path1, path2)

    print(result if result < INF else -1)

solve()