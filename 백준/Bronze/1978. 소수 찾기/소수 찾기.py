n = int(input())
answer = 0
arr = list(map(int, input().split()))
for num in arr:
    if num < 2:
        continue
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            break
    else:
        answer += 1
print(answer)