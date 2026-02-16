import sys
input = sys.stdin.readline

N = int(input().strip())
lst = [int(input().strip()) for _ in range(N)]

stack = []
result = []
cur = 1

for x in lst:
    # x가 나올 때까지 1씩 증가하며 push
    while cur <= x:
        stack.append(cur)
        result.append('+')
        cur += 1

    # 맨 위가 x면 pop, 아니면 불가능
    if stack and stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        break
else:
    print('\n'.join(result))