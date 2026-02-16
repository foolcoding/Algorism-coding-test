m, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in arr:
    if n >= i:
        n += 1
    if n < i:
        break
print(n)