def solve():
    visited = [0] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        if visited[i] != 0:
            continue
        cur = i
        while True:
            # 사이클이 있다: 같은 자리로 돌아왔다
            # 이걸 체크하기 위해서 i를 넣어줌
            visited[cur] = i
            nxt = arr[cur]

            # 방문한 적 없으면 계속 가보기
            if visited[nxt] == 0:
                cur = nxt
                continue

            # 뭐야 나네? (사이클 만들어짐)
            if visited[nxt] == i:
                node = nxt
                # 사이클 돌면서 노드수 세기
                while True:
                    node = arr[node]
                    cnt += 1
                    if node == nxt:
                        break
            break
    print(n - cnt)

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    solve()