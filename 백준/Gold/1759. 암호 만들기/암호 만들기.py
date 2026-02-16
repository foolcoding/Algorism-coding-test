L, C = map(int, input().split())
lista = ['a', 'e', 'i', 'o', 'u']
arr = input().split()
arr.sort()
path = []
def solve(start):
    if len(path) == L:
        cnt = 0
        for i in lista:
            if i in path:
                cnt += 1
        if 1 <= cnt <= L-2:
            print(*path, sep='')
            return

    for i in range(start, C):
        path.append(arr[i])
        solve(i+1)
        path.pop()

solve(0)
