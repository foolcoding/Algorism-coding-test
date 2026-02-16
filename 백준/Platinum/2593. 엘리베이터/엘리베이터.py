import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    X = [0] * (M + 1)  # 시작층
    Y = [0] * (M + 1)  # 간격

    for i in range(1, M + 1):
        xi, yi = map(int, input().split())
        X[i], Y[i] = xi, yi

    A, B = map(int, input().split())

    # 각 층에 설 수 있는 엘베 리스트
    floor_elev = [[] for _ in range(N + 1)]

    # 각 엘베가 멈추는 층 리스트
    stop = [[] for _ in range(M + 1)]

    for i in range(1, M + 1):
        floor = X[i]
        yi = Y[i]
        while True:
            if floor > N:
                break
            floor_elev[floor].append(i)
            stop[i].append(floor)
            floor += yi

    # 시작에서 탈 수 있는 엘베, 도착층에 멈출 수 있는 엘베 표시
    starts = []
    possible = [False] * (M + 1)
    for i in range(1, M + 1):
        if X[i] <= A and (A - X[i]) % Y[i] == 0:
            starts.append(i)
        if X[i] <= B and (B - X[i]) % Y[i] == 0:
            possible[i] = True

    if not starts:
        print(-1)
        return

    # 바로 도착
    for i in starts:
        if possible[i]:
            print(1)
            print(i)
            return

    # 환승 횟수 리스트
    dist = [-1] * (M + 1)

    # 경로 추적 리스트
    parent = [0] * (M + 1)
    q = deque()

    # 초기화
    for s in starts:
        dist[s] = 1
        parent[s] = s
        q.append(s)

    # 갈아타기 여러번 방지
    visited = set()

    finish = -1
    while q:
        # 현재 엘베
        cur = q.popleft()

        # 현재 엘베가 서는 모든 층
        for floor in stop[cur]:
            if floor in visited:
                continue
            visited.add(floor)

            # 갈아탈 수 있는 엘베
            for n in floor_elev[floor]:

                # 처음왔다면 (여기에 오는 최단거리)
                if dist[n] == -1:
                    dist[n] = dist[cur] + 1

                    # cur -> n
                    parent[n] = cur

                    # 목표층에 도달 가능한 엘베를 만나면 종료
                    if possible[n]:
                        finish = n

                        # while까지 끝내기 위함
                        q.clear()
                        break
                    q.append(n)
            if finish != -1:
                break

    if finish == -1:
        print(-1)
        return

    # 거꾸로 강을 거슬러 오르는 저 힘찬 연어들처럼
    end = finish
    path = []
    while True:
        path.append(finish)
        if parent[finish] == finish:
            break
        finish = parent[finish]
    path.reverse()

    print(dist[end])
    for p in path:
        print(p)

solve()
