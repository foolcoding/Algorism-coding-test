import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# 각 학생별로 몇번씩 비교가 되었는지
# 비교가 된 만큼 정렬 되면 댐
# 답이 여러가지 인 경우에는 아무거나 출력하라 했으니까
# 자기보다 앞에오는 사람들 먼저 세우고 그 뒤에 앞에 오는사람이 같은 사람들 아무나 출력
# 앞에오는사람 기준
# 1 4, 2 4, 3 4, 1 2 가 입력값이면
# 4는 자기보다 앞에오는사람 3명, 2는 1명 1이랑 3는 0명이니까
# 1이랑 3 아무거나 출력하고 그다음 2, 4 하면 댐
in_degree = [0] * (n + 1)

# 비교 정보를 저장할 리스트
lista = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lista[a].append(b)  # a가 b 앞에 서야 함
    in_degree[b] += 1   # b보다 앞에 오는 사람 +1

result = []
q = deque()

# 자기 앞에 아무도 없는사람 찾으면 그 사람 큐에 넣고 시작
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    curr_stu = q.popleft()
    result.append(curr_stu)

    # 현재 학생 뒤에 서는
    for next_stu in lista[curr_stu]:
        in_degree[next_stu] -= 1
        # 만약 앞에 선사람이 없어지면 추가
        if in_degree[next_stu] == 0:
            q.append(next_stu)

print(*result)