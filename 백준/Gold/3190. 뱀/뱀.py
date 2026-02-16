import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N = int(input())
    K = int(input())

    # 사과 위치
    apples = set()
    for _ in range(K):
        r, c = map(int, input().split())
        apples.add((r - 1, c - 1))

    L = int(input())
    # X초가 끝난 뒤 회전 정보
    turns = {}
    for _ in range(L):
        x, ch = input().split()
        turns[int(x)] = ch

    bound = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0

    snake = deque([(0, 0)])  # 몸(꼬리…머리), 머리는 맨 뒤
    body = {(0, 0)}          # 충돌 검사용 집합

    t = 0
    while True:
        t += 1
        hx, hy = snake[-1]
        dx, dy = bound[d]
        nx, ny = hx + dx, hy + dy

        # 벽/자기몸 충돌
        if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in body:
            return t

        # 머리 이동
        snake.append((nx, ny))
        body.add((nx, ny))

        if (nx, ny) in apples:      # 사과 있으면 꼬리 유지
            apples.remove((nx, ny))
        else:                       # 없으면 꼬리 한 칸 줄이기
            tx, ty = snake.popleft()
            body.remove((tx, ty))

        # t초가 끝난 뒤 회전
        if t in turns:
            if turns[t] == 'L':
                d = (d - 1) % 4
            else:  # 'D'
                d = (d + 1) % 4

print(solve())