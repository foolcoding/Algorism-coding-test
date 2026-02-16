import sys
input = sys.stdin.readline

n, m = map(int, input().split())

name_to_num = {}
num_to_name = [""]

# 도감 채우기
for i in range(1, n + 1):
    pokemon_name = input().strip()
    name_to_num[pokemon_name] = i
    num_to_name.append(pokemon_name)


for _ in range(m):
    query = input().strip()

    if query.isdigit():
        print(num_to_name[int(query)])
    else:
        print(name_to_num[query])