def solution(data, ext, val_ext, sort_by):
    data_dic = {'code' : 0, 'date' : 1, 'maximum' : 2, 'remain' : 3}
    data = sorted(data, key=lambda x : x[data_dic[sort_by]])
    answer = []
    for i in data:
        if i[data_dic[ext]] < val_ext:
            answer.append(i)
    return answer