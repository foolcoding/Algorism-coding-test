n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    arr.append((int(age), i, name))
arr.sort(key=lambda x: (x[0], x[1]))
for i, _, j in arr:
    print(i, j)