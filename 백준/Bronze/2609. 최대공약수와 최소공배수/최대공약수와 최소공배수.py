a, b = map(int, input().split())

# 최대공약수(GCD) (유클리드 호재법)
tem_a, tem_b = a, b
while tem_b != 0:
    tem_a, tem_b = tem_b, tem_a % tem_b
gcd = tem_a

# 최소공배수(LCM)
lcm = (a * b) // gcd

print(gcd)
print(lcm)