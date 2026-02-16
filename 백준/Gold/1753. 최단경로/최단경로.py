import sys
import heapq

input = sys.stdin.readline
INF = 10**18

V, E = map(int, input().split())
K = int(input())

# 인접 리스트
g = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    g[u].append((v, w))  # 방향 그래프

# 다익스트라
dist = [INF] * (V + 1)
dist[K] = 0
pq = [(0, K)]  # (거리, 정점)

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:  # 오래된 항목 무시
        continue
    for v, w in g[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

# 출력
for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
