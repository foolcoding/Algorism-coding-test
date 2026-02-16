from heapq import heappop, heappush
INF = float("inf")

def daiqk(start, graph, n):
    dist = [INF] * (n+1)
    dist[start] = 0
    pq = [[0, start]]

    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))
    return dist

n, m, x = map(int, input().split())
g = [[] for _ in range(n+1)]
rg = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    g[a].append((b, t))
    rg[b].append((a, t))

go = daiqk(x, g, n)
back = daiqk(x, rg, n)

answer = 0
for i in range(1, n + 1):
    if go[i] + back[i] > answer:
        answer = go[i] + back[i]

print(answer)


