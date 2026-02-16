def solve():
    lista = [[0] * 101 for _ in range(101)]
    for _ in range(4):
        l1, l2, r1, r2 = map(int, input().split())
        for i in range(l2, r2):
            for j in range(l1, r1):
                lista[i][j] = 1
    cnt = 0
    for q in range(101):
        for w in range(101):
            if lista[q][w] == 1:
                cnt += 1
    print(cnt)
solve()

