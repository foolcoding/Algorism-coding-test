alpha_list = {chr(i): -1 for i in range(ord('a'), ord('z') + 1)}
exam = input()
for i in alpha_list.keys():
    alpha_list[i] = exam.find(i)
    print(alpha_list[i], end = ' ')