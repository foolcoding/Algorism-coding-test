from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)
    q = deque()

    # 알파펫 1개 다른거 찾기, death: 1
    for i in range(len(words)):
        w = words[i]

        # begin과 w가 다른 글자 수 세기
        diff = 0
        for j in range(len(begin)):
            if begin[j] != w[j]:
                diff += 1

        if diff == 1:
            visited[i] = True
            q.append((i, 1))

    while q:
        idx, depth = q.popleft()
        
        if words[idx] == target:
            return depth
        
        for j in range(len(words)):
            w = words[j]
            if not visited[j]:
                # words[idx] 와 w 의 다른 글자 개수 세기
                diff = 0
                for k in range(len(words[idx])):
                    if words[idx][k] != w[k]:
                        diff += 1

                if diff == 1:
                    visited[j] = True
                    q.append((j, depth + 1))


