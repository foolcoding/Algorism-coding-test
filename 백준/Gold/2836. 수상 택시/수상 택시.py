import sys
input = sys.stdin.readline

def solve():
    # 역주행 해야하는 경우
    reverse_case = []
    for _ in range(N):
        A, B = map(int, input().split())
        if A > B:
            reverse_case.append((B, A))

    # 역방향없으면 거리만 출력
    if not reverse_case:
        print(M)
        return

    # 구간의 시작점을 기준으로 오름차순 정렬
    reverse_case.sort()

    first_start, first_end = reverse_case[0]
    total_reverse_distance = 0

    for i in range(1, len(reverse_case)):
        next_start, next_end = reverse_case[i]

        # 겹치는 경우, 끝점 갱신
        if next_start <= first_end:
            first_end = max(first_end, next_end)
        
        # 겹치지 않는 경우
        else:
            # 바로 길이 더하기
            total_reverse_distance += (first_end - first_start)
            # 다음 비교 준비
            first_start, first_end = next_start, next_end

    # for 문에서 i랑 그전에꺼랑 비교해서 그 전에껄 더해주니까
    # 마지막 i는 더할 기회가 없어서 마지막에 더해줘야댐
    total_reverse_distance += (first_end - first_start)

    # 거리 M + 역주행거리 * 2
    total_distance = M + (total_reverse_distance * 2)
    print(total_distance)

N, M = map(int, input().split())
solve()