def sel_sort(a):
    s = len(a)
    for i in range(s):
        for j in range(i+1, s):
            temp = 0
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))

a = sel_sort(a)
b = []

for i in a:
    if i not in b:
        b.append(i)
        
for i in b:
    print(i)