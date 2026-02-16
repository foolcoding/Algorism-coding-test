n = int(input())
a = [0, 1]
for i in range(n):
    a.append(a[i] + a[i+1])
print(a[n])