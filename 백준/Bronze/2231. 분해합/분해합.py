num = int(input())
for i in range(num):
    temp = i
    n = i

    while temp > 0:
        n += temp % 10
        temp //= 10

    if num == n:
        print(i)
        num = 0
        break
if num != 0:
    print(0)