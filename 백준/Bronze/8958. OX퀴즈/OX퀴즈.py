T = int(input())
for t in range(T):
    S = input()
    total = 0
    cnt = 0
    for i in range(len(S)):
        if S[i] == 'O':
            cnt += 1
        else:
            cnt = 0
        total += cnt
    print(total)