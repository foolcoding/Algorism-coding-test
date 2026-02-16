from collections import deque

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque()
    for i in range(N):
        p = arr[i]
        is_target = (i == M)
        q.append((p, is_target))

    cnt = 0
    while True:
        p, is_target = q.popleft()

        if q and p < max(x for x, y in q):
            q.append((p, is_target))
        else:
            cnt += 1
            if is_target:
                print(cnt)
                break