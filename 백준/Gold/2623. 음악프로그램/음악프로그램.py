import sys
from collections import deque

# 가수의 수(N)와 보조 PD의 수(M)를 입력받음
n, m = map(int, sys.stdin.readline().split())

# 그래프를 인접 리스트 형태로 초기화
graph = [[] for _ in range(n + 1)]

# 각 가수의 진입 차수(in-degree)를 0으로 초기화
in_degree = [0] * (n + 1)

# 각 PD가 정한 순서를 바탕으로 그래프와 진입 차수를 설정
for _ in range(m):
    pd_list = list(map(int, sys.stdin.readline().split()))
    # 리스트의 첫 번째 값은 가수의 수이므로, 실제 순서 정보만 사용
    for i in range(1, len(pd_list) - 1):
        # pd_list[i] -> pd_list[i+1] 순서로 간선을 추가
        graph[pd_list[i]].append(pd_list[i+1])
        # 도착점인 가수의 진입 차수를 1 증가시킴
        in_degree[pd_list[i+1]] += 1

# 위상 정렬을 위한 큐를 생성
q = deque()

# 진입 차수가 0인 가수(가장 먼저 시작할 수 있는 가수)를 큐에 추가
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)

# 최종 순서를 저장할 리스트
result = []

# 큐가 빌 때까지 위상 정렬을 수행
while q:
    # 큐에서 현재 순서에 해당하는 가수를 꺼냄
    current_singer = q.popleft()
    result.append(current_singer)

    # 현재 가수가 공연한 후에 공연할 다음 가수들을 확인
    for next_singer in graph[current_singer]:
        # 다음 가수들의 진입 차수를 1 감소
        in_degree[next_singer] -= 1
        # 만약 진입 차수가 0이 되었다면, 해당 가수도 큐에 추가
        if in_degree[next_singer] == 0:
            q.append(next_singer)

# 최종적으로 순서를 정할 수 있었는지 확인
# 결과 리스트의 가수 수가 전체 가수 수와 다르면 사이클이 존재한다는 의미
if len(result) != n:
    print(0)
else:
    # 정해진 순서를 하나씩 출력
    for singer in result:
        print(singer)