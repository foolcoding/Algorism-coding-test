def dfs(lo, hi, depth):
    if lo > hi:
        return
    mid = (lo + hi) // 2
    levels[depth].append(arr[mid])
    dfs(lo, mid - 1, depth + 1)
    dfs(mid + 1, hi, depth + 1)

n = int(input().strip())
arr = list(map(int, input().split()))
levels = [[] for _ in range(n)]

dfs(0, len(arr) - 1, 0)

for d in range(n):
    print(*levels[d])

