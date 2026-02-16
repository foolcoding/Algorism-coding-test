n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

def dfs(i, total, picked):
    global result
    if i == n:  # arr 길이 만큼 채우고
        if picked and total == s:   # 빈배열이 아니고, 원소의 합이 s일때
            result += 1
        return

    dfs(i + 1, total, picked)       # 빈 부분수열은 버림 (크기가 양수인거만 문제에서 찾으라고 해서)
    dfs(i + 1, total + arr[i], True)

dfs(0, 0, False)
print(result)

