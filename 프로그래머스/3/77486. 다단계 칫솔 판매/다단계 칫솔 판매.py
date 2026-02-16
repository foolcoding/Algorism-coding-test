from collections import defaultdict

def solution(enroll, referral, seller, amount):
    # 추천인
    parent = defaultdict(int)
    for i in range(len(enroll)):
        if referral[i] == "-":
            parent[enroll[i]] = None
        else:
            parent[enroll[i]] = referral[i]

    # 각 사람별 수익
    profit = {name: 0 for name in enroll}

    # 각 판매 건 처리
    for i in range(len(seller)):
        cur = seller[i]
        money = amount[i] * 100  # 칫솔 한 개 100원

        while True:
            if money <= 0 or cur is None:
                break

            commission = money // 10  # 10% 추천인에게 전달
            my_money = money - commission  # 내가 가져가는 금액

            profit[cur] += my_money     # 내 수익

            # 다음으로 넘길 정보
            cur = parent[cur]   # 내 추천인
            money = commission  # 분배한 중개료

    # enroll 순서대로
    result = []
    for i in enroll:
        result.append(profit[i])
    return result

    # return [profit[name] for name in enroll]


