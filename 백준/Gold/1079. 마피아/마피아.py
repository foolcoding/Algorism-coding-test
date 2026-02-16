import sys

def solve():
    n = int(sys.stdin.readline())
    initial_guilt = list(map(int, sys.stdin.readline().split()))
    r_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    mafia_player = int(sys.stdin.readline())

    max_nights_survived = 0
    is_alive = [True] * n

    def find_max_path(nights, num_alive, current_guilt):
        nonlocal max_nights_survived

        # 기저 조건 1: 생존자가 2명이고 밤인 경우 (최적화)
        # 마피아가 남은 1명을 죽이고 게임이 끝나므로, nights + 1이 결과가 됨.
        if num_alive == 2 and num_alive % 2 == 0:
            max_nights_survived = max(max_nights_survived, nights + 1)
            return

        # 기저 조건 2: 마피아만 남은 경우 (기존)
        if num_alive == 1:
            max_nights_survived = max(max_nights_survived, nights)
            return

        # 밤/낮 페이즈 결정
        if num_alive % 2 == 0:  # 밤 페이즈
            for i in range(n):
                if i == mafia_player or not is_alive[i]:
                    continue

                # --- 가지치기(Pruning) 로직 시작 ---
                # i를 죽였을 때 다음 낮에 마피아가 죽는지 미리 시뮬레이션
                
                # 1. 가상으로 i를 죽인 후의 상태 생성
                hypothetical_is_alive = list(is_alive)
                hypothetical_is_alive[i] = False
                next_guilt = list(current_guilt)
                for j in range(n):
                    if hypothetical_is_alive[j]:
                        next_guilt[j] += r_matrix[i][j]

                # 2. 가상 상태에서 다음 날 누가 죽는지 확인
                hypothetical_victim = -1
                max_g = -1
                for j in range(n):
                    if hypothetical_is_alive[j] and next_guilt[j] > max_g:
                        max_g = next_guilt[j]
                for j in range(n):
                    if hypothetical_is_alive[j] and next_guilt[j] == max_g:
                        hypothetical_victim = j
                        break
                
                # 3. 만약 마피아가 죽는다면, 이 경로는 더 탐색할 필요 없음
                if hypothetical_victim == mafia_player:
                    # 이 경로는 nights + 1에서 끝나므로 최대값만 갱신하고 continue
                    max_nights_survived = max(max_nights_survived, nights + 1)
                    continue # 가지치기!
                # --- 가지치기 로직 끝 ---

                # (가지치기 되지 않은 경우에만) 실제 재귀 호출 수행
                is_alive[i] = False
                find_max_path(nights + 1, num_alive - 1, next_guilt)
                is_alive[i] = True # 백트래킹

        else:  # 낮 페이즈
            victim_idx = -1
            max_g = -1
            for i in range(n):
                if is_alive[i] and current_guilt[i] > max_g:
                    max_g = current_guilt[i]
            for i in range(n):
                if is_alive[i] and current_guilt[i] == max_g:
                    victim_idx = i
                    break
            
            if victim_idx == mafia_player:
                max_nights_survived = max(max_nights_survived, nights)
                return

            is_alive[victim_idx] = False
            find_max_path(nights, num_alive - 1, current_guilt)
            is_alive[victim_idx] = True

    find_max_path(0, n, initial_guilt)
    print(max_nights_survived)

solve()