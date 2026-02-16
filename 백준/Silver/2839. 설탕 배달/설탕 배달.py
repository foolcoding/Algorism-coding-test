n = int(input())

for i in range(n // 5, -1, -1): 
    rest = n - 5 * i
    if rest % 3 == 0:
        print(i + (rest // 3))
        break
else:
    print(-1)