import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())

    lista = list(range(101))
    for _ in range(N + M):
        a, b = map(int, input().split())
        lista[a] = b

    dist = [-1] * 101
    q = deque([1])
    dist[1] = 0

    while q:
        curr = q.popleft()
        if curr == 100:
            print(dist[curr])
            return
        for dice in range(1, 7):
            nxt = curr + dice
            if nxt > 100:
                continue
            nxt = lista[nxt]
            if dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1
                q.append(nxt)

solve()
