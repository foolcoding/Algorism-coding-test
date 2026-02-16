A, B, V = map(int, input().split())
dis = V - A
dai = A - B
days = (dis + dai - 1) // dai
print(int(days) + 1)