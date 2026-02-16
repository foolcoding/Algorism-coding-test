def solve():
    window = sum(arr[:K])
    answer = window

    for i in range(K, N):
        window += arr[i] - arr[i - K]
        if window > answer:
            answer = window
    print(answer)

N, K = map(int, input().split())
arr = list(map(int, input().split()))
solve()