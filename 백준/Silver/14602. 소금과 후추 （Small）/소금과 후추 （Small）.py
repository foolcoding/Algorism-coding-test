m,n,k,w = list(map(int, input().split())) # 행,열,최고밝기,정수
lista = [list(map(int, input().split())) for _ in range(m)]
result = []

for y in range(m-w+1):
    for x in range(n-w+1):
        listb = []   # 빈리스트 2개를 쓰긴했지만 다음엔 1개만 쓰자
        for i in range(w):
            for j in range(w):
                listb.append(lista[y+i][x+j])
        listb.sort()
        result.append(listb[w*w//2]) # x를 넣는걸 생각해보자

for i in range(m-w+1):
    print(*result[i*(n-w+1):(i+1)*(n-w+1)])