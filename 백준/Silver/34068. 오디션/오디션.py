import sys

# N: 참가자 수, M: 결투 횟수
N, M = map(int, sys.stdin.readline().split())

# 각 참가자의 승리 횟수를 저장할 리스트
wins = [0] * (N + 1)

# M번의 결투 결과에서 승자의 승리 횟수만 1씩 증가
for _ in range(M):
    winner, _ = map(int, sys.stdin.readline().split())
    wins[winner] += 1

# 승리 횟수 리스트를 오름차순으로 정렬 (참가자 번호는 이제 중요하지 않음)
current_scores = sorted(wins[1:])

total_additional_duels = 0
previous_target_score = -1

# 정렬된 점수 리스트를 순회
for score in current_scores:
    # 현재 참가자의 목표 점수는 자신의 현재 점수와
    # 이전 참가자의 목표 점수+1 중 더 큰 값이어야 한다.
    target_score = max(score, previous_target_score + 1)
    
    # 필요한 추가 승수(결투 수)를 총합에 더한다.
    total_additional_duels += (target_score - score)
    
    # 다음 참가자를 위해 현재 참가자의 목표 점수를 저장한다.
    previous_target_score = target_score

print(total_additional_duels)