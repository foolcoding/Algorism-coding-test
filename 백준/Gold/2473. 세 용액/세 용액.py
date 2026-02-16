import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    lista = sorted(list(map(int, input().split())))
    min_v = float('inf')
    result = []

    for i in range(n - 2):
        cur_v = lista[i]
        left = i + 1
        right = n - 1
        while left < right:
            left_v = lista[left]
            right_v = lista[right]

            cur_sum = cur_v + left_v + right_v

            if abs(cur_sum) < min_v:
                min_v = abs(cur_sum)
                result = [cur_v, left_v, right_v]

            if cur_sum < 0:
                left += 1
            elif cur_sum > 0:
                right -= 1
            else:   # 합이 0일 경우
                print(cur_v, left_v, right_v)
                return

    print(*result)


solve()