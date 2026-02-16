def solve():
    import sys
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    INF = float("inf")
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0

    # 버스 정보 입력
    for _ in range(m):
        a, b, c = map(int, input().split())
        # 입력에 중복노선이 있길래 최솟값으로 받음
        if dist[a][b] > c:
            dist[a][b] = c

    # 경유지를 고정하고 i와 j를 돌리는 이유
    # 반대로 해버리면 모든 경유지가 고려되지 않은 채
    # i -> k가 갱신되지 않은채 i -> j와 값을 비교하게 되서
    # 최소경로를 보장하지 못함
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if dist[y][x] == INF:
                # 도달 불가능한 경우
                print(0, end=' ')
            else:
                print(dist[y][x], end=' ')
        print()
solve()