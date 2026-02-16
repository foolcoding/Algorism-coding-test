T = int(input())
total = 0
arr = [[0]*100 for _ in range(100)]
for tc in range(T):
    w, h = map(int, input().split())
    for i in range(h, h + 10):
        for j in range(w, w + 10):
            arr[i][j] = 1
    total += arr.count(3)

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            total += 1
print(total)

