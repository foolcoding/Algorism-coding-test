arr = [list(map(int, input().split())) for x in range(9)]
max_val = -1
idx1 = 0
idx2 = 0
for i in arr:
    for j in i:
        if j > max_val:
            max_val = j
            idx1 = arr.index(i) + 1
            idx2 = i.index(j) + 1
print(max_val)
print(idx1, idx2)