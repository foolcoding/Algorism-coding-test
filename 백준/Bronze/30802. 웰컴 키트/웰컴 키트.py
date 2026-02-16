n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

cnt = 0
for count in arr:
    cnt += (count + t - 1) // t
pen_a = n // p
pen_b = n % p
print(cnt)
print(pen_a, pen_b)