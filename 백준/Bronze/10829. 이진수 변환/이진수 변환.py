def solve(n):
    if n == 0:
        return
    solve(n // 2)
    print(n % 2, end = '')

n = int(input())
solve(n)
