n = int(input())
arr = set()
for i in range(n):
    a, b = input().split()
    if b == 'enter':
        arr.add(a)
    else:
        arr.discard(a)

len_arr = len(arr)
sorted_arr = sorted(arr, reverse=True)
for i in sorted_arr:
    print(i)