import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
lista = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

# 사회자가 부르는 순서대로 처리
count = 0
for row in lista:
    for num in row:
        count += 1
        for y in range(5):
            for x in range(5):
                if board[y][x] == num:
                    board[y][x] = 0

        # 빙고 카운트
        bingo_cnt = 0

        # 가로 5줄
        for y in range(5):
            ok = True
            for x in range(5):
                if board[y][x] != 0:
                    ok = False
                    break
            if ok:
                bingo_cnt += 1

        # 세로 5줄
        for y in range(5):
            ok = True
            for x in range(5):
                if board[x][y] != 0:
                    ok = False
                    break
            if ok:
                bingo_cnt += 1

        # 대각선 (좌상→우하)
        ok = True
        for i in range(5):
            if board[i][i] != 0:
                ok = False
                break
        if ok:
            bingo_cnt += 1

        # 대각선 (우상→좌하)
        ok = True
        for i in range(5):
            if board[i][4 - i] != 0:
                ok = False
                break
        if ok:
            bingo_cnt += 1

        if bingo_cnt >= 3:
            print(count)
            sys.exit()