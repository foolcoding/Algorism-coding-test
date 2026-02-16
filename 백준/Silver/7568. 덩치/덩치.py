n = int(input())
people = []
for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

ranks = []
for i in range(n):
    rank = 1
    for j in range(n):
        # 자기자신
        if i == j:
            continue
        x1, y1 = people[i]
        x2, y2 = people[j]
        if x2 > x1 and y2 > y1:
            rank += 1
    ranks.append(str(rank))
    print(rank, end= ' ')