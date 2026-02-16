T = int(input())
for t in range(T):
    a, b = input().split()
    for i in range(len(b)):
        print(int(a) * b[i], end='')
    print()