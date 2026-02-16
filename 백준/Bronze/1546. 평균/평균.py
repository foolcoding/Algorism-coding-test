n = int(input())

scores = list(map(int, input().split()))

m = max(scores)

new_sum = 0
for score in scores:
    new_sum += score / m * 100

new_avg = new_sum / n

print(new_avg)