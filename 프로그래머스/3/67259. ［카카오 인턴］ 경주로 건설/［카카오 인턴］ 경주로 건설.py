import heapq

def solution(board):
    n = len(board)

    if n == 1:
        return 0

    bound = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    INF = float('inf')
    cost = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    pq = []  # 비용, y, x, 방향

    # 시작점
    # 아래 다익스트라는 그 전의 방향으로 cost를 결정하기 때문에
    # 그 전의 방향이 없는 시작점을 정해주고 들어가야댐
    for d, (dy, dx) in enumerate(bound):
        ny, nx = 0 + dy, 0 + dx
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
            cost[ny][nx][d] = 100
            heapq.heappush(pq, (100, ny, nx, d))

    answer = 0

    while pq:
        c, y, x, d_prev = heapq.heappop(pq)

        # 이미 더 좋은 비용이 있다면
        if c > cost[y][x][d_prev]:
            continue

        # 도착 지점이면 최소값 갱신
        if y == n - 1 and x == n - 1:
            answer = c
            break

        # 4방향으로 이동
        for nd, (dy, dx) in enumerate(bound):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if board[ny][nx] == 1:
                continue

            # 직선으로 가고 코너 돌면 500 추가
            nc = c + 100
            if nd != d_prev:
                nc += 500

            if cost[ny][nx][nd] > nc:
                cost[ny][nx][nd] = nc
                heapq.heappush(pq, (nc, ny, nx, nd))

    return answer