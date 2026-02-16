import sys

sys.setrecursionlimit(10**6) # 재귀 깊이 제한 설정
input = sys.stdin.readline
N = int(input())
M = int(input())
parent = [i for i in range(N + 1)]

def find_set(x):
    if x == parent[x]:
        return x

    parent[x] = find_set(parent[x])
    return parent[x]

def union_set(a, b):
    a = find_set(a)
    b = find_set(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 도시 연결 정보를 입력받아 union
for i in range(N):
    link_info = list(map(int, input().split()))
    for j in range(len(link_info)):
        # 두 도시가 연결되어 있으면
        if link_info[j] == 1:
            # 두 도시를 합침
            union_set(i + 1, j + 1)

travel_plan = list(map(int, input().split()))

# 여행 계획에 속한 첫 번째 도시의 대표 노드를 찾음
root = find_set(travel_plan[0])

# 두 번째 도시부터 마지막 도시까지 순회
# 같은 집합이면 어떻게든 갈수있으니까 YES, 루트가 다르면 NO
flag = True
for i in range(1, M):
    if find_set(travel_plan[i]) != root:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")