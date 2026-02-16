def solve():
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x : x[1])

    # used[i] = i번째 회의실의 마지막 '종료 시각'
    used = [-1] * k
    cnt = 0

    for curr_start, curr_end in arr:
        best_room = -1
        best_end = -2
        for i in range(k):
            if used[i] < curr_start and used[i] > best_end:
                best_end = used[i]
                best_room = i
        if best_room != -1:
            used[best_room] = curr_end
            cnt += 1
    return cnt

print(solve())




