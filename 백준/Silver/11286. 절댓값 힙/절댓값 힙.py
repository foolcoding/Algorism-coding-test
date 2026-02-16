import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]  # 입력 저장
he_arr = []  # 절댓값 힙

for x in arr:
    if x != 0:
        heapq.heappush(he_arr, (abs(x), x))
    else:
        if he_arr:
            print(heapq.heappop(he_arr)[1])
        else:
            print(0)