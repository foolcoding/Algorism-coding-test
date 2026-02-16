'''
6팀이 모두 경기를 치르면 15경기
각 팀의 승 + 무 + 패 = 5
승리와 패배는 같아야함
무승부는 항상 짝수 (승패가 같으면 항상 짝수)
모든 불가능한 조건을 찾아내고 싶었지만 불가능하다고 판단해
위의 조건을 가지치기로 쓰고 dfs시도

모두 리그전을 치르는 건 순서를 고려하고 중복이 없는 경우
= 조합을 구해서 dfs하면 되겠다

세가지 경우가 생김
승, 패
무승부
패, 승
'''

from itertools import combinations
import sys
input = sys.stdin.readline

# 6팀이 순서가 상관있고 중복이 없이(조합) 모든경기를 치르면 15경기
teams = [0, 1, 2, 3, 4, 5]
games = list(combinations(teams, 2))

def dfs(game_idx, lista):
    global is_pos

    # 기저조건, 모든경기 마쳤으니 가능
    if game_idx == 15:
        is_pos = True
        return

    team1, team2 = games[game_idx]

    # team1 승, team2 패
    if lista[team1][0] > 0 and lista[team2][2] > 0:
        lista[team1][0] -= 1
        lista[team2][2] -= 1
        dfs(game_idx + 1, lista)
        lista[team1][0] += 1
        lista[team2][2] += 1
        if is_pos: return

    # 무승부
    if lista[team1][1] > 0 and lista[team2][1] > 0:
        lista[team1][1] -= 1
        lista[team2][1] -= 1
        dfs(game_idx + 1, lista)
        lista[team1][1] += 1
        lista[team2][1] += 1
        if is_pos: return

    # team1 패, team2 승
    if lista[team1][2] > 0 and lista[team2][0] > 0:
        lista[team1][2] -= 1
        lista[team2][0] -= 1
        dfs(game_idx + 1, lista)
        lista[team1][2] += 1
        lista[team2][0] += 1
        if is_pos: return

for _ in range(4):
    arr = list(map(int, input().split()))
    lista = []
    for i in range(0, 18, 3):
        a, b, c = arr[i], arr[i + 1], arr[i + 2]
        lista.append([a, b, c])

    # 가지치기
    victory = sum(row[0] for row in lista)
    defeat = sum(row[2] for row in lista)

    # 각 팀의 승 + 무 + 패가 5가 아니거나, 승과 패가 다르면 불가능
    is_invalid = False
    for i in range(6):
        if sum(lista[i]) != 5:
            is_invalid = True
            break

    if is_invalid or victory != defeat:
        print(0, end = ' ')
        continue

    is_pos = False
    dfs(0, lista)

    if is_pos:
        print(1, end = ' ')
    else:
        print(0, end = ' ')


