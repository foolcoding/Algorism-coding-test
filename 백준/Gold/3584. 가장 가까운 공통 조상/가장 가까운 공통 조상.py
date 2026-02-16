import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    parent = [0] * (N + 1)

    for _ in range(N - 1):
        A, B = map(int, input().split())
        parent[B] = A

    n1, n2 = map(int, input().split())
    parents1 = [n1]

    # node1의 조상들을 '부모'를 따라 올라가며 기록
    current = n1
    while parent[current] != 0:
        parents1.append(parent[current])
        current = parent[current]

    # node2의 조상을 '부모'를 따라 올라가며 확인
    current = n2
    while True:
        # 처음으로 만나는 node1의 조상이 바로 LCA
        if current in parents1:
            print(current)
            return
        current = parent[current]

T = int(input())
for _ in range(T):
    solve()