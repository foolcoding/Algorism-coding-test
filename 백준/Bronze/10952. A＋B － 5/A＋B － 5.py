while True:
    n1, n2 = map(int, input().split())
    if not n1 and not n2:
        break
    print(n1+n2)