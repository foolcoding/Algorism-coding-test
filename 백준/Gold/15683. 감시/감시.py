import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
# 사무실 지도 정보를 저장할 리스트
office = []

# CCTV의 위치와 종류를 저장할 리스트, 어제 스도쿠에서 제로인덱스 만들어주던거랑 같음
cctvs = []
for r in range(n):
    row = list(map(int, input().split()))
    office.append(row)
    for c in range(m):
        if 1 <= row[c] <= 5:
            cctvs.append((row[c], r, c))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cctv_directions = [
    [],
    [[0], [1], [2], [3]],  # 1번 CCTV
    [[0, 2], [1, 3]],  # 2번 CCTV
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번 CCTV
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번 CCTV
    [[0, 1, 2, 3]]  # 5번 CCTV
]

min_blind_spot = float('inf')

def watch(board, r, c, direction):
    for d in direction:
        nr, nc = r, c
        while True:
            nr += dr[d]
            nc += dc[d]
            if not (0 <= nr < n and 0 <= nc < m) or board[nr][nc] == 6:
                break
            if board[nr][nc] == 0:
                board[nr][nc] = '#'

def dfs(cctv_index, board):
    global min_blind_spot

    if cctv_index == len(cctvs):
        count = 0
        for r in range(n):
            for c in range(m):
                if board[r][c] == 0:
                    count += 1
        min_blind_spot = min(min_blind_spot, count)
        return

    cctv_type, r, c = cctvs[cctv_index]

    for directions in cctv_directions[cctv_type]:
        temp_board = copy.deepcopy(board)
        watch(temp_board, r, c, directions)
        dfs(cctv_index + 1, temp_board)

dfs(0, office)

print(min_blind_spot)
