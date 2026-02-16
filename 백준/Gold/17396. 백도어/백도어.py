from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    sight = list(map(int, input().split()))

    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        # 어디 한쪽으로만 갈 수 있다는 말이 없어서 둘다 연결 (양방향 그래프)
        graph[a].append((b, t))
        graph[b].append((a, t))

    best = [float('inf')] * N
    q = []
    heappush(q, (0, 0))

    while q:
        cost, curr = heappop(q)

        # 지금 처리하는게 더 오래걸리면 무시
        if best[curr] < cost:
            continue

        # 연결된 노드들 확인
        for i in graph[curr]:
            nc = cost + i[1]

            # 새로운 경로가 기존 경로보다 짧을 때
            if nc < best[i[0]]:

                # 시야에 보이는 곳인데 최종 목적지가 아니면 무시
                if sight[i[0]] == 1 and i[0] != N - 1:
                    continue

                best[i[0]] = nc
                heappush(q, (nc, i[0]))

    if best[N - 1] == float('inf'):
        print(-1)
    else:
        print(best[N - 1])

solve()