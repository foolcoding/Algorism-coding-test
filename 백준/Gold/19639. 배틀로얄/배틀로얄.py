import sys
input = sys.stdin.readline

def solve():
    X, Y, M = map(int, input().split())
    max_hp = M
    hp = M

    enemies = []
    for i in range(1, X + 1):
        dmg = int(input())
        enemies.append((dmg, i))

    items = []
    for i in range(1, Y + 1):
        heal = int(input())
        items.append((heal, i))

    # 데미지는 내림차순해서 피가 제일 많을 때 제일 큰 데미지를 견디게 해서 계산하기 쉽게
    # 아이템은 가장 작은거부터 새용해서 낭비를 줄이기
    enemies.sort(key=lambda x: x[0], reverse=True)
    items.sort(key=lambda x: x[0])

    answer = []
    j = 0   # 아이템 포인터

    for dmg, eidx in enemies:
        # hp보다 dmg가 크다면 회복템을 하나씩 먹어서 hp가 dmg보다 커질떄 까지
        while True:
            if j == Y or hp > dmg:
                break

            heal, iidx = items[j]
            answer.append(iidx)   # 아이템 사용
            hp = min(max_hp, hp + heal)     # 최대체력 이상 회복 불가능
            j += 1

        if hp <= dmg:
            print(0)
            return

        hp -= dmg
        answer.append(-eidx)     # 적 처리

    # 남은 아이템 전부 사용
    while True:
        if j == Y:
            break
        answer.append(items[j][1])
        j += 1

    if len(answer) != X + Y:
        print(0)
        return

    for x in answer:
        print(x)

solve()
