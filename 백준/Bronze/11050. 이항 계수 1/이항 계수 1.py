N, K = map(int, input().split())

guma = 1
for i in range(N, N - K, -1):
    guma *= i

keria = 1
for i in range(1, K + 1):
    keria *= i

result = guma // keria
print(result)