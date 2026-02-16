arr = list(map(int, input().split()))
a = [1, 2, 3, 4, 5, 6, 7, 8]
d = [8, 7, 6, 5, 4, 3, 2, 1]

# 입력받은 리스트를 기준 리스트와 비교합니다.
if arr == a:
    print("ascending")
elif arr == d:
    print("descending")
else:
    print("mixed")