import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

n = int(input())
m = int(input())

parents = [i for i in range(n + 1)]
enemies = [[] for _ in range(n + 1)]

for _ in range(m):
    relation, p_str, q_str = input().split()
    p, q = int(p_str), int(q_str)

    if relation == 'F':
        union(p, q)
    else:
        enemies[p].append(q)
        enemies[q].append(p)

# 적의 적은 친구
for i in range(1, n + 1):
    # i번 학생의 적이 2명 이상일 경우
    if len(enemies[i]) > 1:
        # 첫 번째 적을 기준으로 나머지 모든 적들을 union
        first_enemy = enemies[i][0]
        for j in range(1, len(enemies[i])):
            union(first_enemy, enemies[i][j])

# 최종 팀의 개수 계산
teams = set()
for i in range(1, n + 1):
    # 각 학생의 최종 대표자를 찾아 set에 추가
    teams.add(find_set(i))

print(len(teams))