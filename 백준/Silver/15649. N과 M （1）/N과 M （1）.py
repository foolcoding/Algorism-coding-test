n, m = map(int, input().split())
path = []
used = [0] * (n + 1)
def solve(used):
    if len(path) == m:
        print(*path)
        return
    for i in range(1, n+1):
        if not used[i]:
            used[i] = 1
            path.append(i)
            solve(used)
            used[i] = 0
            path.pop()

solve(used)