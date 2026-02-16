import sys, heapq

def solve():
    input = sys.stdin.readline
    n = int(input())
    classes = [tuple(map(int, input().split())) for _ in range(n)]
    classes.sort()

    pq = []
    answer = 0

    for s, t in classes:
        while pq and pq[0] <= s:
            heapq.heappop(pq)
        heapq.heappush(pq, t)
        if len(pq) > answer:
            answer = len(pq)
    print(answer)

solve()