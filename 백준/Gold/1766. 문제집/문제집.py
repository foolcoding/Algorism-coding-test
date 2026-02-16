import sys
import heapq
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    cnt = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        cnt[b] += 1

    pq = []
    for v in range(1, N + 1):
        if cnt[v] == 0:
            heapq.heappush(pq, v)

    result = []
    while pq:
        cur = heapq.heappop(pq)
        result.append(cur)
        for nxt in arr[cur]:
            cnt[nxt] -= 1
            if cnt[nxt] == 0:
                heapq.heappush(pq, nxt)
    print(*result)
solve()