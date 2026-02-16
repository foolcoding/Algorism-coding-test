import sys
from collections import deque

# --- 입력 처리 ---
input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# --- 방향 벡터 (상, 하, 좌, 우) ---
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# --- 1. 너비 우선 탐색(BFS)을 이용한 섬 구분 및 번호 할당 ---
def find_islands(r, c, island_num):
    """
    BFS를 수행하여 연결된 땅을 하나의 섬으로 묶고 번호를 붙입니다.
    """
    q = deque([(r, c)])
    visited[r][c] = True
    grid[r][c] = island_num
    
    while q:
        curr_r, curr_c = q.popleft()
        for i in range(4):
            nr, nc = curr_r + dr[i], curr_c + dc[i]
            # 지도 범위 내에 있고, 방문하지 않은 땅(1)인 경우
            if 0 <= nr < N and 0 <= nc < M and \
               not visited[nr][nc] and grid[nr][nc] == 1:
                visited[nr][nc] = True
                grid[nr][nc] = island_num
                q.append((nr, nc))

island_count = 0
for r in range(N):
    for c in range(M):
        if grid[r][c] == 1 and not visited[r][c]:
            island_count += 1
            find_islands(r, c, island_count)

# --- 2. 가능한 모든 다리 찾기 ---
edges = []
def find_bridges(r, c, start_island):
    """
    주어진 땅(r, c)에서 시작하여 놓을 수 있는 모든 다리를 탐색합니다.
    """
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        bridge_len = 0
        while 0 <= nr < N and 0 <= nc < M:
            # 같은 섬에 부딪히면 다리 건설 불가
            if grid[nr][nc] == start_island:
                break
            # 바다(0)를 만나면 다리 길이 증가
            elif grid[nr][nc] == 0:
                bridge_len += 1
                nr += dr[i]
                nc += dc[i]
            # 다른 섬에 도착한 경우
            else:
                # 다리 길이는 2 이상이어야 함
                if bridge_len > 1:
                    end_island = grid[nr][nc]
                    edges.append((bridge_len, start_island, end_island))
                break

for r in range(N):
    for c in range(M):
        if grid[r][c] != 0: # 땅인 경우에만 다리 탐색 시작
            find_bridges(r, c, grid[r][c])

# --- 3. 크루스칼 알고리즘과 유니온-파인드를 이용한 MST 구축 ---
# 다리 길이를 기준으로 오름차순 정렬
edges.sort()

# 유니온-파인드를 위한 부모 테이블
parent = list(range(island_count + 1))

def find_parent(x):
    """
    특정 원소의 루트 부모를 찾습니다.
    """
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    """
    두 원소가 속한 집합을 합칩니다.
    """
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

total_bridge_length = 0
edges_used = 0

for length, island1, island2 in edges:
    # 두 섬의 부모가 같지 않다면, 즉 사이클이 발생하지 않는다면 다리 건설
    if find_parent(island1) != find_parent(island2):
        union_parent(island1, island2)
        total_bridge_length += length
        edges_used += 1

# --- 4. 최종 결과 확인 및 출력 ---
# 모든 섬이 하나의 집합으로 연결되었는지 확인
# (섬이 1개 이상일 때)
if island_count > 0:
    root = find_parent(1)
    all_connected = True
    for i in range(2, island_count + 1):
        if root != find_parent(i):
            all_connected = False
            break
else: # 섬이 아예 없는 경우
    all_connected = True


# 사용된 다리의 수가 (섬의 개수 - 1)이고 모든 섬이 연결된 경우
if all_connected and edges_used == island_count - 1:
    print(total_bridge_length)
else:
    # 섬이 0개나 1개일 경우 필요한 다리는 0개
    if island_count <= 1 and total_bridge_length == 0:
        print(0)
    else:
        print(-1)