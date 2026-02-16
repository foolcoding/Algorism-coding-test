import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    grape = [[False] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        grape[a][b] = True

    for k in range(1, n + 1):
        gk = grape[k]
        for i in range(1, n + 1):
            if grape[i][k]:
                for j in range(1, n + 1):
                    if gk[j]:
                        grape[i][j] = True

    s = int(input())
    for y in range(s):
        a, b = map(int, input().split())
        if grape[a][b]:
            print(-1)

        elif grape[b][a]:
            print(1)

        else:
            print(0)

solve()