import sys

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

lista = sum(arr[:x])
max_v = lista
cnt = 1

for i in range(x, n):
    lista = lista - arr[i - x] + arr[i]

    if lista > max_v:
        max_v = lista
        cnt = 1
    elif lista == max_v:
        cnt += 1

if max_v == 0:
    print('SAD')
else:
    print(max_v)
    print(cnt)