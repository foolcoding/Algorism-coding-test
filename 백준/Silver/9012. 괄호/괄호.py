def solve():
    n = int(input())
    for _ in range(n):
        s = input().strip()
        stack = []
        for i in s:
            if i == '(':
                stack.append('(')
            else:
                if not stack:
                    stack.append(')')
                    break
                stack.pop()
        if not stack: print('YES')
        else: print('NO')
solve()
