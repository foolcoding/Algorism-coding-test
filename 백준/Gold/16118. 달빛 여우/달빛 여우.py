import sys
import heapq
input = sys.stdin.readline
INF = float("inf")

def dijkstra_fox():
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

def dijkstra_wolf():
    dist = [[INF] * (n + 1) for _ in range(2)]
    dist[0][1] = 0
    pq = [(0, 1, 0)]
    while pq:
        d, u, s = heapq.heappop(pq)
        if d > dist[s][u]:
            continue
        for v, w in graph[u]:
            if s == 0:
                nd = d + (w // 2)
            else:
                nd = d + (w * 2)
            ns = 1 - s
            if nd < dist[ns][v]:
                dist[ns][v] = nd
                heapq.heappush(pq, (nd, v, ns))
    return dist

def solve():
    for _ in range(m):
        a, b, d = map(int, input().split())
        w = d * 2
        graph[a].append((b, w))
        graph[b].append((a, w))

    fox = dijkstra_fox()
    wolf = dijkstra_wolf()

    answer = 0
    for i in range(1, n + 1):
        wolf_best = min(wolf[0][i], wolf[1][i])
        if fox[i] < wolf_best:
            answer += 1
    print(answer)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
solve()
