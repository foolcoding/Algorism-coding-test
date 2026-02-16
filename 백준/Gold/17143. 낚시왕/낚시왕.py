import sys
input = sys.stdin.readline

def solve():
    R, C, M = map(int, input().split())
    sharks = dict()
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        sharks[(r, c)] = (s, d, z)

    answer = 0

    # 1번 열부터 C번 열까지 이동
    for fisher in range(1, C + 1):
        catch_pos = None
        min_row = R + 1

        # 현재 열에서 가장 가까운 상어 잡기
        for (r, c), _ in sharks.items():
            if c == fisher and r < min_row:
                min_row = r
                catch_pos = (r, c)

        # 찾으면 상어 한마리 잡기
        if catch_pos is not None:
            answer += sharks[catch_pos][2]   # 상어 크기
            del sharks[catch_pos]

        new_sharks = dict()

        for (r, c), (s, d, z) in sharks.items():
            nr, nc, nd = r, c, d

            # 위, 아래 => 세로 이동
            if d == 1 or d == 2:
                if R > 1:
                    move = s % (2 * (R - 1))

                    # 벽까지 한 번에 점프하면서 방향 뒤집기
                    while move > 0:
                        if nd == 1:  # 위로
                            dist = nr - 1          # 위쪽 벽(1번 행)까지 거리
                            if move <= dist:
                                nr -= move
                                move = 0
                            else:
                                nr = 1            # 벽 도착
                                move -= dist
                                nd = 2            # 아래로 방향 전환
                        else:       # nd == 2, 아래로
                            dist = R - nr         # 아래쪽 벽(R번 행)까지 거리
                            if move <= dist:
                                nr += move
                                move = 0
                            else:
                                nr = R
                                move -= dist
                                nd = 1            # 위로 방향 전환

            # 오른쪽, 왼쪽 => 가로 이동
            else:
                if C > 1:
                    move = s % (2 * (C - 1))

                    while move > 0:
                        if nd == 4:  # 왼쪽
                            dist = nc - 1          # 왼쪽 벽(1번 열)까지 거리
                            if move <= dist:
                                nc -= move
                                move = 0
                            else:
                                nc = 1
                                move -= dist
                                nd = 3            # 오른쪽으로 전환
                        else:       # nd == 3, 오른쪽
                            dist = C - nc         # 오른쪽 벽(C번 열)까지 거리
                            if move <= dist:
                                nc += move
                                move = 0
                            else:
                                nc = C
                                move -= dist
                                nd = 4            # 왼쪽으로 전환

            # 같은 칸에 여러 상어가 모이면 가장 큰 상어만 남기기
            if (nr, nc) in new_sharks:
                if new_sharks[(nr, nc)][2] < z:
                    new_sharks[(nr, nc)] = (s, nd, z)
            else:
                new_sharks[(nr, nc)] = (s, nd, z)

        sharks = new_sharks

    print(answer)

solve()
