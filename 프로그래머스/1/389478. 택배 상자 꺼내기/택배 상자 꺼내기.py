def solution(n, w, num):
    row = (num - 1) // w    # 찾을 상자의 행
    widx = (num - 1) % w    # 지그재그 무시 찾을 상자의 열
    col = widx if row % 2 == 0 else w - 1 - widx # 지그재그 고려한 찾을 상자열 행

    top = (n - 1) // w  # 맨 윗줄 행 번호
    last = n % w    # 맨 윗줄의 상자 후

    if last == 0:   # top이 꽉찼음
        top_col = True
    else:   # 찾을 상자 행에 top에 상자가 존재하는지
        if top % 2 == 0:    # top이 짝수행
            top_col = col < last
        else:   # top이 홀수행
            top_col = col >= w - last # 거꾸로 체크
    return (top - row) + (1 if top_col else 0)