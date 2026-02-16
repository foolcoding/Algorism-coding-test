from collections import deque
import sys
input = sys.stdin.readline

def solve():
    fun = input().strip()
    n = int(input())
    s = input().strip()                               # "[1,2,3,4]" 또는 "[]"
    arr = deque([] if n == 0 else s[1:-1].split(',')) # 안전 파싱

    flag = False
    for ch in fun:
        if ch == 'R':
            flag = not flag
        elif ch == 'D':
            if not arr:
                print('error')
                return
            if flag:
                arr.pop()
            else:
                arr.popleft()

    if flag:
        print('[' + ','.join(reversed(arr)) + ']')
    else:
        print('[' + ','.join(arr) + ']')

T = int(input())
for _ in range(T):
    solve()
