str = input()
a = set()
for i in range(len(str)):
    for j in range(i, len(str)):
        a.add(str[i:j+1])
print(len(a))