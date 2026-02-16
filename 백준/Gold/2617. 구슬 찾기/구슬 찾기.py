from collections import deque

N, M = map(int, input().split())
grapha = [[] for _ in range(N+1)]
graphb = [[] for _ in range(N+1)]
for ___ in range(M):
    a, b = map(int, input().split())
    grapha[a].append(b)
    graphb[b].append(a)

def bfs(start, graph):
    q = deque([start])
    visited = [False] * (N+1)
    visited[start] = True
    cnt = 0
    while q:
        go = q.popleft()

        for gogo in graph[go]:
            if not visited[gogo]:
                q.append(gogo)
                visited[gogo] = True
                cnt += 1
    return cnt

result = 0
for i in range(N+1):
    if bfs(i, grapha) > N // 2:
        result += 1
        continue
    if bfs(i, graphb) > N // 2:
        result += 1
print(result)



