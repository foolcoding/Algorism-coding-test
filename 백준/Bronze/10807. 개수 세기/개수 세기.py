cnt = int(input())
num_list = list(map(int, input().split()))
target = int(input())
answer = 0
for i in range(cnt):
    if num_list[i] == target:
        answer += 1
print(answer)